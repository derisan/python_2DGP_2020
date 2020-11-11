from typing import Tuple

from pico2d import *

import gfw
from gobj import res


class Player:
    KEYDOWN_SPACE = (SDL_KEYDOWN, SDLK_SPACE)

    def __init__(self):
        self.pos = 150, get_canvas_height() // 2
        self.delta: Tuple[float, float] = 0, 0
        self.image = gfw.image.load(res('cube.png'))
        self.time = 0
        self.FPS = 10

    def handle_event(self, e):
        pair = e.type, e.key
        if pair == Player.KEYDOWN_SPACE:
            pass

    def update(self):
        self.time += gfw.delta_time

    def draw(self):
        self.image.composite_draw(0, 'h', *self.pos)

    def get_bb(self):
        pass
