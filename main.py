import random
import curses

s = curses.initscr()
curses.curs_set(0)
sh, sw = s.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)

snk_x = sw/4
snk_y = sh/2

cobrinha = [
    [snk_y, snk_x],
    [snk_y-1, snk_x-1],
    [snk_y-2, snk_x-2]
]

torta = [sh/2, sw/2]
w.addch(int(torta[0]), int(torta[1]), curses.ACS_PI)

key = curses.KEY_RIGHT

while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    if cobrinha[0][0] in [0, sh] or cobrinha[0][1] in [0, sw] or cobrinha[0] in cobrinha[1:]:
        curses.endwin()
        quit()

    new_head = [cobrinha[0][0], cobrinha[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    cobrinha.insert(0, new_head)

    if cobrinha[0] == torta:
        torta = None
        while torta is None:
            nf = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            torta = nf if nf not in cobrinha else None
        w.addch(torta[0], torta[1], curses.ACS_PI)
    else:
        rabinho = cobrinha.pop()
        w.addch(int(rabinho[0]), int(rabinho[1]), ' ')

    w.addch(int(cobrinha[0][0]), int(cobrinha[0][1]), curses.ACS_CKBOARD)
