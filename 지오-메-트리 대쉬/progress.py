from pico2d import *
import gfw
import gobj

MAX_LEN = 500
START_XPOS = 150

def init():
    global images, time, frame, FPS, x, btn_bg, btn_fg
    images = []
    images.append(gfw.image.load('Assets/cat_1.png'))
    images.append(gfw.image.load('Assets/cat_2.png'))
    images.append(gfw.image.load('Assets/cat_3.png'))

    time = 0
    frame = 0
    FPS = 6
    x = START_XPOS
    btn_bg = gfw.image.load('Assets/pg_bg.png')
    btn_fg = gfw.image.load('Assets/pg_fg.png')


def update():
    global images, time, frame, FPS
    time += gfw.delta_time
    frame = round(time * FPS) % len(images)


def draw():
    images[frame].composite_draw(0, 'h', x, gobj.CANVAS_HEIGHT - 40, w=40, h=40)
    btn_bg.draw_to_origin(START_XPOS, gobj.CANVAS_HEIGHT - 70, w=MAX_LEN, h=5)
    btn_fg.draw_to_origin(START_XPOS, gobj.CANVAS_HEIGHT - 70, w=x-START_XPOS, h=5)


def handle_event(e):
    pass


def move(cur, total):
    global x
    x = START_XPOS + (cur / total) * MAX_LEN
