import sys
from datetime import *
from . import functions as fn
from . import glob
import ssl
from typing import List


PY3 = sys.version_info[0] == 3

if PY3:  # Python 3+
    from urllib.parse import quote
else:  # Python 2.X
    from urllib import quote


class ParametersError(ValueError):
    pass


class DateError(ValueError):
    pass


class CredentialsError(ValueError):
    pass


class LoginError(AttributeError):
    pass


class WebRequestError(ValueError):
    pass


def paramCheck(country, indicator=None):
    # country is string, no indicator
    if isinstance(country, str) and indicator is None:
        encoded_country = quote(country)
        return "/calendar/country/" + encoded_country

    # country is list, no indicator
    elif isinstance(country, list) and indicator is None:
        encoded = [quote(c) for c in country]
        multiCountry = ",".join(encoded)
        return "/calendar/country/" + multiCountry

    # country list + indicator string
    elif isinstance(country, list) and isinstance(indicator, str):
        encoded_country = [quote(c) for c in country]
        encoded_indicator = quote(indicator)
        multiCountry = ",".join(encoded_country)
        return "/calendar/country/" + multiCountry + "/indicator/" + encoded_indicator

    # country string + indicator list
    elif isinstance(country, str) and isinstance(indicator, list):
        encoded_indicator = [quote(i) for i in indicator]
        multiInd = ",".join(encoded_indicator)
        return "/calendar/country/" + quote(country) + "/indicator/" + multiInd

    # country string + indicator string  <<<<<< CORREÇÃO IMPORTANTE
    elif isinstance(country, str) and isinstance(indicator, str):
        encoded_country = quote(country)
        encoded_indicator = quote(indicator)
        return (
            "/calendar/country/" + encoded_country + "/indicator/" + encoded_indicator
        )

    # both lists
    else:
        encoded_country = [quote(c) for c in country]
        encoded_ind = [quote(i) for i in indicator]
        multiCountry = ",".join(encoded_country)
        multiInd = ",".join(encoded_ind)
        return "/calendar/country/" + multiCountry + "/indicator/" + multiInd


def checkCalendarId(id):
    linkAPI = "/calendar/calendarid"
    if isinstance(id, str):
        linkAPI += "/" + quote(id)
    else:
        encoded = [quote(str(x)) for x in id]
        multi = ",".join(encoded)
        linkAPI += "/" + multi
    return linkAPI


def getCalendarId(id=None, output_type=None):
    """
    Return calendar events by it's specific Id.
    ===========================================================

    Parameters:
    -----------
    Id: Specific Id or Ids.
    output_type: string.
             'dict'(default) for dictionary format output, 'df' for data frame,
             'raw' for list of dictionaries without any parsing.

    Notes
    -----
    All parameters are optional. When not supplying parameters, data for all calendar events will be provided.

    Example
    -------
    getCalendarId(id = None, output_type = None)

    getCalendarId(id = '174108', output_type = None)

    getCalendarId(id = ['174108','160025','160030'], output_type = 'df')

    """

    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context

    if id == None:
        linkAPI = "/calendar"
    else:
        linkAPI = checkCalendarId(id)

    return fn.dataRequest(api_request=linkAPI, output_type=output_type)


def getCalendarData(
    country=None,
    category=None,
    initDate=None,
    endDate=None,
    importance=None,
    ticker=None,
    event=None,
    output_type=None,
    values=None,
):
    """
    Returns Lastest Updates by country, by country and initial date, by initial date only.
    =================================================================================
    Parameters:
    -----------
        country: string or list.
                country = 'united states'
                country = ['united states', 'portugal']
        category: string
                category='inflation rate'
        ticker: string or list.
                ticker = 'IJCUSA'
                ticker=['IJCUSA','SPAINFACORD','BAHRAININFNRATE']
        importance: string.
                importance = '2'
        event: string or list.
                event = 'GDP Growth Rate QoQ Final GDP'
                event =['GDP Growth Rate QoQ Final GDP','Industrial Production MoM']
        values: boolean.
                values = True
                values = False

        initDate: string.
                initDate = '2021-01-01'
        endDate:string.
                endDate = '2021-01-03'

        output_type: string.
             'dict'(default) for dictionary format output, 'df' for data frame,
             'raw' for list of dictionaries directly from the web.
    Notes
    -----
    all parameters are optional.

    Example
    -------
            getCalendarData(output_type='df')
            getCalendarData(importance='2', output_type='df')
            getCalendarData(country='all', initDate = '2011-01-01', endDate = '2016-01-01', output_type='df')
            getCalendarData(initDate='2016-01-01', endDate='2016-01-01',importance='3', output_type='df')
            getCalendarData(country='united states',  output_type='df')
            getCalendarData(country = 'United States', initDate = '2011-01-01', endDate = '2016-01-01', output_type='df')
            getCalendarData(country='united states',initDate='2016-01-01', endDate='2016-01-01',importance='3', output_type='df')
            getCalendarData(category='inflation rate', output_type='df')
            getCalendarData(category='inflation rate',importance='2', output_type='df')
            getCalendarData(category='inflation rate',initDate='2016-03-01', endDate='2016-03-03', output_type='df')
            getCalendarData(category='inflation rate',initDate='2016-03-01', endDate='2016-03-03',importance='2', output_type='df')
            getCalendarData(country = ['United States','china'], output_type='df')
            getCalendarData(country=['united states','china'], importance='2', output_type='df')
            getCalendarData(country=['united states', 'china'], initDate = '2016-01-01', endDate = '2016-01-03', output_type='df')
            getCalendarData(country=['united states', 'china'], initDate = '2016-01-01', endDate = '2016-01-03',importance=2, output_type='df')
            getCalendarData(country = 'United States', category = 'initial jobless claims', output_type='df')
            getCalendarData(country = 'United States', category = 'initial jobless claims',initDate = '2011-01-01', endDate = '2016-01-01', output_type='df')
            getCalendarData(ticker=['IJCUSA','SPAINFACORD','BAHRAININFNRATE'], output_type='df')
            getCalendarData(ticker=['IJCUSA','SPAINFACORD','BAHRAININFNRATE'], initDate = '2021-01-01', endDate = '2021-01-03', output_type='df')
            getCalendarData(country= 'United States', event = 'GDP Growth Rate QoQ Final GDP', output_type='df')
            getCalendarData(country= 'United States', event = 'GDP Growth Rate QoQ Final GDP', initDate = '2021-01-01', endDate = '2021-01-03', output_type='df')
    """

    # d is a dictionary used for create the api url
    d = {
        "url_base": "/calendar",
        "country": "",
        "category": "",
        "init_date": "",
        "end_date": "",
        "importance": "",
        "ticker": "",
        "event": "",
        "output_type": "",
        "values": "",
    }
    if initDate and endDate:

        initDateFormat = fn.validate(initDate)
        endDateFormat = fn.validate(endDate)
        fn.validatePeriod(initDate, initDateFormat, endDate, endDateFormat)
        d["init_date"] = f"/{quote(initDate)}"
        d["end_date"] = f"/{quote(endDate)}"

    if ticker:
        d["ticker"] = f"/ticker/{fn.stringOrList(ticker)}"
        api_url_request = "%s%s%s%s" % (
            d["url_base"],
            d["ticker"],
            d["init_date"],
            d["end_date"],
        )

        return fn.dataRequest(api_request=api_url_request, output_type=output_type)

    if country:
        d["country"] = f"/country/{fn.stringOrList(country)}"

    if category:
        d["category"] = f"/indicator/{fn.stringOrList(category)}"

    if event and country:
        d["event"] = f"/event/{fn.stringOrList(event)}"
    elif event and not country:
        return "The parameter 'country' must be provided!"

    if importance:
        d["importance"] = f"&importance={importance}"

    if initDate and endDate and not country and not category:
        d["country"] = f"/country/all"

    if values:
        d["values"] = f"&values=true"
    elif values == False:
        d["values"] = f"&values=false"

    api_url_request = "%s%s%s%s%s%s%s%s" % (
        d["url_base"],
        d["country"],
        d["category"],
        d["event"],
        d["init_date"],
        d["end_date"],
        d["importance"],
        d["values"],
    )
    return fn.dataRequest(api_request=api_url_request, output_type=output_type)


def getCalendarUpdates(output_type=None):
    """
    Returns Lastest Calendar Updates
    =================================================================================
    Parameters:
    -----------


        output_type: string.
             'dict'(default) for dictionary format output,
             'df' for data frame,
             'raw' for list of dictionaries directly from the web.
    Notes
    -----


    Example
    -------
            getCalendarData(output_type='df')

    """

    # d is a dictionary used for create the api url
    d = {
        "url_base": "/calendar/updates",
        "output_type": "",
    }

    api_url_request = d["url_base"]

    return fn.dataRequest(api_request=api_url_request, output_type=output_type)


def getCalendarEventsByGroup(
    group: str, country: str = None, initDate=None, endDate=None, output_type=None
):
    """
    Returns calendar events of the specified group
    =================================================================================
    Parameters:
    -----------
        group: string
            bonds, inflation

        country: string, optional
            'united states'
            'china'


        output_type: string.
             'dict'(default) for dictionary format output,
             'df' for data frame,
             'raw' for list of dictionaries directly from the web.
    Notes
    -----


    Example
    -------
            getCalendarEventsByGroup(group='bond', output_type='df')
            getCalendarEventsByGroup(country='china', group='inflation', endDate='2023-02-01', output_type='df')
            getCalendarEventsByGroup('inflation', initDate='2023-01-01', endDate='2023-02-01', output_type='dict')

    """

    d = {"url_base": "/calendar", "output_type": ""}

    api_url_request = d["url_base"]

    if country:
        api_url_request += f"/country/{fn.stringOrList(country)}"

    if group:
        api_url_request += f"/group/{fn.stringOrList(group)}"
    else:
        return "Group cannot be empty"

    if initDate and endDate:
        initDateFormat = fn.validate(initDate)
        endDateFormat = fn.validate(endDate)
        fn.validatePeriod(initDate, initDateFormat, endDate, endDateFormat)

    if initDate:
        fn.validate(initDate)
        api_url_request += f"/{quote(initDate)}"

    if endDate:
        fn.validate(endDate)
        api_url_request += f"/{quote(endDate)}"

    return fn.dataRequest(api_request=api_url_request, output_type=output_type)


def getCalendarEvents(country: List[str] = None, output_type=None):
    """
    Returns all calendar events or of the specific country passed as parameter.
    =================================================================================
    Parameters:
    ----------
        country: string, optional
            'united states'
            'china'


        output_type: string.
             'dict'(default) for dictionary format output,
             'df' for data frame,
             'raw' for list of dictionaries directly from the web.
    Notes
    -----


    Example
    -------
            getCalendarEvents(output_type='df')
            getCalendarEvents(country='china', output_type='df')
            getCalendarEvents(country=['china', 'canada'] output_type='dict')

    """

    d = {
        "url_base": "/calendar/events",
        "output_type": "",
    }

    api_url_request = d["url_base"]

    if country:
        api_url_request += f"/country/{fn.stringOrList(country)}"

    return fn.dataRequest(api_request=api_url_request, output_type=output_type)
