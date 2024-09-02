import ssl
from typing import List
from . import functions as fn
from . import glob

class LoginError(AttributeError):
    pass

class WebRequestError(ValueError):
    pass


def getIpo(ticker: List[str]=None, country: List[str]=None, startDate: str=None, endDate: str=None, output_type: str=None):
    """
    Returns IPO calendar data.
    ==========================================================
    Parameters:
    -----------
    ticker: string or list of strings, optional
            Get IPO data for the ticker/s specified.
    
    country: string or list of strings, optional
            Get IPO data from stocks of specific countries.

    startDate: string with format: YYYY-MM-DD.
            For example: '2023-10-01'

    endDate: string with format: YYYY-MM-DD.
            For example: '2023-10-31'

    Example:
    --------
    getIpo(ticker = 'SWIN', startDate='2023-10-01', endDate='2023-10-31')
    getIpo(country = ['United States', 'Hong Kong'], startDate='2023-10-31')
    getIpo()
    
    """
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context

    linkAPI = 'https://api.tradingeconomics.com/ipo'
    
    if ticker and country:
        raise ValueError('ticker and country cannot be used together')

    if ticker and fn.isStringOrList(ticker):
        linkAPI += '/ticker/' + fn.stringOrList(ticker)
    elif country and fn.isStringOrList(country):
        linkAPI += '/country/' + fn.stringOrList(country)
    
    try:
        linkAPI += '?c=' + glob.apikey
    except AttributeError:
        raise LoginError('You need to do login before making any request')

    linkAPI = fn.checkDates(linkAPI, startDate, endDate)

    return fn.dataRequest(api_request=linkAPI, output_type=output_type)
