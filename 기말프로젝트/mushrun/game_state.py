from pico2d import *

import gfw
import gobj
from background import Background
from game_platform import Platform
from player import Player

canvas_width = 1280
canvas_height = 800


def enter():
    gfw.world.init(['bg', 'platform', 'player'])

    bg = Background('background/stage1_bg_far.png')
    bg.speed = 10
    gfw.world.add(gfw.layer.bg, bg)

    bg = Background('background/stage1_bg_near.png')
    bg.speed = 150
    bg.y_scale = 1.75
    gfw.world.add(gfw.layer.bg, bg)

    pf = Platform(Platform.Floor, 0, 0)
    gfw.world.add(gfw.layer.platform, pf)

    global player
    player = Player()
    gfw.world.add(gfw.layer.player, player)


paused = False


def update():
    if paused:
        return

    gfw.world.update()

    dx = -50 * gfw.delta_time

    # for obj in gfw.world.objects_at(gfw.layer.platform):
    #     obj.move(dx)


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
