# -*- coding: utf-8 -*-
"""Nava main."""
import argparse
from art import tprint
from .params import NAVA_VERSION
from .functions import nava_help, run_nava


def main():
    """
    CLI main function.

    :return: None
    """
    tprint("nava")
    tprint("V:" + NAVA_VERSION)
    nava_help()
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--file',
        nargs=1,
        metavar="audio file name",
        type=str,
        help="name of the audio file",
    )
    # parse the arguments from the standard input
    args = parser.parse_args()
    run_nava(args)


if __name__ == "__main__":
    main()
