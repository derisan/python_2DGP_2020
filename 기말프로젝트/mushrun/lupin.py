import random

import gfw
import gobj


class Banana:
    images = None
    SPEED = 1.5
    SIZE = 16
    BORDER = 4

    def __init__(self, x, y):
        if Banana.images is None:
            Banana.images = []
            for i in range(3 + 1):
                Banana.images.append(gfw.image.load(gobj.res('monsters/lupin/banana/Frame' + str(i) +
                                                             '.png')))
        self.x, self.y = x, y
        self.time = 0
        self.frame = 0
        self.FPS = 4

    def update(self):
        self.time += gfw.delta_time
        self.frame = round(self.time * self.FPS) % len(self.images)

    def draw(self):
        self.images[self.frame].draw(self.x, self.y)

    def get_bb(self):
        hw = Banana.SIZE - 5
        hh = Banana.SIZE - 5
        x, y = self.x, self.y
        return x - hw, y - hh, x + hw, y + hh

    def move(self, dx):
        self.x += dx * Banana.SPEED
        if self.x + Banana.SIZE < 0:
            gfw.world.remove(self)


class Lupin:
    RUN, THROW, DEAD = range(3)
    images = None
    SIZE = 60

    def __init__(self, x, y):
        self.x, self.y = x, y

        self.FPS = 10
        self.time = 0
        self.cooldown = random.randint(1, 3)
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
                Lupin.images[Lupin.DEAD].append(gfw.image.load(gobj.res('monsters/lupin/dead/Frame' + str(i) +
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

        if self.state == Lupin.DEAD and self.frame >= 2:
            gfw.world.remove(self)

        self.frame = round(self.time * self.FPS) % len(self.images[self.state])

    def draw(self):
        self.images[self.state][self.frame].draw(self.x, self.y, w=Lupin.SIZE, h=Lupin.SIZE)

    def move(self, dx):
        self.x += dx
        if self.x + Lupin.SIZE < 0:
            gfw.world.remove(self)

    def throw_banana(self):
        banana = Banana(self.x - 30, self.y - 10)
        gfw.world.add(gfw.layer.throwing, banana)

    def reset_things(self):
        self.cooldown = random.randint(1, 3)
        self.time = 0
        self.frame = 0

    def get_bb(self):
        hw = Lupin.SIZE // 2
        hh = Lupin.SIZE // 2
        x, y = self.x, self.y
        return x - hw, y - hh, x + hw, y + hh

    def die(self):
        self.state = Lupin.DEAD
        self.reset_things()
