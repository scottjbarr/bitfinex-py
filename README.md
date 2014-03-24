# Bitfinex Python Client

A Python client for the Bitfinex API.

Most of the unauthenticated calls have been implemented.  It is planned to
implement the remainder of the API.


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

Or you can just run the tests

    nosetests


## Usage

See the examples directory for samples.

e.g.

    PYTHONPATH=.:$PYTHONPATH python examples/basic.py


## Compatibility

This code has been tested on

- Python 2.7.5
- Python 3.3.1


## TODO

- Package the code so it can be installed by pip.
- Implement all API calls.


## References

- https://www.bitfinex.com/pages/api


## Licence

The MIT License (MIT)

Copyright (c) 2014 Scott Barr

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
