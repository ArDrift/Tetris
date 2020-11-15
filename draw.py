#!/usr/bin/env python3

import pyconio

def field(w, h):
  for y in range(h + 1):
    for x in range(0, 2):
      pyconio.gotoxy(x*w + 1, y + 1)
      pyconio.write("║")
   
    pyconio.write("\n")
    
  pyconio.gotoxy(1, h + 1)
  pyconio.write("╚")
  for x in range(w - 1):
    pyconio.write("═")
  pyconio.write("╝")
  
  pyconio.flush()


class Tetromino:
  def __init__(self, shape, posx, posy):
    if shape == "I":
      self.units = [[1, 1, 1, 1]]
      self.color = pyconio.CYAN
    elif shape == "J":
      self.units = [[1, 0, 0], [1, 1, 1]]
      self.color = pyconio.BLUE
    elif shape == "L":
      self.units = [[0, 0, 1], [1, 1, 1]]
      self.color = pyconio.BROWN
    elif shape == "O":
      self.units = [[1, 1], [1, 1]]
      self.color = pyconio.YELLOW
    elif shape == "S":
      self.units = [[0, 1, 1], [1, 1, 0]]
      self.color = pyconio.GREEN
    elif shape == "T":
      self.units = [[0, 1, 0], [1, 1, 1]]
      self.color = pyconio.MAGENTA
    elif shape == "Z":
      self.units = [[1, 1, 0], [0, 1, 1]]
      self.color = pyconio.RED
      
    self.pos = [posx, posy]


  def __str__(self):
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
    ujsor = 0
    pyconio.gotoxy(self.pos[0], self.pos[1])
    for c in str(self):
      if c == "\n":
        ujsor += 1
        pyconio.gotoxy(self.pos[0], self.pos[1] + ujsor)
      else:
        pyconio.write(c)


