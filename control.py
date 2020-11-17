#!/usr/bin/env python3

import pyconio

def rotate(tetro):
    """
    Rotates the tetromino clockwise.
    """
    newunits = []
    for elem in range(len(tetro.units[0])):
        newlista = []
        for lista in range(len(tetro.units) - 1, -1, -1):
            newlista.append(tetro.units[lista][elem])
        newunits.append(newlista)

    tetro.units = newunits


def control_ingame(shape, fsize):
    key = pyconio.getch()
    if key == pyconio.UP:
        rotate(shape)
    elif key == pyconio.DOWN:
        shape.pos[1] = min(shape.pos[1] + 1, fsize - 1)
    elif key == pyconio.LEFT:
        shape.pos[0] = max(shape.pos[0] - 2, 2)
    elif key == pyconio.RIGHT:
        shape.pos[0] = min(shape.pos[0] + 2, fsize)
    elif key == pyconio.ESCAPE:
        return False

    return True
