import random

import gfw
import gobj

MESO_SIZE = 15


class Meso:
    def __init__(self, type: str, x, y):
        self.x, self.y = x, y
        self.images = []
        for i in range(3 + 1):
            self.images.append(gfw.image.load(gobj.res('coins/' + type + '/Frame' + str(i) + '.png')))
        self.time = 0
        self.frame = 0
        self.FPS = 4

    def update(self):
        self.time += gfw.delta_time
        self.frame = round(self.time * self.FPS) % len(self.images)

    def draw(self):
        self.images[self.frame].draw(self.x, self.y)

    def move(self, dx):
        self.x += dx
        if self.x + MESO_SIZE < 0:
            gfw.world.remove(self)
            print(self)

    def get_bb(self):
        hw = MESO_SIZE
        hh = MESO_SIZE
        x, y = self.x, self.y
        # print(x - hw, y - hh, x + hw, y + hh)
        return x - hw, y - hh, x + hw, y + hh

    @staticmethod
    def get_random_meso() -> str:
        return random.choice(['bronze', 'gold', 'bill', 'sack'])
