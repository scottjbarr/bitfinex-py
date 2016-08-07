# Bitfinex Python Client

__DEPRECATED__ : _I consider this repo dead as of August 2nd 2016, when
Bitfinex was hacked. Feel free to fork it._

A Python client for the Bitfinex API.

Most of the unauthenticated calls have been implemented.  It is planned to
implement the remainder of the API.

## Installation

    pip install bitfinex


## Poll The Order Book

Run the ```bitfinex-poll-orderbook``` script in a terminal.

Press ```Ctrl-c``` to exit.

    bitfinex-poll-orderbook

## Setup

Install the libs

    pip install -r ./requirements.txt


## Tests

Depending on your system, install one of the following libs

- pyinotify (Linux)
- pywin32 (Windows)
- MacFSEvents (OSX)

Sniffer will watch for changes

    sniffer -x --nocapture

Or Sniffer with code coverage enabled...

    sniffer -x --nocapture -x--with-coverage -x--cover-html -x--cover-package=bitfinex

Or you can just run the tests

    nosetests

### Test Coverage

Test coverage of the code. View cover/index.html to view detailed reports.

    nosetests --with-coverage --cover-html --cover-package bitfinex


## Usage

See the examples directory for samples.

e.g.

    PYTHONPATH=.:$PYTHONPATH python examples/basic.py


## Compatibility

This code has been tested on

- Python 2.7.5
- Python 3.3.1


## TODO

- Implement all API calls that Bitfinex make available.


## References

- [https://www.bitfinex.com/pages/api](https://www.bitfinex.com/pages/api)
- [https://community.bitfinex.com/showwiki.php?title=Sample+API+Code](https://community.bitfinex.com/showwiki.php?title=Sample+API+Code)
- [https://gist.github.com/jordanbaucke/5812039](https://gist.github.com/jordanbaucke/5812039)

## Licence

The MIT License (MIT)

Copyright (c) 2014-2015 Scott Barr

See [LICENSE.md](LICENSE.md)
