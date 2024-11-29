import unittest
import pandas as pd
import sys
import requests
import time

sys.path.insert (0, '../tradingeconomics')
import tradingeconomics as te

te.login('guest:guest')

class TestHelpers(unittest.TestCase):

    def tearDown(self):
        time.sleep(3)

    def test_checkCountry_single(self):

        import tradingeconomics.indicators as indicators
        linkAPI = 'https://api.tradingeconomics.com/country/'
        string_1 = indicators.checkCountry('united states', linkAPI)

        string_2 = 'https://api.tradingeconomics.com/country/united%20states'

        self.assertEqual(string_1, string_2)

    def test_checkCountry_multiple(self):

        import tradingeconomics.indicators as indicators
        linkAPI = 'https://api.tradingeconomics.com/country/'
        string_1 = indicators.checkCountry(['united states', 'china'], linkAPI)

        string_2 = 'https://api.tradingeconomics.com/country/united%20states%2Cchina'

        self.assertEqual(string_1, string_2)

    def test_checkIndicator_single(self):
        import tradingeconomics.indicators as indicators
        linkAPI = 'https://api.tradingeconomics.com/country/all'

        string_1 = indicators.checkIndic('gdp', linkAPI)

        string_2 = 'https://api.tradingeconomics.com/country/all/gdp'

        self.assertEqual(string_1, string_2)

    def test_checkIndicator_multiple(self):
        import tradingeconomics.indicators as indicators
        linkAPI = 'https://api.tradingeconomics.com/country/all'

        string_1 = indicators.checkIndic(['gdp', 'exports'], linkAPI)

        string_2 = 'https://api.tradingeconomics.com/country/all/gdp%2Cexports'

        self.assertEqual(string_1, string_2)

    def test_checkCountryRatings_single(self):
        import tradingeconomics.indicators as indicators
        linkAPI = 'https://api.tradingeconomics.com/ratings/'
        string_1 = indicators.checkCountryRatings('united states')

        string_2 = 'https://api.tradingeconomics.com/ratings/united%20states'

        self.assertEqual(string_1, string_2)


    def test_checkCountryRatings_multiple(self):
        import tradingeconomics.indicators as indicators
        linkAPI = 'https://api.tradingeconomics.com/ratings/'
        string_1 = indicators.checkCountryRatings(['united states', 'china'])

        string_2 = 'https://api.tradingeconomics.com/ratings/united%20states%2Cchina'

        self.assertEqual(string_1, string_2)


class TestgetIndicatorsData(unittest.TestCase):

    def tearDown(self):
        time.sleep(3)

    def test_getIndicatorData_indicator(self):
        a = te.getIndicatorData(indicators='gdp', output_type='df')
        
        url = 'https://api.tradingeconomics.com/country/all/gdp?c=guest:guest'
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')

        a = a.sort_values(by='Country')
        a = a.reset_index(drop=True)

        b = b.sort_values(by='Country')
        b = b.reset_index(drop=True)
        self.assertTrue(a.equals(b))

    
    def test_getIndicatorData_country(self):
        a = te.getIndicatorData(country='sweden', output_type='df')
        
        url = 'https://api.tradingeconomics.com/country/sweden?c=guest:guest'
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')

        a = a.sort_values(by=['LatestValueDate', 'Source', 'Category'])
        a = a.reset_index(drop=True)

        b = b.sort_values(by=['LatestValueDate', 'Source', 'Category'])
        b = b.reset_index(drop=True)

        for col in b.columns:
            if b[col].dtype == 'object':
                b[col] = b[col].str.strip()

        self.assertTrue(a.equals(b))

    def test_getIndicatorData_countries(self):
        a = te.getIndicatorData(country=['mexico', 'sweden'], output_type='df')

        url = 'https://api.tradingeconomics.com/country/mexico%2Csweden?c=guest:guest'
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')

        a = a.sort_values(by=['Country', 'LatestValueDate', 'Source', 'Category'])
        a = a.reset_index(drop=True)

        b = b.sort_values(by=['Country', 'LatestValueDate', 'Source', 'Category'])
        b = b.reset_index(drop=True)

        for col in b.columns:
            if b[col].dtype == 'object':
                b[col] = b[col].str.strip()

        self.assertTrue(a.equals(b))

    
    def test_getIndicatorData_countries_indicator(self):
        a = te.getIndicatorData(country=['portugal', 'sweden'], indicators='gdp', output_type='df')

        # url = 'https://api.tradingeconomics.com/indicators/portugal%2Csweden/gdp?c=guest:guest'
        # data = requests.get(url).json()

        # b = pd.DataFrame.from_dict(data, orient='columns')

        # a = a.sort_values(by=['Country', 'Ticker', 'LatestValueDate', 'Source', 'Category'])
        # a = a.reset_index(drop=True)

        # b = b.sort_values(by=['Country', 'Ticker',  'LatestValueDate', 'Source', 'Category'])
        # b = b.reset_index(drop=True)

        # for col in b.columns:
        #     b[col] = b[col].str.strip()

        # self.assertTrue(a.equals(b))
        b = 'Error: You can not use both country and indicators parameters at the same time.'
        self.assertEqual(a, b)


    def test_getIndicatorData_country_indicator(self):
        a = te.getIndicatorData(country='sweden', indicators='gdp', output_type='df')

        # url = 'https://api.tradingeconomics.com/indicators/sweden/gdp?c=guest:guest'
        # data = requests.get(url).json()

        # b = pd.DataFrame.from_dict(data, orient='columns')

        # a = a.sort_values(by=['Country', 'Ticker', 'LatestValueDate', 'Source', 'Category'])
        # a = a.reset_index(drop=True)

        # b = b.sort_values(by=['Country', 'Ticker',  'LatestValueDate', 'Source', 'Category'])
        # b = b.reset_index(drop=True)

        # for col in b.columns:
        #     b[col] = b[col].str.strip()
        b = 'Error: You can not use both country and indicators parameters at the same time.'
        self.assertEqual(a, b)
        # self.assertTrue(a.equals(b))


    # def test_getIndicatorData_calendar(self):
    #     a = te.getIndicatorData(calendar=1, output_type='df')

    #     url = 'https://api.tradingeconomics.com/indicators?calendar=1&c=guest:guest'
    #     data = requests.get(url).json()

    #     b = pd.DataFrame.from_dict(data, orient='columns')

    #     a = a.sort_values(by=['Category', 'CategoryGroup'])
    #     a = a.reset_index(drop=True)

    #     b = b.sort_values(by=['Category', 'CategoryGroup'])
    #     b = b.reset_index(drop=True)

    #     for col in b.columns:
    #         if b[col].dtype == 'object':
    #             b[col] = b[col].str.strip()

    #     self.assertTrue(a.equals(b))


class TestgetRatings(unittest.TestCase):

    def tearDown(self):
        time.sleep(5)

    # def test_getCreditRatings_country(self):
    #     a = te.getRatings(output_type='df')

    #     url = f'https://api.tradingeconomics.com/ratings?c=guest:guest'
    #     data = requests.get(url).json()

    #     b = pd.DataFrame.from_dict(data, orient='columns')

    #     a = a.sort_values(by=['Country'])
    #     a = a.reset_index(drop=True)

    #     b = b.sort_values(by=['Country'])
    #     b = b.reset_index(drop=True)

    #     self.assertTrue(a.equals(b))


class TestgetDiscontinuedIndicator(unittest.TestCase):
    def tearDown(self):
        time.sleep(3)

    def test_getDiscontinuedIndicator(self):
        a = te.getDiscontinuedIndicator(output_type='df')

        url = 'https://api.tradingeconomics.com/country/all/discontinued?c=guest:guest'
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')

        a = a.sort_values(by=['Country', 'Category'])
        a = a.reset_index(drop=True)

        b = b.sort_values(by=['Country', 'Category'])
        b = b.reset_index(drop=True)

        self.assertTrue(a.equals(b))

    def test_DiscontinuedIndicator_country(self):
        a = te.getDiscontinuedIndicator(country=['united states', 'china'], output_type='df')

        url = 'https://api.tradingeconomics.com/country/united%20states%2Cchina/discontinued?c=guest:guest'
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')

        a = a.sort_values(by=['Country', 'Category', 'CreateDate'])
        a = a.reset_index(drop=True)

        b = b.sort_values(by=['Country', 'Category', 'CreateDate'])
        b = b.reset_index(drop=True)

        self.assertTrue(a.equals(b))

    
class TestgetIndicatorByCategoryGroup(unittest.TestCase):
    def tearDown(self):
        time.sleep(3)

    def test_getIndicatorByCategoryGroup_country_category(self):
        a = te.getIndicatorByCategoryGroup(country='sweden', category_group = 'gdp', output_type='df')

        url = 'https://api.tradingeconomics.com/country/sweden?c=guest:guest&group=gdp'
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')

        a = a.sort_values(by=['Country', 'HistoricalDataSymbol'])
        a = a.reset_index(drop=True)

        b = b.sort_values(by=['Country', 'HistoricalDataSymbol'])
        b = b.reset_index(drop=True)

        self.assertTrue(a.equals(b))

    
    def test_getIndicatorByCategoryGroup_country(self):
        a = te.getIndicatorByCategoryGroup(country = 'sweden', output_type = 'df')
        b = "Country and category are required"
        self.assertEqual(a,b)


class TestgetIndicatorByTicker(unittest.TestCase):
    def tearDown(self):
        time.sleep(3)

    def test_getIndicatorByTicker(self):
        a = te.getIndicatorByTicker(ticker = 'USURTOT', output_type = 'df')

        url = "https://api.tradingeconomics.com/country/ticker/USURTOT?c=guest:guest"
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')

        a = a.sort_values(by=['Country'])
        a = a.reset_index(drop=True)

        b = b.sort_values(by=['Country'])
        b = b.reset_index(drop=True)

        self.assertTrue(a.equals(b))
  

class TestgetLatestUpdates(unittest.TestCase):

    def tearDown(self):
        time.sleep(3)

    def test_getLatestUpdates_country(self):
        a = te.getLatestUpdates(country = 'united states', output_type = 'df')

        url = "https://api.tradingeconomics.com/updates/country/united%20states?c=guest:guest"
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')

        a = a.sort_values(by=['Country', 'HistoricalDataSymbol'])
        a = a.reset_index(drop=True)

        b = b.sort_values(by=['Country', 'HistoricalDataSymbol'])
        b = b.reset_index(drop=True)

        self.assertTrue(a.equals(b))

    def test_getLatestUpdates_init_date(self):
        a = te.getLatestUpdates(country = 'united states',init_date = '2021-06-01', output_type = 'df')

        url = "https://api.tradingeconomics.com/updates/country/united%20states/2021-06-01?c=guest:guest"
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')

        a = a.sort_values(by=['Country', 'HistoricalDataSymbol'])
        a = a.reset_index(drop=True)

        b = b.sort_values(by=['Country', 'HistoricalDataSymbol'])
        b = b.reset_index(drop=True)

        self.assertTrue(a.equals(b))

    def test_getLatestUpdates_countries(self):
        a = te.getLatestUpdates(country =['united states', 'portugal'],init_date = '2021-06-01', output_type = 'df')

        url = "https://api.tradingeconomics.com/updates/country/united%20states%2Cportugal/2021-06-01?c=guest:guest"
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')

        a = a.sort_values(by=['Country', 'HistoricalDataSymbol'])
        a = a.reset_index(drop=True)

        b = b.sort_values(by=['Country', 'HistoricalDataSymbol'])
        b = b.reset_index(drop=True)

        self.assertTrue(a.equals(b))

    # def test_getLatestUpdates_init_date_time(self):
    #     a = te.getLatestUpdates(init_date = '2021-10-18', time='15:20', output_type = 'df')

    #     url = "https://api.tradingeconomics.com/updates/2021-10-18?c=guest:guest&time=15:20"
    #     data = requests.get(url).json()

    #     b = pd.DataFrame.from_dict(data, orient='columns')

    #     a = a.sort_values(by=['Country', 'HistoricalDataSymbol'])
    #     a = a.reset_index(drop=True)

    #     b = b.sort_values(by=['Country', 'HistoricalDataSymbol'])
    #     b = b.reset_index(drop=True)

    #     self.assertTrue(a.equals(b))

class TestgetPeers(unittest.TestCase):

    def tearDown(self):
        time.sleep(3)

    # def test_getPeers_ticker(self):
    #     a = te.getPeers(ticker ='CPI YOY', output_type = 'df')

    #     url = "https://api.tradingeconomics.com/peers/CPI%20YOY?c=guest:guest"
    #     data = requests.get(url).json()

    #     b = pd.DataFrame.from_dict(data, orient='columns')

    #     a = a.sort_values(by=['Ticker', 'Peer'])
    #     a = a.reset_index(drop=True)

    #     b = b.sort_values(by=['Ticker', 'Peer'])
    #     b = b.reset_index(drop=True)

    #     self.assertTrue(a.equals(b))


class TestgetAllCountries(unittest.TestCase):
    def tearDown(self):
        time.sleep(3)

    def test_getAllCountries(self):
        a = te.getAllCountries(output_type='df')

        url = "https://api.tradingeconomics.com/country/?c=guest:guest"
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')

        a = a.sort_values(by=['Country', 'Continent', 'ISO3'])
        a = a.reset_index(drop=True)

        b = b.sort_values(by=['Country', 'Continent', 'ISO3'])
        b = b.reset_index(drop=True)

        self.assertTrue(a.equals(b))


class TestgetIndicatorChanges(unittest.TestCase):

    def tearDown(self):
        time.sleep(3)

    def test_getIndicatorChanges(self):
        a = te.getIndicatorChanges(output_type='df')

        url = "https://api.tradingeconomics.com/changes?c=guest:guest"
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')

        a = a.sort_values(by=['Country', 'Category', 'Ticker'])
        a = a.reset_index(drop=True)

        b = b.sort_values(by=['Country', 'Category', 'Ticker'])
        b = b.reset_index(drop=True)

        self.assertTrue(a.equals(b))

    def test_getIndicatorChanges_start_date(self):
        a = te.getIndicatorChanges(start_date='2024-10-29', output_type='df')

        url = "https://api.tradingeconomics.com/changes/2024-10-29?c=guest:guest"
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')

        a = a.sort_values(by=['Country', 'Category', 'Ticker'])
        a = a.reset_index(drop=True)

        b = b.sort_values(by=['Country', 'Category', 'Ticker'])
        b = b.reset_index(drop=True)

        self.assertTrue(a.equals(b))