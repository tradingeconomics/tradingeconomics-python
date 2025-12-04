import unittest
from unittest.mock import patch
from tradingeconomics.indicators import getCreditRatingsUpdates
from tradingeconomics import glob


class TestGetCreditRatingsUpdates(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.indicators.fn.dataRequest", return_value={"updates": "ok"})
    def test_get_credit_ratings_updates(self, mock_request):
        # Get credit ratings updates
        result = getCreditRatingsUpdates()

        expected_url = (
            "https://api.tradingeconomics.com/credit-ratings/updates?c=TESTKEY"
        )

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"updates": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.indicators.fn.dataRequest", return_value={"updates": "df"})
    def test_get_credit_ratings_updates_with_output_type(self, mock_request):
        # Get credit ratings updates with output type
        result = getCreditRatingsUpdates(output_type="df")

        expected_url = (
            "https://api.tradingeconomics.com/credit-ratings/updates?c=TESTKEY"
        )

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, {"updates": "df"})
