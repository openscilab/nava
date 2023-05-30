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
   A Python library for playing sound everywhere natively and securely.'''


setup(
    name='nava',
    packages=['nava'],
    version='0.1',
    description='A Python library for playing sound everywhere natively and securely. ',
    long_description=read_description(),
    long_description_content_type='text/markdown',
    author='OpenSciLab Development Team',
    # author_email='info@pycm.io',
    url='https://github.com/openscilab/nava',
    download_url='https://github.com/openscilab/nava/tarball/v0.1',
    keywords="sound wav music mp3 player audio",
    project_urls={
        'Webpage': 'https://openscilab.com/',
        'Source': 'https://github.com/openscilab/nava',
        'Discord': 'https://discord.gg/mtuMS8AjDS',
    },
    install_requires=get_requires(),
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
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
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Manufacturing',
        'Topic :: Multimedia',
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Multimedia :: Sound/Audio :: Players',
        'Topic :: Multimedia :: Sound/Audio :: Players :: MP3',
    ],
    license='MIT',
)
