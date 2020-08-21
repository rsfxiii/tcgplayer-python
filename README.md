# TCGPlayer

[![Version badge](https://img.shields.io/badge/Python-3.7-COLOR.svg)](https://shields.io/)
![Coverage badge](badges/coverage.svg)
![License badge](badges/license-GPL-blue.svg)

**TCGPlayer** is a Python library to interact with the TCGPlayer (Trading Card Game Player) API. 

## To Contribute
1. Fork the repo, and clone your fork
2. Find an issue to work on **or** create an issue to propose changes
3. Make changes to fork
4. Tag @rsfxiii in the PR to have it reviewed

## Installation

`tcgplayer` requires at least Python 3.7
1. Install the package: `pip install tcgplayer`
2. Edit the `.env` file and add your TCGPlayer API credentials:

```
# .env
PUB_KEY=my-tcg-pubkey
PRIV_key=my-tcg-privkey
```

At this point, you should be ready to use the `Client` to make calls to whatever TCG Player API endpoints you want.

## Usage

```
# Import the resource endpoint you want to use
from tcgplayer.api.endpoints import Category

# Refresh your access token for the session
access_token = Client.refresh_access_token()

# Make an API call to TCGPlayer
all_categories = Client.handle_request('GET', Category.list(), {}, access_token)

# Make a call with path params
specific_category = Client.handle_request('get', Category.get_details(1), {}, access_token)

# Make a call with both path and query params
category_groups = Client.handle_request('get', Category.get_groups(1), {'limit': 10}, access_token)
```

> NOTE: Endpoint methods, like `Category.get_details` will accept *path* params, while `Client.handle_request` will accept *query* params.

## Project Goals

0. Write a maintainable, clean, and tested Python library:
    * Adhere to [PEP8 Style Guide for Python](https://www.python.org/dev/peps/pep-0008/)
    * Pair features with reasonable, effective unit tests
    * Lint, document, and distribute the package

1. Retrieve data from the [TCGPlayer API](https://docs.tcgplayer.com/docs):
    * Implement Class-based representation of the TCG Player API structure
      * Top-Level Endpoints: **App**, **Catalog**, **Inventory**, **Prices**

