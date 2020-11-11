import random

from pico2d import *

import gfw
import gobj
from background import HorzScrollBackground
from player import Player
from platformer import Platformer

canvas_width = 800
canvas_height = 400


def enter():
    gfw.world.init(['bg', 'platform', 'player'])

    bg = HorzScrollBackground('game_background.png')
    bg.speed = 50
    gfw.world.add(gfw.layer.bg, bg)

    global bgm
    bgm = gfw.sound.load('Assets/main_bgm.ogg')
    bgm.set_volume(64)
    bgm.repeat_play()

    global player
    player = Player()
    gfw.world.add(gfw.layer.player, player)


def exit():
    bgm.stop()


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
    move_platform()


def draw():
    gfw.world.draw()
    gobj.draw_collision_box()


def move_platform():
    x = 0
    dx = -200 * gfw.delta_time
    for layer in range(gfw.layer.platform, gfw.layer.player):
        for obj in gfw.world.objects_at(layer):
            obj.move(dx)
            x = obj.right

    cw = get_canvas_width()
    while x < cw:
        pf = Platformer(Platformer.LONG, x, 0)
        gfw.world.add(gfw.layer.platform, pf)
        x += pf.width


if __name__ == '__main__':
    gfw.run_main()
