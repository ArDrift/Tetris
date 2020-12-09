#!/usr/bin/env python3

import pyconio
import platform

def ground(field):
    """
    Prints the playing field (matrix) in its current state.
    Boundaries are indicated with box-drawing characters,
    and tetrominos with block elements.
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
    """
    Prints a section containing the tetromino to come,
    after the current one is placed.
    The box's position depends on the matrix's size.
    """
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
    """
    Prints a section that is used for displaying the points and levels,
    as both the label and value should be given as parameters,
    in addition to the y position of the box.
    The box scales with the value's length, and has a height of 1 unit.
    """
    pyconio.textcolor(pyconio.WHITE)
    pyconio.gotoxy(len(field) + len(field[0]) - len(label), posy+1)
    pyconio.write(label)
    pyconio.gotoxy(len(field) + len(field[0]), posy)
    pyconio.write("╔" + "═" * len(str(val)) + "╗")
    pyconio.gotoxy(len(field) + len(field[0]), posy+1)
    pyconio.write("║{}║".format(val))
    pyconio.gotoxy(len(field) + len(field[0]), posy+2)
    pyconio.write("╚" + "═" * len(str(val)) + "╝")


def screen(tetro, field, next, points, level):
    """
    Prints the ingame screen to the terminal, consisting of the matrix,
    size-, points- and level sections, and the active tetromino.
    """
    ground(field)
    nextsection(field, next)
    valsection(field, len(field), 1, "SIZE:")
    valsection(field, points, len(field)-1, "PTS:")
    valsection(field, level, len(field)-4, "LVL:")
    tetro.print()
    pyconio.flush()


def get_color(shape):
    """
    Getter function used to create tetrominos
    and recreate the matrix from a saved game, based on its letters.
    """
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


class Shape:
    """
    This class enables tetromino creation based on letters,
    to be able to identify them more easily.
    """
    def __init__(self, letter):
        if letter == "I":
             self.units = [[1, 1, 1, 1]]
        elif letter == "J":
            self.units = [[1, 0, 0], [1, 1, 1]]
        elif letter == "L":
            self.units = [[0, 0, 1], [1, 1, 1]]
        elif letter == "O":
            self.units = [[1, 1], [1, 1]]
        elif letter == "S":
            self.units = [[0, 1, 1], [1, 1, 0]]
        elif letter == "T":
            self.units = [[0, 1, 0], [1, 1, 1]]
        elif letter == "Z":
            self.units = [[1, 1, 0], [0, 1, 1]]


class Tetromino:
    """
    This class defines a tetromino (or tetrimino as in Tetris-language):
    with its shape that consists of 4 units,
    next to each other (0s and 1s in a 2D list),
    its color based on the standard color scheme of the Tetris game,
    and its position (X, Y integers in a list).
    """
    def __init__(self, letter, posx, posy):
        self.units = Shape(letter).units
        self.pos = [posx, posy]
        self.color = get_color(letter)
        self.shape = letter


    def __str__(self):
        """
        Returns the visual representation of a tetromino,
        using Unicode block elements.
        Since the full block character has a size of 9x18 pixels (1:2 ratio),
        each unit is represented by 2 full blocks,
        or 2 spaces where a unit should be left out.
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

        return res


    def print(self):
        """
        Prints the teromino to the screen.
        This method is required because of the newline character in the string.
        Using this print, the tetrominoes' new lines
        will be written to their proper position,
        not to the beginning of the new line.
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
    """
    Sends the ANSI escape sequence for hiding the terminal cursor.
    Since this is not supported by the default Windows console,
    there's no need to send anything.
    """
    if platform.system() != "Windows":
        csi = "\033["
        if show:
            print(csi + "?25h")
        else:
            print(csi + "?25l")


def logo(file="logo.txt"):
    """
    Prints the content of the given file under logos/ (or logo.txt as default),
    used for printing the title Tetris (in Russian), with the original colors.
    To use different colors for printing, a pipe character must be used as
    separator between different sections.
    """
    pyconio.gotoxy(0,5)
    colors = [pyconio.RED,pyconio.BROWN,pyconio.YELLOW,
              pyconio.GREEN,pyconio.CYAN,pyconio.MAGENTA]
    with open("logos/{}".format(file), "rt", encoding="utf-8") as logo:
        for line in logo:
            letters = line.rstrip("\n").split("|")
            for letter in range(len(letters)):
                pyconio.textcolor(colors[letter])
                pyconio.write(letters[letter])
            pyconio.write("\n")

    pyconio.flush()
    pyconio.textbackground(pyconio.RESET)
    pyconio.textcolor(pyconio.RESET)
