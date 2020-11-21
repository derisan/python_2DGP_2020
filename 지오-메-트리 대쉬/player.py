from typing import Tuple

from pico2d import *

import gfw
import gobj
from platformer import Platformer


class Player:
    KEYDOWN_SPACE = (SDL_KEYDOWN, SDLK_SPACE)

    RUNNING, FALLING, JUMPING, DEAD = range(4)
    GRAVITY = 3000
    JUMP = 600

    def __init__(self):
        self.pos = 150, 100
        self.delta: Tuple[float, float] = 0, 0
        self.image = gfw.image.load('Assets/cube.png')
        self.time = 0
        self.jump_speed = 0
        self.rotation = 0
        self.state = Player.RUNNING
        self.n_die = 0
        self.jump_sound = load_wav('Assets/jump.wav')

    def handle_event(self, e):
        pair = e.type, e.key
        if pair == Player.KEYDOWN_SPACE:
            self.jump()

    def update(self):
        if self.state == Player.DEAD:
            return

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
            elif self.state != Player.RUNNING:
                if self.jump_speed < 0 and int(foot) <= t:
                    self.move((0, t - foot))
                    self.state = Player.RUNNING
                    self.jump_speed = 0
                    if platform.type == Platformer.JUMP:
                        self.force_to_jump()

        if self.is_fall():
            self.die()

    def get_platform(self, foot):
        selected = None
        sel_top = 0
        x, y = self.pos
        for platform in gfw.world.objects_at(gfw.layer.platform):
            l, b, r, t = platform.get_bb()
            if x < l or x > r:
                continue
            mid = (b + t) // 2
            if foot < mid:
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
        if self.state == Player.FALLING or self.state == Player.JUMPING:
            return
        if self.state == Player.RUNNING:
            self.state = Player.JUMPING
        self.jump_speed = Player.JUMP
        self.rotation -= 90
        self.jump_sound.play()

    def force_to_jump(self):
        self.state = Player.JUMPING
        self.jump_speed = Player.JUMP + 200
        self.rotation -= 90

    def die(self):
        self.state = Player.DEAD
        self.n_die += 1

    def is_fall(self):
        x, y = self.pos
        hu = gobj.UNIT // 2
        if y + hu < 0:
            return True
        return False

    def reset(self):
        self.state = Player.RUNNING
        self.pos = 150, 100
        self.jump_speed = 0
        self.rotation = 0
