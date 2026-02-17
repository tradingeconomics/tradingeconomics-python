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


def getID(ID):
    linkAPI = "/eurostat/historical/"
    if type(ID) is str:
        linkAPI += quote(ID)
    else:
        linkAPI += quote(",".join(ID), safe="")
    return linkAPI


def getHistoricalEurostat(ID=None, initDate=None, endDate=None, output_type=None):
    """
    Return historical Eurostat data.
    =================================================================
    Parameters:
    -----------
    ID: string.
             String to get data for particular ID.
             For example, ID = '24804'.
    initDate: string.
             String to get data by start date.
             For example, initDate = '2015-01-01'.
    endDate: string.
             String to get data by start date.
             For example, endDate = '2020-01-01'.
    output_type: string.
            'df'(default) for dictionary format output,
            'raw' for list of dictionaries without any parsing.
    Notes
    -----
    Without credentials only sample data will be provided.
    Example
    -------
    getHistoricalEurostat(ID = '24804', output_type = 'df')
    getHistoricalEurostat(ID = '24804', initDate ='2015-01-01', output_type = 'df')
    getHistoricalEurostat(ID = '24804', initDate ='2015-01-01', endDate = '2020-01-01', output_type = 'df')

    """
    fn.setup_ssl_context()

    if ID == None:
        raise ValueError("An ID needs to be supplied.")

    linkAPI = ""
    if ID != None:
        linkAPI = getID(ID)
    if (initDate is not None) and (endDate == None):
        linkAPI = getID(ID) + "?d1=" + initDate
    elif (initDate is not None) and (endDate is not None):
        linkAPI = getID(ID) + "?d1=" + initDate + "&d2=" + endDate

    return fn.dataRequest(api_request=linkAPI, output_type=output_type)
