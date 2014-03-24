# Bitfinex Python Client

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

## References

- https://www.bitfinex.com/pages/api
- http://pastebin.com/j7jzFNRA
