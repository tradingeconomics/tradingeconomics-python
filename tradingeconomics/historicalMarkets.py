import json
import itertools
import urllib
import pandas as pd
import sys
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from . import functions as fn
from . import glob
import ssl

PY3 = sys.version_info[0] == 3

if PY3:  # Python 3+
    from urllib.request import urlopen  # type: ignore
    from urllib.parse import quote  # type: ignore
else:  # Python 2.X
    from urllib import urlopen  # type: ignore
    from urllib import quote  # type: ignore


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


def parseData(data):
    datafr = pd.DataFrame.from_dict(data)
    datafr["dates"] = pd.to_datetime(datafr["dates"], format="%d/%m/%Y")
    indx = datafr["dates"]
    datafr = datafr[["symbol", "open", "high", "low", "close"]]
    datafr = datafr.set_index(indx)
    datafr.index.name = None
    # del datafr.index.name
    return datafr


def fetchMarkets(symbol=None, initDate=None, endDate=None, output_type=None):
    """
    Return historical information for specific markets symbol.
    =================================================================

    Parameters:
    -----------
    symbol: Unique symbol used by TradingEconomics.
             For example: 'aapl:us'
    initDate: string with format: YYYY-MM-DD.
             For example: '2011-01-01'
    endDate: string with format: YYYY-MM-DD.
    output_type: string.
             'dict'(default) for dictionary format output,
             'df' for dataframe,
             'raw' for list of dictionaries without any parsing.

    Notes
    -----
    A symbol must be provided.

    Example
    -------
    fetchMarkets(symbol = 'indu:ind')
    fetchMarkets(symbol = 'indu:ind', initDate = '2017-01-01', endDate = '2017-06-15', output_type='raw')
    fetchMarkets(symbol = ['aapl:us', 'indu:ind'], initDate = '2017-01-01', endDate = '2017-06-15')
    """
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context

    linkAPI = "/markets/historical/"

    if type(symbol) is not str:
        linkAPI = "/markets/historical/" + quote(",".join(symbol), safe="")
    else:
        linkAPI = "/markets/historical/" + quote(symbol, safe="")

    if (initDate is not None) and (endDate is not None):
        try:
            initDateFormat = fn.validate(initDate)
        except ValueError:
            raise DateError(
                "Incorrect initDate format, should be YYYY-MM-DD or MM-DD-YYYY."
            )
        try:
            endDateFormat = fn.validate(endDate)
        except ValueError:
            raise DateError(
                "Incorrect endDate format, should be YYYY-MM-DD or MM-DD-YYYY."
            )
        try:
            fn.validatePeriod(initDate, initDateFormat, endDate, endDateFormat)
        except ValueError:
            raise DateError("Invalid time period.")
        linkAPI += "?d1=" + quote(initDate) + "&d2=" + quote(endDate)

    elif (initDate is not None) and endDate == None:
        try:
            initDateFormat = fn.validate(initDate)
        except ValueError:
            raise DateError(
                "Incorrect initDate format, should be YYYY-MM-DD or MM-DD-YYYY."
            )
            if initDate > str(date.today()):
                raise DateError("Initial date out of range.")
        linkAPI += "?d1=" + quote(initDate)

    elif initDate == None and (endDate is not None):
        initDate = (
            datetime.strptime(endDate, "%Y-%m-%d") - relativedelta(months=1)
        ).strftime("%Y-%m-%d")
        linkAPI += "?d1=" + quote(initDate) + "&d2=" + quote(endDate)

    return fn.dataRequest(api_request=linkAPI, output_type=output_type)
