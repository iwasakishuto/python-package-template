```sh
# Run this program to prepare the environment for your package.
$ python3 _quickstart.py
```

***

# python-package-template

![header](https://github.com/iwasakishuto/python-package-template/blob/master/src/_images/header.png?raw=true)
[![PyPI version](https://badge.fury.io/py/{{ REPOSITORY_NAME }}.svg)](https://pypi.org/project/{{ REPOSITORY_NAME }}/)
[![GitHub version](https://badge.fury.io/gh/{{ AUTHOR }}%2F{{ REPOSITORY_NAME }}.svg)](https://github.com/{{ AUTHOR }}/{{ REPOSITORY_NAME }})
[![Execute Python package](https://github.com/{{ AUTHOR }}/{{ REPOSITORY_NAME }}/actions/workflows/execute_python_package.yml/badge.svg)](https://github.com/{{ AUTHOR }}/{{ REPOSITORY_NAME }}/actions/workflows/execute_python_package.yml/badge.svg)
[![Upload Python Package](https://github.com/{{ AUTHOR }}/{{ REPOSITORY_NAME }}/actions/workflows/upload_python_package.yml/badge.svg)](https://github.com/{{ AUTHOR }}/{{ REPOSITORY_NAME }}/actions/workflows/upload_python_package.yml/badge.svg)
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)](https://github.com/{{ AUTHOR }}/{{ REPOSITORY_NAME }}/blob/master/LICENSE)

{{ DESCRIPTION }}

## Installation

I recommend you to use these tools to **avoid the chaos** of the python environment. See other sites for how to install these tools.

### Pyenv + Poetry

- [Pyenv](https://github.com/pyenv/pyenv) is a python installation manager.
- [Poetry](https://python-poetry.org/) is a packaging and dependency manager.

```sh
$ git clone https://github.com/{{ AUTHOR }}/{{ REPOSITORY_NAME }}.git
$ cd {{ REPOSITORY_NAME }}
$ pyenv install 3.8.9
$ pyenv local 3.8.9
$ python -V
Python 3.8.9
$ poetry install
```
