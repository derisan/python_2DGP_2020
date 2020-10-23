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
        pair = evt.type, evt.key
        if pair == Player.KEYDOWN_C:
            self.player.jump()


class JumpState:
    @staticmethod
    def get(player):
        if not hasattr(JumpState, 'singleton'):
            JumpState.singleton = JumpState()
            JumpState.singleton.player = player
            JumpState.singleton.images = []
            JumpState.singleton.images.append(gfw.image.load(gobj.res('player/jump/Frame0.png')))

        return JumpState.singleton

    def __init__(self):
        self.time = 0
        self.frame = 0
        self.jump_speed = Player.JUMP

    def enter(self):
        self.time = 0
        self.frame = 0
        self.jump_speed = Player.JUMP

    def exit(self):
        pass

    def draw(self):
        self.images[self.frame].draw(*self.player.pos)

    def update(self):
        self.player.move((0, self.jump_speed * gfw.delta_time))
        self.jump_speed -= Player.GRAVITY * gfw.delta_time

        _, foot, _, _ = self.player.get_bb()
        platform = self.player.get_platform(foot)
        if platform is not None:
            l, b, r, t = platform.get_bb()
            if self.jump_speed < 0 and int(foot) <= t:
                self.player.move((0, t - foot))
                self.player.set_state(RunningState)

    def handle_event(self, evt):
        pass


class Player:
    KEYDOWN_C = (SDL_KEYDOWN, SDLK_c)
    KEYDOWN_SPACE = (SDL_KEYDOWN, SDLK_SPACE)

    SLIDE_DURATION = 1.0
    GRAVITY = 3000
    JUMP = 750

    def __init__(self):
        self.pos: Tuple = 150, 105
        self.delta: Tuple = 0, 0

        self.pet = Pet(*self.pos)
        gfw.world.add(gfw.layer.player, self.pet)

        self.state = None
        self.set_state(RunningState)

    def update(self):
        self.state.update()
        self.pet.know_pos(self.pos)

    def draw(self):
        self.state.draw()

    def handle_event(self, evt):
        self.state.handle_event(evt)
        self.pet.handle_event(evt)

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

    def jump(self):
        if self.state == JumpState:
            return
        self.set_state(JumpState)

    def move(self, diff: Tuple):
        self.pos = gobj.point_add(self.pos, diff)

    def get_platform(self, foot):
        selected = None
        sel_top = 0
        x, y = self.pos
        for platform in gfw.world.objects_at(gfw.layer.platform):
            l, b, r, t = platform.get_bb()
            if x < l or x > r:
                continue
            if foot < b:
                continue
            if selected is None:
                selected = platform
                sel_top = t
            else:
                if t > sel_top:
                    selected = platform
                    sel_top = t
        return selected
