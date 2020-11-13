# Copyright (c) 2018 Czirkos Zoltan. MIT license, see LICENSE file.

import colorama

BLACK = 0
BLUE = 1
GREEN = 2
CYAN = 3
RED = 4
MAGENTA = 5
BROWN = 6       # this may be dark yellow on your terminal
LIGHTGRAY = 7
DARKGRAY = 8
LIGHTBLUE = 9
LIGHTGREEN = 10
LIGHTCYAN = 11
LIGHTRED = 12
LIGHTMAGENTA = 13
YELLOW = 14
LIGHTYELLOW = YELLOW
WHITE = 15
RESET = -1

textcolors = {
    BLACK: colorama.ansi.Fore.BLACK,
    BLUE: colorama.ansi.Fore.BLUE,
    GREEN: colorama.ansi.Fore.GREEN,
    CYAN: colorama.ansi.Fore.CYAN,
    RED: colorama.ansi.Fore.RED,
    MAGENTA: colorama.ansi.Fore.MAGENTA,
    BROWN: colorama.ansi.Fore.YELLOW,
    LIGHTGRAY: colorama.ansi.Fore.WHITE,
    DARKGRAY: colorama.ansi.Fore.LIGHTBLACK_EX,
    LIGHTBLUE: colorama.ansi.Fore.LIGHTBLUE_EX,
    LIGHTGREEN: colorama.ansi.Fore.LIGHTGREEN_EX,
    LIGHTCYAN: colorama.ansi.Fore.LIGHTCYAN_EX,
    LIGHTRED: colorama.ansi.Fore.LIGHTRED_EX,
    LIGHTMAGENTA: colorama.ansi.Fore.LIGHTMAGENTA_EX,
    YELLOW: colorama.ansi.Fore.LIGHTYELLOW_EX,
    WHITE: colorama.ansi.Fore.LIGHTWHITE_EX,
    RESET: colorama.ansi.Fore.RESET,
}

backgroundcolors = {
    BLACK: colorama.ansi.Back.BLACK,
    BLUE: colorama.ansi.Back.BLUE,
    GREEN: colorama.ansi.Back.GREEN,
    CYAN: colorama.ansi.Back.CYAN,
    RED: colorama.ansi.Back.RED,
    MAGENTA: colorama.ansi.Back.MAGENTA,
    BROWN: colorama.ansi.Back.YELLOW,
    LIGHTGRAY: colorama.ansi.Back.WHITE,
    DARKGRAY: colorama.ansi.Back.LIGHTBLACK_EX,
    LIGHTBLUE: colorama.ansi.Back.LIGHTBLUE_EX,
    LIGHTGREEN: colorama.ansi.Back.LIGHTGREEN_EX,
    LIGHTCYAN: colorama.ansi.Back.LIGHTCYAN_EX,
    LIGHTRED: colorama.ansi.Back.LIGHTRED_EX,
    LIGHTMAGENTA: colorama.ansi.Back.LIGHTMAGENTA_EX,
    YELLOW: colorama.ansi.Back.LIGHTYELLOW_EX,
    WHITE: colorama.ansi.Back.LIGHTWHITE_EX,
    RESET: colorama.ansi.Back.RESET,
}
