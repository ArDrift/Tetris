#!/usr/bin/env python3

def rotate(tetro):
  newunits = []
  for elem in range(len(tetro.units[0])):
    newlista = []
    for lista in range(len(tetro.units) - 1, -1, -1):
      newlista.append(tetro.units[lista][elem])
    newunits.append(newlista)
      
  tetro.units = newunits
