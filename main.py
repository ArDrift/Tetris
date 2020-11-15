#!/usr/bin/env python3

import pyconio
from control import *
from draw import *

def mainloop(shape):
  pyconio.settitle("Tetris")
  with pyconio.rawkeys():
    while True:
      field(20 + 2, 20)
      shape.print()
      if pyconio.kbhit():
        key = pyconio.getch()
        pyconio.clrscr()
        if key == pyconio.UP:
          rotate(shape)
        elif key == pyconio.DOWN:
          move(shape, "l")
        elif key == pyconio.LEFT:
          move(shape, "b")
        elif key == pyconio.RIGHT:
          move(shape, "j")
        elif key == pyconio.ESCAPE:
          break
      pyconio.flush()


def main():
  shapes = ["I", "J", "L", "O", "S", "T", "Z"]
  #field(20 + 2, 20)
  pyconio.clrscr()
  elem = Tetromino("I", 10, 1)

  mainloop(elem)


main()
