from pico2d import *

sounds = {}


def load(file):
    global sounds
    if file in sounds:
        return sounds[file]

    if file.split('.')[1] == 'wav':
        sound = load_wav(file)
    else:
        sound = load_music(file)

    sounds[file] = sound
    return sound


def unload(file):
    global sounds
    if file in sounds:
        del sounds[file]
