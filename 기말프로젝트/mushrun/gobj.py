import random
from typing import Tuple

from pico2d import *

import gfw

RES_DIR = './res/'


def res(file: str):
    """
    Return exact resource file path
    """
    return RES_DIR + file


def rand(val):
    """
    Return 0.9 * val ~ 1.1 * val
    """
    return val * random.uniform(0.9, 1.1)


def point_add(point1: Tuple, point2: Tuple) -> Tuple:
    """
    Return point1 + point2
    """
    x1, y1 = point1
    x2, y2 = point2
    return x1 + x2, y1 + y2


def collides_box(a, b):
    """
    Return true if two box collides
    """
    (la, ba, ra, ta) = a.get_bb()
    (lb, bb, rb, tb) = b.get_bb()

    if la > rb:
        return False
    if ra < lb:
        return False
    if ba > tb:
        return False
    if ta < bb:
        return False

    return True


def distance_sq(point1: Tuple, point2: Tuple) -> float:
    """
    Return distance(sq) between two points
    """
    x1, y1 = point1
    x2, y2 = point2
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


def distance(point1: Tuple, point2: Tuple) -> float:
    """
    Return distance between two points
    """
    return math.sqrt(distance_sq(point1, point2))


def draw_collision_box():
    """
    Draw collision box if obj has get_bb()
    """
    for obj in gfw.world.all_objects():
        if hasattr(obj, 'get_bb'):
            draw_rectangle(*obj.get_bb())


def mouse_xy(event):
    """
    Convert mouse cartesian coodinates to pico2d coord-system
    """
    return event.x, get_canvas_height() - event.y - 1


def pt_in_rect(point: Tuple, rect: Tuple) -> bool:
    """
    Return true if the point's in the rect
    """
    x, y = point
    l, b, r, t = rect

    if x < l:
        return False
    if x > r:
        return False
    if y < b:
        return False
    if y > t:
        return False

    return True


class ImageObject:
    def __init__(self, file: str, pos: Tuple):
        self.file = file
        self.image = gfw.image.load(res(file))
        self.pos = pos

    def draw(self):
        self.image.draw(*self.pos)

    def update(self):
        pass

    def __getstate__(self):
        dict = self.__dict__.copy()
        del dict['image']
        return dict

    def __setstate__(self, dict):
        self.__dict__.update(dict)
        self.image = gfw.image.load(res(self.file))


if __name__ == '__main__':
    print("This file is not supposed to be executed directly.")
