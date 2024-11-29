import unittest
import pandas as pd
import os
import sys
import requests
import time

sys.path.insert (0, '../tradingeconomics')
import tradingeconomics as te

te.login('guest:guest')

class TestCreditRatings(unittest.TestCase):

    def tearDown(self):
        time.sleep(3)

    # def test_getCreditRatings_country(self):
    #     a = te.getCreditRatings(country='sweden', output_type='df')

    #     url = f'https://api.tradingeconomics.com/credit-ratings/country/sweden?c=guest:guest'
    #     data = requests.get(url).json()

    #     b = pd.DataFrame.from_dict(data, orient='columns')

    #     a = a.sort_values(by=['Date'])
    #     a = a.reset_index(drop=True)

    #     b = b.sort_values(by=['Date'])
    #     b = b.reset_index(drop=True)

    #     self.assertEqual(True, a.equals(b))

    def test_getCreditRatings_two_country(self):
        a = te.getCreditRatings(country=['mexico', 'sweden'], output_type='df')

        url = f'https://api.tradingeconomics.com/credit-ratings/country/mexico,sweden?c=guest:guest'
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')

        a = a.sort_values(by=['Date'])
        a = a.reset_index(drop=True)

        b = b.sort_values(by=['Date'])
        b = b.reset_index(drop=True)

        self.assertEqual(True, a.equals(b))

    def test_getHistoricalCreditRatings_country(self):

        a = te.getHistoricalCreditRatings(country='sweden', initDate='2010-08-01', endDate='2022-01-01', output_type='df')

        url = f'https://api.tradingeconomics.com/credit-ratings/historical/country/sweden?c=guest:guest&d1=2010-08-01&d2=2022-01-01'
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')

        a = a.sort_values(by=['Date'])
        a = a.reset_index(drop=True)

        b = b.sort_values(by=['Date'])
        b = b.reset_index(drop=True)

        self.assertEqual(True, a.equals(b))
