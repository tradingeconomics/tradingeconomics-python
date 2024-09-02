import ssl
from typing import List
from . import functions as fn
from . import glob

class LoginError(AttributeError):
    pass

class WebRequestError(ValueError):
    pass


def getStockSplits(ticker: List[str]=None, country: List[str]=None, startDate: str=None, endDate: str=None, output_type: str=None):
    """
    Returns stock splits calendar data.
    ==========================================================
    Parameters:
    -----------
    ticker: string or list of strings, optional
            Get stock splits for the ticker/s specified.
    
    startDate: string with format: YYYY-MM-DD.
            For example: '2023-09-01'

    endDate: string with format: YYYY-MM-DD.
            For example: '2023-09-30'

    Example:
    --------
    getStockSplits(ticker = 'MMET', startDate='2023-09-01', endDate='2023-12-01')
    getStockSplits(ticker = ['MMET', 'REX'], startDate='2023-09-01')
    getStockSplits(coutnry = ['Canada', 'United States'])
    getStockSplits()
    
    """

    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context

    linkAPI = 'https://api.tradingeconomics.com/splits'
    
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