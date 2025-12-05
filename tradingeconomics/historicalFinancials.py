import json
import urllib
import pandas as pd
import sys
from datetime import datetime, date
from . import glob
import ssl
from . import functions as fn
from dateutil.relativedelta import relativedelta

PY3 = sys.version_info[0] == 3

if PY3:  # Python 3+
    from urllib.request import urlopen  # type: ignore
    from urllib.parse import quote  # type: ignore
else:  # Python 2.X
    from urllib import urlopen  # type: ignore
    from urllib import quote  # type: ignore


class ParametersError(ValueError):
    pass


class CredentialsError(ValueError):
    pass


class LoginError(AttributeError):
    pass


class DateError(ValueError):
    pass


class WebRequestError(ValueError):
    pass


def getFinancialsHistorical(
    symbol=None, category=None, initDate=None, endDate=None, output_type=None
):
    """
    Returns stocks fundamental information for specific symbols, category and dates.
    ================================================================================
    Parameters:
    -----------
    symbol: string or list.
            String to get data for symbol. For example, symbols = 'aapl:us', symbols = ['aapl:us', 'tsla:us'].
    category: string or list.
            String to get data by category.
            For example, category = 'debt', category = ['assets', 'debt']
    initDate: string with format: YYYY-MM-DD.
            For example: '2023-01-01'
    endDate: string with format: YYYY-MM-DD.
            For example: '2023-01-02'

    output_type: string.
             'dict'(default), 'df' for data frame,
             'raw' for list of unparsed data.
    Example
    -------
    getFinancialsHistorical('aapl:us', 'assets', output_type='df')
    getFinancialsHistorical(symbol=['aapl:us', 'tsla:us'], category=['assets', 'debt'], output_type='df')

    """
    fn.setup_ssl_context()

    if symbol is not None and category is not None:
        if category.__contains__(" "):
            category = category.replace(" ", "-")
        linkAPI = (
            f"/financials/historical/{fn.stringOrListWithAppend(symbol, category)}"
        )
    else:
        return "symbol and category arguments are required"

    linkAPI = fn.checkDates(linkAPI, initDate, endDate)
    return fn.dataRequest(api_request=linkAPI, output_type=output_type)
