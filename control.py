#!/usr/bin/env python3

from draw import Tetromino
import random
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


def generate_random(pos):
    shapes = ["I", "J", "L", "O", "S", "T", "Z"]
    return Tetromino(random.choice(shapes), pos[0], pos[1])


def control_ingame(tetro, fsize):
    key = pyconio.getch()
    if key == pyconio.UP:
        rotatedshape = rotate(tetro)
        if within_boundary(rotatedshape, fsize):
            tetro.units = rotatedshape.units
            rotatedshape = None
    elif key == pyconio.DOWN:
        lowershape = Tetromino(tetro.shape, tetro.pos[0], tetro.pos[1])
        lowershape.units = tetro.units
        lowershape.pos[1] += 1
        if within_boundary(lowershape, fsize):
            tetro.pos[1] += 1
            lowershape = None
    elif key == pyconio.LEFT:
        leftshape = Tetromino(tetro.shape, tetro.pos[0], tetro.pos[1])
        leftshape.units = tetro.units
        leftshape.pos[0] -= 1
        if within_boundary(leftshape, fsize):
            tetro.pos[0] -= 1
            leftshape = None
    elif key == pyconio.RIGHT:
        rightshape = Tetromino(tetro.shape, tetro.pos[0], tetro.pos[1])
        rightshape.units = tetro.units
        rightshape.pos[0] += 1
        if within_boundary(rightshape, fsize):
            tetro.pos[0] += 1
            rightshape = None
    elif key == pyconio.ESCAPE:
        return False

    return True


def within_boundary(tetro, fsize):
    # Determine relative distance from start pos
    rmost = 0
    for s in range(len(tetro.units)):
        for o in range(len(tetro.units[s])):
            if tetro.units[s][o] == 1 and o > rmost:
                rmost = o

    rmostposx = rmost + tetro.pos[0]
    lmostposy = len(tetro.units) - 1 + tetro.pos[1]

    # Outside of x or outside of y
    if tetro.pos[0] <= 0 or rmostposx > fsize // 2 or lmostposy > fsize:
        return False

    return True
