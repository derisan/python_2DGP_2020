import random

import gfw
import gobj

LUPIN_SIZE = 30


class RunningState:
    @staticmethod
    def get(lupin):
        if not hasattr(RunningState, 'singleton'):
            RunningState.singleton = RunningState()
            RunningState.singleton.lupin = lupin
            RunningState.singleton.images = []
            for i in range(2 + 1):
                RunningState.singleton.images.append(gfw.image.load(gobj.res('monsters/lupin/running/Frame' + str(i)
                                                                             + '.png')))
        return RunningState.singleton

    def __init__(self):
        self.FPS = 6
        self.time = 0
        self.cooldown = 1
        self.frame = 0

    def enter(self):
        self.time = 0
        self.cooldown = 1
        self.frame = 0

    def exit(self):
        pass

    def draw(self):
        self.images[self.frame].draw(self.lupin.x, self.lupin.y)

    def update(self):
        self.time += gfw.delta_time
        self.frame = round(self.time * self.FPS) % len(self.images)

        self.cooldown -= gfw.delta_time
        if self.cooldown < 0:
            self.lupin.set_state(ThrowState)

    def handle_event(self, evt):
        pass


class ThrowState:
    @staticmethod
    def get(lupin):
        if not hasattr(ThrowState, 'singleton'):
            ThrowState.singleton = ThrowState()
            ThrowState.singleton.lupin = lupin
            ThrowState.singleton.images = []
            for i in range(9 + 1):
                ThrowState.singleton.images.append(gfw.image.load(gobj.res('monsters/lupin/throw/Frame' + str(i)
                                                                           + '.png')))
        return ThrowState.singleton

    def __init__(self):
        self.FPS = 10
        self.time = 0
        self.frame = 0

    def enter(self):
        self.time = 0
        self.frame = 0

    def exit(self):
        pass

    def draw(self):
        self.images[self.frame].draw(self.lupin.x, self.lupin.y)

    def update(self):
        self.time += gfw.delta_time
        self.frame = round(self.time * self.FPS) % len(self.images)

        if self.frame > 9:
            self.lupin.set_state(RunningState)

    def handle_event(self, evt):
        pass


class DeadState:
    pass


class Banana:
    pass


class Lupin:
    def __init__(self, x, y):
        self.x, self.y = x, y

        self.state = None
        self.set_state(RunningState)

    def update(self):
        self.state.update()

    def draw(self):
        self.state.draw()

    def move(self, dx):
        self.x += dx
        if self.x + LUPIN_SIZE < 0:
            gfw.world.remove(self)

    def get_bb(self):
        hw = LUPIN_SIZE
        hh = LUPIN_SIZE
        x, y = self.x, self.y
        # print(x - hw, y - hh, x + hw, y + hh)
        return x - hw, y - hh, x + hw, y + hh

    def set_state(self, clazz):
        if self.state is not None:
            self.state.exit()
        self.state = clazz.get(self)
        self.state.enter()
