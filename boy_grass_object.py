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
        self.x = random.randint(0,700)
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
        self.x = random.randint(0, 700)
        self.y = 90
        self.frame = random.randint(0,7)
        self.image = load_image('zombie_run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 10
        self.x += 5

    def draw(self):
        frame_width = self.image.w //10
        frame_height = self.image.h
        self.image.clip_draw(self.frame * frame_width, 0, frame_width, frame_height,
                             self.x, self.y, frame_width//5.9, frame_height//5.9)


class Ball:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 599
        size = random.choice(['small', 'big'])
        if size == 'small':
          self.image = load_image('ball21x21.png')
        elif size == 'big':
            self.image = load_image('ball41x41.png')
        self.speed = random.randint(4, 13)

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.y -= self.speed
        if self.y <= 60 + self.image.h / 2 - 6:
            self.y = 60 + self.image.h / 2 - 6
            self.speed = 0



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
    global world

    running = True
    world = []

    grass = Grass()
    world.append(grass)

    team = [Boy() for i in range(11)] + [Zombie() for i in range(4)]
    world+=team

    ball = [Ball() for i in range(20)]
    world+=ball


def update_world():

    for o in world:
        o.update()

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()


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
