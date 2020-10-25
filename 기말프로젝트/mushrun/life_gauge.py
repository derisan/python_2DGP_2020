import gfw
import gobj


class LifeGauge:
    MAX_HP = 10
    MAX_MP = 10

    def __init__(self, x, y):
        self.pos = x, y

        # self.hp = LifeGauge.MAX_HP
        self.hp = 8
        self.mp = LifeGauge.MAX_MP
        self.exp = 0

        self.bg = gfw.image.load(gobj.res('tags/bar3.png'))
        self.hp_0 = gfw.image.load(gobj.res('tags/hp/hp0.png'))
        self.hp_1 = gfw.image.load(gobj.res('tags/hp/hp1.png'))
        self.hp_2 = gfw.image.load(gobj.res('tags/hp/hp2.png'))

    def draw(self):
        self.bg.draw_to_origin(*self.pos)
        x = self.pos[0] + 9
        y = self.pos[1] + 3
        self.hp_0.draw_to_origin(x, y)

        for i in range(1, self.hp):
            x = self.pos[0] + 11 * i
            y = self.pos[1] + 3
            self.hp_1.draw_to_origin(x, y)

        if self.hp == LifeGauge.MAX_HP:
            x = self.pos[0] + 11 * self.hp
            y = self.pos[1] + 3
            self.hp_2.draw_to_origin(x, y)

    def update(self):
        pass
