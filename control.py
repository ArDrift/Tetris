#!/usr/bin/env python3

def rotate(tetro):
  newunits = []
  for elem in range(len(tetro.units[0])):
    newlista = []
    for lista in range(len(tetro.units) - 1, -1, -1):
      newlista.append(tetro.units[lista][elem])
    newunits.append(newlista)
      
  tetro.units = newunits


def move(tetro, irany):
  if irany == "f":
    tetro.pos[1] -= 1
  elif irany == "l":
    tetro.pos[1] += 1
  elif irany == "b":
    tetro.pos[0] -= 2
  elif irany == "j":
    tetro.pos[0] += 2


