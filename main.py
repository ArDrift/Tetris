#!/usr/bin/env python3

import pyconio
import time
import control
import draw
import menu

def mainloop(tetro, field, next, points=0, level=1):
    """
    Prints the field and the currently active tetromino to its given position.
    While ingame, you can control it with UP-DOWN-LEFT-RIGHT as in Tetris.
    Pause the loop with the ESC key, if you choose continue, the current loop
    ends, and is called again with the current parameters.
    """
    game_sec = time.time()
    draw.screen(tetro, field, next, points, level)
    ingame = (True, 0)

    with pyconio.rawkeys():
        while ingame[0]:
            current_sec = time.time()
            # Control mechanism
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
                        # Game over if tetro hits another one, while Y pos is <1
                        else:
                            ingame = (False, points)
                            pyconio.clrscr()
                            draw.logo("game_over.txt")
                            time.sleep(1)
                            # Add to top scores if needed
                            scores = menu.get_scores()
                            if scores is not None and scores != -1:
                                if points > scores[-1].points:
                                    time.sleep(1)
                                    scorechoice = menu.add_score(points)
                                    if scorechoice is not None:
                                        menu.write_score(scorechoice)
                            elif scores == -1:
                                pyconio.gotoxy(12, 25)
                                pyconio.write("Hibás dicsőséglista!", end="\n")
                                pyconio.gotoxy(8, 26)
                                pyconio.write("Ellenőrizd a highscores.txt-t!")
                                pyconio.flush()
                                time.sleep(2.5)
                            else:
                                time.sleep(1)
                                menu.write_score(menu.add_score(points))
                            return main()
                    else:
                        tetro.pos[1] += 1
                # When hit, save tetro and generate new one.
                else:
                    last = tetro
                    next.pos = [len(field) // 4, 0]
                    tetro = next
                    next = control.store_regen(last, field, next)
                # Game ticks
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
        # Pause
        pausechoice = menu.pause()
        if pausechoice == "save":
            control.save_game(tetro, field, next, points, level)
            pausechoice = menu.save_menu()
        if pausechoice == "continue":
            return mainloop(tetro, field, next, points, level)
        elif pausechoice is None:
            return main()


def game_init(mode, fieldsize, level):
    """
    Initialize the game depending on the given mode, either from scratch,
    or by loading an existing saved state.
    This handles non-existing save files too.
    """
    if mode == "new":
        field = control.make_field(fieldsize)
        next = control.make_random([fieldsize * 2,0])
        mainloop(control.make_random([fieldsize//4,0]), field, next, 0, level)
    elif mode == "load":
        loaded = control.load_game("save.txt")
        if loaded is not None:
            (field, shape, pos, next, points, level) = loaded
        else:
            pyconio.gotoxy(5,20)
            pyconio.write("Nem található mentés, biztosan mentettél már?")
            pyconio.gotoxy(20, 29)
            pyconio.write("Vissza: ESC")
            key = pyconio.getch()
            while key != pyconio.ESCAPE:
                key = pyconio.getch()
            return main()
        fieldsize = len(field)
        tetro = draw.Tetromino(shape, pos[0], pos[1])
        next = draw.Tetromino(next, fieldsize * 2, 0)
        mainloop(tetro, field, next, points, level)


def main():
    """
    Executes the main menu from the menu module, and initializes the game,
    if the user selected play.
    """
    pyconio.settitle("Tetris")
    draw.cursor(False)
    selected = menu.main_menu()
    if selected is None or selected == False:
        draw.cursor(True)
        return
    else:
        (mode, fieldsize, level) = selected
        game_init(mode, fieldsize, level)


main()
