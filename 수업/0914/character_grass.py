from pico2d import *

open_canvas()

# fill here
character = load_image('../resources/character.png')
grass = load_image('../resources/grass.png')

character.draw_now(400, 90)
grass.draw_now(400, 30)

delay(5)

close_canvas()
