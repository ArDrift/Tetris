#!/usr/bin/env python3

import pyconio

def field(w, h):
  pyconio.clrscr()
  for y in range(h + 1):
    for x in range(2):
      pyconio.gotoxy(x*w, y + 1)
      pyconio.write("║")
   
    pyconio.write("\n")
    
  pyconio.gotoxy(0, h + 1)
  pyconio.write("╚")
  for x in range(w - 1):
    pyconio.write("═")
  pyconio.write("╝")
  
  pyconio.write("\n")
  
  pyconio.flush()


class Tetromino:
  def __init__(self, shape):
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


def rotate(self):
  newunits = []
  for elem in range(len(self.units[0])):
    newlista = []
    for lista in range(len(self.units) - 1, -1, -1):
      newlista.append(self.units[lista][elem])
    newunits.append(newlista)
      
  self.units = newunits
  return self


def mainloop(shape):
  tet = shape
  with pyconio.rawkeys():
    while True:
      if pyconio.kbhit():
        key = pyconio.getch()
        if key == pyconio.UP:
          pyconio.clrscr()
          for i in range(len(tet)):
            pyconio.gotoxy(0, i * 5)
            pyconio.write(rotate(tet[i]))
          pyconio.flush()
        elif key == pyconio.ESCAPE:
          break


def main():
  shapes = ["I", "J", "L", "O", "S", "T", "Z"]
  #field(20 + 1, 20)
  pyconio.clrscr()
  elemek = []
  for shape in shapes:
    elemek.append(Tetromino(shape))
  #for e in range(len(elemek)):
  #  pyconio.gotoxy(0, e * 5)
  #  pyconio.write(rotate(elemek[e]) ,end="\n")
  #pyconio.flush()
  mainloop(elemek)


main()
