from typing import Tuple
from typing import List

from pico2d import *

import gfw
import gobj


class Player:
    KEYDOWN_C = (SDL_KEYDOWN, SDLK_c)
    KEYDOWN_SPACE = (SDL_KEYDOWN, SDLK_SPACE)
    RUNNING, FALLING, JUMPING, SLIDING, ATTACK = range(5)

    SLIDE_DURATION = 1.0

    GRAVITY = 3000
    JUMP = 1000

    def __init__(self):
        self.pos: Tuple = 150, 110
        self.delta: Tuple = 0, 0
        self.images: List = []
        for i in range(3 + 1):
            self.images.append(gfw.image.load(gobj.res('player/move/Frame' + str(i) + '.png')))
        self.time = 0
        self.FPS = 8

    def update(self):
        self.time += gfw.delta_time

    def draw(self):
        fidx = round(self.time * self.FPS) % len(self.images)
        self.images[fidx].draw(*self.pos)

    def handle_event(self, evt):
        pair = (evt.type, evt.key)
        if pair == Player.KEYDOWN_C:
            pass

    def get_bb(self):
        hw = 36
        hh = 35
        x, y = self.pos
        return x - hw, y - hh, x + hw, y + hh
