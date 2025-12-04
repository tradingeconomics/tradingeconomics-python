import unittest
from unittest.mock import patch
from tradingeconomics.federalReserve import getFedRStates
from tradingeconomics import glob


class TestGetFedRStates(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.federalReserve.fn.dataRequest", return_value={"states": "ok"}
    )
    def test_get_states_no_parameters(self, mock_request):
        # Get all states with no parameters
        result = getFedRStates()

        expected_url = "https://api.tradingeconomics.com/fred/states"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"states": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.federalReserve.fn.dataRequest",
        return_value={"counties": "ok"},
    )
    def test_get_states_with_county(self, mock_request):
        # Get counties for a specific state
        result = getFedRStates(county="arkansas")

        expected_url = (
            "https://api.tradingeconomics.com/fred/counties/arkansas"
        )

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"counties": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.federalReserve.fn.dataRequest",
        return_value=[{"state": "Arkansas"}],
    )
    def test_get_states_with_output_type(self, mock_request):
        # Test with output_type parameter
        result = getFedRStates(output_type="df")

        expected_url = "https://api.tradingeconomics.com/fred/states"

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, [{"state": "Arkansas"}])
