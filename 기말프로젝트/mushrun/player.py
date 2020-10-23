from typing import Tuple
from typing import List

from pico2d import *

import gfw
import gobj
from pet import Pet


class RunningState:
    @staticmethod
    def get(player):
        if not hasattr(RunningState, 'singleton'):
            RunningState.singleton = RunningState()
            RunningState.singleton.player = player
            RunningState.singleton.images = []
            for i in range(3 + 1):
                RunningState.singleton.images.append(gfw.image.load(gobj.res('player/move/Frame' + str(i) + '.png')))

        return RunningState.singleton

    def __init__(self):
        self.FPS = 8
        self.time = 0
        self.frame = 0

    def enter(self):
        self.time = 0
        self.frame = 0

    def exit(self):
        pass

    def draw(self):
        self.images[self.frame].draw(*self.player.pos)

    def update(self):
        self.time += gfw.delta_time
        self.frame = round(self.time * self.FPS) % len(self.images)

    def handle_event(self, evt):
        pass


class Player:
    KEYDOWN_C = (SDL_KEYDOWN, SDLK_c)
    KEYDOWN_SPACE = (SDL_KEYDOWN, SDLK_SPACE)

    SLIDE_DURATION = 1.0
    GRAVITY = 3000
    JUMP = 1000

    def __init__(self):
        self.pos: Tuple = 150, 100
        self.delta: Tuple = 0, 0

        self.pet = Pet(*self.pos)
        gfw.world.add(gfw.layer.player, self.pet)

        self.state = None
        self.set_state(RunningState)

    def update(self):
        self.state.update()

    def draw(self):
        self.state.draw()

    def handle_event(self, evt):
        self.state.handle_event(evt)

    def get_bb(self):
        hw = 36
        hh = 33
        x, y = self.pos
        # print(x - hw, y - hh, x + hw, y + hh)
        return x - hw, y - hh, x + hw, y + hh

    def set_state(self, clazz):
        if self.state is not None:
            self.state.exit()
        self.state = clazz.get(self)
        self.state.enter()
