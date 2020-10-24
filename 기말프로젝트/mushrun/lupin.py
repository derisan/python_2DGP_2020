import random

import gfw
import gobj

LUPIN_SIZE = 30


class Banana:
    pass


class Lupin:
    RUN, THROW, DEAD = range(3)
    images = None
    COOLDOWN = 1

    def __init__(self, x, y):
        self.x, self.y = x, y

        self.FPS = 10
        self.time = 0
        self.cooldown = Lupin.COOLDOWN
        self.frame = 0
        self.state = Lupin.RUN

        if Lupin.images is None:
            Lupin.images = [[] for _ in range(3)]
            for i in range(2 + 1):
                Lupin.images[Lupin.RUN].append(gfw.image.load(gobj.res('monsters/lupin/running/Frame' + str(i) +
                                                                       '.png')))
            for i in range(9 + 1):
                Lupin.images[Lupin.THROW].append(gfw.image.load(gobj.res('monsters/lupin/throw/Frame' + str(i) +
                                                                         '.png')))

            for i in range(2 + 1):
                Lupin.images[Lupin.DEAD].append(gfw.image.load(gobj.res('monsters/lupin/running/Frame' + str(i) +
                                                                        '.png')))

    def update(self):
        self.time += gfw.delta_time
        self.cooldown -= gfw.delta_time

        if self.cooldown < 0 and self.state == Lupin.RUN:
            self.state = Lupin.THROW
            self.throw_banana()

        if self.state == Lupin.THROW and self.frame >= 9:
            self.state = Lupin.RUN
            self.reset_things()

        self.frame = round(self.time * self.FPS) % len(self.images[self.state])

    def draw(self):
        self.images[self.state][self.frame].draw(self.x, self.y)

    def move(self, dx):
        self.x += dx
        if self.x + LUPIN_SIZE < 0:
            gfw.world.remove(self)

    def throw_banana(self):
        # create banana
        pass

    def reset_things(self):
        self.cooldown = Lupin.COOLDOWN
        self.time = 0
        self.frame = 0

    def get_bb(self):
        hw = LUPIN_SIZE
        hh = LUPIN_SIZE
        x, y = self.x, self.y
        # print(x - hw, y - hh, x + hw, y + hh)
        return x - hw, y - hh, x + hw, y + hh
