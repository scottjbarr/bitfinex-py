from setuptools import setup

setup(name='bitfinex',
    version='0.2.0',
    description = 'Python client for the Bitfinex API',
    author = 'Scott Barr',
    author_email = 'scottjbarr@gmail.com',
    url = 'https://github.com/scottjbarr/bitfinex',
    license = 'MIT',
    packages=['bitfinex'],
    scripts = ['scripts/watch_orderbook'],
    download_url = 'https://github.com/scottjbarr/bitfinex/tarball/0.2.0',
    keywords = ['bitcoin', 'btc'],
    classifiers = [],
    zip_safe=True)
