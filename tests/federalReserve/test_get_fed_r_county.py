import unittest
from unittest.mock import patch
from tradingeconomics.federalReserve import getFedRCounty
from tradingeconomics import glob


class TestGetFedRCounty(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.federalReserve.fn.dataRequest", return_value={"state": "ok"}
    )
    def test_county_by_state(self, mock_request):
        # Get counties for a state
        result = getFedRCounty(state="nevada")

        expected_url = (
            "https://api.tradingeconomics.com/fred/snapshot/county/nevada?c=TESTKEY"
        )

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"state": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.federalReserve.fn.dataRequest", return_value={"county": "ok"}
    )
    def test_county_by_name(self, mock_request):
        # Get specific county data
        result = getFedRCounty(county="Pike County, AR")

        expected_url = "https://api.tradingeconomics.com/fred/snapshot/county/Pike%20County%2C%20AR?c=TESTKEY"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"county": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.federalReserve.fn.dataRequest", return_value={"both": "ok"}
    )
    def test_county_with_state_and_county(self, mock_request):
        # Get county data with both state and county parameters
        result = getFedRCounty(state="arkansas", county="Pike County")

        expected_url = "https://api.tradingeconomics.com/fred/snapshot/county/arkansasPike%20County?c=TESTKEY"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"both": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.federalReserve.fn.dataRequest",
        return_value=[{"county": "Pike County"}],
    )
    def test_county_with_output_type(self, mock_request):
        # Test with output_type parameter
        result = getFedRCounty(county="Pike County, AR", output_type="df")

        expected_url = "https://api.tradingeconomics.com/fred/snapshot/county/Pike%20County%2C%20AR?c=TESTKEY"

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, [{"county": "Pike County"}])
