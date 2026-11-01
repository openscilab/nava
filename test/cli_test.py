# -*- coding: utf-8 -*-
r"""
>>> import os
>>> import sys
>>> import nava.cli as cli
>>> from nava.cli import _parse_args, main
>>> from nava.params import NAVA_VERSION
>>> test_sound_path = os.path.join("others", "test.wav")
>>> cli._play_cli(test_sound_path)
>>> cli._play_cli("test2.wav")
Error: Given sound file doesn't exist.
>>> # Test _parse_args with no args
>>> sys.argv = ['nava']
>>> args = _parse_args()
>>> args.filename
>>> args.file
>>> args.loop
False
>>> args.version
False
>>> args.v
False
>>> # Test _parse_args with filename
>>> sys.argv = ['nava', 'test.wav']
>>> args = _parse_args()
>>> args.filename
'test.wav'
>>> # Test _parse_args with --file
>>> sys.argv = ['nava', '--file', 'test.wav']
>>> args = _parse_args()
>>> args.file
'test.wav'
>>> # Test _parse_args with --version
>>> sys.argv = ['nava', '--version']
>>> args = _parse_args()
>>> args.version
True
>>> # Test _parse_args with --loop
>>> sys.argv = ['nava', '--loop', 'test.wav']
>>> args = _parse_args()
>>> args.loop
True
>>> # Test main with --version
>>> sys.argv = ['nava', '--version']
>>> main()
0.9
>>> # Test main with no args (help)
>>> sys.argv = ['nava']
>>> main()
 _   _                      
| \ | |  __ _ __   __  __ _ 
|  \| | / _` |\ \ / / / _` |
| |\  || (_| | \ V / | (_| |
|_| \_| \__,_|  \_/   \__,_|
<BLANKLINE>
<BLANKLINE>
__     __     ___       ___  
\ \   / / _  / _ \     / _ \ 
 \ \ / / (_)| | | |   | (_) |
  \ V /   _ | |_| | _  \__, |
   \_/   (_) \___/ (_)   /_/ 
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
Nava is a Python library that allows users to play sound in Python without any dependencies or platform restrictions.
It is a cross-platform solution that runs on any operating system, including Windows, macOS, and Linux.
Its lightweight and easy-to-use design makes Nava an ideal choice for developers looking to add sound 
functionality to their Python programs.
<BLANKLINE>
Repo : https://github.com/openscilab/nava
Webpage : https://openscilab.com/
<BLANKLINE>
>>> # Test main with invalid file
>>> sys.argv = ['nava', 'nonexistent.wav']
>>> main()
Error: Given sound file doesn't exist.
>>> # Test main with valid file (plays sound)
>>> sys.argv = ['nava', test_sound_path]
>>> main()
>>> sys.argv = ['nava', '--file', test_sound_path]
>>> main()
>>> original_parse_args = cli._parse_args
>>> def raise_keyboard_interrupt():
...     raise KeyboardInterrupt
>>> cli._parse_args = raise_keyboard_interrupt
>>> try:
...     cli.main()
... except SystemExit as e:
...     print("EXIT_CODE", e.code)
... finally:
...     cli._parse_args = original_parse_args
See you. Bye!
EXIT_CODE 1
"""
