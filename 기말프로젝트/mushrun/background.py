from gobj import *


class Background:
    def __init__(self, file: str):
        self.file = file
        self.image = gfw.image.load(res(file))
        self.cw, self.ch = get_canvas_width(), get_canvas_height()
        self.scroll = 0
        self.speed = 0
        self.y_scale = 1

    def update(self):
        self.scroll += self.speed * gfw.delta_time

    def set_scroll(self, scroll):
        self.scroll = scroll

    def draw(self):
        page = self.image.w * self.ch // self.image.h
        curr = int(-self.scroll) % page

        if curr > 0:
            sw = int(1 + self.image.h * curr / self.ch)
            sl = self.image.w - sw
            src = sl, 0, sw, self.image.h
            dw = int(sw * self.ch / self.image.h)
            dst = curr - dw, 0, dw, self.ch // self.y_scale
            self.image.clip_draw_to_origin(*src, *dst)

        dst_width = round(self.image.w * self.ch / self.image.h)
        while curr + dst_width < self.cw:
            dst = curr, 0, dst_width, self.ch // self.y_scale
            self.image.draw_to_origin(*dst)
            curr += dst_width
        if curr < self.cw:
            dw = self.cw - curr
            sw = int(1 + self.image.h * dw / self.ch)
            src = 0, 0, sw, self.image.h
            dw = int(sw * self.ch / self.image.h)
            dst = curr, 0, dw, self.ch // self.y_scale
            self.image.clip_draw_to_origin(*src, *dst)
