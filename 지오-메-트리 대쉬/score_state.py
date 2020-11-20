from pico2d import *
import gfw
import main_state

canvas_width = main_state.canvas_width
canvas_height = main_state.canvas_height

center_x = canvas_width // 2
center_y = canvas_height // 2


def enter():
    global bg, bgm
    bg = gfw.image.load('Assets/loading_screen.jpg')

    bgm = load_music('Assets/applause.wav')
    bgm.set_volume(64)
    bgm.repeat_play()


def exit():
    global bg, bgm
    gfw.image.unload('Assets/loading_screen.jpg')
    del bg
    bgm.stop()
    del bgm


def update():
    pass


def draw():
    bg.draw(center_x, center_y, w=canvas_width, h=canvas_height)


def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()
        if e.key == SDLK_RETURN or e.key == SDLK_KP_ENTER:
            gfw.change(main_state)


if __name__ == '__main__':
    gfw.run_main()
