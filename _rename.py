#coding: utf-8
import os
import re
from pathlib import Path

def rename_repl(match):
    before = match.group(1)
    after = globals().get(before)
    if after is None:
        after = match.group(0)
    else:
        print(f"\tRenamed {before} to {after}")
    return after

def rename(string):
    return re.sub(pattern=r"{{\s+(.+?)\s+}}", repl=rename_repl, string=string)

HERE = os.path.abspath(os.path.dirname(__file__))

if __name__ == "__main__":
    PACKAGE_NAME = REPOSITORY_NAME  = input("> Package Name (Repository Name): ")
    PACKAGE_NAME_CODE = PACKAGE_NAME.replace("-", "")
    REPOSITORY_NAME   = PACKAGE_NAME_CODE
    MODULE_NAME       = input("> Module Name: ")
    DESCRIPTION       = input("> Description: ")
    AUTHOR            = input("> Author: ")
    AUTHOR_EMAIL      = input("> Author's Email: ")
    TWITTER_USERNAME  = input("> Twitter Username: @")
    p = Path(HERE)
    for path in p.glob("**/*"):
        rela_path = str(path.resolve().relative_to(HERE))
        if path.is_dir():
            dirname = rename(rela_path)
            if rela_path != dirname:
                path.rename(dirname)
                print(f"\033[32m[DIR]\033[0m renamed from {rela_path} to {dirname}")
        elif path.is_file():
            try:
                with path.open(mode="r") as f:
                    lines = f.readlines()
                print(f"\033[34m[FILE]\033[0m: {rela_path}")
                lines = [rename(e) for e in lines]
                with path.open(mode="w") as f:
                    f.writelines(lines)
            except Exception as e:
                pass