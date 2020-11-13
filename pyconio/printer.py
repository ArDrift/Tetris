# Copyright (c) 2018 Czirkos Zoltan. MIT license, see LICENSE file.

import colorama
from .colors import *

def write(*args, end="", flush=False, **kwargs):
    """Same as print(), but does not start new line by default, and does
    not call flush() after prints."""
    kwargs['end'] = end
    kwargs['flush'] = flush
    print(*args, **kwargs)


def flush():
    """Send output to the terminal. To be called if many characters were
    drawn to the terminal and there was no \n at the end."""
    write(flush=True)


def gotoxy(x, y):
    """Jump to position (x, y) with the cursor. Upper left corner is (0, 0).
    Note that ANSI terminals use (1,1) for the upper left corner, so
    this is not the same as colorama.Cursor.POS()."""
    write(colorama.Cursor.POS(x+1, y+1))


def clrscr():
    """Clear the screen and return the cursor to the upper left position."""
    write(colorama.ansi.clear_screen(), colorama.Cursor.POS(1, 1))


def textcolor(idx):
    """Change text color to the one specified. See the color constants in
    the colors module."""
    write(textcolors[idx])


def textbackground(idx):
    """Change background color to the one specified. See the color constants in
    the colors module."""
    write(backgroundcolors[idx])


def settitle(title):
    """Set the title of the terminal window."""
    write(colorama.ansi.set_title(title))
