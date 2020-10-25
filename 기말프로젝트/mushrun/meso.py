import random

import gfw
import gobj

MESO_SIZE = 60

PATH = [
    'coins/bronze/Frame',
    'coins/gold/Frame',
    'coins/bill/Frame',
    'coins/sack/Frame'
]


class Meso:
    BRONZE, GOLD, BILL, SACK = range(4)

    def __init__(self, type: int, x, y):
        self.x, self.y = x, y
        self.images = []
        fn = PATH[type]
        for i in range(3 + 1):
            self.images.append(gfw.image.load(gobj.res(fn + str(i) + '.png')))
        self.time = 0
        self.frame = 0
        self.FPS = 6
        self.type = type

    def update(self):
        self.time += gfw.delta_time
        self.frame = round(self.time * self.FPS) % len(self.images)

    def draw(self):
        self.images[self.frame].draw(self.x, self.y, w=MESO_SIZE, h=MESO_SIZE)

    def move(self, dx):
        self.x += dx
        if self.x + MESO_SIZE < 0:
            gfw.world.remove(self)

    def get_bb(self):
        hw = MESO_SIZE // 2
        hh = MESO_SIZE // 2
        x, y = self.x, self.y
        # print(x - hw, y - hh, x + hw, y + hh)
        return x - hw, y - hh, x + hw, y + hh

    def get_type(self):
        return self.type
