#!/usr/bin/env python3

import pyconio

def draw_field(field):
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


def draw_screen(tetro, field):
   pyconio.clrscr()
   draw_field(field)
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

        return "{}{}".format(pyconio.textcolors[self.color], res)


    def print(self):
        """
        Prints the teromino to the screen.
        This method is required because of the newline character in the string.
        Using this print, the tetrominoes' new lines will be written to their proper position,
        not the beginning of the new line.
        """
        ujsor = 0
        pyconio.gotoxy(self.pos[0] * 2, self.pos[1])
        for c in str(self):
            if c == "\n":
                ujsor += 1
                pyconio.gotoxy(self.pos[0] * 2, self.pos[1] + ujsor)
            else:
                pyconio.write(c)


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
