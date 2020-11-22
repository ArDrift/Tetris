#!/usr/bin/env python3

import pyconio
import time
import math
from control import *
from draw import *

def mainloop(tetro, fsize, field):
    """
    Prints the field and the shape selected in main, in its given position,
    then you can control it with UP-DOWN-LEFT-RIGHT as in the Tetris game.
    You can quit with the ESCAPE key.
    """
    pyconio.settitle("Tetris")
    game_sec = math.floor(time.time())
    draw_screen(tetro, field)
    ingame = True

    with pyconio.rawkeys():
        while ingame:
            current_sec = math.floor(time.time())
            if pyconio.kbhit():
                ingame = control_ingame(tetro, fsize)
                draw_screen(tetro, field)
            # Fall mechanism
            if within_boundary(post_move(tetro, "down"), fsize)[0]:
                if current_sec == game_sec:
                    tetro.pos[1] += 1
                    game_sec += 1
                    draw_screen(tetro, field)
            else:
                update_field(field, tetro)


def main():
    fieldsize = 20
    field = make_field(fieldsize)
    mainloop(make_random([5,0]), fieldsize, field)


main()
