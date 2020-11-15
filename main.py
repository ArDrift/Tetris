#!/usr/bin/env python3

import pyconio
from control import *
from draw import *

def mainloop(shape, fsize):
  pyconio.settitle("Tetris")
  with pyconio.rawkeys():
    while True:
      field(fsize[0] + 1, fsize[1])
      shape.print()
      if pyconio.kbhit():
        key = pyconio.getch()
        pyconio.clrscr()
        if key == pyconio.UP:
          rotate(shape)
        elif key == pyconio.DOWN:
          shape.pos[1] = min(shape.pos[1] + 1, fsize[1])
        elif key == pyconio.LEFT:
          shape.pos[0] = max(shape.pos[0] - 2, 2)
        elif key == pyconio.RIGHT:
          shape.pos[0] = min(shape.pos[0] + 2, fsize[0])
        elif key == pyconio.ESCAPE:
          break
        pyconio.flush()


def main():
  fieldsize = [20, 20]
  shapes = ["I", "J", "L", "O", "S", "T", "Z"]
  pyconio.clrscr()
  elem = Tetromino("I", 10, 1)

  mainloop(elem, fieldsize)


main()
