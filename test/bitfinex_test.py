import unittest
import mock
import requests
import httpretty

from decouple import config

from bitfinex.client import Client, TradeClient

API_KEY = config('API_KEY')
API_SECRET = config('API_SECRET')

class BitfinexTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()


    def test_should_have_server(self):
        self.assertEqual("https://api.bitfinex.com/v1", self.client.server())


    def test_should_have_url_for_foo(self):
        expected = "https://api.bitfinex.com/v1/foo"
        self.assertEqual(expected, self.client.url_for("foo"))


    def test_should_have_url_for_path_arg(self):
        expected = "https://api.bitfinex.com/v1/foo/bar"
        actual = self.client.url_for('foo/%s', path_arg="bar")
        self.assertEqual(expected, actual)


    def test_should_have_url_with_parameters(self):
        expected = "https://api.bitfinex.com/v1/foo?a=1&b=2"
        actual = self.client.url_for('foo', parameters={'a': 1, 'b': 2})
        self.assertEqual(expected, actual)


    def test_should_have_url_for(self):
        expected = self.client.url_for("foo")
        self.assertEqual("https://api.bitfinex.com/v1/foo", expected)


    def test_should_have_url_for_with_path_arg(self):
        expected = "https://api.bitfinex.com/v1/foo/bar"
        path = "foo/%s"
        self.assertEqual(expected, self.client.url_for(path, path_arg='bar'))
        self.assertEqual(expected, self.client.url_for(path, 'bar'))


    def test_should_have_url_for_with_parameters(self):
        expected = "https://api.bitfinex.com/v1/foo?a=1"
        self.assertEqual(expected, self.client.url_for("foo", parameters={'a': 1}))
        self.assertEqual(expected, self.client.url_for("foo", None, {'a': 1}))


    def test_should_have_url_for_with_path_arg_and_parameters(self):
        expected = "https://api.bitfinex.com/v1/foo/bar?a=1"
        path = "foo/%s"
        self.assertEqual(expected, self.client.url_for(path, path_arg='bar', parameters={'a': 1}))
        self.assertEqual(expected, self.client.url_for(path, 'bar', {'a': 1}))


    @httpretty.activate
    def test_should_have_symbols(self):
        # mock out the request
        mock_body = '["btcusd","ltcusd","ltcbtc"]'
        url = self.client.url_for('symbols')
        httpretty.register_uri(httpretty.GET, url, body=mock_body, status=200)

        expected = ["btcusd","ltcusd","ltcbtc"]
        self.assertEqual(expected, self.client.symbols())


    @httpretty.activate
    def test_should_have_ticker(self):
        # mock out the request
        mock_body = '{"mid":"562.56495","bid":"562.15","ask":"562.9799","last_price":"562.25","timestamp":"1395552658.339936691"}'
        url = self.client.url_for('ticker/%s', path_arg='btcusd')
        httpretty.register_uri(httpretty.GET, url, body=mock_body, status=200)

        expected = {
            "mid": 562.56495,
            "bid": 562.15,
            "ask": 562.9799,
            "last_price": 562.25,
            "timestamp": 1395552658.339936691
        }

        self.assertEqual(expected, self.client.ticker('btcusd'))


    @httpretty.activate
    def test_should_have_today(self):
        # mock out the request
        mock_body = '{"low":"550.09","high":"572.2398","volume":"7305.33119836"}'
        url = self.client.url_for('today/%s', path_arg='btcusd')
        httpretty.register_uri(httpretty.GET, url, body=mock_body, status=200)

        expected = {
            "low": 550.09,
            "high": 572.2398,
            "volume": 7305.33119836
        }

        self.assertEqual(expected, self.client.today('btcusd'))


    @httpretty.activate
    def test_should_have_stats(self):
        # mock out the request
        mock_body = '[{"period":1,"volume":"7410.27250155"},{"period":7,"volume":"52251.37118006"},{"period":30,"volume":"464505.07753251"}]'
        url = self.client.url_for('stats/%s', path_arg='btcusd')
        httpretty.register_uri(httpretty.GET, url, body=mock_body, status=200)

        expected = [
            {"period": 1, "volume": 7410.27250155},
            {"period": 7, "volume": 52251.37118006},
            {"period": 30,"volume": 464505.07753251}
        ]

        self.assertEqual(expected, self.client.stats('btcusd'))


    @httpretty.activate
    def test_should_have_lendbook(self):
        # mock out the request
        mock_body = '{"bids":[{"rate":"5.475","amount":"15.03894663","period":30,"timestamp":"1395112149.0","frr":"No"},{"rate":"2.409","amount":"14.5121868","period":7,"timestamp":"1395497599.0","frr":"No"}],"asks":[{"rate":"6.351","amount":"15.5180735","period":5,"timestamp":"1395549996.0","frr":"No"},{"rate":"6.3588","amount":"626.94808249","period":30,"timestamp":"1395400654.0","frr":"Yes"}]}'
        url = self.client.url_for('lendbook/%s', 'btc')
        httpretty.register_uri(httpretty.GET, url, body=mock_body, status=200)

        expected = {
            "bids": [
                {"rate": 5.475, "amount": 15.03894663, "period": 30, "timestamp": 1395112149.0, "frr": False},
                {"rate": 2.409, "amount": 14.5121868, "period": 7, "timestamp": 1395497599.0, "frr": False}
            ],
            "asks": [
                {"rate": 6.351, "amount": 15.5180735, "period": 5, "timestamp": 1395549996.0, "frr": False},
                {"rate": 6.3588, "amount": 626.94808249, "period": 30, "timestamp": 1395400654.0, "frr": True}
            ]
        }

        self.assertEqual(expected, self.client.lendbook('btc'))


    @httpretty.activate
    def test_should_have_lendbook_with_parameters(self):
        # mock out the request
        mock_body = '{"bids":[{"rate":"5.475","amount":"15.03894663","period":30,"timestamp":"1395112149.0","frr":"No"},{"rate":"2.409","amount":"14.5121868","period":7,"timestamp":"1395497599.0","frr":"No"}],"asks":[]}'
        parameters = {'limit_bids': 2, 'limit_asks': 0}
        url = self.client.url_for('lendbook/%s', 'btc', parameters)
        httpretty.register_uri(httpretty.GET, url, body=mock_body, status=200)

        expected = {
            "bids": [
                {"rate": 5.475, "amount": 15.03894663, "period": 30, "timestamp": 1395112149.0, "frr": False},
                {"rate": 2.409, "amount": 14.5121868, "period": 7, "timestamp": 1395497599.0, "frr": False}
            ],
            "asks": [
            ]
        }

        self.assertEqual(expected, self.client.lendbook('btc', parameters))


    @httpretty.activate
    def test_should_have_order_book(self):
        # mock out the request
        mock_body = '{"bids":[{"price":"562.2601","amount":"0.985","timestamp":"1395567556.0"}],"asks":[{"price":"563.001","amount":"0.3","timestamp":"1395532200.0"}]}'
        url = self.client.url_for('book/%s', 'btcusd')
        httpretty.register_uri(httpretty.GET, url, body=mock_body, status=200)

        expected = {
            "bids": [
                {"price": 562.2601, "amount": 0.985, "timestamp": 1395567556.0}
            ],
            "asks": [
                {"price": 563.001, "amount": 0.3, "timestamp": 1395532200.0}
            ]
        }

        self.assertEqual(expected, self.client.order_book('btcusd'))


    @httpretty.activate
    def test_should_have_order_book_with_parameters(self):
        # mock out the request
        mock_body = '{"bids":[{"price":"562.2601","amount":"0.985","timestamp":"1395567556.0"}],"asks":[]}'
        parameters = {'limit_asks': 0}
        url = self.client.url_for('book/%s', 'btcusd', parameters)
        httpretty.register_uri(httpretty.GET, url, body=mock_body, status=200)

        expected = {
            "bids": [
                {"price": 562.2601, "amount": 0.985, "timestamp": 1395567556.0}
            ],
            "asks": []
        }

        self.assertEqual(expected, self.client.order_book('btcusd', parameters))


class TestTradeClient(unittest.TestCase):
    def setUp(self):
        self.tc = TradeClient(API_KEY, API_SECRET)

    def test_instantiate_tradeclient(self):
        self.assertIsInstance(self.tc, TradeClient)

    def test_get_active_orders_returns_json(self):
        ao = self.tc.active_orders()
        self.assertIsInstance(ao, list)

    def test_get_active_positions_returns_json(self):
        ap = self.tc.active_positions()
        self.assertIsInstance(ap, list)

    def test_get_full_history(self):
        ap = self.tc.active_positions()
        self.assertIsInstance(ap, list)
