import random
from typing import Tuple
from typing import List

from pico2d import *

import gfw
import gobj
from pet import Pet
from meso import Meso


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

        _, foot, _, _ = self.player.get_bb()
        platform = self.player.get_platform(foot)
        if platform is not None:
            l, b, r, t = platform.get_bb()
            if foot > t:
                self.player.set_state(FallingState)

    def handle_event(self, evt):
        pair = evt.type, evt.key
        if pair == Player.KEYDOWN_C:
            self.player.jump()
        elif pair == Player.KEYDOWN_SPACE:
            self.player.slide()
        elif pair == Player.KEYDOWN_DOWN:
            self.player.move_down_from_platform()


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
        self.jump_count = 0

    def enter(self):
        self.time = 0
        self.frame = 0
        self.jump_count += 1
        if self.jump_count > 2:
            pass
        else:
            self.jump_speed = Player.JUMP

    def exit(self):
        self.jump_count = 0

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
        key_state = SDL_GetKeyboardState(None)
        if key_state[SDL_SCANCODE_C]:
            self.enter()


class FallingState:
    @staticmethod
    def get(player):
        if not hasattr(FallingState, 'singleton'):
            FallingState.singleton = FallingState()
            FallingState.singleton.player = player
            FallingState.singleton.images = []
            FallingState.singleton.images.append(gfw.image.load(gobj.res('player/jump/Frame0.png')))

        return FallingState.singleton

    def __init__(self):
        self.time = 0
        self.frame = 0
        self.jump_speed = 0

    def enter(self):
        self.time = 0
        self.frame = 0
        self.jump_speed = 0

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


class SlidingState:
    @staticmethod
    def get(player):
        if not hasattr(SlidingState, 'singleton'):
            SlidingState.singleton = SlidingState()
            SlidingState.singleton.player = player
            SlidingState.singleton.images = []
            SlidingState.singleton.images.append(gfw.image.load(gobj.res('player/slide/Frame0.png')))

        return SlidingState.singleton

    def __init__(self):
        self.time = 0
        self.frame = 0

    def enter(self):
        self.time = 0
        self.frame = 0
        self.player.bb_idx = 1

    def exit(self):
        self.player.bb_idx = 0

    def draw(self):
        self.images[self.frame].draw(self.player.pos[0], self.player.pos[1] - 15)

    def update(self):
        self.time += gfw.delta_time
        key_state = SDL_GetKeyboardState(None)
        if key_state[SDL_SCANCODE_SPACE]:
            self.time = 0

        if self.time > Player.SLIDE_DURATION:
            self.player.set_state(RunningState)

        _, foot, _, _ = self.player.get_bb()
        platform = self.player.get_platform(foot)
        if platform is not None:
            l, b, r, t = platform.get_bb()
            if foot > t:
                self.player.set_state(FallingState)

    def handle_event(self, evt):
        pass


class Player:
    KEYDOWN_C = (SDL_KEYDOWN, SDLK_c)
    KEYDOWN_SPACE = (SDL_KEYDOWN, SDLK_SPACE)
    KEYDOWN_DOWN = (SDL_KEYDOWN, SDLK_DOWN)

    SLIDE_DURATION = 0.05
    GRAVITY = 3000
    JUMP = 680

    BB_DIFFS = [
        (-25, -33, 25, 33),  # ELSE
        (-25, -33, 25, -15),  # SLIDING
    ]

    def __init__(self):
        self.pos: Tuple = 150, get_canvas_height() // 2
        self.delta: Tuple = 0, 0

        self.pet = Pet(*self.pos)
        gfw.world.add(gfw.layer.player, self.pet)

        self.state = None
        self.set_state(RunningState)

        self.bb_idx = 0
        self.score = 0

    def update(self):
        self.state.update()
        self.pet.know_pos(self.pos)

    def draw(self):
        self.state.draw()

    def handle_event(self, evt):
        self.state.handle_event(evt)
        self.pet.handle_event(evt)

    def get_bb(self):
        l, b, r, t = Player.BB_DIFFS[self.bb_idx]
        x, y = self.pos
        # print(x - hw, y - hh, x + hw, y + hh)
        return x + l, y + b, x + r, y + t

    def set_state(self, clazz):
        if self.state is not None:
            self.state.exit()
        self.state = clazz.get(self)
        self.state.enter()

    def jump(self):
        # if self.state == JumpState or self.state == SlidingState:
        #     return
        self.set_state(JumpState)

    def slide(self):
        # if self.state == JumpState or self.state == FallingState:
        #     return
        self.set_state(SlidingState)

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
            mid = (b + t) // 2
            if foot < mid:
                continue
            if selected is None:
                selected = platform
                sel_top = t
            else:
                if t > sel_top:
                    selected = platform
                    sel_top = t
        return selected

    def move_down_from_platform(self):
        _, foot, _, _ = self.get_bb()
        platform = self.get_platform(foot)
        if not platform.can_pass:
            return

        x, y = self.pos
        y -= platform.height / 2 + 1
        self.pos = x, y

    def item_check(self, item):
        if item.get_type() == Meso.BRONZE:
            self.score += random.randint(1, 49)

        elif item.get_type() == Meso.GOLD:
            self.score += random.randint(50, 99)

        elif item.get_type() == Meso.BILL:
            self.score += random.randint(100, 999)

        elif item.get_type() == Meso.SACK:
            self.score += random.randint(1000, 4999)

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        self.__score = score


