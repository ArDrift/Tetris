#!/usr/bin/env python3

import pyconio
import time
import math
from control import *
from draw import *

def mainloop(shape, fsize):
    """
    Prints the field and the shape selected in main, in its given position,
    then you can control it with UP-DOWN-LEFT-RIGHT as in the Tetris game.
    You can quit with the ESCAPE key.
    """
    pyconio.settitle("Tetris")
    game_sec = math.floor(time.time())
    draw_screen(shape, fsize)
    ingame = True

    with pyconio.rawkeys():
        while ingame:
            current_sec = math.floor(time.time())
            if pyconio.kbhit():
                ingame = control_ingame(shape, fsize)
                draw_screen(shape, fsize)
            # Fall mechanism
            if within_boundary(shape, fsize - 1) and current_sec == game_sec:
                shape.pos[1] += 1
                game_sec += 1
                draw_screen(shape, fsize)
            pyconio.flush()


def main():
    fieldsize = 20
    shapes = ["I", "J", "L", "O", "S", "T", "Z"]
    pyconio.clrscr()
    elem = Tetromino("I", 5, 0)

    mainloop(elem, fieldsize)


main()
