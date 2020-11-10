import gfw
import gobj


class LifeGauge:
    MAX_HP = 10
    MAX_MP = 10
    BG, HP, MP, EXP = range(4)

    def __init__(self, x, y):
        self.pos = x, y

        self.hp = LifeGauge.MAX_HP
        self.mp = LifeGauge.MAX_MP
        self.exp = 0

        self.images = None
        self.get_images()

    def get_images(self):
        """
        Load images used in class
        """
        self.images = [[] for _ in range(3 + 1)]

        self.images[LifeGauge.BG].append(gfw.image.load(gobj.res('tags/bar.png')))

        for i in range(2 + 1):
            self.images[LifeGauge.HP].append(gfw.image.load(gobj.res('tags/hp/hp' + str(i) + '.png')))

        for i in range(2 + 1):
            self.images[LifeGauge.MP].append(gfw.image.load(gobj.res('tags/mp/mp' + str(i) + '.png')))

        for i in range(1 + 1):
            self.images[LifeGauge.EXP].append(gfw.image.load(gobj.res('tags/exp/exp' + str(i) + '.png')))

    def draw(self):
        self.images[LifeGauge.BG][0].draw_to_origin(*self.pos)

        self.hp_draw()
        self.mp_draw()
        self.exp_draw()

    def hp_draw(self):
        if self.hp > 0:
            x = self.pos[0] + 9
            y = self.pos[1] + 3
            self.images[LifeGauge.HP][0].draw_to_origin(x, y)

            x += 2
            h = self.images[LifeGauge.HP][1].h
            self.images[LifeGauge.HP][1].draw_to_origin(x, y, w=11 * (self.hp - 1), h=h)

            if self.hp == LifeGauge.MAX_HP:
                x = self.pos[0] + 11 * self.hp
                y = self.pos[1] + 3
                self.images[LifeGauge.HP][2].draw_to_origin(x, y)

    def mp_draw(self):
        if self.mp > 0:
            x = self.pos[0] + 115
            y = self.pos[1] + 3
            self.images[LifeGauge.MP][0].draw_to_origin(x, y)

            x += 2
            h = self.images[LifeGauge.MP][1].h
            self.images[LifeGauge.MP][1].draw_to_origin(x, y, w=11 * (self.mp - 1), h=h)

            if self.mp == LifeGauge.MAX_HP:
                x += 11 * (self.mp - 1)
                y = self.pos[1] + 3
                self.images[LifeGauge.MP][2].draw_to_origin(x, y)

    def exp_draw(self):
        pass

    def update(self):
        pass

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, hp):
        self.__hp = hp

    @property
    def mp(self):
        return self.__mp

    @mp.setter
    def mp(self, mp):
        self.__mp = mp

