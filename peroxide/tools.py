from cmd import Cmd
from functools import partial, wraps
from pathlib import Path

def columnize(s:list):
    Cmd().columnize(s)

def public (obj):
    columnize(list(filter(lambda s: not s.startswith('_'), dir(obj))))   

def str2path_method(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        args = [args[0], *[Path(a) for a in args[1:]]]
        return f(*args, **kwargs)
    return wrapper

def ext(self):
    return self.suffix[1:] if self.suffix else ''

Path.ext = ext

def readlines(self, strip=True):
    lines = self.read_text().split('\n')
    i = -1
    while not lines[i]:
        del lines[i]
    return lines

Path.readlines = readlines
