import json
import urllib
import pandas as pd
from datetime import *
import sys
from . import functions as fn
from . import glob
import ssl

PY3 = sys.version_info[0] == 3

if PY3:  # Python 3+
    from urllib.request import urlopen
    from urllib.parse import quote
else:  # Python 2.X
    from urllib import urlopen
    from urllib import quote


class ParametersError(ValueError):
    pass


class CredentialsError(ValueError):
    pass


class LoginError(AttributeError):
    pass


class WebRequestError(ValueError):
    pass


def checkLists(lists):
    linkAPI = "/eurostat/"
    if type(lists) is str and lists == "categories":
        linkAPI += "categories"
    elif type(lists) is str and lists == "countries":
        linkAPI += "countries"
    return linkAPI


def getLinkSymbol(symbol):
    linkAPI = "/eurostat/symbol/"
    if type(symbol) is str:
        linkAPI += quote(symbol, safe="")
    else:
        linkAPI += quote(",".join(symbol), safe="")
    return linkAPI


def checkCountry(country):
    linkAPI = "/eurostat/country/"
    if type(country) is str:
        linkAPI += quote(country, safe="")
    else:
        # multiCountry = ",".join(country)
        linkAPI += quote(",".join(country), safe="")
    return linkAPI


def checkcategory(category):
    linkAPI = "/eurostat?category="
    if type(category) is str:
        linkAPI += quote(category, safe="")
    else:
        linkAPI += quote(",".join(category), safe="")
    return linkAPI


def checkcategory_group(category_group):
    linkAPI = "/eurostat?category_group="
    if type(category_group) is str:
        linkAPI += quote(category_group, safe="")
    else:
        linkAPI += quote(",".join(category_group), safe="")
    return linkAPI


def getLinkcategory(country, category):
    linkAPI = "/eurostat/country/"
    if type(country) is str:
        linkAPI += quote(country)
    else:
        linkAPI += quote(",".join(country), safe="")
    if type(category) is str:
        linkAPI += "?category=" + quote(category, safe="")
    return linkAPI


def getLinkcategory_group(country, category_group):
    linkAPI = "/eurostat/country/"
    if type(country) is str:
        linkAPI += quote(country)
    else:
        linkAPI += quote(",".join(country), safe="")
    if type(category_group) is str:
        linkAPI += "?category_group=" + quote(category_group, safe="")
    return linkAPI


def getEurostatData(
    country=None,
    category=None,
    category_group=None,
    lists=None,
    symbol=None,
    output_type=None,
):
    """
     Return Eurostat data by country, category and category_group, also lists with countries and categoreies available.
    ===========================================================================

    Parameters:
    -----------
    country: string.
             String to get data for one country.
    category: string.
             String  to get data for one category.
             For example, category = 'People at risk of income poverty after social transfers'.
    category_group: string.
             String  to get data for one category_group.
             For example, category_group = 'Poverty'.
    symbol: string.
             String  to get data for one symbol
             For example, symbol = '51640'.
    output_type: string.
             'dict'(default) for dictionary format output, 'df' for data frame,
             'raw' for list of dictionaries without any parsing.

    Notes
    -----
    At least one of parameters, country or category, should be provided.

    Example
    -------
    getEurostatData(country = 'Denmark',output_type='df')

    getEurostatData(country = 'Denmark', category = 'People at risk of income poverty after social transfers',output_type='df')

    getEurostatData(country = 'Denmark', category_group = 'Poverty',output_type='df')

    getEurostatData(category = 'People at risk of income poverty after social transfers',output_type='df')

    getEurostatData(category_group = 'Poverty',output_type='df')

    getEurostatData(symbol = '51640',output_type='df')

    getEurostatData(lists='categories',output_type='df')

    getEurostatData(lists='countries',output_type='df')
    """
    fn.setup_ssl_context()

    if (
        country == None
        and category == None
        and category_group == None
        and lists == None
        and symbol == None
    ):
        raise ValueError("At least one of the parameters, needs to be supplied.")
    elif lists != None:
        linkAPI = checkLists(lists)
    elif symbol != None:
        linkAPI = getLinkSymbol(symbol)
    elif country != None and category == None and category_group == None:
        linkAPI = checkCountry(country)
    elif country == None and category != None:
        linkAPI = checkcategory(category)
    elif country == None and category_group != None:
        linkAPI = checkcategory_group(category_group)
    elif country != None and category_group != None:
        linkAPI = getLinkcategory_group(country, category_group)
    elif country != None and category != None:
        linkAPI = getLinkcategory(country, category)

    return fn.dataRequest(api_request=linkAPI, output_type=output_type)


def getEurostatCountries(output_type=None):
    """
    Returns List of List of countries available.
    ==========================================================
    Example
    -------
        te.getEurostatCountries(output_type='df')
    """

    # d is a dictionary used for create the api url
    d = {
        "url_base": "/eurostat/countries",
        "output_type": "",
    }

    api_url_request = d["url_base"]
    return fn.dataRequest(api_request=api_url_request, output_type=output_type)


def getEurostatCategoryGroups(output_type=None):
    """
    Returns List of categories and category groups available..
    ==========================================================

    Example
    -------
        getEurostatCategoryGroups(output_type='df')
    """

    # d is a dictionary used for create the api url
    d = {
        "url_base": "/eurostat/categories",
        "output_type": "",
    }

    api_url_request = d["url_base"]

    return fn.dataRequest(api_request=api_url_request, output_type=output_type)
