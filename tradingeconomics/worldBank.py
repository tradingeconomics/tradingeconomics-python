import json
import urllib
import pandas as pd
import sys
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


class CredentialsError(ValueError):
    pass


class LoginError(AttributeError):
    pass


class WebRequestError(ValueError):
    pass


def checkSeriesCode(linkAPI, series_code):
    linkAPI = "/worldBank/indicator"
    if series_code == None:
        linkAPI += "?s=" + quote(str(series_code))
    else:
        linkAPI += "?s=" + quote("".join(series_code))

    return linkAPI


def checkPageNumber(linkAPI, page_number):
    if page_number != None:
        linkAPI += "/{0}".format(page_number)
    return linkAPI


def checkCountry(linkAPI, country):
    linkAPI = "/worldBank/country/"
    if type(country) is str:
        linkAPI += quote(str(country), safe=",")
    else:
        linkAPI += quote(",".join(country), safe=",")

    return linkAPI


def checkIndicator(linkAPI, indicator):
    linkAPI = "/worldBank/indicator/"
    if type(indicator) is str:
        linkAPI += quote(str(indicator), safe="")
    else:
        linkAPI += quote(",".join(indicator), safe="")

    return linkAPI


def getWBCategories(category=None, page_number=None, output_type=None):
    """
    Return a list of all categories, categories by page number.
    =================================================================================

    Parameters:
    -----------
    categories:list.
             List of strings for all categories and list of categories by page number.
             All categories, for example:
                category = None
             Several categories or one category, for example:
                category = ['education', 'agriculture']
                category = 'education'
             categories by page, for example:
                category = 'education', page_number = 3
                category = ['education', 'agriculture'], page_number = 5
    output_type: string.
             'dict'(default) for dictionary format output, 'df' for data frame,
             'raw' for list of dictionaries directly from the web.

    Notes
    -----
    All parameters are optional. Without parameters a list of all categories will be provided.

    Example
    -------
    getWBCategories(category = None, output_type = None)

    getWBCategories(category = ['education', 'agriculture'], output_type = None)
    """
    url = ""
    fn.setup_ssl_context()
    if category:
        url = "/worldBank/category/" + quote(str(category), safe="")
    else:
        url = "/worldBank/categories"

    if category == None:
        linkAPI = "/worldBank/categories"
    else:
        linkAPI = "/worldBank/category/" + quote(str(category), safe="")

    if page_number != None:
        linkAPI = checkPageNumber(linkAPI, page_number)

    return fn.dataRequest(api_request=linkAPI, output_type=output_type)


def getWBIndicator(series_code=None, url=None, output_type=None):
    """
    Detailed information about specific indicator for all countries using a series
    code or url.
    =================================================================================

    Parameters:
    -----------
    series_code:list.
             List of strings of indicators by series code.
             sring of indicator by country using it's url.
             Specific indicator and country by using series code, for example:
                series_code = 'usa.fr.inr.rinr'(symbol used by TE for a country)
    Url:string.
             Specific indicator and country by using url, for example:
                url = '/united-states/real-interest-rate-percent-wb-data.html'
    output_type: string.
             'dict'(default) for dictionary format output, 'df' for data frame,
             'raw' for list of dictionaries directly from the web.

    Notes
    -----
    A series code or url is required.

    Example
    -------

    getWBIndicator(series_code = 'usa.fr.inr.rinr', url = None, output_type = None)

    getWBIndicator(series_code = None, url = '/united-states/real-interest-rate-percent-wb-data.html', output_type = None)
    """
    fn.setup_ssl_context()

    linkAPI = "/worldBank/indicator/"
    if series_code == None and url == None:
        return "Series code or url is required!"

    if series_code != None:
        linkAPI = "/worldBank/indicator" + "?s=" + quote(str(series_code), safe=",/")
    elif url != None:
        linkAPI = "/worldBank/indicator" + "?url=" + quote(str(url), safe=",/")

    return fn.dataRequest(api_request=linkAPI, output_type=output_type)


def getWBCountry(country=None, page_number=None, output_type=None):
    """
    List of indicators available for a specific country (with pagination).
    =================================================================================

    Parameters:
    -----------
    country:list.
             List of strings of indicators by country.
             country, for example:
                country = 'portugal'
    page_number:
                country = 'portugal', page_number = 3
    output_type: string.
             'dict'(default) for dictionary format output, 'df' for data frame,
             'raw' for list of dictionaries directly from the web.

    Notes
    -----
    A country is required to get a list.

    Example
    -------
    getWBCountry(country = 'portugal', output_type = None) # page_number is no longer needed!
    """
    linkAPI = "/worldBank/country/"
    fn.setup_ssl_context()

    if country == None:
        return "A country is required!"
    else:
        linkAPI = checkCountry(linkAPI, country)

    if page_number != None:
        linkAPI = checkPageNumber(linkAPI, page_number)

    return fn.dataRequest(api_request=linkAPI, output_type=output_type)


def getWBHistorical(series_code=None, output_type=None):
    """
    Historical data for a specific indicator.
    =================================================================================

    Parameters:
    -----------
    series_code:list.
             List of historical data by country.
             for example:
                series_code = None
                series_code = 'usa.fr.inr.rinr'
    output_type: string.
             'dict'(default) for dictionary format output, 'df' for data frame,
             'raw' for list of dictionaries directly from the web.

    Notes
    -----
    A series code is required.

    Example
    -------

    getWBHistorical(series_code = 'usa.fr.inr.rinr', output_type = None)
    """
    fn.setup_ssl_context()

    linkAPI = "/worldBank/historical"

    if series_code == None:
        return "A series code is required!"
    else:
        linkAPI += "?s=" + quote(str(series_code))

    return fn.dataRequest(api_request=linkAPI, output_type=output_type)
