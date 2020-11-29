#!/usr/bin/env python3

import pyconio
import math

def ground(field):
    """
    Prints the playing field according to the its current state,
    indicated with box-drawing characters and block elements.
    """
    pyconio.textcolor(pyconio.WHITE)
    pyconio.gotoxy(1, 0)
    pyconio.write("╔" + "═" * len(field) + "╗")
    for line in range(len(field)):
        pyconio.gotoxy(1, line + 1)
        pyconio.textcolor(pyconio.WHITE)
        pyconio.write("║")
        for row in range(len(field[line])):
            if field[line][row] != 0:
                pyconio.textcolor(get_color(field[line][row]))
                pyconio.write("█" * 2)
            else:
                pyconio.write(" " * 2)
        pyconio.textcolor(pyconio.WHITE)
        pyconio.write("║")

    pyconio.gotoxy(1, len(field) + 1)
    pyconio.write("╚" + "═" * len(field) + "╝")


def nextsection(field, next):
    size = 10
    start_x = len(field) + size // 2
    start_y = len(field) // 2 - 3
    pyconio.gotoxy(start_x + 2, start_y - 1)
    pyconio.write("N E X T")
    pyconio.gotoxy(start_x, start_y)
    pyconio.write("╔" + "═" * (size-1) + "╗")
    for y in range((size // 2) - 1):
        pyconio.gotoxy(start_x, start_y + 1 + y)
        pyconio.write("║")
        for x in range(size - 1):
            pyconio.write(" ")
        pyconio.write("║")
    pyconio.gotoxy(start_x, start_y + size // 2)
    pyconio.write("╚" + "═" * (size-1) + "╝")

    next.pos = [(start_x + 2) // 2, start_y + 2]
    next.print()


def valsection(field, val, posy, label):
    pyconio.textcolor(pyconio.WHITE)
    pyconio.gotoxy(len(field) + len(field[0]) - len(label), posy+1)
    pyconio.write(label)
    pyconio.gotoxy(len(field) + len(field[0]), posy)
    pyconio.write("╔" + "═" * (int(math.log(max(1, val), 10)) + 1) + "╗")
    pyconio.gotoxy(len(field) + len(field[0]), posy+1)
    pyconio.write("║{}║".format(val))
    pyconio.gotoxy(len(field) + len(field[0]), posy+2)
    pyconio.write("╚" + "═" * (int(math.log(max(1, val), 10)) + 1) + "╝")


def screen(tetro, field, next, points, level):
    ground(field)
    nextsection(field, next)
    valsection(field, points, len(field)-1, "PTS:")
    valsection(field, level, len(field)-4, "LVL:")
    tetro.print()
    pyconio.flush()


def get_color(shape):
    if shape == "I":
        return pyconio.CYAN
    elif shape == "J":
        return pyconio.BLUE
    elif shape == "L":
        return pyconio.BROWN
    elif shape == "O":
        return pyconio.YELLOW
    elif shape == "S":
        return pyconio.GREEN
    elif shape == "T":
        return pyconio.MAGENTA
    elif shape == "Z":
        return pyconio.RED


class Tetromino:
    """
    This class defines a tetromino (or tetrimino as in Tetris-language):
    with its shape that consists of 4 units next to each other (0s and 1s in a 2D list),
    its color based on the standard color scheme of the Tetris game,
    and its position (X, Y integers in a list).
    """
    def __init__(self, shape, posx, posy):
        if shape == "I":
            self.units = [[1, 1, 1, 1]]
        elif shape == "J":
            self.units = [[1, 0, 0], [1, 1, 1]]
        elif shape == "L":
            self.units = [[0, 0, 1], [1, 1, 1]]
        elif shape == "O":
            self.units = [[1, 1], [1, 1]]
        elif shape == "S":
            self.units = [[0, 1, 1], [1, 1, 0]]
        elif shape == "T":
            self.units = [[0, 1, 0], [1, 1, 1]]
        elif shape == "Z":
            self.units = [[1, 1, 0], [0, 1, 1]]

        self.pos = [posx, posy]
        self.color = get_color(shape)
        self.shape = shape


    def __str__(self):
        """
        Returns the visual representation of a tetromino using Unicode block elements.
        Since the full block character has a size of 9x18 pixels (1:2 ratio),
        each unit is represented by 2 full blocks (or 2 spaces where a unit should be left out).
        """
        res = ""
        for sorszam in range(len(self.units)):
            for unit in self.units[sorszam]:
                if unit == 1:
                    res += ("█") * 2
                else:
                    res += " " * 2
            if sorszam != len(self.units) - 1:
                res += ("\n")

        return str(res)


    def print(self):
        """
        Prints the teromino to the screen.
        This method is required because of the newline character in the string.
        Using this print, the tetrominoes' new lines will be written to their proper position,
        not the beginning of the new line.
        """
        newline = 0
        newrow = 0
        start_x = self.pos[0] * 2
        start_y = self.pos[1]

        pyconio.gotoxy(start_x, start_y)
        for c in str(self):
            if c == "\n":
                newline += 1
                newrow = 0
                pyconio.gotoxy(start_x, start_y + newline)
            elif c == " ":
                newrow += 1
                pyconio.gotoxy(start_x + newrow, start_y + newline)
            else:
                pyconio.textcolor(self.color)
                pyconio.write(c)

def cursor(show):
    csi = "\033["
    if show:
        print(csi + "?25h")
    else:
        print(csi + "?25l")


def print_field(field):
    pyconio.gotoxy(1, len(field) + 2)
    print("  ", end="")
    pyconio.textcolor(pyconio.WHITE)
    for i in range(len(field[0])):
        print(i, end=" ")
    print("")
    for l in range(len(field)):
        pyconio.textcolor(pyconio.WHITE)
        print("{:2}".format(l), end=" ")
        for r in range(len(field[l])):
            if field[l][r] != 0:
                pyconio.textcolor(get_color(field[l][r]))
            else:
                pyconio.textcolor(pyconio.DARKGRAY)
            print("{}".format(field[l][r]), end=" ")
        print("")
