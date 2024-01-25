<div align="center">
    <img src="https://github.com/openscilab/nava/raw/main/others/logo.png" width="300" height="300">
    <h1>Nava</h1>
    <br/>
    <a href="https://www.python.org/">
        <img src="https://img.shields.io/badge/built%20with-Python3-green.svg" alt="built with Python3"/>
    </a>
    <a href="https://badge.fury.io/py/nava">
        <img src="https://badge.fury.io/py/nava.svg" alt="PyPI version" height="18">
    </a>
	<a href="https://codecov.io/gh/openscilab/nava">
		<img src="https://codecov.io/gh/openscilab/nava/branch/main/graph/badge.svg" alt="Codecov">
	</a>
    <a href="https://discord.gg/MCbPKCFBs3">
        <img src="https://img.shields.io/discord/1064533716615049236.svg" alt="Discord Channel">
    </a>
</div>

## Table of contents
   * [Overview](https://github.com/openscilab/nava#overview)
   * [Installation](https://github.com/openscilab/nava#installation)
   * [Usage](https://github.com/openscilab/nava#usage)
   * [Issues & Bug Reports](https://github.com/openscilab/nava#issues--bug-reports)
   * [Contribution](https://github.com/openscilab/nava/blob/main/.github/CONTRIBUTING.md)
   * [Authors](https://github.com/openscilab/nava/blob/main/AUTHORS.md)
   * [License](https://github.com/openscilab/nava/blob/main/LICENSE)
   * [Show Your Support](https://github.com/openscilab/nava#show-your-support)
   * [Changelog](https://github.com/openscilab/nava/blob/main/CHANGELOG.md)
   * [Code of Conduct](https://github.com/openscilab/nava/blob/main/.github/CODE_OF_CONDUCT.md)

## Overview

<p align="justify">
Nava is a Python library that allows users to play sound in Python without any dependencies or platform restrictions. It is a cross-platform solution that runs on any operating system, including Windows, macOS, and Linux. Its lightweight and easy-to-use design makes Nava an ideal choice for developers looking to add sound functionality to their Python programs.
</p>

<table>
	<tr>
		<td align="center">PyPI Counter</td>
		<td align="center">
            <a href="http://pepy.tech/project/nava">
                <img src="http://pepy.tech/badge/nava">
            </a>
        </td>
	</tr>
	<tr>
		<td align="center">Github Stars</td>
		<td align="center">
            <a href="https://github.com/openscilab/nava">
                <img src="https://img.shields.io/github/stars/openscilab/nava.svg?style=social&label=Stars">
            </a>
        </td>
	</tr>
</table>



<table>
	<tr> 
		<td align="center">Branch</td>
		<td align="center">main</td>
		<td align="center">dev</td>
	</tr>
    <tr>
		<td align="center">Linux CI</td>
		<td align="center"><img src="https://github.com/openscilab/nava/workflows/Linux/badge.svg?branch=main"></td>
		<td align="center"><img src="https://github.com/openscilab/nava/workflows/Linux/badge.svg?branch=dev"></td>
	</tr>
	<tr>
		<td align="center">Windows CI</td>
		<td align="center"><img src="https://github.com/openscilab/nava/workflows/Windows/badge.svg?branch=main"></td>
		<td align="center"><img src="https://github.com/openscilab/nava/workflows/Windows/badge.svg?branch=dev"></td>
	</tr>
	<tr>
		<td align="center">macOS CI</td>
		<td align="center"><img src="https://github.com/openscilab/nava/workflows/macOS/badge.svg?branch=main"></td>
		<td align="center"><img src="https://github.com/openscilab/nava/workflows/macOS/badge.svg?branch=dev"></td>
	</tr>
</table>

<table>
	<tr> 
		<td align="center">Code Quality</td>
		<td align="center"><a href="https://app.codacy.com/gh/openscilab/nava/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/9c384b4e400340ae94772c1d7e1842d0"></a></td>
		<td align="center"><a href="https://www.codefactor.io/repository/github/openscilab/nava"><img src="https://www.codefactor.io/repository/github/openscilab/nava/badge" alt="CodeFactor"></a></td>
		<td align="center"><a href="https://codebeat.co/projects/github-com-openscilab-nava-dev"><img alt="codebeat badge" src="https://codebeat.co/badges/75df9d9c-af95-4038-8a1d-9f3618856871"></a></td>
	</tr>
</table>

## Installation

### PyPI

- Check [Python Packaging User Guide](https://packaging.python.org/installing/)     
- Run `pip install nava==0.3`

### Source code
- Download [Version 0.3](https://github.com/openscilab/nava/archive/v0.3.zip) or [Latest Source](https://github.com/openscilab/nava/archive/dev.zip)
- Run `pip install .`

### Conda

- Check [Conda Managing Package](https://conda.io/)
- Update Conda using `conda update conda`
- Run `conda install -c openscilab nava`

## Usage

### Basic

```python
from nava import play
play("alarm.wav")
```

### Async mode

⚠️ The `async_mode` parameter has a default value of `False`

```python
import time
from nava import play, stop
sound_id = play("alarm.wav", async_mode=True)
time.sleep(4)
stop(sound_id)
```

### Error

```python
from nava import play, NavaBaseError

try:
    play("alarm.wav")
except NavaBaseError as e:
    print(str(e))
```


## Issues & bug reports

Just fill an issue and describe it. We'll check it ASAP! or send an email to [info@openscilab.com](mailto:info@openscilab.com "info@openscilab.com").

- Please complete the issue template
 
You can also join our discord server

<a href="https://discord.gg/MCbPKCFBs3">
  <img src="https://img.shields.io/discord/1064533716615049236.svg?style=for-the-badge" alt="Discord Channel">
</a>

## Show your support

<h3>Star this repo</h3>

Give a ⭐️ if this project helped you!

<h3>Donate to our project</h3>

If you do like our project and we hope that you do, can you please support us? Our project is not and is never going to be working for profit. We need the money just so we can continue doing what we do ;-) .

<a href="https://openscilab.com/#donation" target="_blank"><img src="https://github.com/openscilab/nava/raw/main/others/donation.png" height="90px" width="270px" alt="Nava Donation"></a>
