import unittest
from unittest.mock import patch, MagicMock
import main

class TestWeatherApp(unittest.TestCase):

    @patch('main.requests.get')
    def test_fetch_weather_success(self, mock_get):
        # Mocking the response from requests.get
        mock_response = MagicMock()
        mock_response.json.return_value = {
            'name': 'Test City',
            'main': {'temp': 20, 'pressure': 1000, 'humidity': 50},
            'weather': [{'description': 'sunny', 'main': 'Clear'}],
            'wind': {'speed': 5}
        }
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        data = main.fetch_weather("dummy_api_key", "Test City")

        self.assertIsNotNone(data)
        self.assertEqual(data['name'], 'Test City')
        self.assertEqual(data['main']['temp'], 20)

    @patch('main.requests.get')
    def test_fetch_weather_failure(self, mock_get):
        # Mocking a request exception
        mock_get.side_effect = main.requests.exceptions.RequestException("Connection error")

        data = main.fetch_weather("dummy_api_key", "Test City")

        self.assertIsNone(data)

    def test_compose_email_parts(self):
        weather_data = {
            'name': 'Test City',
            'main': {'temp': 20},
            'weather': [{'description': 'sunny'}]
        }
        location = "Test City"

        text, html = main.compose_email_parts(weather_data, location)

        self.assertIn("Test City", text)
        self.assertIn("20", text)
        self.assertIn("sunny", text)

        self.assertIn("Test City", html)
        self.assertIn("20", html)
        self.assertIn("sunny", html)

    @patch('main.smtplib.SMTP_SSL')
    def test_send_email(self, mock_smtp):
        # Mock the SMTP server instance
        mock_server = MagicMock()
        mock_smtp.return_value.__enter__.return_value = mock_server

        main.send_email(
            "Test Subject",
            "Test Body Text",
            "<html><body>Test Body HTML</body></html>",
            "sender@example.com",
            "password",
            "recipient@example.com"
        )

        mock_server.login.assert_called_with("sender@example.com", "password")
        mock_server.sendmail.assert_called()

if __name__ == '__main__':
    unittest.main()
