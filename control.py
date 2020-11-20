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
        if not within_boundary(rotatedshape, fsize)[0]:
            if tetro.pos[1] < fsize - within_boundary(rotatedshape, fsize)[2]:
                if tetro.pos[0] > 5:
                    tetro.pos[0] -= within_boundary(rotatedshape, fsize)[1]
                else:
                    tetro.pos[0] += within_boundary(rotatedshape, fsize)[1]
                tetro.units = rotatedshape.units
        else:
            tetro.units = rotatedshape.units
        rotatedshape = None

    elif key == pyconio.DOWN:
        if within_boundary(post_move(tetro, "down"), fsize)[0]:
            tetro.pos[1] += 1
    elif key == pyconio.LEFT:
        if within_boundary(post_move(tetro, "left"), fsize)[0]:
            tetro.pos[0] -= 1
    elif key == pyconio.RIGHT:
        if within_boundary(post_move(tetro, "right"), fsize)[0]:
            tetro.pos[0] += 1
            rightshape = None

    #if not within_boundary(shape, fsize)[0] and within_boundary(shape, fsize)[2]:
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
        return [False, rmost, lmostposy - tetro.pos[1]]

    return [True]
