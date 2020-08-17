# coding: utf-8
import sys
import argparse

def func(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser(prog="command-name", add_help=True)
    args = parser.parse_args(argv)
