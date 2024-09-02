import ssl
from typing import List
from . import functions as fn
from . import glob

class LoginError(AttributeError):
    pass

def getDividends(symbols: List[str]=None, startDate: str=None, endDate: str=None, output_type: str=None):
    """
    Returns dividends calendar data.
    ==========================================================
    Parameters:
    -----------
    symbols: string or list of strings, optional
            Get dividends for the symbol/s specified.

    startDate: string with format: YYYY-MM-DD.
            For example: '2022-01-01'

    endDate: string with format: YYYY-MM-DD.
            For example: '2023-01-01'

    Example:
    --------
    getDividends(symbols = 'msft:us', startDate='2016-01-01', endDate='2017-12-31')
    getDividends(symbols = 'msft:us', startDate='2016-01-01')
    getDividends(symbols = 'msft:us')
    getDividends()
    
    """

    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context

    linkAPI = 'https://api.tradingeconomics.com/dividends'

    if symbols and fn.isStringOrList(symbols):
        linkAPI += '/symbol/' + fn.stringOrList(symbols)

    try:
        linkAPI += '?c=' + glob.apikey
    except AttributeError:
        raise LoginError('You need to do login before making any request')

    linkAPI = fn.checkDates(linkAPI, startDate, endDate)

    return fn.dataRequest(api_request=linkAPI, output_type=output_type)


