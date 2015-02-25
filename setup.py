from setuptools import setup

# Runtime dependencies. See requirements.txt for development dependencies.
dependencies = [
    'requests',
    'httpretty'
]

setup(name='bitfinex',
    version='0.2.3',
    description = 'Python client for the Bitfinex API',
    author = 'Scott Barr',
    author_email = 'scottjbarr@gmail.com',
    url = 'https://github.com/scottjbarr/bitfinex',
    license = 'MIT',
    packages=['bitfinex'],
    scripts = ['scripts/watch_orderbook'],
    requires = dependencies,
    download_url = 'https://github.com/scottjbarr/bitfinex/tarball/0.2.3',
    keywords = ['bitcoin', 'btc'],
    classifiers = [],
    zip_safe=True)
