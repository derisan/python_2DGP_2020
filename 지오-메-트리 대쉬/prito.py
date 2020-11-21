from pico2d import *
import gobj
import gfw
import random

UP, DOWN, LEFT, RIGHT = range(4)
images = []
hw, hh = gobj.CANVAS_WIDTH // 2, gobj.CANVAS_HEIGHT // 2


def init():
    global images, wrong, success, time_font
    images.append(gfw.image.load('Assets/up.png'))
    images.append(gfw.image.load('Assets/down.png'))
    images.append(gfw.image.load('Assets/left.png'))
    images.append(gfw.image.load('Assets/right.png'))

    wrong = load_wav('Assets/wrong.wav')
    wrong.set_volume(64)
    success = load_wav('Assets/success.wav')
    success.set_volume(64)

    time_font = gfw.font.load('Assets/Maplestory Bold.ttf', 25)


quiz = []
is_gen = False
time = 0


def generate():
    global is_gen, time
    is_gen = True
    num = random.randint(4, 8)
    time = num
    for i in range(num):
        quiz.append(random.randint(UP, RIGHT))


def update():
    global is_gen, time
    if is_gen:
        if len(quiz) == 0:
            is_gen = False
            success.play()
            print("success")
    time -= gfw.delta_time


def handle_event(e):
    if is_gen:
        if SDL_KEYDOWN == e.type:
            if e.key == SDLK_UP or e.key == SDLK_DOWN \
                    or e.key == SDLK_LEFT or e.key == SDLK_RIGHT:
                return check_answer(key_to_int(e.key))

    return True


def draw():
    if len(quiz) > 0:
        for i, arrow in enumerate(quiz):
            images[arrow].draw(hw - 200 + i * 60, hh)

        time_font.draw(hw - 200, hh + 50, f'남은 시간: {int(time)}', (0, 255, 0))


def check_answer(key):
    if key == quiz[0]:
        quiz.pop(0)
        return True
    else:
        wrong.play()
        print("wrong")
        return False


def key_to_int(key):
    if key == SDLK_UP:
        res = 0
    elif key == SDLK_DOWN:
        res = 1
    elif key == SDLK_LEFT:
        res = 2
    else:
        res = 3
    return res


def reset():
    global is_gen
    is_gen = False
    quiz.clear()


def is_timeover():
    if is_gen:
        if time < 0:
            wrong.play()
            return True
    return False
