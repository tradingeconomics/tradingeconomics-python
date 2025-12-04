import unittest
from unittest.mock import patch
from tradingeconomics.markets import getMarketsData, ParametersError
from tradingeconomics import glob


class TestGetMarketsData(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.markets.fn.dataRequest",
        return_value={"markets": "commodities"},
    )
    def test_get_markets_data_commodities(self, mock_request):
        # Get commodities market data
        result = getMarketsData(marketsField="commodities")

        expected_url = "https://api.tradingeconomics.com/markets/commodities?c=TESTKEY"

        mock_request.assert_called_once_with(expected_url, None)
        self.assertEqual(result, {"markets": "commodities"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.markets.fn.dataRequest", return_value={"markets": "currency"}
    )
    def test_get_markets_data_currency(self, mock_request):
        # Get currency market data
        result = getMarketsData(marketsField="currency")

        expected_url = "https://api.tradingeconomics.com/markets/currency?c=TESTKEY"

        mock_request.assert_called_once_with(expected_url, None)
        self.assertEqual(result, {"markets": "currency"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.markets.fn.dataRequest", return_value={"markets": "index"})
    def test_get_markets_data_index(self, mock_request):
        # Get index market data
        result = getMarketsData(marketsField="index")

        expected_url = "https://api.tradingeconomics.com/markets/index?c=TESTKEY"

        mock_request.assert_called_once_with(expected_url, None)
        self.assertEqual(result, {"markets": "index"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.markets.fn.dataRequest", return_value={"markets": "bond"})
    def test_get_markets_data_bond(self, mock_request):
        # Get bond market data
        result = getMarketsData(marketsField="bond")

        expected_url = "https://api.tradingeconomics.com/markets/bond?c=TESTKEY"

        mock_request.assert_called_once_with(expected_url, None)
        self.assertEqual(result, {"markets": "bond"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.markets.fn.dataRequest", return_value={"markets": "bond_10y"}
    )
    def test_get_markets_data_bond_with_type(self, mock_request):
        # Get bond market data with type
        result = getMarketsData(marketsField="bond", type="10Y")

        expected_url = (
            "https://api.tradingeconomics.com/markets/bond?c=TESTKEY&type=10Y"
        )

        mock_request.assert_called_once_with(expected_url, None)
        self.assertEqual(result, {"markets": "bond_10y"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.markets.fn.dataRequest", return_value={"markets": "crypto"}
    )
    def test_get_markets_data_crypto(self, mock_request):
        # Get crypto market data
        result = getMarketsData(marketsField="crypto")

        expected_url = "https://api.tradingeconomics.com/markets/crypto?c=TESTKEY"

        mock_request.assert_called_once_with(expected_url, None)
        self.assertEqual(result, {"markets": "crypto"})

    def test_get_markets_data_invalid_field(self):
        # Test error for invalid marketsField
        with self.assertRaises(ParametersError) as context:
            getMarketsData(marketsField="invalid")

        self.assertIn("Accepted values for marketsField are", str(context.exception))

    def test_get_markets_data_type_without_bond(self):
        # Test error when type is used with non-bond field
        with self.assertRaises(ParametersError) as context:
            getMarketsData(marketsField="index", type="10Y")

        self.assertIn(
            "The type parameter is only available for bonds", str(context.exception)
        )
