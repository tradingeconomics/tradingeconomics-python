import unittest
from unittest.mock import patch
from tradingeconomics.markets import getMarketsComponents
from tradingeconomics import glob


class TestGetMarketsComponents(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.markets.fn.dataRequest", return_value={"components": "ok"})
    def test_get_markets_components_single(self, mock_request):
        # Get components for single index
        result = getMarketsComponents(symbols="psi20:ind")

        expected_url = (
            "https://api.tradingeconomics.com/markets/components/psi20%3Aind"
        )

        mock_request.assert_called_once_with(expected_url, None)
        self.assertEqual(result, {"components": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.markets.fn.dataRequest",
        return_value={"components": "multiple"},
    )
    def test_get_markets_components_multiple(self, mock_request):
        # Get components for multiple indexes
        result = getMarketsComponents(symbols=["psi20:ind", "indu:ind"])

        expected_url = "https://api.tradingeconomics.com/markets/components/psi20%3Aind%2Cindu%3Aind"

        mock_request.assert_called_once_with(expected_url, None)
        self.assertEqual(result, {"components": "multiple"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.markets.fn.dataRequest", return_value={"components": "raw"}
    )
    def test_get_markets_components_with_output_type(self, mock_request):
        # Get components with output type
        result = getMarketsComponents(
            symbols=["psi20:ind", "indu:ind"], output_type="raw"
        )

        expected_url = "https://api.tradingeconomics.com/markets/components/psi20%3Aind%2Cindu%3Aind"

        mock_request.assert_called_once_with(expected_url, "raw")
        self.assertEqual(result, {"components": "raw"})
