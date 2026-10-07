from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
SPEED = 10
HALF = 50

IDLE, MOVE = 0, 1
LEFT, RIGHT = 0, 1

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
dx, dy = 0, 0
direction = RIGHT
state = IDLE
frame = 0

tuk_ground = None
character = None


def handle_events():
    global running, dx, dy, direction

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dx += 1
                direction = RIGHT
            elif event.key == SDLK_LEFT:
                dx -= 1
                direction = LEFT
            elif event.key == SDLK_UP:
                dy += 1
            elif event.key == SDLK_DOWN:
                dy -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dx -= 1
            elif event.key == SDLK_LEFT:
                dx += 1
            elif event.key == SDLK_UP:
                dy -= 1
            elif event.key == SDLK_DOWN:
                dy += 1


def update():
    global x, y, state, frame

    if dx != 0 or dy != 0:
        if state != MOVE:
            state = MOVE
            frame = 0
    else:
        if state != IDLE:
            state = IDLE
            frame = 0

    x += dx * SPEED
    y += dy * SPEED

    if x < HALF:
        x = HALF
    if x > TUK_WIDTH - HALF:
        x = TUK_WIDTH - HALF
    if y < HALF:
        y = HALF
    if y > TUK_HEIGHT - HALF:
        y = TUK_HEIGHT - HALF

    frame = (frame + 1) % 8


def draw():
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    if direction == RIGHT:
        if state == IDLE:
            character.clip_draw(frame * 100, 300, 100, 100, x, y)
        else:
            character.clip_draw(frame * 100, 100, 100, 100, x, y)
    else:
        if state == IDLE:
            character.clip_draw(frame * 100, 200, 100, 100, x, y)
        else:
            character.clip_draw(frame * 100, 0, 100, 100, x, y)

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
