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

    x = 0
    cw = get_canvas_width()
    while x < cw:
        t = random.choice([0, 1])
        pf = Platformer(t, x, 0)
        gfw.world.add(gfw.layer.platform, pf)
        x += pf.width


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


def draw():
    gfw.world.draw()
    gobj.draw_collision_box()


if __name__ == '__main__':
    gfw.run_main()
