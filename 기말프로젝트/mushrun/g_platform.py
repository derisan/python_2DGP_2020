import gfw
import gobj

INFO = [
    (640, 80, 'platform/platform.png'),
]


class Platform:
    Floor, Short, Long = range(3)

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
        return self.left, self.bottom, self.left + self.width, self.bottom + self.height - 8

    def move(self, dx):
        self.left += dx
        if self.left + self.width < 0:
            # print('count was:', gfw.world.count_at(gfw.layer.platform))
            gfw.world.remove(self)

    def right(self):
        return self.left + self.width
