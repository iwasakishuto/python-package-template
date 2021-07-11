# coding: utf-8
import argparse
import re

from .generic_utils import str_strip


class DictParamProcessor(argparse.Action):
    """Receive an argument as a dictionary.

    Raises:
        ValueError: You must give one argument for each one keyword.

    Examples:
        >>> import argparse
        >>> from {{ MODULE_NAME }}.utils import DictParamProcessor
        >>> parser = argparse.ArgumentParser()
        >>> parser.add_argument("--dict-params", action=DictParamProcessor)
        >>> args = parser.parse_args(args=["--dict-params", "foo = [a, b, c]", "--dict-params", "bar=d"])
        >>> args.dict_params
        {'foo': ['a', 'b', 'c'], 'bar': 'd'}
        >>> args = parser.parse_args(args=["--dict-params", "foo=a, bar=b"])
        ValueError: too many values to unpack (expected 2)

    Note:
        If you run from the command line, execute as follows::

            $ python app.py --dict-params "foo = [a, b, c]" --dict-params bar=c
    """

    def __call__(self, parser, namespace, values, option_strings=None):
        param_dict = getattr(namespace, self.dest) or {}
        k, v = values.split("=")
        match = re.match(pattern=r"\[(.+)\]", string=str_strip(v))
        if match is not None:
            v = [str_strip(e) for e in match.group(1).split(",")]
        else:
            v = str_strip(v)
        param_dict[str_strip(k)] = v
        setattr(namespace, self.dest, param_dict)
