import unittest
import pandas as pd
import os
import sys
import requests
import time

sys.path.insert (0, '../tradingeconomics')
import tradingeconomics as te

te.login('guest:guest')

class TestForecasts(unittest.TestCase):

    def tearDown(self):
        time.sleep(3)

    def test_getForecastUpdates(self):
        a = te.getForecastUpdates(output_type='df')

        url = f'https://api.tradingeconomics.com/forecast/updates?c=guest:guest'
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')
        
        a['Ticker'] = a['Ticker'].str.strip()
        a = a.sort_values(by=['LastUpdate', 'Ticker'])
        a = a.reset_index(drop=True)

        b['Ticker'] = b['Ticker'].str.strip()
        b = b.sort_values(by=['LastUpdate', 'Ticker'])
        b = b.reset_index(drop=True)

        self.assertEqual(True, a.equals(b))


    def test_getForecastUpdates_country(self):
        a = te.getForecastUpdates(country='france', output_type='df')

        url = f'https://api.tradingeconomics.com/forecast/updates?c=guest:guest&country=france'
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')
        
        a['Ticker'] = a['Ticker'].str.strip()
        a = a.sort_values(by=['LastUpdate', 'Ticker'])
        a = a.reset_index(drop=True)

        b['Ticker'] = b['Ticker'].str.strip()
        b = b.sort_values(by=['LastUpdate', 'Ticker'])
        b = b.reset_index(drop=True)

        self.assertEqual(True, a.equals(b))


    def test_getForecastUpdates_country_date(self):
        a = te.getForecastUpdates(country='france', init_date='2024-11-20', output_type='df')

        url = f'https://api.tradingeconomics.com/forecast/updates?c=guest:guest&country=france&date=2024-11-20'
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')
        
        a['Ticker'] = a['Ticker'].str.strip()
        a = a.sort_values(by=['LastUpdate', 'Ticker'])
        a = a.reset_index(drop=True)

        b['Ticker'] = b['Ticker'].str.strip()
        b = b.sort_values(by=['LastUpdate', 'Ticker'])
        b = b.reset_index(drop=True)

        self.assertEqual(True, a.equals(b))

if __name__ == '__main__':
    unittest.main()