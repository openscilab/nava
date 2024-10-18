# -*- coding: utf-8 -*-
"""Setup module."""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def get_requires():
    """Read requirements.txt."""
    requirements = open("requirements.txt", "r").read()
    return list(filter(lambda x: x != "", requirements.split()))


def read_description():
    """Read README.md and CHANGELOG.md."""
    try:
        with open("README.md") as r:
            description = "\n"
            description += r.read()
        with open("CHANGELOG.md") as c:
            description += "\n"
            description += c.read()
        return description
    except Exception:
        return '''
   Nava is a Python library that allows users to play sound in Python without any dependencies or platform restrictions.
   It is a cross-platform solution that runs on any operating system, including Windows, macOS, and Linux.
   Its lightweight and easy-to-use design makes Nava an ideal choice for developers looking to add sound functionality to their Python programs.'''


setup(
    name='nava',
    packages=['nava'],
    version='0.7',
    description='A Python library for playing sound everywhere natively and securely.',
    long_description=read_description(),
    long_description_content_type='text/markdown',
    author='Nava Development Team',
    author_email='nava@openscilab.com',
    url='https://github.com/openscilab/nava',
    download_url='https://github.com/openscilab/nava/tarball/v0.7',
    keywords="sound wav music mp3 player audio",
    project_urls={
        'Webpage': 'https://openscilab.com/',
        'Source': 'https://github.com/openscilab/nava',
        'Discord': 'https://discord.gg/MCbPKCFBs3',
    },
    install_requires=get_requires(),
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Manufacturing',
        'Topic :: Multimedia',
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Multimedia :: Sound/Audio :: Players',
        'Topic :: Multimedia :: Sound/Audio :: Players :: MP3',
    ],
    license='MIT',
    entry_points={
        'console_scripts': [
            'nava = nava.__main__:main',
        ]})
