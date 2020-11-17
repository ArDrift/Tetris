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
    with pyconio.rawkeys():
        while True:
            field(fsize)
            shape.print()
            current_sec = math.floor(time.time())
            if pyconio.kbhit():
                key = pyconio.getch()
                pyconio.clrscr()
                if key == pyconio.UP:
                    rotate(shape)
                elif key == pyconio.DOWN:
                    shape.pos[1] = min(shape.pos[1] + 1, fsize - 1)
                elif key == pyconio.LEFT:
                    shape.pos[0] = max(shape.pos[0] - 2, 2)
                elif key == pyconio.RIGHT:
                    shape.pos[0] = min(shape.pos[0] + 2, fsize)
                elif key == pyconio.ESCAPE:
                    break
            if shape.pos[1] < fsize - 1 and current_sec == game_sec:
                pyconio.clrscr()
                shape.pos[1] += 1
                game_sec += 1
            pyconio.flush()


def main():
    fieldsize = 20
    shapes = ["I", "J", "L", "O", "S", "T", "Z"]
    pyconio.clrscr()
    elem = Tetromino("T", 10, 1)

    mainloop(elem, fieldsize)


main()
