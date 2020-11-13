import pyconio
import time

# Init
pyconio.settitle("pyconio test")

# Positioning
pyconio.clrscr()
pyconio.gotoxy(0, 0)
pyconio.textcolor(pyconio.LIGHTGREEN)
pyconio.write("Hello")
pyconio.gotoxy(10, 0)
pyconio.textbackground(pyconio.LIGHTBLUE)
pyconio.write("world!")
print()

# Printing color codes
print(pyconio.backgroundcolors[pyconio.RESET], end="")
print("{}Hello {}world!".format(pyconio.textcolors[pyconio.RED], pyconio.textcolors[pyconio.GREEN]))

# Color combinations
for b in range(0, 16):
    pyconio.gotoxy(5, 5+b)
    for t in range(0, 16):
        pyconio.textcolor(t)
        pyconio.textbackground(b)
        pyconio.write(" X ")
    pyconio.write("\n")
print()

# Raw input
pyconio.textbackground(pyconio.RESET)
pyconio.textcolor(pyconio.RESET)
print("Raw input test, press keys and then Enter:")
pyconio.rawmode()
while True:
    ch = pyconio.getch()
    if ch == pyconio.ENTER:
        break
    print(ch, end=" ")
print()
pyconio.normalmode()

# Raw input buffering
print("Raw input buffering test, 3s delay, press any keys")
pyconio.rawmode()
time.sleep(3)
if not pyconio.kbhit():
    print("No keys pressed.")
else:
    while pyconio.kbhit():
        print(pyconio.getch(), end=" ")
    print()
print()
pyconio.normalmode()

# Normal input
name = input("Enter your name: ")
print("Hello,", name)
