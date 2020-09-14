from pico2d import *

open_canvas()

grass = load_image('../resources/grass.png')
character = load_image('../resources/run_animation.png')

# fill here

x = 0
frame = 0
while x < 800:
	clear_canvas()
	x += 4
	grass.draw(400, 30)
	character.clip_draw(frame * 100, 0, 100, 100, x, 90)
	frame = (frame + 1) % 8
	update_canvas()
	delay(0.05)
	get_events()

close_canvas()
