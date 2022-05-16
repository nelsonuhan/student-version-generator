# student-version-generator

Creates a "student version" of a Jupyter notebook by:

1. Removing all output from code cells.
2. Deleting all cells with a `solution` tag.

## Installation

```
pip install git+https://github.com/nelsonuhan/student-version-generator
```

## Usage

```
usage: sv [-h] filename

positional arguments:
  filename    Notebook with solutions

  optional arguments:
    -h, --help  show this help message and exit
```
