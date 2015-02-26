from setuptools import setup

version='0.2.5'

# Runtime dependencies. See requirements.txt for development dependencies.
dependencies=[
    'requests',
    'httpretty'
]

setup(name='bitfinex',
    version=version,
    description='Python client for the Bitfinex API',
    author='Scott Barr',
    author_email='scottjbarr@gmail.com',
    url='https://github.com/scottjbarr/bitfinex',
    license='MIT',
    packages=['bitfinex'],
    scripts=['scripts/watch_orderbook'],
    install_requires=dependencies,
    download_url='https://github.com/scottjbarr/bitfinex/tarball/%s' % version,
    keywords=['bitcoin', 'btc'],
    classifiers=[],
    zip_safe=True)
