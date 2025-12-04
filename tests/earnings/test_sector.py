import unittest
from unittest.mock import patch
from tradingeconomics.earnings import getEarnings
from tradingeconomics import glob


class TestSector(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.earnings.fn.checkDates", side_effect=lambda url, s, e: url)
    @patch("tradingeconomics.earnings.fn.dataRequest", return_value={"sector": "ok"})
    def test_sector_parameter(self, mock_request, mock_dates):
        # Provide a sector filter and ensure URL is built correctly
        result = getEarnings(sector="technology")

        expected_url = "/earnings-revenues/sector/technology"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"sector": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.earnings.fn.checkDates", side_effect=lambda url, s, e: url)
    @patch("tradingeconomics.earnings.fn.dataRequest", return_value={"sector": "ok"})
    def test_sector_output_type_raw(self, mock_request, mock_dates):
        result = getEarnings(sector="finance", output_type="raw")

        expected_url = "/earnings-revenues/sector/finance"

        mock_request.assert_called_once_with(
            api_request=expected_url, output_type="raw"
        )
        self.assertEqual(result, {"sector": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.earnings.fn.checkDates", side_effect=lambda url, s, e: url)
    @patch("tradingeconomics.earnings.fn.dataRequest", return_value={"sector": "ok"})
    def test_multiple_sectors(self, mock_request, mock_dates):
        result = getEarnings(sector=["technology", "finance", "healthcare"])

        expected_url = "/earnings-revenues/sector/technology,finance,healthcare"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"sector": "ok"})
