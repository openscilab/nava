# -*- coding: utf-8 -*-
"""
>>> import os
>>> import sys
>>> from nava.cli import parse_args, run, main
>>> from nava.params import NAVA_VERSION
>>> test_sound_path = os.path.join("others", "test.wav")
>>> # Test parse_args with no args
>>> sys.argv = ['nava']
>>> args = parse_args()
>>> args.filename
>>> args.file
>>> args.loop
False
>>> args.version
False
>>> args.v
False
>>> # Test parse_args with filename
>>> sys.argv = ['nava', 'test.wav']
>>> args = parse_args()
>>> args.filename
'test.wav'
>>> # Test parse_args with --file
>>> sys.argv = ['nava', '--file', 'test.wav']
>>> args = parse_args()
>>> args.file
'test.wav'
>>> # Test parse_args with --version
>>> sys.argv = ['nava', '--version']
>>> args = parse_args()
>>> args.version
True
>>> # Test parse_args with --loop
>>> sys.argv = ['nava', '--loop', 'test.wav']
>>> args = parse_args()
>>> args.loop
True
>>> # Test main with --version
>>> sys.argv = ['nava', '--version']
>>> main()
0.8
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
\ \   / / _  / _ \     ( _ ) 
 \ \ / / (_)| | | |    / _ \ 
  \ V /   _ | |_| | _ | (_) |
   \_/   (_) \___/ (_) \___/ 
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
A Python library for playing sound everywhere natively and securely.
<BLANKLINE>
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
"""
