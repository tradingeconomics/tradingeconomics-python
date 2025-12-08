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
            "/calendar/country/united%20states",
        )

    def test_multiple_countries(self):
        url = paramCheck(["united states", "china"])
        self.assertEqual(
            url,
            "/calendar/country/united%20states,china",
        )

    def test_country_and_indicator(self):
        url = paramCheck("united states", "inflation rate")
        self.assertEqual(
            url,
            "/calendar/country/united%20states/indicator/inflation%20rate",
        )


class TestCheckCalendarId(unittest.TestCase):
    """Tests for URL construction in checkCalendarId()."""

    def test_single_id(self):
        url = checkCalendarId("12345")
        self.assertEqual(
            url,
            "/calendar/calendarid/12345",
        )

    def test_multiple_ids(self):
        url = checkCalendarId(["111", "222", "333"])
        self.assertEqual(
            url,
            "/calendar/calendarid/111,222,333",
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
            "/calendar/calendarid/555",
        )

    @patch("tradingeconomics.calendar.fn.dataRequest")
    @patch("tradingeconomics.calendar.glob.apikey", "guest:guest")
    def test_getCalendarId_no_id(self, mock_request):
        getCalendarId(id=None)
        url = mock_request.call_args[1]["api_request"]
        self.assertEqual(
            url,
            "/calendar",
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
            "/calendar/country/united%20states",
        )

    @patch("tradingeconomics.calendar.fn.dataRequest")
    @patch("tradingeconomics.calendar.glob.apikey", "guest:guest")
    def test_country_and_category(self, mock_request):
        getCalendarData(country="united states", category="inflation rate")
        url = mock_request.call_args[1]["api_request"]
        self.assertEqual(
            url,
            "/calendar/country/united%20states/indicator/inflation%20rate",
        )

    @patch("tradingeconomics.calendar.fn.dataRequest")
    @patch("tradingeconomics.calendar.glob.apikey", "guest:guest")
    def test_ticker_only(self, mock_request):
        getCalendarData(ticker="IJCUSA")
        url = mock_request.call_args[1]["api_request"]
        self.assertEqual(
            url,
            "/calendar/ticker/IJCUSA",
        )

    @patch("tradingeconomics.calendar.fn.dataRequest")
    @patch("tradingeconomics.calendar.glob.apikey", "guest:guest")
    def test_event_without_country(self, mock_request):
        result = getCalendarData(event="GDP")
        self.assertEqual(result, "The parameter 'country' must be provided!")

    @patch("tradingeconomics.calendar.fn.dataRequest")
    @patch("tradingeconomics.calendar.glob.apikey", "guest:guest")
    def test_country_with_dates(self, mock_request):
        getCalendarData(
            country="united states", initDate="2020-01-01", endDate="2020-01-02"
        )
        url = mock_request.call_args[1]["api_request"]
        self.assertEqual(
            url,
            "/calendar/country/united%20states/2020-01-01/2020-01-02",
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
            "/calendar/events",
        )

    @patch("tradingeconomics.calendar.fn.dataRequest")
    @patch("tradingeconomics.calendar.glob.apikey", "guest:guest")
    def test_get_events_for_country(self, mock_request):
        getCalendarEvents(country="china")
        url = mock_request.call_args[1]["api_request"]
        self.assertEqual(
            url,
            "/calendar/events/country/china",
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
            "/calendar/group/bonds",
        )

    @patch("tradingeconomics.calendar.fn.dataRequest")
    @patch("tradingeconomics.calendar.glob.apikey", "guest:guest")
    def test_group_with_country(self, mock_request):
        getCalendarEventsByGroup(group="bonds", country="united states")
        url = mock_request.call_args[1]["api_request"]
        self.assertEqual(
            url,
            "/calendar/country/united%20states/group/bonds",
        )

    @patch("tradingeconomics.calendar.fn.dataRequest")
    @patch("tradingeconomics.calendar.glob.apikey", "guest:guest")
    def test_group_with_dates(self, mock_request):
        getCalendarEventsByGroup(
            group="inflation", initDate="2023-01-01", endDate="2023-02-01"
        )
        url = mock_request.call_args[1]["api_request"]
        self.assertEqual(
            url,
            "/calendar/group/inflation/2023-01-01/2023-02-01",
        )

    @patch("tradingeconomics.calendar.fn.dataRequest")
    @patch("tradingeconomics.calendar.glob.apikey", "guest:guest")
    def test_group_with_country_and_dates(self, mock_request):
        getCalendarEventsByGroup(
            group="inflation",
            country="china",
            initDate="2023-01-01",
            endDate="2023-02-01",
        )
        url = mock_request.call_args[1]["api_request"]
        self.assertEqual(
            url,
            "/calendar/country/china/group/inflation/2023-01-01/2023-02-01",
        )

    def test_group_empty_returns_error(self):
        result = getCalendarEventsByGroup(group=None)
        self.assertEqual(result, "Group cannot be empty")


class TestGetCalendarUpdates(unittest.TestCase):
    """Tests for getCalendarUpdates()."""

    @patch("tradingeconomics.calendar.fn.dataRequest")
    @patch("tradingeconomics.calendar.glob.apikey", "guest:guest")
    def test_get_calendar_updates(self, mock_request):
        from tradingeconomics.calendar import getCalendarUpdates

        getCalendarUpdates()
        url = mock_request.call_args[1]["api_request"]
        self.assertEqual(
            url,
            "/calendar/updates",
        )

    @patch("tradingeconomics.calendar.fn.dataRequest")
    @patch("tradingeconomics.calendar.glob.apikey", "guest:guest")
    def test_get_calendar_updates_with_output_type(self, mock_request):
        from tradingeconomics.calendar import getCalendarUpdates

        getCalendarUpdates(output_type="df")
        url = mock_request.call_args[1]["api_request"]
        output_type = mock_request.call_args[1]["output_type"]
        self.assertEqual(url, "/calendar/updates")
        self.assertEqual(output_type, "df")


class TestGetCalendarDataAdvanced(unittest.TestCase):
    """Advanced tests for getCalendarData() with importance, values, and events."""

    @patch("tradingeconomics.calendar.fn.dataRequest")
    @patch("tradingeconomics.calendar.glob.apikey", "guest:guest")
    def test_with_importance(self, mock_request):
        getCalendarData(country="united states", importance="2")
        url = mock_request.call_args[1]["api_request"]
        self.assertEqual(
            url,
            "/calendar/country/united%20states?importance=2",
        )

    @patch("tradingeconomics.calendar.fn.dataRequest")
    @patch("tradingeconomics.calendar.glob.apikey", "guest:guest")
    def test_with_importance_and_dates(self, mock_request):
        getCalendarData(
            country="united states",
            initDate="2023-01-01",
            endDate="2023-01-31",
            importance="3",
        )
        url = mock_request.call_args[1]["api_request"]
        self.assertEqual(
            url,
            "/calendar/country/united%20states/2023-01-01/2023-01-31?importance=3",
        )

    @patch("tradingeconomics.calendar.fn.dataRequest")
    @patch("tradingeconomics.calendar.glob.apikey", "guest:guest")
    def test_with_values_true(self, mock_request):
        getCalendarData(country="united states", values=True)
        url = mock_request.call_args[1]["api_request"]
        self.assertEqual(
            url,
            "/calendar/country/united%20states?values=true",
        )

    @patch("tradingeconomics.calendar.fn.dataRequest")
    @patch("tradingeconomics.calendar.glob.apikey", "guest:guest")
    def test_with_values_false(self, mock_request):
        getCalendarData(country="united states", values=False)
        url = mock_request.call_args[1]["api_request"]
        self.assertEqual(
            url,
            "/calendar/country/united%20states?values=false",
        )

    @patch("tradingeconomics.calendar.fn.dataRequest")
    @patch("tradingeconomics.calendar.glob.apikey", "guest:guest")
    def test_with_event_and_country(self, mock_request):
        getCalendarData(country="united states", event="GDP Growth Rate")
        url = mock_request.call_args[1]["api_request"]
        self.assertEqual(
            url,
            "/calendar/country/united%20states/event/GDP%20Growth%20Rate",
        )

    @patch("tradingeconomics.calendar.fn.dataRequest")
    @patch("tradingeconomics.calendar.glob.apikey", "guest:guest")
    def test_with_event_country_and_dates(self, mock_request):
        getCalendarData(
            country="united states",
            event="GDP Growth Rate",
            initDate="2023-01-01",
            endDate="2023-12-31",
        )
        url = mock_request.call_args[1]["api_request"]
        self.assertEqual(
            url,
            "/calendar/country/united%20states/event/GDP%20Growth%20Rate/2023-01-01/2023-12-31",
        )

    @patch("tradingeconomics.calendar.fn.dataRequest")
    @patch("tradingeconomics.calendar.glob.apikey", "guest:guest")
    def test_with_multiple_events(self, mock_request):
        getCalendarData(
            country="united states",
            event=["GDP Growth Rate", "Inflation Rate"],
        )
        url = mock_request.call_args[1]["api_request"]
        self.assertEqual(
            url,
            "/calendar/country/united%20states/event/GDP%20Growth%20Rate,Inflation%20Rate",
        )

    @patch("tradingeconomics.calendar.fn.dataRequest")
    @patch("tradingeconomics.calendar.glob.apikey", "guest:guest")
    def test_ticker_with_dates(self, mock_request):
        getCalendarData(ticker="IJCUSA", initDate="2023-01-01", endDate="2023-01-31")
        url = mock_request.call_args[1]["api_request"]
        self.assertEqual(
            url,
            "/calendar/ticker/IJCUSA/2023-01-01/2023-01-31",
        )

    @patch("tradingeconomics.calendar.fn.dataRequest")
    @patch("tradingeconomics.calendar.glob.apikey", "guest:guest")
    def test_ticker_with_multiple_tickers(self, mock_request):
        getCalendarData(ticker=["IJCUSA", "SPAINFACORD"])
        url = mock_request.call_args[1]["api_request"]
        self.assertEqual(
            url,
            "/calendar/ticker/IJCUSA,SPAINFACORD",
        )

    @patch("tradingeconomics.calendar.fn.dataRequest")
    @patch("tradingeconomics.calendar.glob.apikey", "guest:guest")
    def test_dates_only_fallback_to_all(self, mock_request):
        getCalendarData(initDate="2023-01-01", endDate="2023-01-31")
        url = mock_request.call_args[1]["api_request"]
        self.assertEqual(
            url,
            "/calendar/country/all/2023-01-01/2023-01-31",
        )

    @patch("tradingeconomics.calendar.fn.dataRequest")
    @patch("tradingeconomics.calendar.glob.apikey", "guest:guest")
    def test_multiple_countries_and_categories(self, mock_request):
        getCalendarData(
            country=["united states", "china"],
            category=["gdp", "inflation rate"],
        )
        url = mock_request.call_args[1]["api_request"]
        self.assertEqual(
            url,
            "/calendar/country/united%20states,china/indicator/gdp,inflation%20rate",
        )

    @patch("tradingeconomics.calendar.fn.dataRequest")
    @patch("tradingeconomics.calendar.glob.apikey", "guest:guest")
    def test_category_with_importance(self, mock_request):
        getCalendarData(category="inflation rate", importance="2")
        url = mock_request.call_args[1]["api_request"]
        self.assertEqual(
            url,
            "/calendar/indicator/inflation%20rate?importance=2",
        )

    @patch("tradingeconomics.calendar.fn.dataRequest")
    @patch("tradingeconomics.calendar.glob.apikey", "guest:guest")
    def test_combined_importance_and_values(self, mock_request):
        getCalendarData(country="united states", importance="2", values=True)
        url = mock_request.call_args[1]["api_request"]
        self.assertEqual(
            url,
            "/calendar/country/united%20states?importance=2&values=true",
        )


if __name__ == "__main__":
    unittest.main()
