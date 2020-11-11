from pico2d import *
import gfw
from gobj import res
import main_state

canvas_width = main_state.canvas_width
canvas_height = main_state.canvas_height

center_x = canvas_width // 2
center_y = canvas_height // 2


def enter():
    global background, files, file_index, elapsed, bgm
    background = gfw.image.load(res('loading_screen.jpg'))

    bgm = gfw.sound.load('Assets/loading.ogg')
    bgm.set_volume(64)
    bgm.repeat_play()

    import asset_to_json
    files = []
    with open('assets.json') as f:
        data = json.load(f)
        for i in data:
            for v in data[i]:
                files.append(v)
    file_index = 0
    elapsed = 0


def exit():
    global background
    gfw.image.unload(res('loading_screen,jpg'))
    del background

    bgm.stop()

def update():
    global file_index, elapsed

    elapsed += gfw.delta_time

    if file_index < len(files):
        file = files[file_index]
        extension = file.split('.')[1]
        if extension in ['jpg', 'png']:
            gfw.image.load(file)
        elif extension in ['mp3', 'wav', 'ogg']:
            gfw.sound.load(file)
        file_index += 1
        print(f"Load file: {file}")
    else:
        return


def draw():
    background.draw(center_x, center_y, w=canvas_width, h=canvas_height)


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
