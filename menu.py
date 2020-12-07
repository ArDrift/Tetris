#!/usr/bin/env python3

import pyconio
import draw

class Button:
    def __init__(self, text, function):
        self.text = text
        self.function = function
        self.active = False


    def __str__(self):
        return self.text

def main_menu(settings=None):
    pyconio.clrscr()
    buttons = [Button("Játék indítása", "start"),
               Button("Dicsőséglista", "toplist"),
               Button("Beállítások", "options"),
               Button("Betöltés", "load"),
               Button("Kilépés", "quit")]
    if settings is not None:
        return menu(buttons, settings)
    else:
        return menu(buttons)


def pause():
    pyconio.clrscr()
    buttons = [Button("Játék folytatása", "continue"),
               Button("Mentés", "save"),
               Button("Kilépés", "quit")]
    return menu(buttons)


def menu(buttons, data=None):
    pyconio.textcolor(pyconio.WHITE)
    buttons[0].active = True
    while True:
        draw.logo()
        for btn in buttons:
            if btn.active:
                pyconio.textbackground(pyconio.WHITE)
                pyconio.textcolor(pyconio.BLACK)
            else:
                pyconio.textbackground(pyconio.RESET)
                pyconio.textcolor(pyconio.RESET)
            pyconio.gotoxy(20, 20+buttons.index(btn))
            pyconio.write(btn)

            pyconio.gotoxy(15, 30)
            pyconio.textcolor(pyconio.RESET)
            pyconio.textbackground(pyconio.RESET)
            pyconio.write("Irányítás: ↑ ↓ ENTER ESC")
        pyconio.flush()

        pyconio.rawmode()
        key = pyconio.getch()
        active = buttons.index([x for x in buttons if x.active][0])
        if key == pyconio.ENTER:
                return select(buttons[active].function, data)
        elif key == pyconio.DOWN:
            buttons[active].active = False
            if active == len(buttons)-1:
                buttons[0].active = True
            else:
                buttons[active+1].active = True
        elif key == pyconio.UP:
            buttons[active].active = False
            if active == 0:
                buttons[-1].active = True
            else:
                buttons[active-1].active = True
        elif key == pyconio.ESCAPE:
            select("quit")
            return False


def select(func, data=None):
    pyconio.clrscr()
    # Main menu
    if func == "start":
        if data is not None:
            return ("new", data.size, data.level)
        else:
            return ("new", 20, 1)
        pyconio.clrscr()
    elif func == "toplist":
        return list_scores(get_scores(), (20,20))
    elif func == "options":
        return options((20, 20), data)
    elif func == "load":
        return ("load", 20, 1)
        pyconio.clrscr()
    elif func == "quit":
        pyconio.textbackground(pyconio.RESET)
        pyconio.textcolor(pyconio.RESET)
        pyconio.clrscr()
        draw.cursor(True)
        return None
    # Options menu
    elif func == "size":
        return (func, setting_adjust(data.size, "Méret", 20, 100, 2))
    elif func == "level":
        return (func, setting_adjust(data.level, "Kezdő szint", 1, 10))
    # Pause menu
    else:
        return func


def setting_adjust(setting, label, min_val, max_val, delta=1):
    draw.logo()
    pyconio.textbackground(pyconio.RESET)
    pyconio.textcolor(pyconio.RESET)
    pyconio.gotoxy(20,20)
    pyconio.write("{}: {:3}".format(label, setting), flush=True)
    pyconio.gotoxy(20,30)
    pyconio.write("Mentés: ENTER", end="\n", flush=True)
    pyconio.gotoxy(20,31)
    pyconio.write("Vissza: ESC", end="\n", flush=True)
    initial = setting
    pyconio.rawmode()
    key = pyconio.getch()
    while key != pyconio.ENTER:
        if key == pyconio.UP:
            if setting < max_val:
                setting += delta
        elif key == pyconio.DOWN:
            if setting > min_val:
                setting -= delta
        elif key == pyconio.ESCAPE:
            setting = initial
            break
        pyconio.gotoxy(20,20)
        pyconio.write("{}: {:3}".format(label, setting), flush=True)
        key = pyconio.getch()
    return setting


def options(pos, settings=None):
    pyconio.clrscr()
    pyconio.gotoxy(pos[0], pos[1])
    buttons = [Button("Pálya mérete", "size"),
               Button("Kezdő szint", "level")]
    if settings is None:
        settings = Options()
    try:
        (selected, set_value) = menu(buttons, settings)
    except TypeError:
        return settings
    if selected == "size":
        settings.size = set_value
    elif selected == "level":
        settings.level = set_value
    pyconio.rawmode()
    key = pyconio.getch()
    while key != pyconio.ESCAPE:
        key = pyconio.getch()
    return main_menu(settings)


class Options:
    def __init__(self, size=None, level=None):
        if size is None:
            self.size = 20
        else:
            self.size = size
        if level is None:
            self.level = 1
        else:
            self.level = level


class Score:
    def __init__(self, name, points):
        self.name = name
        self.points = points


    def __str__(self):
        return "{}: {} pts".format(self.name, self.points)

    def __int__(self):
        return self.points


def get_scores():
    scores = []
    try:
        with open("highscores.txt", "rt") as f:
            for line in f:
                linelist = line.rstrip("\n").split(": ")
                for section in range(len(linelist)):
                    if section == 0:
                        name = linelist[section]
                    elif section == 1:
                        points = int(linelist[section])
                scores.append(Score(name, points))

            return scores
    except FileNotFoundError:
        return None
    except ValueError as e:
        return -1


def list_scores(scorelist, pos):
    pyconio.clrscr()
    draw.logo()
    pyconio.gotoxy(pos[0], pos[1])
    pyconio.textcolor(pyconio.WHITE)
    if scorelist is None:
        pyconio.gotoxy(pos[0]-15, pos[1])
        pyconio.write("A file nem található, biztosan játszottál már?")
    elif scorelist == -1:
        pyconio.gotoxy(pos[0]-13, pos[1])
        pyconio.write("Hibás file, ellenőrizd a pontszámokat!")
    else:
        for i in range(len(scorelist)):
            if i+1 == 1:
                pyconio.textcolor(pyconio.YELLOW)
            elif i+1 == 2:
                pyconio.textcolor(pyconio.LIGHTGRAY)
            elif i+1 == 3:
                pyconio.textcolor(pyconio.BROWN)
            else:
                pyconio.textcolor(pyconio.RESET)
            pyconio.gotoxy(pos[0], pos[1]+i)
            pyconio.write("{}. {}".format(i+1, scorelist[i]), end="\n")

    pyconio.gotoxy(pos[0], pos[1]+pos[1]//2)
    pyconio.write("Vissza: ESC")
    pyconio.flush()
    pyconio.rawmode()
    key = pyconio.getch()
    while key != pyconio.ESCAPE:
        key = pyconio.getch()
    pyconio.clrscr()
    return main_menu()


def add_score(score):
    pyconio.gotoxy(20,20)
    pyconio.textcolor(pyconio.RESET)
    pyconio.textbackground(pyconio.RESET)
    pyconio.write("Szép volt, dicsőséglistára kerültél!", end="\n")
    pyconio.gotoxy(20,21)
    pyconio.normalmode()
    name = input("Add meg a neved: ")
    pyconio.rawmode()
    scorelist = get_scores()
    if scorelist is not None:
        scorelist.append(Score(name, score))
        scorelist.sort(key=int, reverse=True)
        if len(scorelist) > 5:
            scorelist.pop(-1)
    else:
        scorelist = [Score(name, score)]

    return scorelist


def write_score(scorelist):
    with open("highscores.txt", "wt") as f:
        for score in scorelist:
            f.write("{}: {}\n".format(score.name, score.points))
