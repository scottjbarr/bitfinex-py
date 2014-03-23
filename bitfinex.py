import requests
import json

PROTOCOL = "https"
HOST = "api.bitfinex.com"
VERSION = "v1"

PATH_SYMBOLS = "symbols"
PATH_TICKER = "ticker/%s"
PATH_TODAY = "today/%s"

class Client(object):

    def __initialize__(self):
        pass

    def server(self):
        return "%s://%s/%s" % (PROTOCOL, HOST, VERSION)

    def url_for(self, path, parameters = ()):

        # build the basic url
        url = "%s/%s" % (self.server(), path)

        # If there are parameters, interpolate them into the URL.
        # In this case the path that was provided will have string
        # interpolation characters in it, such as PATH_TICKER
        if len(parameters) > 0:
            url = url % parameters

        return url

    def symbols(self):
        """
        GET symbols

        curl https://api.bitfinex.com/v1/symbols
        ['btcusd','ltcusd','ltcbtc']
        """
        return self._get(self.url_for(PATH_SYMBOLS))

    def ticker(self, symbol):
        '''
        GET ticker/:symbol

        curl https://api.bitfinex.com/v1/ticker/btcusd
        {u'ask': u'562.9999', u'timestamp': u'1395552290.70933607', u'bid': u'562.25', u'last_price': u'562.25', u'mid': u'562.62495'}
        '''
        data = self._get(self.url_for(PATH_TICKER, (symbol)))

        # all values can be converted to floats
        return self._convert_to_floats(data)

    def today(self, symbol):
        '''
        GET today/:symbol

        curl "https://api.bitfinex.com/v1/today/btcusd"
        {"low":"550.09","high":"572.2398","volume":"7305.33119836"}
        '''

        data = self._get(self.url_for(PATH_TODAY, (symbol)))

        # all values can be converted to floats
        return self._convert_to_floats(data)

    def _convert_to_floats(self, data):
        """
        Convert all values in a dict to floats
        """
        for key, value in data.iteritems():
            data[key] = float(value)

        return data

    def _get(self, url):
        # print 'Response Code: ' + str(r.status_code)
        # print 'Response Header: ' + str(r.headers)
        # print 'Response Content: '+ str(r.content)
        response = requests.get(url) #, data={}, headers=headers)

        return json.loads(response.content)
