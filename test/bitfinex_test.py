import unittest
import mock
from helpers import *
import requests
import httpretty

import bitfinex

class BitfinexTest(unittest.TestCase):

    def setUp(self):
        self.client = bitfinex.Client()


    def test_should_have_server(self):
        self.assertEqual("https://api.bitfinex.com/v1", self.client.server())

    def test_should_have_url_for_foo(self):
        expected = "https://api.bitfinex.com/v1/foo"
        self.assertEqual(expected, self.client.url_for("foo"))

    def test_should_have_url_for_ticker_symbol(self):
        expected = "https://api.bitfinex.com/v1/ticker/foo"
        actual = self.client.url_for(bitfinex.PATH_TICKER, ("foo"))
        self.assertEqual(expected, actual)

    def test_should_have_url_for_symbols(self):
        expected = self.client.url_for("foo")
        self.assertEqual("https://api.bitfinex.com/v1/foo", expected)

    def test_should_have_ticker_for_symbol(self):
        expected = self.client.url_for("foo/%s", ('bar'))
        self.assertEqual("https://api.bitfinex.com/v1/foo/bar", expected)

    @httpretty.activate
    def test_should_have_symbols(self):
        # mock out the symbol request
        httpretty.register_uri(httpretty.GET, self.client.url_for('symbols'),
                           body='["btcusd","ltcusd","ltcbtc"]',
                           status=200)

        expected = ["btcusd","ltcusd","ltcbtc"]
        self.assertEqual(expected, self.client.symbols())

    @httpretty.activate
    def test_should_have_ticker(self):

        # mock out the ticker request
        mock_body = '{"mid":"562.56495","bid":"562.15","ask":"562.9799","last_price":"562.25","timestamp":"1395552658.339936691"}'
        url = self.client.url_for(bitfinex.PATH_TICKER, ('btcusd'))
        httpretty.register_uri(httpretty.GET, url,
                           body=mock_body,
                           status=200)

        expected = {
            "mid": 562.56495,
            "bid": 562.15,
            "ask": 562.9799,
            "last_price": 562.25,
            "timestamp": 1395552658.339936691
        }

        self.assertEqual(expected, self.client.ticker('btcusd'))
