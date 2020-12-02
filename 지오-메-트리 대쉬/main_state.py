import random

from pico2d import *

import gfw
import gobj
from background import HorzScrollBackground
from player import Player
from platformer import Platformer
import stage_gen
import score_state
import prito
import progress

canvas_width = gobj.CANVAS_WIDTH
canvas_height = gobj.CANVAS_HEIGHT


def enter():
    gfw.world.init(['bg', 'platform', 'spike', 'player', 'ui'])

    bg = HorzScrollBackground('game_background.png')
    bg.speed = 50
    gfw.world.add(gfw.layer.bg, bg)

    global bgm
    bgm = load_music('Assets/LetsMarch.ogg')
    bgm.set_volume(50)
    bgm.repeat_play()

    global player
    player = Player()
    gfw.world.add(gfw.layer.player, player)

    global font
    font = gfw.font.load('Assets/Maplestory Bold.ttf', 25)

    stage_gen.load(gobj.res('stage_01.txt'))

    prito.init()
    prito.reset()
    gfw.world.add(gfw.layer.ui, prito)
    global prito_cooldown
    prito_cooldown = random.uniform(5, 10)

    progress.init()
    gfw.world.add(gfw.layer.ui, progress)


def exit():
    global bgm
    bgm.stop()
    del bgm


def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
        return
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()
            return
        elif e.key == SDLK_p:
            global paused
            paused = not paused
        elif e.key == SDLK_RETURN:
            if not paused:
                return
            global prito_cooldown
            prito_cooldown = random.uniform(5, 10)
            paused = False
            bgm.repeat_play()

    player.handle_event(e)
    if not prito.handle_event(e):
        player.die()


paused = False


def update():
    if paused:
        return
    gfw.world.update()

    global prito_cooldown
    prito_cooldown -= gfw.delta_time

    if prito_cooldown < 0 and not prito.is_gen:
        prito_cooldown = random.uniform(5, 10)
        prito.generate()

    if prito.is_timeover():
        player.die()

    dx = -250 * gfw.delta_time

    for layer in range(gfw.layer.platform, gfw.layer.spike + 1):
        for obj in gfw.world.objects_at(layer):
            obj.move(dx)

    check_spike()
    is_win()
    stage_gen.update(dx)

    if player.state == Player.DEAD:
        retry()
        return


def check_spike():
    global n_collide
    for spike in gfw.world.objects_at(gfw.layer.spike):
        if gobj.collides_box(player, spike):
            player.die()
            break


def is_win() -> bool:
    for platform in gfw.world.objects_at(gfw.layer.platform):
        if platform.type != Platformer.GOAL:
            continue;
        if gobj.collides_box(player, platform):
            gfw.change(score_state)


def draw():
    gfw.world.draw()
    gobj.draw_collision_box()

    font.draw(0, get_canvas_height() - 15, f'Attempt: {player.n_die}', (255, 0, 0))


def retry():
    global paused
    for platform in gfw.world.objects_at(gfw.layer.platform):
        gfw.world.remove(platform)
    stage_gen.reset()
    player.reset()
    prito.reset()
    bgm.stop()
    paused = True


if __name__ == '__main__':
    gfw.run_main()
