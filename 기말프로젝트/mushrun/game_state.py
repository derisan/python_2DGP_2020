import random

from pico2d import *

import gfw
import gobj
from background import Background
from g_platform import Platform
from player import Player
from meso import Meso

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


paused = False


def update():
    if paused:
        return

    gfw.world.update()

    move_platform()


def move_platform():
    x = 0
    dx = -175 * gfw.delta_time
    for layer in range(gfw.layer.enemy, gfw.layer.item + 1):
        for obj in gfw.world.objects_at(layer):
            obj.move(dx)
            if hasattr(obj, 'right'):
                r = obj.right
                if x < r:
                    x = r

    cw = get_canvas_width()
    while x < cw:
        pf = Platform(Platform.Floor, x, 0)
        gfw.world.add(gfw.layer.platform, pf)

        meso = Meso(Meso.get_random_meso(), x + pf.width // 2, random.randint(200, 500))
        gfw.world.add(gfw.layer.item, meso)

        x += pf.width
        # print('adding platform:', gfw.world.count_at(gfw.layer.platform))


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

    if player.handle_event(evt):
        return


def exit():
    pass


if __name__ == '__main__':
    gfw.run_main()
