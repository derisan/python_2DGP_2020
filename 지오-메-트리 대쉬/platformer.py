import gfw
import gobj

INFO = [
    (5 * gobj.UNIT, 0.5 * gobj.UNIT, 'l_platform.png'),
    (1.5 * gobj.UNIT, 0.5 * gobj.UNIT, 's_platform.png'),
]


class Platformer:
    LONG, SHORT = range(2)

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

    def move(self, dx):
        self.left += dx
        if self.left + self.width < 0:
            gfw.world.remove(self)

    @property
    def right(self):
        return self.left + self.width
