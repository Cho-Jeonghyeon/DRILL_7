from pico2d import *
import random


# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)
        pass

    def update(self):
        pass


class Boy:
    def __init__(self):
        self.x = random.randint(100,700)
        self.y = 90
        self.image = load_image('run_animation.png')
        self.frame = random.randint(0,7)

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

    def update(self):
        self.x += 5
        self.frame = (self.frame + 1) % 8

class Zombie:
    def __init__(self):
        self.x, self.y = 100,170
        self.frame = 0
        self.image = load_image('zombie_run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 10
        self.x += 5

    def draw(self):
        frame_width = self.image.w //10
        frame_height = self.image.h
        self.image.clip_draw(self.frame * frame_width, 0, frame_width, frame_height,
                             self.x, self.y, frame_width//2, frame_height//2)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def reset_world():
    global running
    global grass
    global team
    running = True
    grass = Grass()
    team = [Boy() for i in range(10)]


def update_world():
    grass.update()
    for boy in team:
       boy.update()


def render_world():
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    update_canvas()
    pass


open_canvas()

reset_world()
running = True
while running:
    handle_events()
    #게임로직
    update_world()
    #렌더링
    render_world()
    delay(0.05)

close_canvas()
