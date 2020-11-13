# Copyright (c) 2018 Czirkos Zoltan. MIT license, see LICENSE file.

import sys
from .keys import *
from .printer import flush

class _ConsoleUnix:
    _unixkeycodes = {
        "\x1BOP": F1,
        "\x1BOQ": F2,
        "\x1BOR": F3,
        "\x1BOS": F4,
        "\x1B[15~": F5,
        "\x1B[17~": F6,
        "\x1B[18~": F7,
        "\x1B[19~": F8,
        "\x1B[20~": F9,
        "\x1B[21~": F10,
        "\x1B[23~": F11,
        "\x1B[24~": F12,

        "\x1B[A": UP,
        "\x1B[B": DOWN,
        "\x1B[D": LEFT,
        "\x1B[C": RIGHT,
        "\x1B[5~": PAGEUP,
        "\x1B[6~": PAGEDOWN,
        "\x1B[H": HOME,
        "\x1B[F": END,
        "\x1B[2~": INSERT,
        "\x1B[3~": DELETE,
        "\x1B[1;5A": CTRLUP,
        "\x1B[1;5B": CTRLDOWN,
        "\x1B[1;5D": CTRLLEFT,
        "\x1B[1;5C": CTRLRIGHT,
        "\x1B[5;5~": CTRLPAGEUP,
        "\x1B[6;5~": CTRLPAGEDOWN,
        "\x1B[1;5H": CTRLHOME,
        "\x1B[1;5F": CTRLEND,
        "\x1B[3;5~": CTRLDELETE,
    }

    def __init__(self):
        import termios, select, atexit
        self._ubstdin = open(sys.stdin.fileno(), "rb", buffering=0)
        self._putbackbuf = None
        self.normalmode()
        atexit.register(self.normalmode)

    def normalmode(self):
        import termios
        fd = self._ubstdin.fileno()
        attr = termios.tcgetattr(fd)
        attr[3] |= termios.ICANON | termios.ECHO
        termios.tcsetattr(fd, termios.TCSADRAIN, attr)

    def rawmode(self):
        import termios
        fd = self._ubstdin.fileno()
        attr = termios.tcgetattr(fd)
        attr[3] &= ~termios.ICANON & ~termios.ECHO
        termios.tcsetattr(fd, termios.TCSADRAIN, attr)

    def _rawgetch(self):
        if self._putbackbuf is not None:
            temp = self._putbackbuf
            self._putbackbuf = None
            return temp
        return chr(ord(self._ubstdin.read(1)))

    def _putback(self, ch):
        if self._putbackbuf is not None:
            raise BufferError("Can only put back one item")
        self._putbackbuf = ch

    def getch(self):
        s = self._rawgetch()
        if s == "\x7F":
            return BACKSPACE
        if s != "\x1B" or not self.kbhit():    # only an escape sequence if other chars can be read
            return ord(s)
        # read following chars and concatenate to see the escape sequence
        s += self._rawgetch()
        if s[-1] == "O":   # VT100 f1-f4: OP-OS
            s += self._rawgetch()
        elif s[-1] == "[": # other: always delimited by uppercase char or tilde
            s += self._rawgetch()
            while not (s[-1].isupper() or s[-1] == "~"):
                s += self._rawgetch()
        else:   # unknown sequence, return verbatim
            self._putback(s[-1])
            return ord(s[0])
        return self._unixkeycodes.get(s, UNKNOWNKEY)

    def kbhit(self):
        import select
        dr, dw, de = select.select([self._ubstdin], [], [], 0)
        return dr != []


class _ConsoleWindows:
    _windowskeycodes = {
        72: UP,
        80: DOWN,
        75: LEFT,
        77: RIGHT,
        73: PAGEUP,
        81: PAGEDOWN,
        71: HOME,
        79: END,
        82: INSERT,
        83: DELETE,
        141: CTRLUP,
        145: CTRLDOWN,
        115: CTRLLEFT,
        116: CTRLRIGHT,
        134: CTRLPAGEUP,
        118: CTRLPAGEDOWN,
        119: CTRLHOME,
        117: CTRLEND,
        146: CTRLINSERT,
        147: CTRLDELETE,
    }

    def __init__(self):
        import msvcrt
        self.normalmode()

    def normalmode(self):
        pass

    def rawmode(self):
        pass

    def _rawgetch(self):
        import msvcrt
        return ord(msvcrt.getch())

    def getch(self):
        code = self._rawgetch()
        if code == 0x7F:
            return BACKSPACE
        if code == 0x0D:    # linux compat
            return ENTER
        if code != 0xE0:
            return code
        code = self._rawgetch()
        return self._windowskeycodes.get(code, UNKNOWNKEY)

    def kbhit(self):
        import msvcrt
        return msvcrt.kbhit() != 0


_impl = None
_rawmode = None


def getch():
    """Get one raw character from terminal. This can detect F1-F10, cursor keys,
    backspace and other controlling keys: see the keyboard constants.
    ASCII code is returned for other keys. Non-ASCII keys probably won't work.
    Characters are not echoed to the screen when in raw mode.
    Only to be used after calling rawmode().
    Note that backspace will be code 8, regardless of terminal settings
    (whether it sent BS or DEL char). Enter will always be 10, even on Windows.
    On Windows, this function sometimes returns 0's, so just ignore them.
    Also function keys are not supported on Windows."""
    assert(_rawmode)
    flush()
    return _impl.getch()


def kbhit():
    """Detect if a key is pressed. If so, it can be read with getch().
    Only to be used after calling rawmode()."""
    assert(_rawmode)
    flush()
    return _impl.kbhit()


def rawmode():
    """Switch the terminal to raw mode, to detect F1-F10, cursor keys and
    other controlling keys. Use getch() and kbhit() afterwards.
    Characters are not echoed to the screen when in raw mode.
    Switching back to line-oriented mode is possible using normalmode()."""
    global _rawmode
    _rawmode = True
    return _impl.rawmode()


def normalmode():
    """Switch the terminal back to normal, line-oriented mode. Characters
    are echoed to the screen when in normal mode."""
    global _rawmode
    _rawmode = False
    return _impl.normalmode()


def rawkeys():
    """Returns an object which can be used in the Python 'with' statement.
    Entering sets raw mode, exiting restores normal mode."""
    class helper:
        def __enter__(self):
            rawmode()
        def __exit__(self, type, value, tb):
            normalmode()

    return helper()

try:
    _impl = _ConsoleWindows()
except ImportError:
    _impl = _ConsoleUnix()
normalmode()
