from typing import Tuple
from typing import List

from pico2d import *

import gfw
import gobj


class RunningState:
    @staticmethod
    def get(pet):
        if not hasattr(RunningState, 'singleton'):
            RunningState.singleton = RunningState()
            RunningState.singleton.pet = pet
            RunningState.singleton.images = []
            for i in range(5 + 1):
                RunningState.singleton.images.append(gfw.image.load(gobj.res('pet/move/Frame' + str(i) + '.png')))

        return RunningState.singleton

    def __init__(self):
        self.FPS = 6
        self.time = 0
        self.frame = 0

    def enter(self):
        self.time = 0
        self.frame = 0

    def exit(self):
        pass

    def draw(self):
        self.images[self.frame].composite_draw(0, 'h', *self.pet.pos)

    def update(self):
        self.time += gfw.delta_time
        self.frame = round(self.time * self.FPS) % len(self.images)

    def handle_event(self, evt):
        pair = (evt.type, evt.key)
        if pair == Pet.KEYDOWN_T:
            self.pet.set_state(SkillState)


class SkillState:
    @staticmethod
    def get(pet):
        if not hasattr(SkillState, 'singleton'):
            SkillState.singleton = SkillState()
            SkillState.singleton.pet = pet
            SkillState.singleton.images = []
            for i in range(3 + 1):
                SkillState.singleton.images.append(gfw.image.load(gobj.res('pet/love/Frame' + str(i) + '.png')))
        return SkillState.singleton

    def __init__(self):
        self.FPS = 4
        self.time = 0
        self.frame = 0

    def enter(self):
        self.time = 0
        self.frame = 0

    def exit(self):
        pass

    def draw(self):
        self.images[self.frame].composite_draw(0, 'h', *self.pet.pos)

    def update(self):
        self.repeat = len(self.images) * 3
        self.time += gfw.delta_time
        frame = round(self.time * self.FPS)
        if frame >= self.repeat:
            self.pet.set_state(RunningState)
        else:
            self.frame = frame % 4

    def handle_event(self, evt):
        pass


class Pet:
    KEYDOWN_T = (SDL_KEYDOWN, SDLK_t)

    def __init__(self, x, y):
        self.pos: Tuple = x - 50, y + 30
        self.delta: Tuple = 0, 0
        self.state = None
        self.set_state(RunningState)

    def update(self):
        self.state.update()

    def draw(self):
        self.state.draw()

    def handle_event(self, evt):
        self.state.handle_event(evt)

    def set_state(self, clazz):
        if self.state is not None:
            self.state.exit()
        self.state = clazz.get(self)
        self.state.enter()
