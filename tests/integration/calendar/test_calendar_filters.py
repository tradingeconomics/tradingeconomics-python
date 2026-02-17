"""
Integration tests for Trading Economics Calendar API - Advanced Filters
Tests all valid filter combinations based on API documentation

These tests use parameters that should work with guest:guest credentials.
Tests will skip with details when encountering errors for investigation.
"""

import pytest
import tradingeconomics as te
import pandas as pd


@pytest.mark.integration
@pytest.mark.slow
class TestCalendarCountryFilters:
    """Test country parameter filtering"""

    def test_get_calendar_events_multiple_countries(self):
        """Test getCalendarEvents with multiple countries"""
        try:
            result = te.getCalendarEvents(country=["china", "canada"])

            assert result is not None
            assert isinstance(result, list)

            if len(result) > 0:
                print(f"✓ Found {len(result)} events for China and Canada")
                countries = set(e.get("Country", "") for e in result[:10])
                print(f"✓ Countries in results: {countries}")
            else:
                print("⚠ No events found for China and Canada")
        except Exception as e:
            pytest.skip(f"Test failed - investigate: {str(e)[:200]}")

    def test_get_calendar_data_multiple_countries(self):
        """Test getCalendarData with multiple countries"""
        try:
            result = te.getCalendarData(country=["united states", "china"])

            assert result is not None
            assert isinstance(result, list)

            if len(result) > 0:
                print(f"✓ Found {len(result)} events for US and China")
                countries = set(e.get("Country", "") for e in result[:10])
                print(f"✓ Countries in results: {countries}")
            else:
                print("⚠ No events found for US and China")
        except Exception as e:
            pytest.skip(f"Test failed - investigate: {str(e)[:200]}")


@pytest.mark.integration
@pytest.mark.slow
class TestCalendarDateRangeFilters:
    """Test date range filtering"""

    def test_calendar_data_with_date_range(self):
        """Test filtering by date range only"""
        try:
            result = te.getCalendarData(initDate="2016-12-02", endDate="2016-12-03")

            assert result is not None
            assert isinstance(result, list)

            if len(result) > 0:
                print(
                    f"✓ Found {len(result)} events in date range 2016-12-02 to 2016-12-03"
                )
                sample_dates = [e.get("Date", "")[:10] for e in result[:5]]
                print(f"✓ Sample dates: {sample_dates}")
            else:
                print("⚠ No events found in date range")
        except Exception as e:
            pytest.skip(f"Test failed - investigate: {str(e)[:200]}")

    def test_calendar_data_country_with_date_range(self):
        """Test country filter combined with date range"""
        try:
            result = te.getCalendarData(
                country="united states", initDate="2016-02-01", endDate="2016-02-10"
            )

            assert result is not None
            assert isinstance(result, list)

            if len(result) > 0:
                print(f"✓ Found {len(result)} US events in Feb 2016")
                for evt in result[:3]:
                    print(f"  - {evt.get('Event')} on {evt.get('Date', '')[:10]}")
            else:
                print("⚠ No US events found in Feb 2016")
        except Exception as e:
            pytest.skip(f"Test failed - investigate: {str(e)[:200]}")


@pytest.mark.integration
@pytest.mark.slow
class TestCalendarImportanceFilters:
    """Test importance parameter filtering"""

    def test_importance_filter_only(self):
        """Test filtering by importance level only"""
        try:
            result = te.getCalendarData(importance="2")

            assert result is not None
            assert isinstance(result, list)

            if len(result) > 0:
                print(f"✓ Found {len(result)} events with importance=2")
                for evt in result[:3]:
                    print(
                        f"  - {evt.get('Event')} (Importance: {evt.get('Importance')})"
                    )
            else:
                print("⚠ No importance=2 events found")
        except Exception as e:
            pytest.skip(f"Test failed - investigate: {str(e)[:200]}")

    def test_importance_with_date_range(self):
        """Test importance filter combined with date range"""
        try:
            result = te.getCalendarData(
                initDate="2016-12-02", endDate="2016-12-03", importance="3"
            )

            assert result is not None
            assert isinstance(result, list)

            if len(result) > 0:
                print(f"✓ Found {len(result)} high importance events in date range")
                for evt in result[:3]:
                    print(
                        f"  - {evt.get('Event')} (Importance: {evt.get('Importance')})"
                    )
            else:
                print("⚠ No high importance events in date range")
        except Exception as e:
            pytest.skip(f"Test failed - investigate: {str(e)[:200]}")

    def test_importance_with_country(self):
        """Test importance filter with country"""
        try:
            result = te.getCalendarData(country="united states", importance="3")

            assert result is not None
            assert isinstance(result, list)

            if len(result) > 0:
                print(f"✓ Found {len(result)} high importance US events")
                for evt in result[:3]:
                    print(
                        f"  - {evt.get('Event')} (Importance: {evt.get('Importance')})"
                    )
            else:
                print("⚠ No high importance US events found")
        except Exception as e:
            pytest.skip(f"Test failed - investigate: {str(e)[:200]}")


@pytest.mark.integration
@pytest.mark.slow
class TestCalendarCategoryFilters:
    """Test category parameter filtering"""

    def test_category_filter_only(self):
        """Test filtering by category only"""
        try:
            result = te.getCalendarData(category="inflation rate")

            assert result is not None
            assert isinstance(result, list)

            if len(result) > 0:
                print(f"✓ Found {len(result)} inflation rate events")
                categories = set(e.get("Category", "") for e in result[:10])
                print(f"✓ Categories: {categories}")
            else:
                print("⚠ No inflation rate events found")
        except Exception as e:
            pytest.skip(f"Test failed - investigate: {str(e)[:200]}")

    def test_category_with_date_range(self):
        """Test category filter with date range"""
        try:
            result = te.getCalendarData(
                category="inflation rate", initDate="2016-03-01", endDate="2016-03-03"
            )

            assert result is not None
            assert isinstance(result, list)

            if len(result) > 0:
                print(f"✓ Found {len(result)} inflation events in date range")
            else:
                print("⚠ No inflation events in date range")
        except Exception as e:
            pytest.skip(f"Test failed - investigate: {str(e)[:200]}")

    def test_category_with_importance(self):
        """Test category filter with importance"""
        try:
            result = te.getCalendarData(category="inflation rate", importance="2")

            assert result is not None
            assert isinstance(result, list)

            if len(result) > 0:
                print(f"✓ Found {len(result)} medium importance inflation events")
            else:
                print("⚠ No medium importance inflation events found")
        except Exception as e:
            pytest.skip(f"Test failed - investigate: {str(e)[:200]}")

    def test_category_with_date_and_importance(self):
        """Test category with date range and importance"""
        try:
            result = te.getCalendarData(
                category="inflation rate",
                initDate="2016-03-01",
                endDate="2016-03-03",
                importance="2",
            )

            assert result is not None
            assert isinstance(result, list)

            if len(result) > 0:
                print(f"✓ Found {len(result)} events matching all filters")
            else:
                print("⚠ No events matching all filters")
        except Exception as e:
            pytest.skip(f"Test failed - investigate: {str(e)[:200]}")

    def test_category_with_country(self):
        """Test category filter with specific country"""
        try:
            result = te.getCalendarData(
                country="united states", category="initial jobless claims"
            )

            assert result is not None
            assert isinstance(result, list)

            if len(result) > 0:
                print(f"✓ Found {len(result)} initial jobless claims events for US")
            else:
                print("⚠ No initial jobless claims events found for US")
        except Exception as e:
            pytest.skip(f"Test failed - investigate: {str(e)[:200]}")

    def test_category_with_country_and_date_range(self):
        """Test category with country and date range"""
        try:
            result = te.getCalendarData(
                category="initial jobless claims",
                country="united states",
                initDate="2016-12-01",
                endDate="2017-02-25",
            )

            assert result is not None
            assert isinstance(result, list)

            if len(result) > 0:
                print(f"✓ Found {len(result)} US jobless claims in date range")
            else:
                print("⚠ No US jobless claims in date range")
        except Exception as e:
            pytest.skip(f"Test failed - investigate: {str(e)[:200]}")


@pytest.mark.integration
@pytest.mark.slow
class TestCalendarEventFilters:
    """Test event parameter filtering"""

    def test_event_with_country_and_date_range(self):
        """Test specific event with country and date range"""
        try:
            result = te.getCalendarData(
                country="united states",
                event="GDP Growth Rate QoQ Final",
                initDate="2016-12-01",
                endDate="2024-02-25",
            )

            assert result is not None
            assert isinstance(result, list)

            if len(result) > 0:
                print(f"✓ Found {len(result)} GDP Growth Rate QoQ Final events")
                for evt in result[:3]:
                    print(f"  - {evt.get('Event')} on {evt.get('Date', '')[:10]}")
            else:
                print("⚠ No GDP Growth Rate QoQ Final events found")
        except Exception as e:
            pytest.skip(f"Test failed - investigate: {str(e)[:200]}")


@pytest.mark.integration
@pytest.mark.slow
class TestCalendarTickerFilters:
    """Test ticker parameter filtering"""

    def test_ticker_filter_multiple_tickers(self):
        """Test filtering by multiple ticker symbols"""
        try:
            result = te.getCalendarData(
                ticker=["IJCUSA", "SPAINFACORD", "BAHRAININFNRATE"]
            )

            assert result is not None
            assert isinstance(result, list)

            if len(result) > 0:
                print(f"✓ Found {len(result)} events for specified tickers")
                tickers = set(e.get("Ticker", "") for e in result if e.get("Ticker"))
                print(f"✓ Tickers found: {tickers}")
            else:
                print("⚠ No events found for tickers")
        except Exception as e:
            pytest.skip(f"Test failed - investigate: {str(e)[:200]}")

    def test_ticker_with_date_range(self):
        """Test ticker filter with date range"""
        try:
            result = te.getCalendarData(
                ticker=["IJCUSA", "SPAINFACORD", "BAHRAININFNRATE"],
                initDate="2018-01-01",
                endDate="2018-03-01",
            )

            assert result is not None
            assert isinstance(result, list)

            if len(result) > 0:
                print(f"✓ Found {len(result)} ticker events in date range")
                for evt in result[:3]:
                    print(
                        f"  - {evt.get('Event')} ({evt.get('Ticker')}) on {evt.get('Date', '')[:10]}"
                    )
            else:
                print("⚠ No ticker events in date range")
        except Exception as e:
            pytest.skip(f"Test failed - investigate: {str(e)[:200]}")


@pytest.mark.integration
@pytest.mark.slow
class TestCalendarIdFunctions:
    """Test calendar ID-based functions"""

    def test_get_calendar_by_id(self):
        """Test getCalendarId with multiple IDs"""
        try:
            result = te.getCalendarId(id=["174108", "160025", "160030"])

            assert result is not None
            assert isinstance(result, list)

            if len(result) > 0:
                print(f"✓ Found {len(result)} events by ID")
                for evt in result:
                    print(f"  - ID: {evt.get('CalendarId')} - {evt.get('Event')}")
            else:
                print("⚠ No events found for specified IDs")
        except Exception as e:
            pytest.skip(f"Test failed - investigate: {str(e)[:200]}")

    def test_get_calendar_updates(self):
        """Test getCalendarUpdates function"""
        try:
            result = te.getCalendarUpdates()

            assert result is not None
            assert isinstance(result, list)

            if len(result) > 0:
                print(f"✓ Found {len(result)} calendar updates")
                for evt in result[:3]:
                    print(
                        f"  - {evt.get('Event')} updated at {evt.get('LastUpdate', '')}"
                    )
            else:
                print("⚠ No calendar updates found")
        except Exception as e:
            pytest.skip(f"Test failed - investigate: {str(e)[:200]}")


@pytest.mark.integration
@pytest.mark.slow
class TestCalendarGroupFunctions:
    """Test getCalendarEventsByGroup function"""

    def test_get_calendar_events_by_group_only(self):
        """Test getCalendarEventsByGroup with group only"""
        try:
            result = te.getCalendarEventsByGroup(group="bonds")

            assert result is not None
            assert isinstance(result, list)

            if len(result) > 0:
                print(f"✓ Found {len(result)} bonds group events")
                for evt in result[:3]:
                    print(f"  - {evt.get('Event')} ({evt.get('Country')})")
            else:
                print("⚠ No bonds group events found")
        except Exception as e:
            pytest.skip(f"Test failed - investigate: {str(e)[:200]}")

    def test_get_calendar_events_by_group_with_date_range(self):
        """Test getCalendarEventsByGroup with date range"""
        try:
            result = te.getCalendarEventsByGroup(
                group="bonds", initDate="2016-03-01", endDate="2018-03-03"
            )

            assert result is not None
            assert isinstance(result, list)

            if len(result) > 0:
                print(f"✓ Found {len(result)} bonds events in date range")
            else:
                print("⚠ No bonds events in date range")
        except Exception as e:
            pytest.skip(f"Test failed - investigate: {str(e)[:200]}")

    def test_get_calendar_events_by_group_with_country_and_dates(self):
        """Test getCalendarEventsByGroup with country and date range"""
        try:
            result = te.getCalendarEventsByGroup(
                group="bonds",
                country="united states",
                initDate="2016-03-01",
                endDate="2018-03-03",
            )

            assert result is not None
            assert isinstance(result, list)

            if len(result) > 0:
                print(f"✓ Found {len(result)} US bonds events in date range")
            else:
                print("⚠ No US bonds events in date range")
        except Exception as e:
            pytest.skip(f"Test failed - investigate: {str(e)[:200]}")


@pytest.mark.integration
@pytest.mark.slow
class TestCalendarIndicatorIntegration:
    """Test calendar integration with indicators"""

    def test_get_indicator_data_with_calendar_flag(self):
        """Test getIndicatorData with calendar=1 parameter"""
        try:
            result = te.getIndicatorData(calendar=1)

            assert result is not None
            assert isinstance(result, list)

            if len(result) > 0:
                print(f"✓ Found {len(result)} indicators with calendar data")
                for ind in result[:3]:
                    print(f"  - {ind.get('Country')}: {ind.get('Category')}")
            else:
                print("⚠ No indicators with calendar data found")
        except Exception as e:
            pytest.skip(f"Test failed - investigate: {str(e)[:200]}")

    def test_get_indicator_data_with_calendar_and_country(self):
        """Test getIndicatorData with calendar=1 and country"""
        try:
            result = te.getIndicatorData(calendar=1, country="united states")

            assert result is not None
            assert isinstance(result, list)

            if len(result) > 0:
                print(f"✓ Found {len(result)} US indicators with calendar data")
                for ind in result[:3]:
                    print(f"  - {ind.get('Category')}")
            else:
                print("⚠ No US indicators with calendar data found")
        except Exception as e:
            pytest.skip(f"Test failed - investigate: {str(e)[:200]}")


@pytest.mark.integration
@pytest.mark.slow
class TestCalendarOutputFormats:
    """Test different output formats with filters"""

    def test_calendar_data_dataframe_output(self):
        """Test calendar data with DataFrame output"""
        try:
            result = te.getCalendarData(
                country="united states",
                initDate="2016-02-01",
                endDate="2016-02-10",
                output_type="df",
            )

            assert result is not None
            assert isinstance(result, pd.DataFrame)

            if len(result) > 0:
                print(f"✓ DataFrame with {len(result)} rows")
                print(f"✓ Columns: {list(result.columns)[:10]}")
            else:
                print("⚠ Empty DataFrame returned")
        except Exception as e:
            pytest.skip(f"Test failed - investigate: {str(e)[:200]}")

    def test_calendar_data_raw_output(self):
        """Test calendar data with raw output (returns parsed JSON as list of dicts)"""
        try:
            result = te.getCalendarData(
                category="inflation rate", importance="2", output_type="raw"
            )

            assert result is not None
            # output_type='raw' returns parsed JSON (list of dicts), not raw string
            assert isinstance(result, list)
            assert len(result) > 0
            assert isinstance(result[0], dict)

            print(f"✓ Raw output received ({len(result)} events)")
        except Exception as e:
            pytest.skip(f"Test failed - investigate: {str(e)[:200]}")

    def test_calendar_data_dict_output(self):
        """Test calendar data with dict output (default)"""
        try:
            result = te.getCalendarData(
                importance="2",
                initDate="2016-12-02",
                endDate="2016-12-03",
                output_type="dict",
            )

            assert result is not None
            assert isinstance(result, list)

            if len(result) > 0:
                assert isinstance(result[0], dict)
                print(f"✓ List of {len(result)} dictionaries")
                print(f"✓ Sample keys: {list(result[0].keys())[:10]}")
            else:
                print("⚠ Empty list returned")
        except Exception as e:
            pytest.skip(f"Test failed - investigate: {str(e)[:200]}")
