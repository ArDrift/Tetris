#!/usr/bin/env python3

import pyconio
import time
import math
from control import *
from draw import *

def mainloop(tetro, field, next):
    """
    Prints the field and the shape selected in main, in its given position,
    then you can control it with UP-DOWN-LEFT-RIGHT as in the Tetris game.
    You can quit with the ESCAPE key.
    """
    pyconio.settitle("Tetris")
    game_sec = math.floor(time.time())
    draw_screen(tetro, field, next)
    ingame = True

    with pyconio.rawkeys():
        while ingame:
            current_sec = math.floor(time.time())
            if pyconio.kbhit():
                ingame = control_ingame(tetro, field)
                draw_screen(tetro, field, next)
            # Fall mechanism
            if move_valid(post_move(tetro, "down"), field)[0]:
                if current_sec == game_sec:
                    if hit_tetro(post_move(tetro, "down"), field):
                        last = tetro
                        next.pos = [5,0]
                        tetro = next
                        next = store_regen(last, field, next)
                    else:
                        tetro.pos[1] += 1
                    game_sec += 1
                    draw_screen(tetro, field, next)
            else:
                last = tetro
                next.pos = [5,0]
                tetro = next
                next = store_regen(last, field, next)
            if line_full(field):
                delete_full(field)
                draw_screen(tetro, field, next)
        #print_field(field)


def main():
    fieldsize = 20
    field = make_field(fieldsize)
    next = make_random([fieldsize * 2,0])
    mainloop(make_random([5,0]), field, next)


main()
