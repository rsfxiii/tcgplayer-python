# TCGPlayer(Under Development)

[![Generic badge](https://img.shields.io/badge/Python-3.7-COLOR.svg)](https://shields.io/)

**TCGPlayer** is a Python library to interact with the TCGPlayer (Trading Card Game Player) API.

## (Current) Features
* Auto-loads configuration `config.ini` file from local directory & handles authorization behind the scenes

## Endpoint Methods

### Catalog Endpoints
**Categories**
- `.list` - List all Categories of TCGPlayer resources
- `.get_details` - View detailed information about a Category
- `.get_search_manifest` - Retrieve search manfiest for a Category (sorting & filtering options)
- `.search_products` - Search for Product within Category by search term
- `.list_groups` - List all Category Groups
- `.get_printings` - Retrieve printinggs within a Category
- `.get_rarities` - Retrieive rarities within a Category
- `.list_conditions` - List conditions within a Category
- `.list_languages` - List available languages associated with a Category
- `.list_media` - List available media associated with a Category

**Groups**
- `list` - List details of all Groups in the Catalog

## Project Goals

0. Write a maintainable, clean, and tested Python library:
    * Adhere to [PEP8 Style Guide for Python](https://www.python.org/dev/peps/pep-0008/)
    * Pair features with reasonable, effective unit tests
    * Lint, document, and distribute the package

1. Retrieve data from the [TCGPlayer API](https://docs.tcgplayer.com/docs):
    * Implement Class-based representation of the TCG Player API structure
      * Top-Level Endpoints: **App**, **Catalog**, **Inventory**, **Prices**, **Stores**
