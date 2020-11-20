import random

from pico2d import *

import gfw
import gobj
from background import HorzScrollBackground
from player import Player
import stage_gen

canvas_width = 800
canvas_height = 400


def enter():
    gfw.world.init(['bg', 'platform', 'spike', 'player'])

    bg = HorzScrollBackground('game_background.png')
    bg.speed = 50
    gfw.world.add(gfw.layer.bg, bg)

    global bgm
    bgm = load_music('Assets/Remembrance.ogg')
    bgm.set_volume(64)
    bgm.repeat_play()

    global player
    player = Player()
    gfw.world.add(gfw.layer.player, player)

    global font
    font = gfw.font.load('Assets/Maplestory Bold.ttf', 25)

    stage_gen.load(gobj.res('stage_01.txt'))


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

    player.handle_event(e)


paused = False


def update():
    if paused:
        return
    gfw.world.update()

    dx = -250 * gfw.delta_time

    for layer in range(gfw.layer.platform, gfw.layer.spike + 1):
        for obj in gfw.world.objects_at(layer):
            obj.move(dx)

    check_spike()

    stage_gen.update(dx)


def check_spike():
    global n_collide
    for spike in gfw.world.objects_at(gfw.layer.spike):
        if gobj.collides_box(player, spike):
            player.die()
            break


def draw():
    gfw.world.draw()
    gobj.draw_collision_box()

    font.draw(0, get_canvas_height() - 15, f'Attempt: {1}', (255, 0, 0))


if __name__ == '__main__':
    gfw.run_main()
