# coding: utf-8
import sys
import argparse

def hoge(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser(prog="<hoge>", add_help=True)
    args = parser.parse_args(argv)
