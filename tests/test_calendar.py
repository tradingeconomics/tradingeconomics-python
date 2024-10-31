import unittest
import pandas as pd
import os
import sys
import requests
import time

sys.path.insert (0, '../tradingeconomics')
import tradingeconomics as te

te.login('guest:guest')

class TestgetCalendarId(unittest.TestCase):

    def tearDown(self):
        time.sleep(3)

    def test_getCalendarIdWithIds(self):
        a = te.getCalendarId(id = ['174108','160025','160030'], output_type = 'df')

        url = f'https://api.tradingeconomics.com/calendar/calendarid/174108,160025,160030?c=guest:guest'
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')
        
        a = a.sort_values(by=['CalendarId'])
        a = a.reset_index(drop=True)

        b = b.sort_values(by=['CalendarId'])
        b = b.reset_index(drop=True)
        self.assertEqual(True, a.equals(b))

    
    def test_getCalendarIdNoId(self):
        a = te.getCalendarId(id = None, output_type = 'df')

        url = f'https://api.tradingeconomics.com/calendar/?c=guest:guest'
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')
        
        a = a.sort_values(by=['CalendarId'])
        a = a.reset_index(drop=True)

        b = b.sort_values(by=['CalendarId'])
        b = b.reset_index(drop=True)
        self.assertEqual(True, a.equals(b))


    def test_getCalendarIdWithId(self):
        a = te.getCalendarId(id = '174108', output_type = 'df')

        url = f'https://api.tradingeconomics.com/calendar/calendarid/174108?c=guest:guest'
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')
        
        a = a.sort_values(by=['CalendarId'])
        a = a.reset_index(drop=True)

        b = b.sort_values(by=['CalendarId'])
        b = b.reset_index(drop=True)
        self.assertEqual(True, a.equals(b))


class TestgetCalendarData(unittest.TestCase):
    def tearDown(self):
        time.sleep(3)
    
    def test_getCalendarDataNoArguments(self):
        a = te.getCalendarData(output_type = 'df')

        url = f'https://api.tradingeconomics.com/calendar?c=guest:guest'
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')
        
        a = a.sort_values(by=['CalendarId'])
        a = a.reset_index(drop=True)

        b = b.sort_values(by=['CalendarId'])
        b = b.reset_index(drop=True)
        self.assertEqual(True, a.equals(b))


    def test_getCalendarDataImportance(self):
        a = te.getCalendarData(importance = '3', output_type = 'df')

        url = f'https://api.tradingeconomics.com/calendar?c=guest:guest&importance=3'
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')
        
        a = a.sort_values(by=['CalendarId'])
        a = a.reset_index(drop=True)

        b = b.sort_values(by=['CalendarId'])
        b = b.reset_index(drop=True)
        self.assertEqual(True, a.equals(b))
    

    def test_getCalendarDataCountryAllWithDates(self):
        a = te.getCalendarData(country = 'all', initDate = '2011-01-01', endDate = '2016-01-01', output_type = 'df')

        url = f'https://api.tradingeconomics.com/calendar/country/all/2011-01-01/2016-01-01?c=guest:guest'
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')
        
        a = a.sort_values(by=['CalendarId'])
        a = a.reset_index(drop=True)

        b = b.sort_values(by=['CalendarId'])
        b = b.reset_index(drop=True)
        self.assertEqual(True, a.equals(b))

    
    def test_getCalendarDataWithDatesAndImportance(self):
        a = te.getCalendarData(initDate='2016-01-01', endDate='2016-01-01',importance='3', output_type='df')

        url = f'https://api.tradingeconomics.com/calendar/country/all/2016-01-01/2016-01-01?c=guest:guest&importance=3'
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')

        a = a.sort_values(by=['CalendarId'])
        a = a.reset_index(drop=True)

        b = b.sort_values(by=['CalendarId'])
        b = b.reset_index(drop=True)
        self.assertEqual(True, a.equals(b))

    def test_getCalendarDataCountry(self):
        a = te.getCalendarData(country = 'united states', output_type = 'df')

        url = f'https://api.tradingeconomics.com/calendar/country/united%20states?c=guest:guest'
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')

        a = a.sort_values(by=['CalendarId'])
        a = a.reset_index(drop=True)

        b = b.sort_values(by=['CalendarId'])
        b = b.reset_index(drop=True)
        self.assertEqual(True, a.equals(b))

    def test_getCalendarDataCountryWithDates(self):
        a = te.getCalendarData(country = 'united states', initDate = '2011-01-01', endDate = '2016-01-01', output_type = 'df')

        url = f'https://api.tradingeconomics.com/calendar/country/united%20states/2011-01-01/2016-01-01?c=guest:guest'
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')

        a = a.sort_values(by=['CalendarId'])
        a = a.reset_index(drop=True)

        b = b.sort_values(by=['CalendarId'])
        b = b.reset_index(drop=True)
        self.assertEqual(True, a.equals(b))

    
    def test_getCalendarDataCountryWithDatesAndImportance(self):
        a = te.getCalendarData(country = 'united states', initDate = '2011-01-01', endDate = '2016-01-01', importance = '3', output_type = 'df')

        url = f'https://api.tradingeconomics.com/calendar/country/united%20states/2011-01-01/2016-01-01?c=guest:guest&importance=3'
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')

        a = a.sort_values(by=['CalendarId'])
        a = a.reset_index(drop=True)

        b = b.sort_values(by=['CalendarId'])
        b = b.reset_index(drop=True)
        self.assertEqual(True, a.equals(b))

    
    def test_getCalendarDataCategory(self):
        a = te.getCalendarData(category = 'inflation rate', output_type = 'df')

        url = f'https://api.tradingeconomics.com/calendar/indicator/inflation rate?c=guest:guest'
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')

        a = a.sort_values(by=['CalendarId'])
        a = a.reset_index(drop=True)
        
        b = b.sort_values(by=['CalendarId'])
        b = b.reset_index(drop=True)
        self.assertEqual(True, a.equals(b))

    
    def test_getCalendarDataCategoryWithImportance(self):
        a = te.getCalendarData(category = 'inflation rate', importance = '3', output_type = 'df')

        url = f'https://api.tradingeconomics.com/calendar/indicator/inflation rate?c=guest:guest&importance=3'
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')

        a = a.sort_values(by=['CalendarId'])
        a = a.reset_index(drop=True)
        
        b = b.sort_values(by=['CalendarId'])
        b = b.reset_index(drop=True)
        self.assertEqual(True, a.equals(b))

    
    def test_getCalendarDataCategoryWithDates(self):
        a = te.getCalendarData(category = 'inflation rate', initDate='2016-03-01', endDate='2016-03-03', output_type = 'df')

        url = f'https://api.tradingeconomics.com/calendar/indicator/inflation rate/2016-03-01/2016-03-03?c=guest:guest'
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')

        a = a.sort_values(by=['CalendarId'])
        a = a.reset_index(drop=True)
        
        b = b.sort_values(by=['CalendarId'])
        b = b.reset_index(drop=True)
        self.assertEqual(True, a.equals(b))

    # TODO: also test with YYYY-MM-DDThh:mm:ss format
    def test_getCalendarDataCategoryWithDatesAndImportance(self):
        a = te.getCalendarData(category = 'inflation rate', initDate='2016-03-01', endDate='2016-03-03', importance = '3', output_type = 'df')

        url = f'https://api.tradingeconomics.com/calendar/indicator/inflation rate/2016-03-01/2016-03-03?c=guest:guest&importance=3'
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')

        a = a.sort_values(by=['CalendarId'])
        a = a.reset_index(drop=True)
        
        b = b.sort_values(by=['CalendarId'])
        b = b.reset_index(drop=True)
        self.assertEqual(True, a.equals(b))
        
    
    def test_getCalendarDataCountries(self):
        a = te.getCalendarData(country = ['united states', 'china'], output_type = 'df')

        url = f'https://api.tradingeconomics.com/calendar/country/united%20states,china?c=guest:guest'
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')

        a = a.sort_values(by=['CalendarId'])
        a = a.reset_index(drop=True)
        
        b = b.sort_values(by=['CalendarId'])
        b = b.reset_index(drop=True)
        self.assertEqual(True, a.equals(b))

    
    def test_getCalendarDataCountriesWithDates(self):
        a = te.getCalendarData(country = ['united states', 'china'], importance=2, output_type = 'df')

        url = f'https://api.tradingeconomics.com/calendar/country/united%20states,china?c=guest:guest&importance=2'
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')

        a = a.sort_values(by=['CalendarId'])
        a = a.reset_index(drop=True)
        
        b = b.sort_values(by=['CalendarId'])
        b = b.reset_index(drop=True)
        self.assertEqual(True, a.equals(b))

    
    def test_getCalendarDataCountriesWithDates(self):
        a = te.getCalendarData(country = ['united states', 'china'], initDate='2016-03-01', endDate='2016-03-03', output_type = 'df')

        url = f'https://api.tradingeconomics.com/calendar/country/united%20states,china/2016-03-01/2016-03-03?c=guest:guest'
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')

        a = a.sort_values(by=['CalendarId'])
        a = a.reset_index(drop=True)
        
        b = b.sort_values(by=['CalendarId'])
        b = b.reset_index(drop=True)
        self.assertEqual(True, a.equals(b))

    
    def test_getCalendarDataCountriesWithDatesAndImportance(self):
        a = te.getCalendarData(country = ['united states', 'china'], initDate='2016-03-01', endDate='2016-03-03', importance = '3', output_type = 'df')

        url = f'https://api.tradingeconomics.com/calendar/country/united%20states,china/2016-03-01/2016-03-03?c=guest:guest&importance=3'
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')

        a = a.sort_values(by=['CalendarId'])
        a = a.reset_index(drop=True)
        
        b = b.sort_values(by=['CalendarId'])
        b = b.reset_index(drop=True)
        self.assertEqual(True, a.equals(b))

    
    def test_getCalendarDataCountryAndCategory(self):
        a = te.getCalendarData(country = 'united states', category = 'initial jobless claims', output_type = 'df')

        url = f'https://api.tradingeconomics.com/calendar/country/united%20states/indicator/initial jobless claims?c=guest:guest'
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')

        a = a.sort_values(by=['CalendarId'])
        a = a.reset_index(drop=True)
        
        b = b.sort_values(by=['CalendarId'])
        b = b.reset_index(drop=True)
        self.assertEqual(True, a.equals(b))


    def test_getCalendarDataCountryAndCategoryWithDates(self):
        a = te.getCalendarData(country = 'united states', category = 'initial jobless claims', initDate = '2011-01-01', endDate = '2016-01-01', output_type = 'df')

        url = f'https://api.tradingeconomics.com/calendar/country/united%20states/indicator/initial jobless claims/2011-01-01/2016-01-01?c=guest:guest'
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')
        
        a = a.sort_values(by=['CalendarId'])
        a = a.reset_index(drop=True)
        
        b = b.sort_values(by=['CalendarId'])
        b = b.reset_index(drop=True)

        self.assertEqual(True, a.equals(b))

    def test_getCalendarDataTicker(self):
        a = te.getCalendarData(ticker = ['IJCUSA','SPAINFACORD','BAHRAININFNRATE'], output_type = 'df')

        url = f'https://api.tradingeconomics.com/calendar/ticker/IJCUSA,SPAINFACORD,BAHRAININFNRATE?c=guest:guest'
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')
        
        a = a.sort_values(by=['CalendarId'])
        a = a.reset_index(drop=True)
        
        b = b.sort_values(by=['CalendarId'])
        b = b.reset_index(drop=True)

        self.assertEqual(True, a.equals(b))

    def test_getCalendarDataTickerWithDates(self):
        a = te.getCalendarData(ticker = ['IJCUSA','SPAINFACORD','BAHRAININFNRATE'], initDate = '2021-01-01', endDate = '2021-01-03', output_type = 'df')

        url = f'https://api.tradingeconomics.com/calendar/ticker/IJCUSA,SPAINFACORD,BAHRAININFNRATE/2021-01-01/2021-01-03?c=guest:guest'
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')
        
        a = a.sort_values(by=['CalendarId'])
        a = a.reset_index(drop=True)
        
        b = b.sort_values(by=['CalendarId'])
        b = b.reset_index(drop=True)

        self.assertEqual(True, a.equals(b))

    def test_getCalendarDataWithEvent(self):
        a = te.getCalendarData(country='United States', event='GDP Growth Rate QoQ Final', initDate='2016-12-01', endDate='2024-02-25', output_type = 'df')

        url = f'https://api.tradingeconomics.com/calendar/country/united%20states/event/GDP Growth Rate QoQ Final/2016-12-01/2024-02-25?c=guest:guest'
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')
        
        a = a.sort_values(by=['CalendarId'])
        a = a.reset_index(drop=True)
        
        b = b.sort_values(by=['CalendarId'])
        b = b.reset_index(drop=True)

        self.assertEqual(True, a.equals(b))

    
    def test_getCalendarDataWithCountryEventAndDates(self):
        a = te.getCalendarData(country='United States', event='GDP Growth Rate QoQ Final', initDate='2016-12-01', endDate='2024-02-25', output_type = 'df')

        url = f'https://api.tradingeconomics.com/calendar/country/united%20states/event/GDP Growth Rate QoQ Final/2016-12-01/2024-02-25?c=guest:guest'
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')
        
        a = a.sort_values(by=['CalendarId'])
        a = a.reset_index(drop=True)
        
        b = b.sort_values(by=['CalendarId'])
        b = b.reset_index(drop=True)

        self.assertEqual(True, a.equals(b))

    
    def test_getCalendarDataWithCountriesEventAndDates(self):
        a = te.getCalendarData(country=['United States'], event='GDP Growth Rate QoQ Final', initDate='2016-12-01', endDate='2024-02-25', output_type = 'df')

        url = f'https://api.tradingeconomics.com/calendar/country/united%20states/event/GDP Growth Rate QoQ Final/2016-12-01/2024-02-25?c=guest:guest'
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')
        
        a = a.sort_values(by=['CalendarId'])
        a = a.reset_index(drop=True)
        
        b = b.sort_values(by=['CalendarId'])
        b = b.reset_index(drop=True)

        self.assertEqual(True, a.equals(b))

    def test_getCalendarDataWithEventAndDates(self):
        a = te.getCalendarData(country=['United States'], event=['GDP Growth Rate QoQ Final', ], initDate='2016-12-01', endDate='2024-02-25', output_type = 'df')

        url = f'https://api.tradingeconomics.com/calendar/country/united%20states/event/GDP Growth Rate QoQ Final/2016-12-01/2024-02-25?c=guest:guest'
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')
        
        a = a.sort_values(by=['CalendarId'])
        a = a.reset_index(drop=True)
        
        b = b.sort_values(by=['CalendarId'])
        b = b.reset_index(drop=True)

        self.assertEqual(True, a.equals(b))
    

class TestgetCalendarEvents(unittest.TestCase):
    def tearDown(self):
        time.sleep(3)

    def test_getCalendarEventsNoArguments(self):
        a = te.getCalendarEvents(output_type = 'df')

        url = f'https://api.tradingeconomics.com/calendar/events?c=guest:guest'
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')

        a = a.sort_values(by=['Event'])
        a = a.reset_index(drop=True)

        b = b.sort_values(by=['Event'])
        b = b.reset_index(drop=True)

        self.assertEqual(True, a.equals(b))

    
    def test_getCalendarEventsCountry(self):
        a = te.getCalendarEvents(country = 'united states', output_type = 'df')

        url = f'https://api.tradingeconomics.com/calendar/events/country/united%20states?c=guest:guest'
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')

        a = a.sort_values(by=['Event'])
        a = a.reset_index(drop=True)

        b = b.sort_values(by=['Event'])
        b = b.reset_index(drop=True)

        self.assertEqual(True, a.equals(b))

    
    def test_getCalendarEventsMultipleCountries(self):
        a = te.getCalendarEvents(country = ['united states', 'china'], output_type = 'df')

        url = f'https://api.tradingeconomics.com/calendar/events/country/united%20states,china?c=guest:guest'
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')

        a = a.sort_values(by=['Event'])
        a = a.reset_index(drop=True)

        b = b.sort_values(by=['Event'])
        b = b.reset_index(drop=True)

        self.assertEqual(True, a.equals(b))



class TestgetCalendarEventsByGroup(unittest.TestCase):
    def tearDown(self):
        time.sleep(3)

    def test_getCalendarEventsByGroupNoArguments(self):
        a = te.getCalendarEventsByGroup(group='bonds', output_type = 'df')

        url = f'https://api.tradingeconomics.com/calendar/group/bonds?c=guest:guest'
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')

        a = a.sort_values(by=['CalendarId'])
        a = a.reset_index(drop=True)

        b = b.sort_values(by=['CalendarId'])
        b = b.reset_index(drop=True)

        self.assertEqual(True, a.equals(b))

    def test_getCalendarEventsByGroupWithDates(self):
        a = te.getCalendarEventsByGroup(group='bonds', initDate='2023-01-01', endDate='2023-02-01', output_type = 'df')

        url = f'https://api.tradingeconomics.com/calendar/group/bonds/2023-01-01/2023-02-01?c=guest:guest'
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')

        a = a.sort_values(by=['CalendarId'])
        a = a.reset_index(drop=True)

        b = b.sort_values(by=['CalendarId'])
        b = b.reset_index(drop=True)

        self.assertEqual(True, a.equals(b))

    
    def test_getCalendarEventsByGroupWithDate(self):
        a = te.getCalendarEventsByGroup(group='bonds', endDate='2023-02-01', output_type = 'df')

        url = f'https://api.tradingeconomics.com/calendar/group/bonds/2023-02-01?c=guest:guest'
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')

        a = a.sort_values(by=['CalendarId'])
        a = a.reset_index(drop=True)

        b = b.sort_values(by=['CalendarId'])
        b = b.reset_index(drop=True)

        self.assertEqual(True, a.equals(b))

    def test_getCalendarEventByGroupWithCountry(self):
        a = te.getCalendarEventsByGroup(group='bonds', country='united states', output_type = 'df')

        url = f'https://api.tradingeconomics.com/calendar/country/united states/group/bonds?c=guest:guest'
        data = requests.get(url).json()

        b = pd.DataFrame.from_dict(data, orient='columns')

        a = a.sort_values(by=['CalendarId'])
        a = a.reset_index(drop=True)

        b = b.sort_values(by=['CalendarId'])
        b = b.reset_index(drop=True)

        self.assertEqual(True, a.equals(b))
    
