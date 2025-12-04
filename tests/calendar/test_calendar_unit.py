# tests/test_calendar_unit.py
# Unit tests for tradingeconomics.calendar
# These tests validate URL construction logic, parameter handling,
# and internal behavior using mocks. No real API calls are made.

import unittest
from unittest.mock import patch
from tradingeconomics.calendar import (
    paramCheck,
    checkCalendarId,
    getCalendarId,
    getCalendarData,
    getCalendarEvents,
    getCalendarEventsByGroup,
)


class TestParamCheck(unittest.TestCase):
    """Tests for URL construction in paramCheck()."""

    def test_single_country(self):
        url = paramCheck("united states")
        self.assertEqual(
            url,
            "https://api.tradingeconomics.com/calendar/country/united%20states",
        )

    def test_multiple_countries(self):
        url = paramCheck(["united states", "china"])
        self.assertEqual(
            url,
            "https://api.tradingeconomics.com/calendar/country/united%20states,china",
        )

    def test_country_and_indicator(self):
        url = paramCheck("united states", "inflation rate")
        self.assertEqual(
            url,
            "https://api.tradingeconomics.com/calendar/country/united%20states/indicator/inflation%20rate",
        )


class TestCheckCalendarId(unittest.TestCase):
    """Tests for URL construction in checkCalendarId()."""

    def test_single_id(self):
        url = checkCalendarId("12345")
        self.assertEqual(
            url,
            "https://api.tradingeconomics.com/calendar/calendarid/12345",
        )

    def test_multiple_ids(self):
        url = checkCalendarId(["111", "222", "333"])
        self.assertEqual(
            url,
            "https://api.tradingeconomics.com/calendar/calendarid/111,222,333",
        )


class TestGetCalendarId(unittest.TestCase):
    """Tests for getCalendarId() ensuring correct URL assembly and behavior."""

    @patch("tradingeconomics.calendar.fn.dataRequest")
    @patch("tradingeconomics.calendar.glob.apikey", "guest:guest")
    def test_getCalendarId_with_single_id(self, mock_request):
        getCalendarId(id="555")
        url = mock_request.call_args[1]["api_request"]
        self.assertEqual(
            url,
            "https://api.tradingeconomics.com/calendar/calendarid/555?c=guest:guest",
        )

    @patch("tradingeconomics.calendar.fn.dataRequest")
    @patch("tradingeconomics.calendar.glob.apikey", "guest:guest")
    def test_getCalendarId_no_id(self, mock_request):
        getCalendarId(id=None)
        url = mock_request.call_args[1]["api_request"]
        self.assertEqual(
            url,
            "https://api.tradingeconomics.com/calendar?c=guest:guest",
        )


class TestGetCalendarData(unittest.TestCase):
    """Tests for URL construction in getCalendarData()."""

    @patch("tradingeconomics.calendar.fn.dataRequest")
    @patch("tradingeconomics.calendar.glob.apikey", "guest:guest")
    def test_country_only(self, mock_request):
        getCalendarData(country="united states")
        url = mock_request.call_args[1]["api_request"]
        self.assertEqual(
            url,
            "https://api.tradingeconomics.com/calendar/country/united%20states?c=guest:guest",
        )

    @patch("tradingeconomics.calendar.fn.dataRequest")
    @patch("tradingeconomics.calendar.glob.apikey", "guest:guest")
    def test_country_and_category(self, mock_request):
        getCalendarData(country="united states", category="inflation rate")
        url = mock_request.call_args[1]["api_request"]
        self.assertEqual(
            url,
            "https://api.tradingeconomics.com/calendar/country/united%20states/indicator/inflation%20rate?c=guest:guest",
        )

    @patch("tradingeconomics.calendar.fn.dataRequest")
    @patch("tradingeconomics.calendar.glob.apikey", "guest:guest")
    def test_ticker_only(self, mock_request):
        getCalendarData(ticker="IJCUSA")
        url = mock_request.call_args[1]["api_request"]
        self.assertEqual(
            url,
            "https://api.tradingeconomics.com/calendar/ticker/IJCUSA?c=guest:guest",
        )

    @patch("tradingeconomics.calendar.fn.dataRequest")
    @patch("tradingeconomics.calendar.glob.apikey", "guest:guest")
    def test_event_without_country(self, mock_request):
        result = getCalendarData(event="GDP")
        self.assertEqual(result, "The parameter 'country' must be provided!")

    @patch("tradingeconomics.calendar.fn.dataRequest")
    @patch("tradingeconomics.calendar.glob.apikey", "guest:guest")
    def test_country_with_dates(self, mock_request):
        getCalendarData(country="united states", initDate="2020-01-01", endDate="2020-01-02")
        url = mock_request.call_args[1]["api_request"]
        self.assertEqual(
            url,
            "https://api.tradingeconomics.com/calendar/country/united%20states/2020-01-01/2020-01-02?c=guest:guest",
        )


class TestGetCalendarEvents(unittest.TestCase):
    """Tests for getCalendarEvents()."""

    @patch("tradingeconomics.calendar.fn.dataRequest")
    @patch("tradingeconomics.calendar.glob.apikey", "guest:guest")
    def test_get_all_events(self, mock_request):
        getCalendarEvents()
        url = mock_request.call_args[1]["api_request"]
        self.assertEqual(
            url,
            "https://api.tradingeconomics.com/calendar/events?c=guest:guest",
        )

    @patch("tradingeconomics.calendar.fn.dataRequest")
    @patch("tradingeconomics.calendar.glob.apikey", "guest:guest")
    def test_get_events_for_country(self, mock_request):
        getCalendarEvents(country="china")
        url = mock_request.call_args[1]["api_request"]
        self.assertEqual(
            url,
            "https://api.tradingeconomics.com/calendar/events/country/china?c=guest:guest",
        )


class TestGetCalendarEventsByGroup(unittest.TestCase):
    """Tests for getCalendarEventsByGroup()."""

    @patch("tradingeconomics.calendar.fn.dataRequest")
    @patch("tradingeconomics.calendar.glob.apikey", "guest:guest")
    def test_basic_group(self, mock_request):
        getCalendarEventsByGroup(group="bonds")
        url = mock_request.call_args[1]["api_request"]
        self.assertEqual(
            url,
            "https://api.tradingeconomics.com/calendar/group/bonds?c=guest:guest",
        )

    @patch("tradingeconomics.calendar.fn.dataRequest")
    @patch("tradingeconomics.calendar.glob.apikey", "guest:guest")
    def test_group_with_country(self, mock_request):
        getCalendarEventsByGroup(group="bonds", country="united states")
        url = mock_request.call_args[1]["api_request"]
        self.assertEqual(
            url,
            "https://api.tradingeconomics.com/calendar/country/united%20states/group/bonds?c=guest:guest",
        )


if __name__ == "__main__":
    unittest.main()
