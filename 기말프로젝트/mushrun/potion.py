import random

import gfw
import gobj

POTION_SIZE = 60

PATH = [
    'potions/hp.png',
    'potions/mp.png',
]


class Potion:
    HP, MP = range(2)

    def __init__(self, type: int, x, y):
        self.x, self.y = x, y
        fn = PATH[type]
        self.images = gfw.image.load(gobj.res(fn))
        self.time = 0
        self.type = type

    def update(self):
        self.time += gfw.delta_time

    def draw(self):
        self.images.draw(self.x, self.y, w=POTION_SIZE, h=POTION_SIZE)

    def move(self, dx):
        self.x += dx
        if self.x + POTION_SIZE < 0:
            gfw.world.remove(self)

    def get_bb(self):
        hw = POTION_SIZE // 2
        hh = POTION_SIZE // 2
        x, y = self.x, self.y
        return x - hw, y - hh, x + hw, y + hh

    def get_type(self):
        return self.type
