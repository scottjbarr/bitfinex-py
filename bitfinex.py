import requests
import json

PROTOCOL = "https"
HOST = "api.bitfinex.com"
VERSION = "v1"

PATH_SYMBOLS = "symbols"
PATH_TICKER = "ticker/%s"
PATH_TODAY = "today/%s"
PATH_STATS = "stats/%s"

class Client(object):
    """
    Client for the bitfinex.com API.

    See https://www.bitfinex.com/pages/api for API documentation.
    """

    def __initialize__(self):
        pass

    def server(self):
        return "%s://%s/%s" % (PROTOCOL, HOST, VERSION)

    def url_for(self, path, parameters = ()):

        # build the basic url
        url = "%s/%s" % (self.server(), path)

        # If there are parameters, interpolate them into the URL.
        # In this case the path that was provided will need to have string
        # interpolation characters in it, such as PATH_TICKER
        if len(parameters) > 0:
            url = url % parameters

        return url

    def symbols(self):
        """
        GET /symbols

        curl https://api.bitfinex.com/v1/symbols
        ['btcusd','ltcusd','ltcbtc']
        """
        return self._get(self.url_for(PATH_SYMBOLS))

    def ticker(self, symbol):
        '''
        GET /ticker/:symbol

        curl https://api.bitfinex.com/v1/ticker/btcusd
        {
            'ask': '562.9999',
            'timestamp': '1395552290.70933607',
            'bid': '562.25',
            'last_price': u'562.25',
            'mid': u'562.62495'}
        '''
        data = self._get(self.url_for(PATH_TICKER, (symbol)))

        # convert all values to floats
        return self._convert_to_floats(data)

    def today(self, symbol):
        '''
        GET /today/:symbol

        curl "https://api.bitfinex.com/v1/today/btcusd"
        {"low":"550.09","high":"572.2398","volume":"7305.33119836"}
        '''

        data = self._get(self.url_for(PATH_TODAY, (symbol)))

        # convert all values to floats
        return self._convert_to_floats(data)

    def stats(self, symbol):
        '''
        curl https://api.bitfinex.com/v1/stats/btcusd
        [
            {"period":1,"volume":"7410.27250155"},
            {"period":7,"volume":"52251.37118006"},
            {"period":30,"volume":"464505.07753251"}
        ]
        '''
        data = self._get(self.url_for(PATH_STATS, (symbol)))

        for period in data:

            for key, value in period.iteritems():
                if key == 'period':
                    new_value = int(value)
                elif key == 'volume':
                    new_value = float(value)

                period[key] = new_value

        return data


    def _convert_to_floats(self, data):
        """
        Convert all values in a dict to floats
        """
        for key, value in data.iteritems():
            data[key] = float(value)

        return data

    def _get(self, url):
        response = requests.get(url)

        return json.loads(response.content)
