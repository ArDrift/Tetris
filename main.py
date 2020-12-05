#!/usr/bin/env python3

import pyconio
import time
import control
import draw

def mainloop(tetro, field, next, points=0, level=1):
    """
    Prints the field and the shape selected in main, in its given position,
    then you can control it with UP-DOWN-LEFT-RIGHT as in the Tetris game.
    You can quit with the ESCAPE key.
    """
    pyconio.settitle("Tetris")
    draw.cursor(False)
    game_sec = time.time()
    draw.screen(tetro, field, next, points, level)
    ingame = [True, 0]

    with pyconio.rawkeys():
        while ingame[0]:
            current_sec = time.time()
            if pyconio.kbhit():
                ingame = control.ingame(tetro, field)
                points += ingame[1] * level
                draw.screen(tetro, field, next, points, level)
            # Fall mechanism
            if round(current_sec, min(level, 2)) >= round(game_sec, min(level, 2)):
                if control.move_valid(control.post_move(tetro, "down"), field):
                    if control.hit(control.post_move(tetro, "down"), field):
                        if tetro.pos[1] >= 1:
                            last = tetro
                            next.pos = [5,0]
                            tetro = next
                            next = control.store_regen(last, field, next)
                        else:
                            ingame = [False, points]
                    else:
                        tetro.pos[1] += 1
                else:
                    last = tetro
                    next.pos = [5,0]
                    tetro = next
                    next = control.store_regen(last, field, next)
                game_sec += control.speed_sec(level)
                draw.screen(tetro, field, next, points, level)
            # Line clear
            if control.line_full(field):
                points += control.delete_full(field) * level
                draw.screen(tetro, field, next, points, level)
            # Level up
            if points >= level**2 * 1000:
                level += 1
                draw.screen(tetro, field, next, points, level)
        draw.cursor(True)


def main(mode="new", fieldsize=20):
    if mode == "new":
        field = control.make_field(fieldsize)
        next = control.make_random([fieldsize * 2,0])
        mainloop(control.make_random([5,0]), field, next)
    elif mode == "load":
        (field, shape, pos, next, points, level) = control.load_game("save.txt")
        tetro = draw.Tetromino(shape, pos[0], pos[1])
        next = draw.Tetromino(next, fieldsize * 2, 0)
        mainloop(tetro, field, next, points, level)
