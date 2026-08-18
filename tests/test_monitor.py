import unittest
from unittest.mock import patch

from monitor import check_url


class TestCheckURL(unittest.TestCase):

    @patch("monitor.requests.get")
    def test_successful_request(self, mock_get):
        mock_get.return_value.status_code = 200

        with patch("builtins.print") as mock_print:
            check_url("https://example.com")

        output = "\n".join(
            str(call.args[0]) for call in mock_print.call_args_list
        )

        self.assertIn("Status: ONLINE", output)
        self.assertIn("HTTP Status: 200", output)

    @patch("monitor.requests.get")
    def test_client_error(self, mock_get):
        mock_get.return_value.status_code = 404

        with patch("builtins.print") as mock_print:
            check_url("https://example.com/not-found")

        output = "\n".join(
            str(call.args[0]) for call in mock_print.call_args_list
        )

        self.assertIn("Status: CLIENT ERROR", output)
        self.assertIn("HTTP Status: 404", output)

    @patch("monitor.requests.get")
    def test_server_error(self, mock_get):
        mock_get.return_value.status_code = 500

        with patch("builtins.print") as mock_print:
            check_url("https://example.com/server-error")

        output = "\n".join(
            str(call.args[0]) for call in mock_print.call_args_list
        )

        self.assertIn("Status: SERVER ERROR", output)
        self.assertIn("HTTP Status: 500", output)


if __name__ == "__main__":
    unittest.main()
