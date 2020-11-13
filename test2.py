import pyconio

pyconio.clrscr()
print("Use cursor keys to control the asterisk")

x = 40
y = 12
pyconio.rawmode()
while True:
    pyconio.gotoxy(x, y)
    pyconio.textcolor(pyconio.LIGHTGREEN)
    pyconio.write("*")
    pyconio.gotoxy(80, 24)
    
    key = pyconio.getch()
    pyconio.gotoxy(x, y)
    pyconio.textcolor(pyconio.BLUE)
    pyconio.write(".")

    if key == pyconio.UP:
        y = max(y-1, 1)
    elif key == pyconio.DOWN:
        y = min(y+1, 23)
    elif key == pyconio.LEFT:
        x = max(x-1, 0)
    elif key == pyconio.RIGHT:
        x = min(x+1, 79)
    elif key == pyconio.ESCAPE:
        break
pyconio.normalmode()
