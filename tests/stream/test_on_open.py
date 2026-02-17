import unittest
from unittest.mock import patch, MagicMock, call
import json
from tradingeconomics import glob
from tradingeconomics import stream


class TestOnOpen(unittest.TestCase):

    @patch.object(glob, "_event", ["AAPL:US", "united states"])
    @patch("builtins.print")
    def test_on_open_with_subscriptions(self, mock_print):
        # Test on_open sends subscription messages for each event
        mock_ws = MagicMock()

        stream.on_open(mock_ws)

        # Verify print statements
        self.assertIn(call("+++ Socket is open!"), mock_print.call_args_list)
        self.assertIn(
            call("+++ Subscribe to {0}".format("AAPL:US")), mock_print.call_args_list
        )
        self.assertIn(
            call("+++ Subscribe to {0}".format("united states")),
            mock_print.call_args_list,
        )

        # Verify subscription messages sent
        expected_calls = [
            call(json.dumps({"topic": "subscribe", "to": "AAPL:US"})),
            call(json.dumps({"topic": "subscribe", "to": "united states"})),
        ]
        mock_ws.send.assert_has_calls(expected_calls, any_order=False)
        self.assertEqual(mock_ws.send.call_count, 2)

    @patch.object(glob, "_event", [])
    @patch("builtins.print")
    def test_on_open_without_subscriptions(self, mock_print):
        # Test on_open with no events subscribed
        mock_ws = MagicMock()

        stream.on_open(mock_ws)

        # Verify socket open message
        mock_print.assert_called_once_with("+++ Socket is open!")

        # Verify no subscription messages sent
        mock_ws.send.assert_not_called()

    @patch.object(glob, "_event", ["single_event"])
    @patch("builtins.print")
    def test_on_open_single_event(self, mock_print):
        # Test on_open with single event
        mock_ws = MagicMock()

        stream.on_open(mock_ws)

        # Verify subscription for single event
        mock_ws.send.assert_called_once_with(
            json.dumps({"topic": "subscribe", "to": "single_event"})
        )


if __name__ == "__main__":
    unittest.main()
