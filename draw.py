#!/usr/bin/env python3

import pyconio

def field(s):
  """
  Prints a playing field indicated with box-drawing characters.
  The field's size should be specified with an integer (here s). 
  """
  pyconio.textcolor(pyconio.WHITE)
  for y in range(s):
    for x in range(2):
      pyconio.gotoxy(x*(s+1) + 1, y + 1)
      pyconio.write("║")
   
    pyconio.write("\n")
    
  pyconio.gotoxy(1, s + 1)
  pyconio.write("╚")
  for x in range(s):
    pyconio.write("═")
  pyconio.write("╝")
  
  pyconio.flush()


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
    pyconio.gotoxy(self.pos[0], self.pos[1])
    for c in str(self):
      if c == "\n":
        ujsor += 1
        pyconio.gotoxy(self.pos[0], self.pos[1] + ujsor)
      else:
        pyconio.write(c)


