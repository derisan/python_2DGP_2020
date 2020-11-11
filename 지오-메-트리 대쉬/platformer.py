import gfw
import gobj

UNIT = 30
INFO = [
    (5 * UNIT, 0.5 * UNIT, 'l_platform.png'),
    (1 * UNIT, 0.5 * UNIT, 's_platform.png'),
]


class Platformer:
    SHORT, LONG = range(2)

    def __init__(self, type, left, bottom):
        self.left = left
        self.bottom = bottom
        self.width, self.height, fn = INFO[type]
        self.image = gfw.image.load(gobj.res(fn))

    def update(self):
        pass

    def draw(self):
        self.image.draw_to_origin(self.left, self.bottom, self.width, self.height)

    def get_bb(self):
        return self.left, self.bottom, self.left + self.width, self.bottom + self.height
