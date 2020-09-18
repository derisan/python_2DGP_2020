from pico2d import *
import helper


# Game object class here
class Grass:
	def __init__(self):
		self.image = load_image("../res/grass.png")

	def draw(self):
		self.image.draw(400, 30)


class Boy:
	def __init__(self):
		self.x, self.y = get_canvas_width() // 2, 85
		self.frame = 0
		self.image = load_image("../res/run_animation.png")
		self.delta = 0
		self.speed = 0

	def update(self):
		global target
		self.frame = (self.frame + 1) % 8
		self.delta = helper.delta((self.x, self.y), (target[0], target[1]), self.speed)
		result = helper.move_toward((self.x, self.y), (self.delta[0], self.delta[1]), (target[0], target[1]))

		if result[1] is True:
			self.speed = 0
		else:
			self.x = result[0][0]
			self.y = result[0][1]

	def speedup(self):
		self.speed += 1

	def draw(self):
		self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


def handle_events():
	global running, target, boy
	for event in get_events():
		if event.type == SDL_QUIT:
			running = False
		elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
			running = False
		elif (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
			target[0] = event.x
			target[1] = get_canvas_height() - event.y - 1
			boy.speedup()


# initialization code
open_canvas()
boy = Boy()
grass = Grass()

target = [get_canvas_width() // 2, 85]

running = True
while running:
	clear_canvas()

	handle_events()

	boy.update()

	grass.draw()
	boy.draw()
	update_canvas()

	delay(0.016)

# finalization code
close_canvas()
