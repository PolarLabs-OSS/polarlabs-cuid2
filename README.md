# PolarLabs CUID2 Batch Toolkit

An independent, MIT-licensed extension of [gordon-code/cuid2](https://github.com/gordon-code/cuid2), adding a bounded command-line batch generator. The original implementation, copyright and MIT license are retained. See [UPSTREAM.md](UPSTREAM.md) for full provenance. Not affiliated with the original maintainers.

## PolarLabs batch CLI

Install the source package locally, then generate a batch of IDs:

```bash
pip install -e .
polarlabs-cuid2 --count 5 --length 24
```

Options: `--count` (1–10000) and `--length` (2–98). Values outside those bounds are rejected. To run our isolated tests: `PYTHONPATH=src:. python -m unittest discover -s polarlabs_tests -v` on Linux/macOS; on Windows PowerShell set `$env:PYTHONPATH='src;.'` before the test command.

The original upstream README follows below. The badge and installation instructions in that section refer to the *original* package, not a PolarLabs release.

---

# cuid2

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://img.shields.io/badge/python-3.8+-blue.svg)
[![PyPi](https://img.shields.io/pypi/v/cuid2.svg)](https://pypi.python.org/pypi/cuid2)
[![PyPi](https://img.shields.io/pypi/dm/cuid2.svg)](https://pypi.python.org/pypi/cuid2)
[![cuid2](https://snyk.io/advisor/python/cuid2/badge.svg)](https://snyk.io/advisor/python/cuid2)

CUID2 for Python 3. Next generation GUIDs. Collision-resistant ids optimized for 
horizontal scaling and performance.

A port of the [CUID2 reference implementation](https://github.com/paralleldrive/cuid2) 
by [Parallel Drive](https://github.com/paralleldrive) to Python 3.

> :memo: Note: Originally taken from https://github.com/overflowdigital before it 
> was unpublished. Thank you to @joshuathompsonlindley for your original contribution!

## What is CUID2?

* Secure: It's not possible to guess the next ID.
* Collision resistant: It's extremely unlikely to generate the same ID twice.
* Horizontally scalable: Generate IDs on multiple machines without coordination.
* Offline-compatible: Generate IDs without a network connection.
* URL and name-friendly: No special characters.

## Why?

For more information on the theory and usage of CUID2, see the 
[following](https://github.com/paralleldrive/cuid2#why).

## Improvements Over CUID

For more information on the improvements of CUID2 over CUID, see the 
[following](https://github.com/paralleldrive/cuid2#improvements-over-cuid).


## Install
```
pip install cuid2
```

## Usage

You can generate CUIDs directly in the terminal with the following:
```bash
$ cuid2
```

Or you can rely on a CUID wrapper if you don't need any customizations:
```python
from typing import Callable
from cuid2 import cuid_wrapper

cuid_generator: Callable[[], str] = cuid_wrapper()

def main():
  my_cuid: str = cuid_generator()
  next_cuid: str = cuid_generator()
```

Finally, for more explicit control of the CUID generator, you can instantiate the class directly:
```python
from cuid2 import Cuid

CUID_GENERATOR: Cuid = Cuid(length=10)

def main():
  my_cuid: str = CUID_GENERATOR.generate()
  next_cuid: str = CUID_GENERATOR.generate()
```
