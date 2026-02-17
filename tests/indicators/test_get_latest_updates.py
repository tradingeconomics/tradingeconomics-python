import unittest
from unittest.mock import patch
from tradingeconomics.indicators import getLatestUpdates
from tradingeconomics import glob


class TestGetLatestUpdates(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.indicators.fn.dataRequest", return_value={"updates": "all"}
    )
    def test_get_latest_updates_no_parameters(self, mock_request):
        # Get all latest updates
        result = getLatestUpdates()

        expected_url = "/updates"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"updates": "all"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.indicators.fn.dataRequest",
        return_value={"updates": "country"},
    )
    def test_get_latest_updates_by_country(self, mock_request):
        # Get latest updates by country
        result = getLatestUpdates(country="united states")

        expected_url = "/updates/country/united%20states"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"updates": "country"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.indicators.fn.validate", return_value="%Y-%m-%d")
    @patch(
        "tradingeconomics.indicators.fn.dataRequest", return_value={"updates": "date"}
    )
    def test_get_latest_updates_by_init_date(self, mock_request, mock_validate):
        # Get latest updates by init date
        result = getLatestUpdates(init_date="2021-06-01")

        expected_url = "/updates/2021-06-01"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"updates": "date"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.indicators.fn.validate", return_value="%Y-%m-%d")
    @patch(
        "tradingeconomics.indicators.fn.dataRequest",
        return_value={"updates": "country_date"},
    )
    def test_get_latest_updates_by_country_and_date(self, mock_request, mock_validate):
        # Get latest updates by country and init date
        result = getLatestUpdates(country="united states", init_date="2021-06-01")

        expected_url = "/updates/country/united%20states/2021-06-01"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"updates": "country_date"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.indicators.fn.validate", return_value="%Y-%m-%d")
    @patch("tradingeconomics.indicators.fn.timeValidate", return_value="%H:%M")
    @patch(
        "tradingeconomics.indicators.fn.dataRequest", return_value={"updates": "time"}
    )
    def test_get_latest_updates_with_time(
        self, mock_request, mock_time_validate, mock_validate
    ):
        # Get latest updates by date and time
        result = getLatestUpdates(init_date="2021-10-18", time="15:20")

        expected_url = "/updates/2021-10-18?time=15:20"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"updates": "time"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.indicators.fn.validate", return_value="%Y-%m-%d")
    @patch(
        "tradingeconomics.indicators.fn.dataRequest",
        return_value={"updates": "multiple"},
    )
    def test_get_latest_updates_multiple_countries(self, mock_request, mock_validate):
        # Get latest updates by multiple countries and date
        result = getLatestUpdates(
            country=["united states", "portugal"], init_date="2021-06-01"
        )

        expected_url = "/updates/country/united%20states,portugal/2021-06-01"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"updates": "multiple"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.indicators.fn.dataRequest",
        return_value={"raw": "json", "updates": "data"},
    )
    def test_get_latest_updates_with_output_type_raw(self, mock_request):
        # Test with output_type='raw'
        result = getLatestUpdates(country="united states", output_type="raw")

        expected_url = "/updates/country/united%20states"

        mock_request.assert_called_once_with(
            api_request=expected_url, output_type="raw"
        )
        self.assertEqual(result, {"raw": "json", "updates": "data"})
