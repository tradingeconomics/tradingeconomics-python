from . import functions as fn
from . import glob
import ssl
from typing import List, Union, Optional


class LoginError(AttributeError):
    pass


def getCreditRatings(
    country: Optional[Union[str, List[str]]] = None, output_type: Optional[str] = None
):
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

    fn.setup_ssl_context()

    linkAPI = "/credit-ratings"

    if country != None:
        linkAPI = linkAPI + f"/country/{fn.stringOrList(country)}"

    return fn.dataRequest(api_request=linkAPI, output_type=output_type)


def getHistoricalCreditRatings(
    country: Optional[Union[str, List[str]]] = None,
    initDate: Optional[str] = None,
    endDate: Optional[str] = None,
    output_type: Optional[str] = None,
):
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

    fn.setup_ssl_context()

    linkAPI = "/credit-ratings/historical"

    if country != None:
        linkAPI = linkAPI + f"/country/{fn.stringOrList(country)}"

    linkAPI = fn.checkDates(linkAPI, initDate, endDate)

    return fn.dataRequest(api_request=linkAPI, output_type=output_type)
