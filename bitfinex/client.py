from __future__ import absolute_import
import requests
import json
import base64
import hmac
import hashlib
import time

PROTOCOL = "https"
HOST = "api.bitfinex.com"
VERSION = "v1"

PATH_SYMBOLS = "symbols"
PATH_TICKER = "ticker/%s"
PATH_TODAY = "today/%s"
PATH_STATS = "stats/%s"
PATH_LENDBOOK = "lendbook/%s"
PATH_ORDERBOOK = "book/%s"

# HTTP request timeout in seconds
TIMEOUT = 5.0



class TradeClient:
    """
    Authenticated client for trading through Bitfinex API
    """

    def __init__(self, key, secret):
        self.URL = "{0:s}://{1:s}/{2:s}".format(PROTOCOL, HOST, VERSION)
        self.KEY = key
        self.SECRET = secret
        pass

    @property
    def _nonce(self):
        """
        Returns a nonce
        Used in authentication
        """
        return str(time.time() * 1000000)

    def _sign_payload(self, payload):
        j = json.dumps(payload)
        data = base64.standard_b64encode(j.encode('utf8'))

        h = hmac.new(self.SECRET.encode('utf8'), data, hashlib.sha384)
        signature = h.hexdigest()
        return {
            "X-BFX-APIKEY": self.KEY,
            "X-BFX-SIGNATURE": signature,
            "X-BFX-PAYLOAD": data
        }

    def place_order(self, amount, price, side, ord_type, symbol='btcusd', exchange='bitfinex'):
        """
        Submit a new order.
        :param amount:
        :param price:
        :param side:
        :param ord_type:
        :param symbol:
        :param exchange:
        :return:
        """
        payload = {

            "request": "/v1/order/new",
            "nonce": self._nonce,
            "symbol": symbol,
            "amount": amount,
            "price": price,
            "exchange": exchange,
            "side": side,
            "type": ord_type

        }

        signed_payload = self._sign_payload(payload)
        r = requests.post(self.URL + "/order/new", headers=signed_payload, verify=True)
        json_resp = r.json()

        try:
            json_resp['order_id']
        except:
            return json_resp['message']

        return json_resp

    def delete_order(self, order_id):
        """
        Cancel an order.
        :param order_id:
        :return:
        """
        payload = {
            "request": "/v1/order/cancel",
            "nonce": self._nonce,
            "order_id": order_id
        }

        signed_payload = self._sign_payload(payload)
        r = requests.post(self.URL + "/order/cancel", headers=signed_payload, verify=True)
        json_resp = r.json()

        try:
            json_resp['avg_excution_price']
        except:
            return json_resp['message']

        return json_resp

    def delete_all_orders(self):
        """
        Cancel all orders.

        :return:
        """
        payload = {
            "request": "/v1/order/cancel/all",
            "nonce": self._nonce,
        }

        signed_payload = self._sign_payload(payload)
        r = requests.post(self.URL + "/order/cancel/all", headers=signed_payload, verify=True)
        json_resp = r.json()
        return json_resp

    def status_order(self, order_id):
        """
        Get the status of an order. Is it active? Was it cancelled? To what extent has it been executed? etc.
        :param order_id:
        :return:
        """
        payload = {
            "request": "/v1/order/status",
            "nonce": self._nonce,
            "order_id": order_id
        }

        signed_payload = self._sign_payload(payload)
        r = requests.post(self.URL + "/order/status", headers=signed_payload, verify=True)
        json_resp = r.json()

        try:
            json_resp['avg_excution_price']
        except:
            return json_resp['message']

        return json_resp

    def active_orders(self):
        """
        Fetch active orders
        """

        payload = {
            "request": "/v1/orders",
            "nonce": self._nonce
        }

        signed_payload = self._sign_payload(payload)
        r = requests.post(self.URL + "/orders", headers=signed_payload, verify=True)
        json_resp = r.json()

        return json_resp

    def active_positions(self):
        """
        Fetch active Positions
        """

        payload = {
            "request": "/v1/positions",
            "nonce": self._nonce
        }

        signed_payload = self._sign_payload(payload)
        r = requests.post(self.URL + "/positions", headers=signed_payload, verify=True)
        json_resp = r.json()
        return json_resp

    def claim_position(self, position_id):
        """
        Claim a position.
        :param position_id:
        :return:
        """
        payload = {
            "request": "/v1/position/claim",
            "nonce": self._nonce,
            "position_id": position_id
        }

        signed_payload = self._sign_payload(payload)
        r = requests.post(self.URL + "/position/claim", headers=signed_payload, verify=True)
        json_resp = r.json()

        return json_resp

    def past_trades(self, timestamp=0, symbol='btcusd'):
        """
        Fetch past trades
        :param timestamp:
        :param symbol:
        :return:
        """
        payload = {
            "request": "/v1/mytrades",
            "nonce": self._nonce,
            "symbol": symbol,
            "timestamp": timestamp
        }

        signed_payload = self._sign_payload(payload)
        r = requests.post(self.URL + "/mytrades", headers=signed_payload, verify=True)
        json_resp = r.json()

        return json_resp

    def place_offer(self, currency, amount, rate, period, direction):
        """

        :param currency:
        :param amount:
        :param rate:
        :param period:
        :param direction:
        :return:
        """
        payload = {
            "request": "/v1/offer/new",
            "nonce": self._nonce,
            "currency": currency,
            "amount": amount,
            "rate": rate,
            "period": period,
            "direction": direction
        }

        signed_payload = self._sign_payload(payload)
        r = requests.post(self.URL + "/offer/new", headers=signed_payload, verify=True)
        json_resp = r.json()

        return json_resp

    def cancel_offer(self, offer_id):
        """

        :param offer_id:
        :return:
        """
        payload = {
            "request": "/v1/offer/cancel",
            "nonce": self._nonce,
            "offer_id": offer_id
        }

        signed_payload = self._sign_payload(payload)
        r = requests.post(self.URL + "/offer/cancel", headers=signed_payload, verify=True)
        json_resp = r.json()

        return json_resp

    def status_offer(self, offer_id):
        """

        :param offer_id:
        :return:
        """
        payload = {
            "request": "/v1/offer/status",
            "nonce": self._nonce,
            "offer_id": offer_id
        }

        signed_payload = self._sign_payload(payload)
        r = requests.post(self.URL + "/offer/status", headers=signed_payload, verify=True)
        json_resp = r.json()

        return json_resp

    def active_offers(self):
        """
        Fetch active_offers
        :return:
        """
        payload = {
            "request": "/v1/offers",
            "nonce": self._nonce
        }

        signed_payload = self._sign_payload(payload)
        r = requests.post(self.URL + "/offers", headers=signed_payload, verify=True)
        json_resp = r.json()

        return json_resp

    def balances(self):
        """
        Fetch balances

        :return:
        """
        payload = {
            "request": "/v1/balances",
            "nonce": self._nonce
        }

        signed_payload = self._sign_payload(payload)
        r = requests.post(self.URL + "/balances", headers=signed_payload, verify=True)
        json_resp = r.json()

        return json_resp

    def history(self, currency, since=0, until=9999999999, limit=500, wallet='exchange'):
        """
        View you balance ledger entries
        :param currency: currency to look for
        :param since: Optional. Return only the history after this timestamp.
        :param until: Optional. Return only the history before this timestamp.
        :param limit: Optional. Limit the number of entries to return. Default is 500.
        :param wallet: Optional. Return only entries that took place in this wallet. Accepted inputs are: “trading”,
        “exchange”, “deposit”.
        """
        payload = {
            "request": "/v1/history",
            "nonce": self._nonce,
            "currency": currency,
            "since": since,
            "until": until,
            "limit": limit,
            "wallet": wallet
        }
        signed_payload = self._sign_payload(payload)
        r = requests.post(self.URL + "/history", headers=signed_payload, verify=True)
        json_resp = r.json()

        return json_resp



class Client:
    """
    Client for the bitfinex.com API.

    See https://www.bitfinex.com/pages/api for API documentation.
    """

    def server(self):
        return u"{0:s}://{1:s}/{2:s}".format(PROTOCOL, HOST, VERSION)


    def url_for(self, path, path_arg=None, parameters=None):

        # build the basic url
        url = "%s/%s" % (self.server(), path)

        # If there is a path_arh, interpolate it into the URL.
        # In this case the path that was provided will need to have string
        # interpolation characters in it, such as PATH_TICKER
        if path_arg:
            url = url % (path_arg)

        # Append any parameters to the URL.
        if parameters:
            url = "%s?%s" % (url, self._build_parameters(parameters))

        return url


    def symbols(self):
        """
        GET /symbols

        curl https://api.bitfinex.com/v1/symbols
        ['btcusd','ltcusd','ltcbtc']
        """
        return self._get(self.url_for(PATH_SYMBOLS))


    def ticker(self, symbol):
        """
        GET /ticker/:symbol

        curl https://api.bitfinex.com/v1/ticker/btcusd
        {
            'ask': '562.9999',
            'timestamp': '1395552290.70933607',
            'bid': '562.25',
            'last_price': u'562.25',
            'mid': u'562.62495'}
        """
        data = self._get(self.url_for(PATH_TICKER, (symbol)))

        # convert all values to floats
        return self._convert_to_floats(data)


    def today(self, symbol):
        """
        GET /today/:symbol

        curl "https://api.bitfinex.com/v1/today/btcusd"
        {"low":"550.09","high":"572.2398","volume":"7305.33119836"}
        """

        data = self._get(self.url_for(PATH_TODAY, (symbol)))

        # convert all values to floats
        return self._convert_to_floats(data)


    def stats(self, symbol):
        """
        curl https://api.bitfinex.com/v1/stats/btcusd
        [
            {"period":1,"volume":"7410.27250155"},
            {"period":7,"volume":"52251.37118006"},
            {"period":30,"volume":"464505.07753251"}
        ]
        """
        data = self._get(self.url_for(PATH_STATS, (symbol)))

        for period in data:

            for key, value in period.items():
                if key == 'period':
                    new_value = int(value)
                elif key == 'volume':
                    new_value = float(value)

                period[key] = new_value

        return data


    def lendbook(self, currency, parameters=None):
        """
        curl "https://api.bitfinex.com/v1/lendbook/btc"

        {"bids":[{"rate":"5.475","amount":"15.03894663","period":30,"timestamp":"1395112149.0","frr":"No"},{"rate":"2.409","amount":"14.5121868","period":7,"timestamp":"1395497599.0","frr":"No"}],"asks":[{"rate":"6.351","amount":"15.5180735","period":5,"timestamp":"1395549996.0","frr":"No"},{"rate":"6.3588","amount":"626.94808249","period":30,"timestamp":"1395400654.0","frr":"Yes"}]}

        Optional parameters

        limit_bids (int): Optional. Limit the number of bids (loan demands) returned. May be 0 in which case the array of bids is empty. Default is 50.
        limit_asks (int): Optional. Limit the number of asks (loan offers) returned. May be 0 in which case the array of asks is empty. Default is 50.
        """
        data = self._get(self.url_for(PATH_LENDBOOK, path_arg=currency, parameters=parameters))

        for lend_type in data.keys():

            for lend in data[lend_type]:

                for key, value in lend.items():
                    if key in ['rate', 'amount', 'timestamp']:
                        new_value = float(value)
                    elif key == 'period':
                        new_value = int(value)
                    elif key == 'frr':
                        new_value = value == 'Yes'

                    lend[key] = new_value

        return data


    def order_book(self, symbol, parameters=None):
        """
        curl "https://api.bitfinex.com/v1/book/btcusd"

        {"bids":[{"price":"561.1101","amount":"0.985","timestamp":"1395557729.0"}],"asks":[{"price":"562.9999","amount":"0.985","timestamp":"1395557711.0"}]}

        The 'bids' and 'asks' arrays will have multiple bid and ask dicts.

        Optional parameters

        limit_bids (int): Optional. Limit the number of bids returned. May be 0 in which case the array of bids is empty. Default is 50.
        limit_asks (int): Optional. Limit the number of asks returned. May be 0 in which case the array of asks is empty. Default is 50.

        eg.
        curl "https://api.bitfinex.com/v1/book/btcusd?limit_bids=1&limit_asks=0"
        {"bids":[{"price":"561.1101","amount":"0.985","timestamp":"1395557729.0"}],"asks":[]}

        """
        data = self._get(self.url_for(PATH_ORDERBOOK, path_arg=symbol, parameters=parameters))

        for type_ in data.keys():
            for list_ in data[type_]:
                for key, value in list_.items():
                    list_[key] = float(value)

        return data


    def _convert_to_floats(self, data):
        """
        Convert all values in a dict to floats
        """
        for key, value in data.items():
            data[key] = float(value)

        return data


    def _get(self, url):
        return requests.get(url, timeout=TIMEOUT).json()


    def _build_parameters(self, parameters):
        # sort the keys so we can test easily in Python 3.3 (dicts are not
        # ordered)
        keys = list(parameters.keys())
        keys.sort()

        return '&'.join(["%s=%s" % (k, parameters[k]) for k in keys])
