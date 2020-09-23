import random
import curses

s = curses.initscr()
curses.curs_set(0) # Set curser to zero so it doesn't show up on the screen
sh, sw = s.getmaxyx() # Height and width
w = curses.newwin(sh, sw, 0, 0) # Create new window
w.keypad(1) # Accepts keypad input
w.timeout(100) # This re-freshes the screen every 100 mili-seconds

snake_x = sw/3 # Snake's initial position
snake_y = sh/2
snake = [
    [snake_y, snake_x],
    [snake_y, snake_x - 1],
    [snake_y, snake_x - 2]
]

food = [sh/2, sw/2]
w.addch(food[0], food[1], curses.ACS_PI)

key = curses.KEY_RIGHT # Initial snake direction

while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key # This will either give us nothing or the next key

    if snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1:]:
        curses.endwin() # kills window
        quit()
    
    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)

    # If the snake runs into the food
    if snake[0] == food:
        food = None
        while food is None:
            nf = [
                random.randint(1, sh - 1),
                random.randint(1, sw - 1)
            ]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        w.addch(tail[0], tail[1], ' ')

    w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
