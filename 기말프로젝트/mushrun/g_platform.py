import gfw
import gobj

UNIT = 60
INFO = [
    (10 * UNIT, 2 * UNIT, 'platform/long_platform.png'),
    (2 * UNIT, 1 * UNIT, 'platform/medium_platform.png'),
    (1 * UNIT, 1 * UNIT, 'platform/small_platform.png')
]


class Platform:
    Floor, Long, Short = range(3)

    def __init__(self, type, left, bottom):
        self.left = left
        self.bottom = bottom
        self.width, self.height, fn = INFO[type]
        self.image = gfw.image.load(gobj.res(fn))
        self.can_pass = type >= Platform.Long

    def update(self):
        pass

    def draw(self):
        self.image.draw_to_origin(self.left, self.bottom, self.width, self.height)

    def get_bb(self):
        return self.left, self.bottom, self.left + self.width, self.bottom + self.height - 8

    def move(self, dx):
        self.left += dx
        if self.left + self.width < 0:
            # print('count was:', gfw.world.count_at(gfw.layer.platform))
            gfw.world.remove(self)

    @property
    def right(self):
        return self.left + self.width
