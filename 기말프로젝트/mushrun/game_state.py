from pico2d import *

import gfw
import gobj
from background import Background

canvas_width = 1280
canvas_height = 800


def enter():
    gfw.world.init(['bg'])

    bg = Background('background/mt_huji.png')
    bg.speed = 10
    gfw.world.add(gfw.layer.bg, bg)

    bg = Background('background/sakura.png')
    bg.speed = 150
    bg.y_scale = 1.5
    gfw.world.add(gfw.layer.bg, bg)


paused = False
def update():
    if paused:
        return

    gfw.world.update()


def draw():
    gfw.world.draw()
    gobj.draw_collision_box()


def handle_event(evt):
    if evt.type == SDL_QUIT:
        gfw.quit()
        return
    elif evt.type == SDL_KEYDOWN:
        if evt.key == SDLK_ESCAPE:
            gfw.pop()
            return


def exit():
    pass


if __name__ == '__main__':
    gfw.run_main()