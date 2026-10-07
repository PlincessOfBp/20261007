from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0

tuk_ground = None
character = None


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def update():
    global frame
    frame = (frame + 1) % 8


def draw():
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 300, 100, 100, x, y)
    update_canvas()


open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

while running:
    handle_events()
    update()
    draw()
    delay(0.05)

close_canvas()
