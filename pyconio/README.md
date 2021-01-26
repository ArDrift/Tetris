# PyConio: Python econio library

Colored output and raw keyboard handling for Linux and Windows console.

This package is created for educational purposes. Uses Jonathan Hartley's [colorama](https://github.com/tartley/colorama) library 
for color output, which is included for convenience.


## Screen and cursor positioning

See the functions in `printer.py`:

```python
import pyconio

pyconio.clrscr()
pyconio.gotoxy(10, 0)
print("Hello world!")
```


## Colored output

See the constants in `colors.py`:

```python
import pyconio

pyconio.textcolor(pyconio.LIGHTGREEN)
pyconio.textbackground(pyconio.BLUE)
print("Hello world!")
```

Color codes can be embedded into strings:

```python
print("{}Hello {}world!".format(pyconio.textcolors[pyconio.RED], pyconio.textcolors[pyconio.GREEN]))
```


## Buffered output

The function `pyconio.write()` works exactly like `print()`, but does not
flush the output by default. This can be used to draw an entire scene.
Then you can use `pyconio.flush()` – but pyconio tries to handle that
the same way Python does, by flushing the output when input is requested.


## Line-oriented input

Just use `input()` as usual.


## Raw keyboard input

Switch to raw mode using `pyconio.rawmode()`. Then use `pyconio.kbhit()` to check
if a key is pressed. `pyconio.getch()` returns an ASCII code or a key code
(see `keys.py`). Finally call `pyconio.normalmode()`.

```python
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
```

You can use `with pyconio.rawkeys()` as well.

## License

MIT license. For the license of the colorama package, see [https://github.com/tartley/colorama/](https://github.com/tartley/colorama/).
