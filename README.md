# TCGPlayer-CLI (Under Development)

[![Generic badge](https://img.shields.io/badge/Python-3.7-COLOR.svg)](https://shields.io/)

## (Current) Features
* Auto-loads configuration from local directory & handles authorization behind the scenes
* Isolated Python 3.7 environment & dependency handling (using [Pipenv](https://docs.pipenv.org/en/latest/))

## Project Goals

0. Create a useful tool with minimal configuration required:
    * Adhere to [PEP8 Style Guide for Python](https://www.python.org/dev/peps/pep-0008/)
    * Pair features with reasonable, effective unit tests
    * Lint, document, and distribute the package

1. Retrieve data from the [TCGPlayer API](https://docs.tcgplayer.com/docs):
    * Use object-oriented features of Python; focus on appropriate inheritance
    * Implement Class-based representation of the TCG Player API structure
      * Top-Level Endpoints: **App**, **Catalog**, **Inventory**, **Prices**, **Stores**
      

2. Provide a command-line tool for interacting with API implementation:
    * Using [Click](https://click.palletsprojects.com/en/7.x/) command-line library to handle heavy-lifting
