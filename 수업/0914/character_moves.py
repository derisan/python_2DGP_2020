from pico2d import *

open_canvas()

grass = load_image('../resources/grass.png')
character = load_image('../resources/character.png')

# fill here
x = 0
while x < 800:
	x += 2
	clear_canvas_now()
	character.draw_now(x, 90)
	grass.draw_now(400, 30)
	delay(0.01)

close_canvas()
