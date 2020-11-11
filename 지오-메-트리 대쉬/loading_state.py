from pico2d import *
import gfw
from gobj import res


def enter():
    global background, files
    background = gfw.image.load(res('loading_screen.jpg'))

    import asset_to_json
    files = []
    with open('assets.json') as f:
        data = json.load(f)
        for i in data:
            for v in data[i]:
                files.append(v)


def exit():
    global background
    gfw.image.unload(res('loading_screen,jpg'))
    del background


def update():
    pass


def draw():
    background.draw(400, 300, w=800, h=600)


def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()


if __name__ == '__main__':
    gfw.run_main()
