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
        if not move_valid(rotatedshape, field)[0]:
            # If rotated is within Y
            if tetro.pos[1] < len(field) - len(rotatedshape.units)-1:
                rotatedshape.pos[0] -= move_valid(rotatedshape, field)[1]
                if not hit_tetro(rotatedshape, field):
                    tetro.pos[0] = rotatedshape.pos[0]
                    tetro.units = rotatedshape.units
        elif not hit_tetro(rotatedshape, field):
            tetro.units = rotatedshape.units
        rotatedshape = None

    elif key == pyconio.DOWN:
        if move_valid(post_move(tetro, "down"), field)[0] and \
        not hit_tetro(post_move(tetro, "down"), field):
            tetro.pos[1] += 1
    elif key == pyconio.LEFT:
        if move_valid(post_move(tetro, "left"), field)[0] and \
        not hit_tetro(post_move(tetro, "left"), field):
            tetro.pos[0] -= 1
    elif key == pyconio.RIGHT:
        if move_valid(post_move(tetro, "right"), field)[0] and \
        not hit_tetro(post_move(tetro, "right"), field):
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


def move_valid(tetro, field):
    rmost = 0
    # Lower most y position
    lmostposy = len(tetro.units) - 1 + tetro.pos[1]
    for line in range(len(tetro.units)):
        for row in range(len(tetro.units[line])):
            # Determine rightmost unit's index
            if tetro.units[line][row] == 1 and row > rmost:
                rmost = row

    rmostposx = rmost + tetro.pos[0]
    # Outside of field (x or y)
    if tetro.pos[0] <= 0 or rmostposx > len(field[0]) or lmostposy > len(field):
        return [False, rmost]

    return [True]


def hit_tetro(tetro, field):
    for line in range(len(tetro.units)):
        for row in range(len(tetro.units[line])):
            #Check for conflicting already placed tetromino
            if tetro.units[line][row] == 1 and \
            field[tetro.pos[1] + line - 1][tetro.pos[0] + row - 1] != 0:
                return True
    return False


def make_field(fsize):
    linelist = []
    rowlist = []
    for line in range(fsize):
        for row in range(fsize // 2):
            rowlist.append(0)
        linelist.append(rowlist)
        rowlist = []

    return linelist


def update_field(tetro, field):
    for line in range(len(tetro.units)):
        for row in range(len(tetro.units[line])):
            if tetro.units[line][row] == 1:
                field[tetro.pos[1] + line - 1][tetro.pos[0] + row - 1] = tetro.shape

    return field


def store_regen(tetro, field):
    update_field(tetro, field)
    tetro = None
    return make_random([5,0])
