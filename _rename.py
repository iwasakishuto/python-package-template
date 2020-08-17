#coding: utf-8
import os
import re
from pathlib import Path
from _conf import *

def rename(string):
    re.sub(pattern=r"{{\s+(.+)\s+}}", repl=lambda m:print(f"Renamed {m.group(1)}");globals().get(m.group(1)), string=string)

if __name__ == "__main__":
    p = Path("")
    os.rename("{{ MODULE_NAME }}", rename)
    for path in p.glob("**/*"):
        if path.is_dir():
            dirname = path.name
            path.rename(dirname)
            print(f"Rename DIR from {path.name} to {dirname}")
        elif path.is_file():
            print(f"FILE: {path.name}")
            with path.open(mode="r") as f:
                lines = [rename(e) for e in f.readlines()]
            with path.open(mode="w") as f:
                f.writelines(lines)
