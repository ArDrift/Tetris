#!/usr/bin/env python3

from draw import Tetromino
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

    rotated = Tetromino(tetro.shape, tetro.pos[0], tetro.pos[1])
    rotated.units = newunits
    return rotated


def control_ingame(shape, fsize):
    key = pyconio.getch()
    if key == pyconio.UP:
        rotatedshape = rotate(shape)
        if within_boundary(rotatedshape, fsize):
            shape.units = rotatedshape.units
            rotatedshape = None
    elif key == pyconio.DOWN:
        lowershape = Tetromino(shape.shape, shape.pos[0], shape.pos[1])
        lowershape.units = shape.units
        lowershape.pos[1] += 1
        if within_boundary(lowershape, fsize):
            shape.pos[1] = shape.pos[1] + 1#min(shape.pos[1] + 1, fsize - 1)
            lowershape = None
    elif key == pyconio.LEFT:
        leftshape = Tetromino(shape.shape, shape.pos[0], shape.pos[1])
        leftshape.units = shape.units
        leftshape.pos[0] -= 1
        if within_boundary(leftshape, fsize):
            shape.pos[0] = shape.pos[0] - 1#max(shape.pos[0] - 1, 2)
            leftshape = None
    elif key == pyconio.RIGHT:
        rightshape = Tetromino(shape.shape, shape.pos[0], shape.pos[1])
        rightshape.units = shape.units
        rightshape.pos[0] += 1
        if within_boundary(rightshape, fsize):
            shape.pos[0] = shape.pos[0] + 1#min(shape.pos[0] + 1, fsize)
            rightshape = None
    elif key == pyconio.ESCAPE:
        return False

    return True


def within_boundary(shape, fsize):
    # Determine relative distance from start pos
    rmost = 0
    for s in range(len(shape.units)):
        for o in range(len(shape.units[s])):
            if shape.units[s][o] == 1 and o > rmost:
                rmost = o

    rmostposx = rmost + shape.pos[0]
    lmostposy = len(shape.units) - 1 + shape.pos[1]

    # Outside of x or outside of y
    #print("\t RM: {} LM: {}, rmost={}".format(rmostposx, lmostposy, rmost))
    if shape.pos[0] <= 0 or rmostposx > fsize // 2 or lmostposy > fsize:
        return False

    return True
