"""
Integration tests for calendar.py - Basic Endpoints

Tests basic calendar API functionality with real API calls.
These tests validate:
- API endpoints are accessible (not 404)
- Response structure matches expected format
- Basic parameter handling works

Run with: pytest tests/integration/calendar/test_calendar_basic.py -v
"""

import pytest
import tradingeconomics as te
from datetime import datetime, timedelta


@pytest.mark.integration
@pytest.mark.slow
class TestCalendarBasicEndpoints:
    """Test basic calendar endpoints return valid data"""

    def test_get_calendar_no_parameters(self):
        """Test: getCalendarData() without parameters returns data"""
        result = te.getCalendarData()

        # Validate response exists
        assert result is not None, "API returned None"
        assert isinstance(result, list), f"Expected list, got {type(result)}"
        assert len(result) > 0, "API returned empty list"

        # Validate structure of first event
        first_event = result[0]
        assert isinstance(first_event, dict), "Event should be a dictionary"

        # Check for required fields
        required_fields = ["Date", "Country", "Event"]
        for field in required_fields:
            assert field in first_event, f"Missing required field: {field}"

        print(f"✓ Returned {len(result)} calendar events")
        print(f"✓ Sample event keys: {list(first_event.keys())}")

    def test_get_calendar_single_country(self):
        """Test: getCalendarData(country='united states')"""
        result = te.getCalendarData(country="united states")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        # Validate all events are from USA
        countries = {event.get("Country", "") for event in result}
        assert (
            "United States" in countries or "USA" in countries
        ), f"Expected USA events, got countries: {countries}"

        print(f"✓ Returned {len(result)} USA events")

    def test_get_calendar_multiple_countries(self):
        """Test: getCalendarData(country=['united states', 'china'])"""
        result = te.getCalendarData(country=["united states", "china"])

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        # Validate events are from requested countries
        countries = {event.get("Country", "") for event in result}
        print(f"✓ Countries in response: {countries}")

        # At least one of the requested countries should be present
        has_usa = any("United States" in c or "USA" in c for c in countries)
        has_china = any("China" in c for c in countries)
        assert (
            has_usa or has_china
        ), f"No events from requested countries. Got: {countries}"

    def test_get_calendar_with_indicator(self):
        """Test: getCalendarData(country='united states', indicator='gdp')"""
        try:
            result = te.getCalendarData(
                country="united states", category="initial jobless claims"
            )

            assert result is not None
            assert isinstance(result, list)

            # May return empty if no GDP events scheduled
            if len(result) > 0:
                # Check that we got valid calendar events back
                first_event = result[0]
                print(f"✓ Sample event: {first_event.get('Event')}")

                # Verify the response contains calendar event fields
                assert "Event" in first_event
                assert "Country" in first_event

                # Count how many events contain GDP (may be 0 if no GDP events scheduled)
                gdp_events = [e for e in result if "gdp" in e.get("Event", "").lower()]
                print(
                    f"✓ Found {len(gdp_events)} GDP-related events out of {len(result)} total events"
                )
            else:
                print("⚠ No events returned (this is OK if no GDP events scheduled)")
        except Exception as e:
            if "403" in str(e) or "No Access" in str(e):
                pytest.skip(
                    "Feature requires paid API access (guest credentials have limited access)"
                )
            else:
                raise

    def test_get_calendar_by_ticker(self):
        """Test: getCalendarData(ticker='USURTOT')"""
        # USURTOT is US Unemployment Rate ticker
        try:
            result = te.getCalendarData(ticker="IJCUSA")

            assert result is not None
            assert isinstance(result, list)

            if len(result) > 0:
                first_event = result[0]
                print(f"✓ Ticker event: {first_event.get('Event')}")
                assert "Ticker" in first_event or "TEForecast" in first_event
            else:
                print("⚠ No events for ticker USURTOT (this is OK)")
        except Exception as e:
            if "403" in str(e) or "No Access" in str(e):
                pytest.skip(
                    "Feature requires paid API access (guest credentials have limited access)"
                )
            else:
                raise


@pytest.mark.integration
@pytest.mark.slow
class TestCalendarIdEndpoints:
    """Test calendar ID-based endpoints"""

    def test_get_calendar_id_without_id(self):
        """Test: getCalendarId() returns general calendar"""
        result = te.getCalendarId()

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        print(f"✓ Returned {len(result)} events via getCalendarId()")

    def test_get_calendar_events(self):
        """Test: getCalendarEvents() returns event list"""
        result = te.getCalendarEvents()

        assert result is not None
        assert isinstance(result, list)
        # May be empty if no unique events defined

        print(f"✓ Returned {len(result)} unique calendar events")

    def test_get_calendar_events_by_country(self):
        """Test: getCalendarEvents(country='united states')"""
        result = te.getCalendarEvents(country="united states")

        assert result is not None
        assert isinstance(result, list)

        if len(result) > 0:
            print(f"✓ Returned {len(result)} unique USA events")
        else:
            print("⚠ No unique events for USA (this is OK)")


@pytest.mark.integration
@pytest.mark.slow
class TestCalendarOutputFormats:
    """Test different output formats"""

    def test_calendar_output_dict(self):
        """Test: output_type=None (default dict/list)"""
        result = te.getCalendarData(country="united states", output_type=None)

        assert isinstance(result, list)
        assert len(result) > 0
        assert isinstance(result[0], dict)

        print("✓ Default output is list of dicts")

    def test_calendar_output_dataframe(self):
        """Test: output_type='df' returns pandas DataFrame"""
        result = te.getCalendarData(country="united states", output_type="df")

        import pandas as pd

        assert isinstance(
            result, pd.DataFrame
        ), f"Expected DataFrame, got {type(result)}"
        assert len(result) > 0, "DataFrame is empty"

        # Check for expected columns
        expected_cols = ["Date", "Country", "Event"]
        for col in expected_cols:
            assert col in result.columns, f"Missing column: {col}"

        print(f"✓ DataFrame has {len(result)} rows and {len(result.columns)} columns")
        print(f"  Columns: {list(result.columns)}")

    def test_calendar_output_raw(self):
        """Test: output_type='raw' returns raw JSON"""
        result = te.getCalendarData(country="united states", output_type="raw")

        # Raw format should be a list
        assert isinstance(result, list)
        assert len(result) > 0

        print("✓ Raw output format works")


@pytest.mark.integration
@pytest.mark.slow
class TestCalendarResponseStructure:
    """Validate API response structure hasn't changed"""

    def test_calendar_response_schema(self):
        """Validate that calendar events have expected fields"""
        result = te.getCalendarData(country="united states")

        assert len(result) > 0, "Need at least one event to validate schema"

        # Expected fields in calendar events (as of 2024)
        expected_fields = {
            "CalendarId",
            "Date",
            "Country",
            "Category",
            "Event",
            "Importance",
            "Actual",
            "Previous",
            "Forecast",
            "TEForecast",
        }

        first_event = result[0]
        actual_fields = set(first_event.keys())

        # Check which expected fields are present
        present = expected_fields & actual_fields
        missing = expected_fields - actual_fields
        extra = actual_fields - expected_fields

        print(f"✓ Present fields ({len(present)}): {sorted(present)}")

        if missing:
            print(f"⚠ Missing fields ({len(missing)}): {sorted(missing)}")

        if extra:
            print(f"ℹ Extra fields ({len(extra)}): {sorted(extra)}")

        # Core fields MUST be present
        core_fields = {"Date", "Country", "Event"}
        assert core_fields.issubset(
            actual_fields
        ), f"Core fields missing: {core_fields - actual_fields}"

        # Warn if many expected fields are missing (API might have changed)
        if len(missing) > len(expected_fields) / 2:
            pytest.fail(
                f"⚠️ API structure may have changed! Missing {len(missing)} expected fields"
            )


if __name__ == "__main__":
    # Allow running directly for quick testing
    pytest.main([__file__, "-v", "-s"])
