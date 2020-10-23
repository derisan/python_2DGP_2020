from typing import Tuple
from typing import List

from pico2d import *

import gfw
import gobj


class Pet:
    def __init__(self, x, y):
        self.pos: Tuple = x - 50, y + 30
        self.delta: Tuple = 0, 0
        self.images: List = []
        for i in range(5 + 1):
            self.images.append(gfw.image.load(gobj.res('pet/move/Frame' + str(i) + '.png')))
        self.time = 0
        self.FPS = 6

    def update(self):
        self.time += gfw.delta_time

    def draw(self):
        fidx = round(self.time * self.FPS) % len(self.images)
        self.images[fidx].composite_draw(0, 'h', *self.pos)

    def handle_event(self, evt):
        pass

    def get_bb(self):
        hw = 22
        hh = 22
        x, y = self.pos
        return x - hw, y - hh, x + hw, y + hh
