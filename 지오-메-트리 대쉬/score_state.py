from pico2d import *
import gfw
import main_state
import gobj

canvas_width = gobj.CANVAS_WIDTH
canvas_height = gobj.CANVAS_HEIGHT

center_x = canvas_width // 2
center_y = canvas_height // 2


def enter():
    global bg, bgm, font
    bg = gfw.image.load('Assets/score_screen.png')

    bgm = load_music('Assets/applause.wav')
    bgm.set_volume(64)
    bgm.play()

    font = gfw.font.load('Assets/Maplestory Bold.ttf', 25)


def exit():
    global bg, bgm
    gfw.image.unload('Assets/score_screen.png')
    del bg
    bgm.stop()
    del bgm


def update():
    pass


def draw():
    bg.draw(center_x, center_y, w=canvas_width, h=canvas_height)
    font.draw(get_canvas_width() - 200, get_canvas_height() - 50, f'시도 횟수: {attempt}', (0, 255, 255))


def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()
        if e.key == SDLK_RETURN or e.key == SDLK_KP_ENTER:
            gfw.change(main_state)


def set_attempt(tries):
    global attempt
    attempt = tries


if __name__ == '__main__':
    gfw.run_main()
