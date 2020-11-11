from pico2d import *
import gobj
import gfw
from platformer import Platformer

UNIT_PER_LINE = 100
SCREEN_LINES = 10
BLOCK_SIZE = gobj.UNIT

lines = []


def load(file):
    global lines, current_x, create_at, map_index
    with open(file, 'r') as f:
        lines = f.readlines()
    current_x = 0
    map_index = 0
    create_at = get_canvas_width() + 2 * BLOCK_SIZE


def count():
    """ stage 파일의 라인 수 """
    return len(lines) // SCREEN_LINES * UNIT_PER_LINE


def update(dx):
    global current_x, create_at
    current_x += dx
    while current_x < create_at:
        create_column()


def create_column():
    global current_x, map_index
    y = BLOCK_SIZE // 2;
    for row in range(SCREEN_LINES):
        ch = get(map_index, row)
        create_object(ch, current_x, y)
        y += BLOCK_SIZE
    current_x += BLOCK_SIZE
    map_index += 1


def create_object(ch, x, y):
    if ch in ['O', 'P']:
        dy = 3
        y -= dy * BLOCK_SIZE // 2
        x -= BLOCK_SIZE // 2
        obj = Platformer(ord(ch) - ord('O'), x, y)
        gfw.world.add(gfw.layer.platform, obj)


def get(x, y):
    col = x % UNIT_PER_LINE
    row = x // UNIT_PER_LINE * SCREEN_LINES + SCREEN_LINES - 1 - y
    return lines[row][col]
