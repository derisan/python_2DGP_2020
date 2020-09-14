from pico2d import *

open_canvas()

grass = load_image('../resources/grass.png')
character = load_image('../resources/character.png')

# fill here

x = 0
while x < 800:
	clear_canvas()
	x += 2
	character.draw(x, 90)
	grass.draw(400, 30)
	update_canvas()
	delay(0.01)
	get_events()

close_canvas()
