#!/usr/bin/env python3

import pyconio
import main

def print_list():
    pyconio.textcolor(pyconio.WHITE)
    pyconio.write("Játék indítása: ENTER", end="\n")
    pyconio.write("Dicsőségtábla: 1", end="\n")
    pyconio.write("Beállítások: 2", end="\n")
    pyconio.write("Kilépés: ESCAPE", end="\n")
    pyconio.flush()


def initial():
    print_list()
    while True:
        with pyconio.rawkeys():
            key = pyconio.getch()
            if key == pyconio.ENTER:
                main.main()
            elif key == 49:
                scores = get_scores()
                if scores is not None:
                    list_scores(scores)
                    print_list()
                else:
                    print_list()
            elif key == 50:
                #options()
                print("options")
                print_list()
            elif key == pyconio.ESCAPE:
                return


def get_scores():
    pyconio.normalmode()
    save = input("Add meg a mentés nevét (útvonalát), pl: 'tetris.save': ")
    try:
        with open(save, "rt") as f:
            for line in f:
                if line.rstrip("\n") != None:
                    for score in line.split(", "):
                        try:
                            score = int(score)
                        except:
                            raise ValueError("Hibás mentés!")
                    return line.split(", ")
                else:
                    break
    except FileNotFoundError:
        print("A file nem található, kérlek add meg a helyes útvonalat!")
        return


def list_scores(scorelist):
    for hscore in scorelist:
        print(hscore)


initial()
