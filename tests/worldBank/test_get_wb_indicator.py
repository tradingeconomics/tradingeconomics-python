import unittest
from unittest.mock import patch
from tradingeconomics.worldBank import getWBIndicator
from tradingeconomics import glob


class TestGetWBIndicator(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.worldBank.fn.dataRequest",
        return_value={"indicator": "series_code"},
    )
    def test_get_wb_indicator_by_series_code(self, mock_request):
        # Get indicator by series code
        result = getWBIndicator(series_code="usa.fr.inr.rinr")

        expected_url = "/worldBank/indicator?s=usa.fr.inr.rinr"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"indicator": "series_code"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.worldBank.fn.dataRequest", return_value={"indicator": "url"}
    )
    def test_get_wb_indicator_by_url(self, mock_request):
        # Get indicator by URL
        result = getWBIndicator(
            url="/united-states/real-interest-rate-percent-wb-data.html"
        )

        expected_url = "/worldBank/indicator?url=/united-states/real-interest-rate-percent-wb-data.html"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"indicator": "url"})

    def test_get_wb_indicator_no_parameters(self):
        # Test that error message is returned when no parameters provided
        result = getWBIndicator()

        self.assertEqual(result, "Series code or url is required!")

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.worldBank.fn.dataRequest",
        return_value={"indicator": "series_code_df"},
    )
    def test_get_wb_indicator_with_output_type(self, mock_request):
        # Get indicator with DataFrame output type
        result = getWBIndicator(series_code="usa.fr.inr.rinr", output_type="df")

        expected_url = "/worldBank/indicator?s=usa.fr.inr.rinr"

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, {"indicator": "series_code_df"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.worldBank.fn.dataRequest",
        return_value=[{"raw": "indicator_data"}],
    )
    def test_get_wb_indicator_output_type_raw(self, mock_request):
        # Get indicator with raw output type
        result = getWBIndicator(series_code="usa.fr.inr.rinr", output_type="raw")

        expected_url = "/worldBank/indicator?s=usa.fr.inr.rinr"

        mock_request.assert_called_once_with(
            api_request=expected_url, output_type="raw"
        )
        self.assertEqual(result, [{"raw": "indicator_data"}])


if __name__ == "__main__":
    unittest.main()
