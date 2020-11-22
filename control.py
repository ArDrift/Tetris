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


def make_random(pos):
    shapes = ["I", "J", "L", "O", "S", "T", "Z"]
    return Tetromino(random.choice(shapes), pos[0], pos[1])


def control_ingame(tetro, field):
    key = pyconio.getch()
    if key == pyconio.UP:
        rotatedshape = rotate(tetro)
        if not within_boundary(rotatedshape, field)[0]:
            if tetro.pos[1] < len(field) - within_boundary(rotatedshape, field)[2]:
                if tetro.pos[0] > 5:
                    tetro.pos[0] -= within_boundary(rotatedshape, field)[1]
                else:
                    tetro.pos[0] += within_boundary(rotatedshape, field)[1]
                tetro.units = rotatedshape.units
        else:
            tetro.units = rotatedshape.units
        rotatedshape = None

    elif key == pyconio.DOWN:
        if within_boundary(post_move(tetro, "down"), field)[0]:
            tetro.pos[1] += 1
    elif key == pyconio.LEFT:
        if within_boundary(post_move(tetro, "left"), field)[0]:
            tetro.pos[0] -= 1
    elif key == pyconio.RIGHT:
        if within_boundary(post_move(tetro, "right"), field)[0]:
            tetro.pos[0] += 1
    elif key == pyconio.ESCAPE:
        return False

    return True


def post_move(tetro, dir):
    postshape = Tetromino(tetro.shape, tetro.pos[0], tetro.pos[1])
    postshape.units = tetro.units
    if dir == "down":
        postshape.pos[1] += 1
    elif dir == "left":
        postshape.pos[0] -= 1
    elif dir == "right":
        postshape.pos[0] += 1

    return postshape


def within_boundary(tetro, field):
    # Determine relative distance from start pos
    rmost = 0
    for s in range(len(tetro.units)):
        for o in range(len(tetro.units[s])):
            if tetro.units[s][o] == 1 and o > rmost:
                rmost = o

    rmostposx = rmost + tetro.pos[0]
    lmostposy = len(tetro.units) - 1 + tetro.pos[1]

    # Outside of x or outside of y
    if tetro.pos[0] <= 0 or rmostposx > len(field[0]) or lmostposy > len(field):
        return [False, rmost, lmostposy - tetro.pos[1]]

    return [True]


def make_field(fsize):
    linelist = []
    rowlist = []
    for line in range(fsize):
        for row in range(fsize // 2):
            rowlist.append(0)
        linelist.append(rowlist)
        rowlist = []

    return linelist


def update_field(field, tetro):
    for line in range(len(tetro.units)):
        for row in range(len(tetro.units[line])):
            if tetro.units[line][row] == 1:
                field[tetro.pos[1] + line - 1][tetro.pos[0] + row - 1] = tetro.shape

    return field
