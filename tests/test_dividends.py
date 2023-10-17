import unittest
import pandas as pd
import os
import sys

sys.path.insert (0, '../tradingeconomics')
import tradingeconomics as te

te.login('guest:guest')

class TestgetDividends(unittest.TestCase):

    def test_getDividends_startDate_endDate(self):
        a = te.getDividends(startDate='2017-01-01', endDate='2018-01-01', output_type='df')
        data = [
                    {
                        "DateEx": "2017-01-03",
                        "Symbol": "ORCL:US             ",
                        "Name": "Oracle",
                        "Actual": 0.15,
                        "DatePayment": "2017-01-26",
                        "Currency": "USD",
                        "LastUpdate": "2023-09-27T23:09:00"
                    },
                    {
                        "DateEx": "2017-01-04",
                        "Symbol": "AXP:US              ",
                        "Name": "American Express",
                        "Actual": 0.32,
                        "DatePayment": "2017-02-10",
                        "Currency": "USD",
                        "LastUpdate": "2023-09-27T18:11:00"
                    },
                    {
                        "DateEx": "2017-01-04",
                        "Symbol": "BMY:US              ",
                        "Name": "Bristol-Myers Squibb",
                        "Actual": 0.39,
                        "DatePayment": "2017-02-01",
                        "Currency": "USD",
                        "LastUpdate": "2023-09-27T18:29:00"
                    }
                ]
        b = pd.DataFrame(data)
        a['Symbol'] = a['Symbol'].str.strip()
        a = a.sort_values(by=['Symbol'])
        a = a.reset_index(drop=True)

        b['Symbol'] = b['Symbol'].str.strip()
        b = b.sort_values(by=['Symbol'])
        b = b.reset_index(drop=True)

        self.assertEqual(True, a.equals(b))

    def test_getDividends(self):
        a = te.getDividends(output_type='df')
        data = [
                    {
                        "DateEx": "2023-07-19",
                        "Symbol": "CAT:US              ",
                        "Name": "Caterpillar",
                        "Actual": 1.3,
                        "DatePayment": "2023-08-18",
                        "Currency": "USD",
                        "LastUpdate": "2023-09-27T18:41:00"
                    },
                    {
                        "DateEx": "2023-07-20",
                        "Symbol": "APA:US              ",
                        "Name": "APA",
                        "Actual": 0.25,
                        "DatePayment": "2023-08-22",
                        "Currency": "USD",
                        "LastUpdate": "2023-09-27T18:00:00"
                    },
                    {
                        "DateEx": "2023-07-20",
                        "Symbol": "CL:US               ",
                        "Name": "Colgate-Palmolive",
                        "Actual": 0.48,
                        "DatePayment": "2023-08-15",
                        "Currency": "USD",
                        "LastUpdate": "2023-09-27T19:00:00"
                    }
                ]
        b = pd.DataFrame(data)
        a['Symbol'] = a['Symbol'].str.strip()
        a = a.sort_values(by=['Symbol'])
        a = a.reset_index(drop=True)

        b['Symbol'] = b['Symbol'].str.strip()
        b = b.sort_values(by=['Symbol'])
        b = b.reset_index(drop=True)
        self.assertEqual(True, a.equals(b))

    def test_getDividends_symbol(self):
        a = te.getDividends(symbols='aapl:us', output_type='df')
        data = [
            {
                "DateEx": "2023-08-11",
                "Symbol": "AAPL:US             ",
                "Name": "Apple",
                "Actual": 0.24,
                "DatePayment": "2023-08-17",
                "Currency": "USD",
                "LastUpdate": "2023-09-27T17:21:00"
            }
        ]

        b = pd.DataFrame(data)
        a['Symbol'] = a['Symbol'].str.strip()
        a = a.sort_values(by=['Symbol'])
        a = a.reset_index(drop=True)

        b['Symbol'] = b['Symbol'].str.strip()
        b = b.sort_values(by=['Symbol'])
        b = b.reset_index(drop=True)
        self.assertEqual(True, a.equals(b))

    def test_getDividends_startDate(self):
        a = te.getDividends(startDate='2017-01-01', output_type='df')
        data = [
            {
                "DateEx": "2017-01-03",
                "Symbol": "ORCL:US             ",
                "Name": "Oracle",
                "Actual": 0.15,
                "DatePayment": "2017-01-26",
                "Currency": "USD",
                "LastUpdate": "2023-09-27T23:09:00"
            },
            {
                "DateEx": "2017-01-04",
                "Symbol": "AXP:US              ",
                "Name": "American Express",
                "Actual": 0.32,
                "DatePayment": "2017-02-10",
                "Currency": "USD",
                "LastUpdate": "2023-09-27T18:11:00"
            },
            {
                "DateEx": "2017-01-04",
                "Symbol": "BMY:US              ",
                "Name": "Bristol-Myers Squibb",
                "Actual": 0.39,
                "DatePayment": "2017-02-01",
                "Currency": "USD",
                "LastUpdate": "2023-09-27T18:29:00"
            }
        ]

        b = pd.DataFrame(data)
        a['Symbol'] = a['Symbol'].str.strip()
        a = a.sort_values(by=['Symbol'])
        a = a.reset_index(drop=True)

        b['Symbol'] = b['Symbol'].str.strip()
        b = b.sort_values(by=['Symbol'])
        b = b.reset_index(drop=True)
        
        self.assertEqual(True, a.equals(b))

if __name__ == '__main__':
    unittest.main()
