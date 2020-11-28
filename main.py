#!/usr/bin/env python3

import pyconio
import time
import math
import control
import draw

def mainloop(tetro, field, next, points):
    """
    Prints the field and the shape selected in main, in its given position,
    then you can control it with UP-DOWN-LEFT-RIGHT as in the Tetris game.
    You can quit with the ESCAPE key.
    """
    pyconio.settitle("Tetris")
    game_sec = math.floor(time.time())
    draw.screen(tetro, field, next, points)
    ingame = [True, 0]

    with pyconio.rawkeys():
        while ingame[0]:
            current_sec = math.floor(time.time())
            if pyconio.kbhit():
                ingame = control.ingame(tetro, field)
                points += ingame[1]
                draw.screen(tetro, field, next, points)
            # Fall mechanism
            if current_sec == game_sec:
                if control.move_valid(control.post_move(tetro, "down"), field):
                    if control.hit(control.post_move(tetro, "down"), field):
                        if tetro.pos[1] >= 1:
                            last = tetro
                            next.pos = [5,0]
                            tetro = next
                            next = control.store_regen(last, field, next)
                        else:
                            ingame = [False, points]
                    else:
                        tetro.pos[1] += 1
                else:
                    last = tetro
                    next.pos = [5,0]
                    tetro = next
                    next = control.store_regen(last, field, next)
                game_sec += 1
                draw.screen(tetro, field, next, points)
            if control.line_full(field):
                points += control.delete_full(field)
                draw.screen(tetro, field, next, points)


def main():
    fieldsize = 20
    field = control.make_field(fieldsize)
    next = control.make_random([fieldsize * 2,0])
    points = 0
    mainloop(control.make_random([5,0]), field, next, points)


main()
