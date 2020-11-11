from typing import Tuple

from pico2d import *

import gfw
import gobj


class Player:
    KEYDOWN_SPACE = (SDL_KEYDOWN, SDLK_SPACE)

    RUNNING, FALLING = range(2)
    GRAVITY = 500
    JUMP = 800

    def __init__(self):
        self.pos = 150, get_canvas_height() // 2
        self.delta: Tuple[float, float] = 0, 0
        self.image = gfw.image.load(gobj.res('cube.png'))
        self.time = 0
        self.jump_speed = 0
        self.rotation = 0
        self.state = Player.RUNNING

    def handle_event(self, e):
        pair = e.type, e.key
        if pair == Player.KEYDOWN_SPACE:
            self.jump()
            self.rotation -= 90

    def update(self):
        self.time += gfw.delta_time

        if self.state != Player.RUNNING:
            self.move((0, self.jump_speed * gfw.delta_time))
            self.jump_speed -= Player.GRAVITY * gfw.delta_time

        _, foot, _, _ = self.get_bb()
        platform = self.get_platform(foot)
        if platform is not None:
            l, b, r, t = platform.get_bb()
            if self.state == Player.RUNNING:
                if foot > t:
                    self.state = Player.FALLING
                    self.jump_speed = 0
            elif self.state == Player.FALLING:
                if self.jump_speed < 0 and int(foot) <= t:
                    self.move((0, t - foot))
                    self.state = Player.RUNNING
                    self.jump_speed = 0

    def get_platform(self, foot):
        selected = None
        sel_top = 0
        x, y = self.pos
        for platform in gfw.world.objects_at(gfw.layer.platform):
            l, b, r, t = platform.get_bb()
            if x < l or x > r:
                continue
            if foot < b:
                continue
            if selected is None:
                selected = platform
                sel_top = t
            else:
                if t > sel_top:
                    selected = platform
                    sel_top = t
        return selected

    def draw(self):
        rot = gobj.to_rad(self.rotation)
        self.image.composite_draw(rot, 'h', *self.pos, w=gobj.UNIT, h=gobj.UNIT)

    def get_bb(self):
        hu = gobj.UNIT // 2
        x, y = self.pos
        return x - hu, y - hu, x + hu, y + hu

    def move(self, diff):
        self.pos = gobj.point_add(self.pos, diff)

    def jump(self):
        self.jump_speed = Player.JUMP
