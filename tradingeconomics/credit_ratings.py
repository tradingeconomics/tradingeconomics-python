from . import functions as fn
from . import glob
import ssl
from typing import List


class LoginError(AttributeError):
    pass


def getCreditRatings(country: List[str]=None, output_type: str=None):
    """
    Returns a list of all countries credit ratings.

    Parameters:
    ----------
    country: str or list.
        Country name or list of countries separated by commas.
    out_type: str.
        Output type options are: df, raw, dict.

    Example:
    -------
    getCreditRatings()
    getCreditRatings(country='sweden')
    getCreditRatings(country=['mexico', 'sweden'])
    """

    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context
    
    linkAPI = 'https://api.tradingeconomics.com/credit-ratings'
    
    if country != None:
        linkAPI = linkAPI + f'/country/{fn.isStringOrList(country)}'

    try:
        linkAPI += '?c=' + glob.apikey
    except AttributeError:
        raise LoginError('You need to do login before making any request')

    return fn.dataRequest(api_request=linkAPI, output_type=output_type)


def getHistoricalCreditRatings(country: List[str]=None, initDate: str=None, endDate: str=None, output_type: str=None):
    """
    Returns historical credit ratings by country and date.

    Parameters:
    ----------
    country: str or list.
        Country name or list of countries separated by commas.
    initDate: str.
        Initial date of the historical data.
    endDate: str.
        End date of the historical data.
    out_type: str.
        Output type options are: df, raw, dict.

    Example:
    -------
    getHistoricalCreditRatings()
    getHistoricalCreditRatings(country='mexico')
    getHistoricalCreditRatings(country='mexico', initDate='2010-08-01')
    getHistoricalCreditRatings(country='mexico', initDate='2010-08-01', endDate='2012-01-01')
    """

    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context
    
    linkAPI = 'https://api.tradingeconomics.com/credit-ratings/historical'
    
    if country != None:
        linkAPI = linkAPI + f'/country/{fn.isStringOrList(country)}'

    try:
        linkAPI += '?c=' + glob.apikey
    except AttributeError:
        raise LoginError('You need to do login before making any request')

    linkAPI = fn.checkDates(linkAPI, initDate, endDate)

    return fn.dataRequest(api_request=linkAPI, output_type=output_type)


