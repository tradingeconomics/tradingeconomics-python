import unittest
import pandas as pd
import os
import sys
import requests
import time

sys.path.insert (0, '../tradingeconomics')
import tradingeconomics as te

te.login('guest:guest')

class TestForecastsUpdates(unittest.TestCase):

    def tearDown(self):
        time.sleep(5)

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

    def test_getForecastUpdates_date(self):
        a = te.getForecastUpdates(init_date='2024-11-20', output_type='df')

        url = f'https://api.tradingeconomics.com/forecast/updates?start_date=2024-11-20&c=guest:guest'
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')
        
        a['Ticker'] = a['Ticker'].str.strip()
        a = a.sort_values(by=['LastUpdate', 'Ticker'])
        a = a.reset_index(drop=True)

        b['Ticker'] = b['Ticker'].str.strip()
        b = b.sort_values(by=['LastUpdate', 'Ticker'])
        b = b.reset_index(drop=True)
        
        self.assertEqual(True, a.equals(b))

class TestForecastsMarkets(unittest.TestCase):

    def tearDown(self):
        time.sleep(5)

    def test_getForecastsMarkets_category(self):

        a = te.getMarketsForecasts(category='index', output_type='df')

        url = f'https://api.tradingeconomics.com/markets/forecasts/index?c=guest:guest'
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')

        a['Symbol'] = a['Symbol'].str.strip()
        a = a.sort_values(by=['Symbol'])
        a = a.reset_index(drop=True)

        b['Symbol'] = b['Symbol'].str.strip()
        b = b.sort_values(by=['Symbol'])
        b = b.reset_index(drop=True)

        self.assertEqual(True, a.equals(b))


    def test_getForecastsMarkets_symbol(self):
        a = te.getMarketsForecasts(symbol='aapl:us', output_type='df')

        url = f'https://api.tradingeconomics.com/markets/forecasts/symbol/aapl:us?c=guest:guest'
        data = requests.get(url).json()
        b = pd.DataFrame.from_dict(data, orient='columns')

        a['Symbol'] = a['Symbol'].str.strip()
        a = a.sort_values(by=['Symbol'])
        a = a.reset_index(drop=True)

        b['Symbol'] = b['Symbol'].str.strip()
        b = b.sort_values(by=['Symbol'])
        b = b.reset_index(drop=True)

        self.assertEqual(True, a.equals(b))

    
    def test_getForecastsMarkets_symbols(self):
        a = te.getMarketsForecasts(symbol=['AAPL:US','DAX:IND', 'INDU:IND'], output_type='df')

        url = f'https://api.tradingeconomics.com/markets/forecasts/symbol/AAPL:US,DAX:IND,INDU:IND?c=guest:guest'
        data = requests.get(url).json()
        b = pd.DataFrame.from_dict(data, orient='columns')

        a['Symbol'] = a['Symbol'].str.strip()
        a = a.sort_values(by=['Symbol', 'Country'])
        a = a.reset_index(drop=True)

        b['Symbol'] = b['Symbol'].str.strip()
        b = b.sort_values(by=['Symbol', 'Country'])
        b = b.reset_index(drop=True)

        self.assertEqual(True, a.equals(b))


class TestForecastsIndicators(unittest.TestCase):

    def tearDown(self):
        time.sleep(5)

    def test_getForecastsIndicators_country(self):
        a = te.getForecastData(country=['mexico', 'sweden'], output_type='df')

        url = 'https://api.tradingeconomics.com/forecast/country/mexico,sweden?c=guest:guest'
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')

        a['Country'] = a['Country'].str.strip()
        a = a.sort_values(by=['Country', 'Category'])
        a = a.reset_index(drop=True)

        b['Country'] = b['Country'].str.strip()
        b = b.sort_values(by=['Country', 'Category'])
        b = b.reset_index(drop=True)

        self.assertEqual(True, a.equals(b))

    def test_getForecastsIndicators_indicator(self):
        a = te.getForecastData(indicator='gdp', output_type='df')

        url = 'https://api.tradingeconomics.com/forecast/indicator/gdp?c=guest:guest'
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')

        a['Country'] = a['Country'].str.strip()
        a = a.sort_values(by=['Country', 'Category'])
        a = a.reset_index(drop=True)

        b['Country'] = b['Country'].str.strip()
        b = b.sort_values(by=['Country', 'Category'])
        b = b.reset_index(drop=True)

        self.assertEqual(True, a.equals(b))

    def test_getForecastsIndicators_indicators(self):
        a = te.getForecastData(indicator=['gdp', 'population'], output_type='df')

        url = 'https://api.tradingeconomics.com/forecast/indicator/gdp,population?c=guest:guest'
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')

        a['Country'] = a['Country'].str.strip()
        a = a.sort_values(by=['Country', 'Category'])
        a = a.reset_index(drop=True)

        b['Country'] = b['Country'].str.strip()
        b = b.sort_values(by=['Country', 'Category'])
        b = b.reset_index(drop=True)

        self.assertEqual(True, a.equals(b))


    def test_getForecastsIndicators_country_indicator(self):
        a = te.getForecastData(country='mexico', indicator='gdp', output_type='df')

        url = 'https://api.tradingeconomics.com/forecast/country/mexico/indicator/gdp?c=guest:guest'
        data = requests.get(url).json()
        
        b = pd.DataFrame.from_dict(data, orient='columns')

        a['Country'] = a['Country'].str.strip()
        a = a.sort_values(by=['Country', 'Category'])
        a = a.reset_index(drop=True)

        b['Country'] = b['Country'].str.strip()
        b = b.sort_values(by=['Country', 'Category'])
        b = b.reset_index(drop=True)

        self.assertEqual(True, a.equals(b))

    def test_getForecastsIndicators_countries_indicator(self):
        a = te.getForecastData(country=['mexico', 'sweden'], indicator='gdp', output_type='df')

        url = 'https://api.tradingeconomics.com/forecast/country/mexico,sweden/indicator/gdp?c=guest:guest'
        data = requests.get(url).json()
        
        b = pd.DataFrame.from_dict(data, orient='columns')

        a['Country'] = a['Country'].str.strip()
        a = a.sort_values(by=['Country', 'Category'])
        a = a.reset_index(drop=True)

        b['Country'] = b['Country'].str.strip()
        b = b.sort_values(by=['Country', 'Category'])
        b = b.reset_index(drop=True)

        self.assertEqual(True, a.equals(b))

    def test_getForecastsIndicators_countries_indicators(self):
        a = te.getForecastData(country=['mexico', 'sweden'], indicator=['gdp', 'population'], output_type='df')

        url = 'https://api.tradingeconomics.com/forecast/country/mexico,sweden/indicator/gdp,population?c=guest:guest'
        data = requests.get(url).json()
        
        b = pd.DataFrame.from_dict(data, orient='columns')

        a['Country'] = a['Country'].str.strip()
        a = a.sort_values(by=['Country', 'Category'])
        a = a.reset_index(drop=True)

        b['Country'] = b['Country'].str.strip()
        b = b.sort_values(by=['Country', 'Category'])
        b = b.reset_index(drop=True)

        self.assertEqual(True, a.equals(b))

if __name__ == '__main__':
    unittest.main()