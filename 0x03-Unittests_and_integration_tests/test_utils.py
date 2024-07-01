#!/usr/bin/env python3
"""
Unit tests for utils.access_nested_map function.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    """
    Test cases for access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Test access_nested_map function with various inputs.

        Parameters:
        - nested_map (dict): A nested dictionary.
        - path (tuple): A sequence of keys.
        - expected_result: The expected result from accessing nested_map with path.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

if __name__ == '__main__':
    unittest.main()

