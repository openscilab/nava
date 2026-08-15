# -*- coding: utf-8 -*-
"""Nava cli."""
import sys
import argparse
from art import tprint
from .params import NAVA_VERSION, EXIT_MESSAGE, Engine
from .functions import nava_help, play_cli


def parse_args() -> argparse.Namespace:
    """Parse arguments."""
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
    parser.add_argument(
        '--engine',
        choices=[engine.value for engine in Engine],
        type=str.lower,
        default=Engine.AUTO.value,
        help='audio playback engine'
    )
    parser.add_argument('--loop', help='sound play in loop', action='store_true', default=False)
    parser.add_argument('--version', help="version", action='store_true', default=False)
    parser.add_argument('-v', help="version", action='store_true', default=False)
    args = parser.parse_known_args()[0]
    return args


def run(args: argparse.Namespace) -> None:
    """
    Run nava CLI.

    :param args: arguments
    """
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


def main() -> None:
    """CLI main function."""
    try:
        args = parse_args()
        run(args)
    except (KeyboardInterrupt, EOFError):
        print(EXIT_MESSAGE)
        sys.exit(1)
