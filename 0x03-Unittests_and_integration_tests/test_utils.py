#!/usr/bin/env python3
"""
Unit tests for utils.get_json function.
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import get_json


class TestGetJson(unittest.TestCase):
    """
    Tests for the get_json function.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """
        Test get_json function with mocked HTTP calls.
        """
        # Mock the requests.get function
        with patch('requests.get') as mock_get:
            # Mock the return value of json method of the Mock object
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            # Call the get_json function
            result = get_json(test_url)

            # Assertions
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


if __name__ == '__main__':
    unittest.main()
