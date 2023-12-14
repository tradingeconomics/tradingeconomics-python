import unittest
import pandas as pd
import os
import sys
import requests

sys.path.insert (0, '../tradingeconomics')
import tradingeconomics as te

te.login('guest:guest')

class TestgetIpo(unittest.TestCase):

    def test_getIpo(self):
        a = te.getIpo(output_type='df')

        url = f'https://api.tradingeconomics.com/ipo?c=guest:guest'
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')
        
        a['Ticker'] = a['Ticker'].str.strip()
        a = a.sort_values(by=['Ticker'])
        a = a.reset_index(drop=True)

        b['Ticker'] = b['Ticker'].str.strip()
        b = b.sort_values(by=['Ticker'])
        b = b.reset_index(drop=True)
        self.assertEqual(True, a.equals(b))


if __name__ == '__main__':
    unittest.main()