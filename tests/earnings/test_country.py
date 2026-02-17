import unittest
from unittest.mock import patch
from tradingeconomics.earnings import getEarnings
from tradingeconomics import glob


class TestCountry(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.earnings.fn.checkDates", side_effect=lambda url, s, e: url)
    @patch("tradingeconomics.earnings.fn.dataRequest", return_value={"country": "ok"})
    def test_country_parameter(self, mock_request, mock_dates):
        # Provide a country filter and ensure URL is built correctly
        result = getEarnings(country="united states")

        expected_url = "/earnings-revenues/country/united%20states"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"country": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.earnings.fn.checkDates", side_effect=lambda url, s, e: url)
    @patch("tradingeconomics.earnings.fn.dataRequest", return_value={"country": "ok"})
    def test_country_output_type_raw(self, mock_request, mock_dates):
        result = getEarnings(country="mexico", output_type="raw")

        expected_url = "/earnings-revenues/country/mexico"

        mock_request.assert_called_once_with(
            api_request=expected_url, output_type="raw"
        )
        self.assertEqual(result, {"country": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.earnings.fn.checkDates", side_effect=lambda url, s, e: url)
    @patch("tradingeconomics.earnings.fn.dataRequest", return_value={"country": "ok"})
    def test_multiple_countries(self, mock_request, mock_dates):
        result = getEarnings(country=["united states", "mexico", "canada"])

        expected_url = "/earnings-revenues/country/united%20states,mexico,canada"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"country": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.earnings.fn.checkDates",
        side_effect=lambda url, s, e: url + f"&init={s}&end={e}",
    )
    @patch("tradingeconomics.earnings.fn.dataRequest", return_value={"country": "ok"})
    def test_country_with_dates(self, mock_request, mock_dates):
        result = getEarnings(
            country="united states", initDate="2020-01-01", endDate="2020-12-31"
        )

        expected_url = (
            "/earnings-revenues/country/united%20states&init=2020-01-01&end=2020-12-31"
        )

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"country": "ok"})
