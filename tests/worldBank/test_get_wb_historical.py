import unittest
from unittest.mock import patch
from tradingeconomics.worldBank import getWBHistorical
from tradingeconomics import glob


class TestGetWBHistorical(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.worldBank.fn.dataRequest", return_value={"historical": "data"}
    )
    def test_get_wb_historical_with_series_code(self, mock_request):
        # Get historical data by series code
        result = getWBHistorical(series_code="usa.fr.inr.rinr")

        expected_url = "https://api.tradingeconomics.com/worldBank/historical?s=usa.fr.inr.rinr"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"historical": "data"})

    def test_get_wb_historical_no_parameters(self):
        # Test that error message is returned when no series code provided
        result = getWBHistorical()

        self.assertEqual(result, "A series code is required!")

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.worldBank.fn.dataRequest", return_value="df_output")
    def test_get_wb_historical_with_output_type(self, mock_request):
        # Get historical data with DataFrame output type
        result = getWBHistorical(series_code="usa.fr.inr.rinr", output_type="df")

        expected_url = "https://api.tradingeconomics.com/worldBank/historical?s=usa.fr.inr.rinr"

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, "df_output")


if __name__ == "__main__":
    unittest.main()
