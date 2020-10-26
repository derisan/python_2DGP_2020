import random
from typing import Tuple
from typing import List

from pico2d import *

import gfw
import gobj
from pet import Pet
from meso import Meso
from life_gauge import LifeGauge


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

        if self.player.is_dead():
            self.player.die()

    def handle_event(self, evt):
        pair = evt.type, evt.key
        if pair == Player.KEYDOWN_C:
            self.player.jump()
        elif pair == Player.KEYDOWN_SPACE:
            self.player.slide()
        elif pair == Player.KEYDOWN_DOWN:
            self.player.move_down_from_platform()
        elif pair == Player.KEYDOWN_A:
            self.player.basic_attack()


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

        if self.player.is_dead():
            self.player.die()

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

        if self.player.is_dead():
            self.player.die()

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

        if self.player.is_dead():
            self.player.die()

    def handle_event(self, evt):
        pass


class DeadState:
    FALLING, LANDING = range(2)

    @staticmethod
    def get(player):
        if not hasattr(DeadState, 'singleton'):
            DeadState.singleton = DeadState()
            DeadState.singleton.player = player
            DeadState.singleton.images = [[] for _ in range(2)]
            for i in range(11 + 1):
                DeadState.singleton.images[DeadState.FALLING].append(gfw.image.load(gobj.res('tombstone/fall/Frame' +
                                                                                             str(i) + '.png')))

            DeadState.singleton.images[DeadState.LANDING].append(gfw.image.load(gobj.res('tombstone/land/Frame0.png')))

        return DeadState.singleton

    def __init__(self):
        self.time = 0
        self.frame = 0
        self.FPS = 10
        self.speed = 400
        self.option = DeadState.FALLING

    def enter(self):
        self.x, self.y = self.player.pos[0], get_canvas_height()
        self.time = 0

    def exit(self):
        pass

    def draw(self):
        self.images[self.option][self.frame].draw(self.x, self.y)

    def update(self):
        self.time += gfw.delta_time
        self.frame = round(self.time * self.FPS) % len(self.images[self.option])

        self.x = self.player.pos[0]
        self.y -= self.speed * gfw.delta_time

        if self.y < 105:
            self.option = DeadState.LANDING
            self.y = 105
            self.frame = 0

    def handle_event(self, evt):
        pass


class AttackState:
    @staticmethod
    def get(player):
        if not hasattr(AttackState, 'singleton'):
            AttackState.singleton = AttackState()
            AttackState.singleton.player = player
            AttackState.singleton.images = []
            for i in range(2 + 1):
                AttackState.singleton.images.append(gfw.image.load(gobj.res('player/attack/Frame' + str(i) + '.png')))

        return AttackState.singleton

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
        self.images[self.frame].draw(*self.player.pos)

    def update(self):
        self.time += gfw.delta_time
        self.frame = round(self.time * self.FPS)

        if self.frame >= len(self.images):
            self.player.set_state(RunningState)

    def handle_event(self, evt):
        pass


class Player:
    KEYDOWN_C = (SDL_KEYDOWN, SDLK_c)
    KEYDOWN_A = (SDL_KEYDOWN, SDLK_a)
    KEYDOWN_SPACE = (SDL_KEYDOWN, SDLK_SPACE)
    KEYDOWN_DOWN = (SDL_KEYDOWN, SDLK_DOWN)

    SLIDE_DURATION = 0.05
    GRAVITY = 3000
    JUMP = 700

    BB_DIFFS = [
        (-20, -33, 20, 33),  # ELSE
        (-20, -33, 20, -15),  # SLIDING
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
        # each meso's score
        self.ea_score = 0
        self.invincible = 0

        self.life_gauge = LifeGauge(10, 10)
        gfw.world.add(gfw.layer.ui, self.life_gauge)

    def update(self):
        self.state.update()
        self.pet.know_pos(self.pos)

        if self.invincible > 0:
            self.invincible -= gfw.delta_time
        else:
            self.invincible = 0

    def draw(self):
        self.state.draw()

    def handle_event(self, evt):
        self.state.handle_event(evt)
        self.pet.handle_event(evt)

    def get_bb(self):
        l, b, r, t = Player.BB_DIFFS[self.bb_idx]
        x, y = self.pos

        return x + l, y + b, x + r, y + t

    def set_state(self, clazz):
        if self.state is not None:
            self.state.exit()
        self.state = clazz.get(self)
        self.state.enter()

    def jump(self):
        self.set_state(JumpState)

    def slide(self):
        self.set_state(SlidingState)

    def die(self):
        if self.state is not DeadState:
            self.set_state(DeadState)

    def basic_attack(self):
        self.set_state(AttackState)

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
        """
        Add value to score.
        ea_score is used to print '메소를 얻었습니다'
        """
        self.ea_score = 0
        if item.get_type() == Meso.BRONZE:
            self.ea_score = random.randint(1, 49)

        elif item.get_type() == Meso.GOLD:
            self.ea_score = random.randint(50, 99)

        elif item.get_type() == Meso.BILL:
            self.ea_score = random.randint(100, 999)

        elif item.get_type() == Meso.SACK:
            self.ea_score = random.randint(1000, 4999)

        self.score += self.ea_score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        self.__score = score

    def is_dead(self):
        return self.life_gauge.hp == 0

    def decrease_hp(self):
        if self.invincible > 0:
            return
        self.life_gauge.decrease_hp()

    def make_invincible(self, sec):
        if self.invincible <= 0:
            self.invincible = sec
