import unittest
from unittest.mock import patch
from tradingeconomics.indicators import getIndicatorChanges
from tradingeconomics import glob


class TestGetIndicatorChanges(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.indicators.fn.dataRequest", return_value={"changes": "all"}
    )
    def test_get_indicator_changes_no_parameters(self, mock_request):
        # Get all indicator changes
        result = getIndicatorChanges()

        expected_url = "/changes"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"changes": "all"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.indicators.fn.dataRequest",
        return_value={"changes": "filtered"},
    )
    def test_get_indicator_changes_with_start_date(self, mock_request):
        # Get indicator changes from start date
        result = getIndicatorChanges(start_date="2024-10-01")

        expected_url = "/changes/2024-10-01"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"changes": "filtered"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.indicators.fn.dataRequest", return_value={"changes": "df"})
    def test_get_indicator_changes_with_output_type(self, mock_request):
        # Get indicator changes with output type
        result = getIndicatorChanges(start_date="2024-10-01", output_type="df")

        expected_url = "/changes/2024-10-01"

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, {"changes": "df"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.indicators.fn.dataRequest",
        return_value={"raw": "json", "changes": "data"},
    )
    def test_get_indicator_changes_with_output_type_raw(self, mock_request):
        # Test with output_type='raw'
        result = getIndicatorChanges(start_date="2024-10-01", output_type="raw")

        expected_url = "/changes/2024-10-01"

        mock_request.assert_called_once_with(
            api_request=expected_url, output_type="raw"
        )
        self.assertEqual(result, {"raw": "json", "changes": "data"})
