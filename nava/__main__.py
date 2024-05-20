# -*- coding: utf-8 -*-
"""Nava main."""
import argparse
from art import tprint
from .params import NAVA_VERSION
from .functions import nava_help, play_cli


def main():
    """
    CLI main function.

    :return: None
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'filename',
        nargs='?',
        type=str,
        metavar='FILE_PATH',
        help='path to audio file'
    )
    parser.add_argument(
        '--file',
        nargs='?',
        type=str,
        metavar='FILE_PATH',
        help='path to audio file',
    )
    parser.add_argument('--loop', help='sound play in loop', action='store_true', default=False)
    parser.add_argument('--version', help="version", action='store_true', default=False)
    parser.add_argument('-v', help="version", action='store_true', default=False)
    args = parser.parse_known_args()[0]
    if args.version or args.v:
        print(NAVA_VERSION)
    elif args.filename or args.file:
        file_name = args.filename
        if args.file:
            file_name = args.file
        loop = args.loop
        play_cli(file_name, loop=loop)
    else:
        tprint("Nava")
        tprint("V:" + NAVA_VERSION)
        nava_help()
        parser.print_help()


if __name__ == "__main__":
    main()
