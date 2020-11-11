from typing import Tuple

from pico2d import *

import gfw
import gobj


class Player:
    KEYDOWN_SPACE = (SDL_KEYDOWN, SDLK_SPACE)
    GRAVITY = 500
    JUMP = 100
    WIDTH = 30
    HEIGHT = 30

    def __init__(self):
        self.pos = 150, get_canvas_height() // 2
        self.delta: Tuple[float, float] = 0, 0
        self.image = gfw.image.load(gobj.res('cube.png'))
        self.time = 0
        self.jump_speed = 0
        self.rotation = 0

    def handle_event(self, e):
        pair = e.type, e.key
        if pair == Player.KEYDOWN_SPACE:
            self.jump()
            self.rotation -= 90

    def update(self):
        self.time += gfw.delta_time

        self.move((0, self.jump_speed * gfw.delta_time))
        self.jump_speed -= Player.GRAVITY * gfw.delta_time

    def draw(self):
        rot = gobj.to_rad(self.rotation)
        self.image.composite_draw(rot, 'h', *self.pos, w=Player.WIDTH, h=Player.HEIGHT)

    def get_bb(self):
        hw, hh = 15, 15
        x, y = self.pos
        return x - hw, y - hh, x + hw, y + hh

    def move(self, diff):
        self.pos = gobj.point_add(self.pos, diff)

    def jump(self):
        self.jump_speed = Player.JUMP
