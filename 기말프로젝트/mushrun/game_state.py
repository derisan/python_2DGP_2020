import random

from pico2d import *

import gfw
import gobj
from background import Background
from g_platform import Platform
from player import Player
from meso import Meso
import stage_gen

canvas_width = 1280
canvas_height = 600


def enter():
    gfw.world.init(['bg', 'enemy', 'platform', 'item', 'player'])

    bg = Background('background/stage1_bg_far.png')
    bg.speed = 10
    gfw.world.add(gfw.layer.bg, bg)

    bg = Background('background/stage1_bg_near.png')
    bg.speed = 100
    bg.y_scale = 1.75
    gfw.world.add(gfw.layer.bg, bg)

    global player
    player = Player()
    gfw.world.add(gfw.layer.player, player)

    stage_gen.load(gobj.res('stage_01.txt'))


paused = False


def update():
    if paused:
        return

    gfw.world.update()

    dx = -175 * gfw.delta_time
    for layer in range(gfw.layer.enemy, gfw.layer.item + 1):
        for obj in gfw.world.objects_at(layer):
            obj.move(dx)

    stage_gen.update(dx)


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
        elif evt.key == SDLK_p:
            global paused
            paused = not paused

    if player.handle_event(evt):
        return


def exit():
    pass


if __name__ == '__main__':
    gfw.run_main()
