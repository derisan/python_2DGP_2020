from pico2d import *

import gfw
import gobj
import stage_gen
from background import Background
from player import Player

canvas_width = 1200
canvas_height = 610

FONT_SIZE = 50


def enter():
    gfw.world.init(['bg', 'enemy', 'platform', 'item', 'player', 'ui'])

    bg = Background('background/stage1_bg_far.png')
    bg.speed = 10
    gfw.world.add(gfw.layer.bg, bg)

    bg = Background('background/stage1_bg_near.png')
    bg.speed = 100
    bg.y_scale = 1.75
    gfw.world.add(gfw.layer.bg, bg)

    global player
    player = Player()
    gfw.world.add(gfw.layer.player, player)

    global font
    font = gfw.font.load(gobj.res('font/Maplestory Bold.ttf'), FONT_SIZE)

    global font_meso
    font_meso = gfw.font.load(gobj.res('font/morris9.ttf'), 20)

    stage_gen.load(gobj.res('stage_01.txt'))


paused = False


def update():
    global paused
    if paused:
        return

    gfw.world.update()

    dx = -175 * gfw.delta_time
    for layer in range(gfw.layer.enemy, gfw.layer.item + 1):
        for obj in gfw.world.objects_at(layer):
            obj.move(dx)

    check_items()
    check_enemy()

    stage_gen.update(dx)


def check_items():
    for item in gfw.world.objects_at(gfw.layer.item):
        if gobj.collides_box(player, item):
            player.item_check(item)
            gfw.world.remove(item)
            break


def check_enemy():
    global player, paused
    for enemy in gfw.world.objects_at(gfw.layer.enemy):
        if gobj.collides_box(player, enemy):
            # Decrease player's hp
            player.decrease_hp()
            # Invincible for a moment after collision
            gfw.world.remove(enemy)
            break


def draw():
    gfw.world.draw()
    gobj.draw_collision_box()

    font.draw(get_canvas_width() // 2 - FONT_SIZE, get_canvas_height() - FONT_SIZE, str(player.score))
    if player.ea_score > 0:
        font_meso.draw(get_canvas_width() - 300, get_canvas_height() - 50, f'메소를 얻었습니다 (+{player.ea_score})')


def handle_event(evt):
    if evt.type == SDL_QUIT:
        gfw.quit()
        return
    elif evt.type == SDL_KEYDOWN:
        if evt.key == SDLK_ESCAPE:
            gfw.pop()
            return
        elif evt.key == SDLK_p:
            global paused
            paused = not paused

    if player.handle_event(evt):
        return


def exit():
    pass


def pause():
    global paused
    paused = True


def resume():
    global paused
    paused = False


if __name__ == '__main__':
    gfw.run_main()
