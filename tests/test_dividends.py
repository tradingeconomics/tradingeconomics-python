import unittest
import pandas as pd
import os
import sys
import requests
import time

sys.path.insert (0, '../tradingeconomics')
import tradingeconomics as te

te.login('guest:guest')

class TestgetDividends(unittest.TestCase):

    def tearDown(self):
        time.sleep(3)
        
    def test_getDividends_startDate_endDate(self):
        a = te.getDividends(startDate='2017-01-01', endDate='2018-01-01', output_type='df')

        url = f'https://api.tradingeconomics.com/dividends?c=guest:guest&d1=2017-01-01&d2=2018-01-01'
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')

        a['Symbol'] = a['Symbol'].str.strip()
        a = a.sort_values(by=['Symbol'])
        a = a.reset_index(drop=True)

        b['Symbol'] = b['Symbol'].str.strip()
        b = b.sort_values(by=['Symbol'])
        b = b.reset_index(drop=True)

        self.assertEqual(True, a.equals(b))

    def test_getDividends(self):
        a = te.getDividends(output_type='df')

        url = f'https://api.tradingeconomics.com/dividends?c=guest:guest'
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')
        
        a['Symbol'] = a['Symbol'].str.strip()
        a = a.sort_values(by=['Symbol'])
        a = a.reset_index(drop=True)

        b['Symbol'] = b['Symbol'].str.strip()
        b = b.sort_values(by=['Symbol'])
        b = b.reset_index(drop=True)
        self.assertEqual(True, a.equals(b))

    def test_getDividends_symbol(self):
        a = te.getDividends(symbols='aapl:us', output_type='df')

        url = f'https://api.tradingeconomics.com/dividends/symbol/aapl:us?c=guest:guest'
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')
        a['Symbol'] = a['Symbol'].str.strip()
        a = a.sort_values(by=['Symbol'])
        a = a.reset_index(drop=True)

        b['Symbol'] = b['Symbol'].str.strip()
        b = b.sort_values(by=['Symbol'])
        b = b.reset_index(drop=True)
        self.assertEqual(True, a.equals(b))

    def test_getDividends_startDate(self):
        a = te.getDividends(startDate='2017-01-01', output_type='df')
        
        url = f'https://api.tradingeconomics.com/dividends?c=guest:guest&d1=2017-01-01'
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')
        a['Symbol'] = a['Symbol'].str.strip()
        a = a.sort_values(by=['Symbol'])
        a = a.reset_index(drop=True)

        b['Symbol'] = b['Symbol'].str.strip()
        b = b.sort_values(by=['Symbol'])
        b = b.reset_index(drop=True)
        
        self.assertEqual(True, a.equals(b))

if __name__ == '__main__':
    unittest.main()
