# coding: utf-8
import os
import re
from pathlib import Path

CONFIGURATION = {}
HERE = os.path.abspath(os.path.dirname(__file__))


def set_configuration() -> None:
    REPOSITORY_NAME = os.path.basename(HERE)
    PACKAGE_NAME = input(f"> Package Name ({REPOSITORY_NAME}): ")
    if len(PACKAGE_NAME) == 0:
        PACKAGE_NAME = REPOSITORY_NAME
    PACKAGE_NAME_CODE = PACKAGE_NAME.replace("-", "")
    AUTHOR = input("> Author (GitHub username): @")
    CONFIGURATION.update(
        {
            "REPOSITORY_NAME": REPOSITORY_NAME,
            "PACKAGE_NAME": PACKAGE_NAME,
            "PACKAGE_NAME_CODE": PACKAGE_NAME_CODE,
            "MODULE_NAME": input("> Module Name: "),
            "DESCRIPTION": input("> Description: "),
            "AUTHOR": AUTHOR,
            "AUTHOR_EMAIL": input("> Author's Email: "),
            "TWITTER_USERNAME": input("> Twitter Username: @"),
            "PROJECT_URL": f"https://github.com/{ AUTHOR }/{REPOSITORY_NAME}",
            "DOCUMENTATION_URL": f"https://{ AUTHOR }.github.io/{REPOSITORY_NAME}"
        }
    )

def replace(match: re.Match) -> str:
    before: str = match.group(1)
    after: str = CONFIGURATION.get(before)
    if after is None:
        after = match.group(0)
    else:
        print(f"\tRenamed from {before} to {after}")
    return after


def rename(string: str) -> str:
    return re.sub(
        pattern=r"{{(?:\s+)?([A-Z_]+?)(?:\s+)?}}", repl=replace, string=string
    )


if __name__ == "__main__":
    set_configuration()
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
