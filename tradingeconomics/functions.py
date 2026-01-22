from datetime import datetime
import re
import itertools
import urllib
import sys
import json
import pandas as pd
import time
import ssl

PY3 = sys.version_info[0] == 3

if PY3:  # Python 3+
    from urllib.request import urlopen, Request  # type: ignore
    from urllib.parse import quote  # type: ignore
else:  # Python 2.X
    from urllib import urlopen  # type: ignore
    from urllib import quote  # type: ignore
    from urllib2 import Request  # type: ignore


class DateError(ValueError):
    pass


class CredentialsError(ValueError):
    pass


class AuthenticationError(ValueError):
    """Raised when API authentication fails (401/403 errors)"""

    pass


class ParametersError(ValueError):
    pass


class WebRequestError(ValueError):
    pass


def setup_ssl_context():
    """
    Configure SSL context to use unverified HTTPS connections.
    This is needed for compatibility with some API endpoints.
    Call this once at the start of functions that make HTTPS requests.
    """
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        # Python doesn't support this, skip
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context


def credCheck(credentials):
    # pattern = re.compile("^:$")
    # if not(pattern.match(credentials)):
    #    raise CredentialsError('Invalid credentials.')
    if ":" not in credentials:
        raise CredentialsError("Invalid credentials.")


def out_type(init_format, isCommodity=False):
    if isCommodity:
        list_of_countries = init_format.Title.unique()
    else:
        list_of_countries = init_format.Country.unique()
    list_of_cat = init_format.Category.unique()
    dict_start = {el: {elm: 0 for elm in list_of_cat} for el in list_of_countries}
    for i, j in itertools.product(
        range(len(list_of_countries)), range(len(list_of_cat))
    ):
        if isCommodity:
            dict_cntry = init_format.loc[init_format["Title"] == list_of_countries[i]]
        else:
            dict_cntry = init_format.loc[init_format["Country"] == list_of_countries[i]]
        dict_cat = dict_cntry.loc[init_format["Category"] == list_of_cat[j]].to_dict(
            "records"
        )
        dict_start[list_of_countries[i]][list_of_cat[j]] = dict_cat
        for l in range(len(dict_cat)):
            if isCommodity:
                del dict_cat[l]["Title"]
            else:
                del dict_cat[l]["Country"]
            del dict_cat[l]["Category"]
    return dict_start


def validate(date_string):
    formats = ["%Y-%m-%d", "%Y-%m-%d %H:%M", "%Y-%m-%d %H:%M:%S"]
    for format in formats:
        try:
            datetime.strptime(date_string, format)
            return format
        except ValueError:
            pass
    raise DateError(
        "Incorrect data format, should be YYYY-MM-DD or YYYY-MM-DD HH:MM or YYYY-MM-DD HH:MM:SS"
    )


def validatePeriod(initDate, initDateFormat, endDate, endDateFormat):
    try:
        if datetime.strptime(initDate, initDateFormat) > datetime.strptime(
            endDate, endDateFormat
        ):
            raise DateError("Invalid time period, check the supplied date parameters.")
    except ValueError:
        raise DateError(
            "Incorrect data format, should be YYYY-MM-DD or YYYY-MM-DD HH:MM or YYYY-MM-DD HH:MM:SS"
        )


def timeValidate(clientTime):
    try:
        t = time.strptime(clientTime, "%H:%M")
        time.strftime("%H:%M", t)
    except ValueError:
        print("Incorrect time format, should be HH:MM")


def finalLink(link, prmtr):
    linkAPI = link
    for i in range(len(prmtr)):
        if type(prmtr) == str:
            linkAPI = linkAPI + "/" + prmtr
        linkAPI = linkAPI + "/" + str(prmtr[i])
    return linkAPI


# def stringOrList(string_or_list):
#     if type(string_or_list) is not str:
#         return quote(",".join(string_or_list))
#     return quote(string_or_list)


def stringOrListWithAppend(string_or_list_1, string_or_list_2):
    _list_1 = []
    _list_2 = []

    if type(string_or_list_1) is list:
        _list_1 = [s for s in string_or_list_1]
    elif type(string_or_list_1) is str:
        _list_1 = [string_or_list_1]

    if type(string_or_list_2) is list:
        _list_2 = [s for s in string_or_list_2]
    elif type(string_or_list_2) is str:
        _list_2 = [string_or_list_2]

    combinations = list(itertools.product(_list_1, _list_2))
    comb = [":".join(c) for c in combinations]
    return quote(f",".join(comb))


def dataRequest(api_request, output_type):
    """
    Makes an HTTP request to the Trading Economics API and returns parsed data.

    Parameters:
    -----------
    api_request : str
        Full API URL including endpoint and query parameters
    output_type : str or None
        Output format: None/'dict' (list of dicts), 'df' (DataFrame), 'raw' (JSON)

    Returns:
    --------
    list, DataFrame, or dict depending on output_type

    Raises:
    -------
    AuthenticationError: Invalid credentials or missing authentication (401/403)
    ParametersError: Invalid output_type or no data returned
    WebRequestError: HTTP request failure or connection error
    """
    from . import glob

    if PY3:
        from urllib.error import HTTPError, URLError
    else:
        from urllib2 import HTTPError, URLError  # type: ignore

    def outputTypeCheck(outputType):
        if outputType not in (None, "raw", "dict", "df"):
            raise ParametersError("invalid output_type")

    outputTypeCheck(output_type)

    # Normalize relative paths to full URLs
    if not api_request.startswith(("http://", "https://")):
        # Ensure path starts with / for proper concatenation
        if not api_request.startswith("/"):
            api_request = "/" + api_request
        api_request = glob.API_BASE_URL + api_request

    # Build HTTP request and add authentication header if available
    request = Request(api_request)
    if hasattr(glob, "apikey") and glob.apikey:
        request.add_header("Authorization", glob.apikey)

    try:
        # Execute HTTP request and parse JSON response
        with urlopen(request) as response:
            code = response.getcode()
            webResults = json.loads(response.read().decode("utf-8"))

    except HTTPError as e:
        # Handle HTTP errors with specific status codes
        error_code = e.code
        error_body = ""

        try:
            error_body = e.read().decode("utf-8")
            # Try to parse JSON error message from API
            try:
                error_json = json.loads(error_body)
                error_message = error_json.get("message", error_body)
            except:
                error_message = error_body
        except:
            error_message = str(e.reason)

        # Handle authentication/authorization errors
        if error_code == 401:
            raise AuthenticationError(
                f"Authentication failed (401 Unauthorized). "
                f"Invalid API key or missing credentials. "
                f"Please check your login credentials. Details: {error_message}"
            )
        elif error_code == 403:
            raise AuthenticationError(
                f"Access forbidden (403 Forbidden). "
                f"Your API key may not have permission to access this resource. "
                f"Details: {error_message}"
            )
        elif error_code == 404:
            raise ParametersError(
                f"Endpoint not found (404). "
                f"The requested resource does not exist. "
                f"Details: {error_message}"
            )
        elif 400 <= error_code < 500:
            raise ParametersError(
                f"Client error (HTTP {error_code}). "
                f"Invalid request parameters. "
                f"Details: {error_message}"
            )
        elif error_code >= 500:
            raise WebRequestError(
                f"Server error (HTTP {error_code}). "
                f"Trading Economics API is experiencing issues. "
                f"Please try again later. Details: {error_message}"
            )
        else:
            raise WebRequestError(f"HTTP error {error_code}: {error_message}")

    except URLError as e:
        # Handle network-level errors (DNS, connection timeout, etc.)
        raise WebRequestError(
            f"Network error: Unable to connect to Trading Economics API. "
            f"Please check your internet connection. Details: {str(e.reason)}"
        )

    except json.JSONDecodeError as e:
        # Handle invalid JSON responses
        raise WebRequestError(
            f"Invalid JSON response from API. "
            f"The server may be experiencing issues. Details: {str(e)}"
        )

    except Exception as e:
        # Catch-all for unexpected errors
        raise WebRequestError(f"Unexpected error during API request: {str(e)}")

    # Process successful response (code should be 200 or 2xx)
    if 200 <= code < 300:
        # Check if response contains data
        if len(webResults) == 0:
            raise ParametersError("No data available for the provided parameters.")

        # Convert response to requested output format
        if output_type == "df":
            return pd.DataFrame(webResults)
        elif output_type == "raw":
            return webResults
        elif output_type == None or output_type == "dict":
            return webResults
        else:
            raise ParametersError(
                "output_type options : df(default) for data frame or raw for unparsed results."
            )
    else:
        # This should not happen as non-2xx codes trigger HTTPError
        raise WebRequestError(f"Unexpected response code: {code}")


def makeRequestAndParse(api_request, output_type):
    code = None
    webResults = None
    try:
        with urlopen(api_request) as response:
            code = response.getcode()
            webResults = json.loads(response.read().decode("utf-8"))
    except ValueError:
        if code != 200:
            print(urlopen(api_request).read().decode("utf-8"))
        else:
            raise WebRequestError("Something went wrong. Error code = " + str(code))
    if code == 200:
        try:

            if len(webResults) > 0:  # type: ignore
                # names = ['country', 'category', 'historicalDataSymbol', 'lastUpdate']
                # names2 = ['Country', 'Category', 'HistoricalDataSymbol', 'LastUpdate']
                maindf = pd.DataFrame.from_records(webResults)  # type: ignore  # columns=names2

            else:
                raise ParametersError("No data available for the provided parameters.")
            if output_type == None or output_type == "dict":
                output = maindf.to_dict("dict")
            elif output_type == "df":
                output = maindf
            elif output_type == "raw":
                output = webResults
            else:
                raise ParametersError(
                    "output_type options : df(default) for data frame or raw for unparsed results."
                )
            return output
        except ValueError:
            pass
    else:
        return ""


def checkDates(baseLink, initDate=None, endDate=None):
    # Determine separator: ? if no query string yet, & if there is one
    separator = "&" if "?" in baseLink else "?"

    if (initDate is not None) and endDate == None:
        try:
            initDateFormat = validate(initDate)
        except ValueError:
            raise DateError("Incorrect initDate format, should be YYYY-MM-DD.")
        # if initDate > str(date.today()):
        #     raise DateError ('Initial date out of range.')
        baseLink += separator + "d1=" + quote(initDate)

    if (initDate is not None) and (endDate is not None):
        try:
            initDateFormat = validate(initDate)
        except ValueError:
            raise DateError("Incorrect initDate format, should be YYYY-MM-DD.")
        try:
            endDateFormat = validate(endDate)
        except ValueError:
            raise DateError("Incorrect endDate format, should be YYYY-MM-DD.")
        try:
            validatePeriod(initDate, initDateFormat, endDate, endDateFormat)
        except ValueError:
            raise DateError("Invalid time period.")
        baseLink += separator + "d1=" + quote(initDate) + "&d2=" + quote(endDate)

    if initDate == None and (endDate is not None):
        raise DateError("initDate value is missing")
    return baseLink


def stringOrList(value):
    """
    Convert string or list into a comma-separated URL-safe string.
    Each item is encoded individually, commas remain literal.
    """

    if isinstance(value, str):
        # Encode only the string, do not touch commas or colons
        return quote(value, safe=":")

    if isinstance(value, list):
        # Encode each item individually, keeping colons safe
        encoded_items = [quote(str(v), safe=":") for v in value]
        return ",".join(encoded_items)

    # Unexpected type fallback
    return quote(str(value), safe=":")
