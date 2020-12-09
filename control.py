#!/usr/bin/env python3

from draw import Tetromino
import random
import pyconio

def rotate(tetro):
    """
    Creates a new tetromino based on the input, rotated by 90° CW,
    and returns with the rotated one.
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
    """
    Chooses a random letter from the availble ones,
    and returns with a newly created one, with the position given as parameter.
    """
    shapes = ["I", "J", "L", "O", "S", "T", "Z"]
    return Tetromino(random.choice(shapes), pos[0], pos[1])


def ingame(tetro, field):
    """
    This function handles the controlling mechanism of the given tetromino,
    based on the matrix's current state. Returns True while ingame
    and False on pause, in addition to the pluspoints (earned for moving the
    tetromino down, also called as soft drop).
    """
    pluspoints = 0
    key = pyconio.getch()
    if key == pyconio.UP:
        rotatedshape = rotate(tetro)
        if not move_valid(rotatedshape, field):
            # If rotated is within Y
            if tetro.pos[1] < len(field) - len(rotatedshape.units)-1:
                rotatedshape.pos[0] -= rightmost(rotatedshape)
                if not hit(rotatedshape, field):
                    tetro.pos[0] = rotatedshape.pos[0]
                    tetro.units = rotatedshape.units
        elif not hit(rotatedshape, field):
            tetro.units = rotatedshape.units
        rotatedshape = None

    elif key == pyconio.DOWN:
        if move_valid(post_move(tetro, "down"), field) and \
        not hit(post_move(tetro, "down"), field):
            tetro.pos[1] += 1
            pluspoints += 1
    elif key == pyconio.LEFT:
        if move_valid(post_move(tetro, "left"), field) and \
        not hit(post_move(tetro, "left"), field):
            tetro.pos[0] -= 1
    elif key == pyconio.RIGHT:
        if move_valid(post_move(tetro, "right"), field) and \
        not hit(post_move(tetro, "right"), field):
            tetro.pos[0] += 1
    elif key == pyconio.ESCAPE:
        return (False, pluspoints)

    return (True, pluspoints)


def post_move(tetro, dir):
    """
    Returns a newly created tetromino moved with 1 unit in the given direction,
    used for examining if a move is possible before moving the actual tetromino.
    """
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
    """
    Determine whether a tetromino is within the playing field or not.
    This is mostly used in conjunction with the post_move function above.
    """
    # Lower most y position
    lmostposy = len(tetro.units) - 1 + tetro.pos[1]

    rmostposx = rightmost(tetro) + tetro.pos[0]

    if tetro.pos[0] <= 0 or rmostposx > len(field[0]) or lmostposy > len(field):
        return False

    return True


def rightmost(tetro):
    """
    Returns the tetromino's rightmost unit's X position (list index),
    relative to the upper leftmost (first) unit.
    """
    rmost = 0
    for line in range(len(tetro.units)):
        for row in range(len(tetro.units[line])):
            # Determine rightmost unit's index
            if tetro.units[line][row] == 1 and row > rmost:
                rmost = row
    return rmost


def hit(tetro, field):
    """
    Determines whether there already is a placed unit on the field,
    in a position where the current tetromino also has a unit, so basically
    if a tetromino hit another one or not (used in conjunction with post_move).
    """
    for line in range(len(tetro.units)):
        for row in range(len(tetro.units[line])):
            if tetro.units[line][row] == 1 and \
            field[max(0, tetro.pos[1] + line - 1)]\
            [max(0, tetro.pos[0] + row - 1)] != 0:
                return True
    return False


def make_field(fsize):
    """
    Creates a 2D list filled with 0s, with the given size,
    in a 2:1 height:width ratio.
    """
    linelist = []
    rowlist = []
    for line in range(fsize):
        for row in range(fsize // 2):
            rowlist.append(0)
        linelist.append(rowlist)
        rowlist = []

    return linelist


def update_field(tetro, field):
    """
    Updates the field with the tetrominos' units,
    used when a tetromino gets placed.
    """
    for line in range(len(tetro.units)):
        for row in range(len(tetro.units[line])):
            if tetro.units[line][row] == 1:
                field[tetro.pos[1] + line - 1][tetro.pos[0] + row - 1] = tetro.shape

    return field


def store_regen(tetro, field, next):
    """
    Updates the field with the placed tetromino,
    and returns a randomly generated new one.
    """
    update_field(tetro, field)
    tetro = next
    next = make_random([len(field) // 4, 0])
    return next


def line_full(field):
    """
    Checks if a line is full in the matrix.
    """
    for line in field:
        if not 0 in line:
            return True
    return False


def delete_full(field):
    """
    Deletes full lines in the matrix,
    and returns pluspoints based on the no. of deleted lines.
    The pointing scheme tries to follow the usual Tetris point system.
    """
    pluspoints = 0
    for line in range(len(field)):
        if not 0 in field[line]:
            for row in range(len(field[line])):
                field[line][row] = 0
            pluspoints += 100
            for upperline in range(line - 1, -1, -1):
                for row in range(len(field[upperline])):
                    field[upperline + 1][row] = field[upperline][row]

    if pluspoints == 400:
        return pluspoints * 2
    elif pluspoints == 300:
        return pluspoints + 200
    elif pluspoints == 200:
        return pluspoints + 100
    else:
        return pluspoints


def speed_sec(level):
    """
    Returns the time interval in seconds, based on the current level.
    This is used for the fall mechanism, and to detect colliding tetrominos.
    The formula is taken from https://tetris.wiki/Marathon.
    """
    return (0.8 - ((level - 1) * 0.007)) ** (level - 1)


def save_game(tetro, field, next, points, level):
    """
    Saves the game's state, including the matrix, current and next tetromino,
    current points and level, to the save.txt, overriding an existing save.
    """
    dest = open("save.txt", "wt")
    # Field
    for line in range(len(field)):
        for row in range(len(field[line])):
            print(field[line][row], end="", file=dest)
            if row != len(field[line])-1:
                print(" ", end="", file=dest)
        print("", file=dest)
    print("", file=dest)
    # Tetro
    print(tetro.shape, tetro.pos[0], tetro.pos[1], file=dest)
    print("", file=dest)
    # Next
    print(next.shape, file=dest)
    print("", file=dest)
    # Points
    print(points, file=dest)
    print("", file=dest)
    # Level
    print(level, file=dest)
    dest.close()


def load_game(file):
    """
    Loads a save from the given file, and returns with the matrix,
    current and next tetromino, current points and level, or returns None,
    if the file was not found.
    """
    try:
        with open(file, "rt") as f:
            field = []
            section = 0
            for line in f:
                # Change section
                if line == "\n":
                    section += 1
                # Load field
                elif section == 0:
                    sor = []
                    for elem in line.rstrip("\n").split(" "):
                        if elem == "0":
                            sor.append(int(elem))
                        else:
                            sor.append(elem)
                    field.append(sor)
                # Tetro
                elif section == 1:
                    shape = line.split(" ")[0]
                    pos = [int(line.split(" ")[1]),
                           int(line.rstrip("\n").split(" ")[2])]
                # Next
                elif section == 2:
                    next = line.rstrip("\n")
                elif section == 3:
                    pts = int(line.rstrip("\n"))
                elif section == 4:
                    lvl = int(line.rstrip("\n"))
    except FileNotFoundError:
        return None


    return (field, shape, pos, next, pts, lvl)
