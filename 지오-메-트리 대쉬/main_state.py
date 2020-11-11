from pico2d import *

import gfw
import gobj
from background import HorzScrollBackground

canvas_width = 800
canvas_height = 500


def enter():
    gfw.world.init(['bg'])

    bg = HorzScrollBackground('game_background.png')
    bg.speed = 50
    gfw.world.add(gfw.layer.bg, bg)


def exit():
    pass


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


paused = False


def update():
    if paused:
        return
    gfw.world.update()


def draw():
    gfw.world.draw()


if __name__ == '__main__':
    gfw.run_main()
