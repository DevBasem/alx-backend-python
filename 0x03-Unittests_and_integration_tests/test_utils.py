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
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_key):
        """
        Test access_nested_map function raises KeyError for non-existent keys.

        Parameters:
        - nested_map (dict): A nested dictionary.
        - path (tuple): A sequence of keys.
        - expected_key (str): The expected key that triggers the KeyError.
        """
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        
        self.assertEqual(str(cm.exception), expected_key)

if __name__ == '__main__':
    unittest.main()
