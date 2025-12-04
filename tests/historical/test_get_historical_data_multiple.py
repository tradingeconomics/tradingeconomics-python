import unittest
from unittest.mock import patch
from tradingeconomics.historical import getHistoricalData
from tradingeconomics import glob


class TestGetHistoricalDataMultiple(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.historical.fn.finalLink",
        side_effect=lambda url, dates: url + "/" + "/".join(dates),
    )
    @patch(
        "tradingeconomics.historical.fn.dataRequest", return_value={"multiple": "ok"}
    )
    def test_historical_multiple_countries_and_indicators(
        self, mock_request, mock_final_link
    ):
        # Get historical data for multiple countries and indicators (auto-adds 15-year lookback)
        result = getHistoricalData(
            country=["United States", "china"], indicator=["Imports", "Exports"]
        )

        # When no dates provided, auto-adds 15 years lookback date
        assert mock_request.called
        call_args = mock_request.call_args[1]
        assert call_args["output_type"] is None
        self.assertEqual(result, {"multiple": "ok"})
