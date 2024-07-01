#!/usr/bin/env python3
"""
Unit tests for GithubOrgClient class in client module.
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient
from typing import Dict


class TestGithubOrgClient(unittest.TestCase):
    """
    Tests for GithubOrgClient class methods.
    """

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, mock_get_json: Mock) -> None:
        """
        Test org method of GithubOrgClient.
        """
        # Mock the return value of get_json
        expected_result: Dict[str, str] = {"login": "mocked_org"}
        mock_get_json.return_value = expected_result

        # Create an instance of GithubOrgClient
        client = GithubOrgClient(org_name)

        # Assert that org property returns the expected result
        self.assertEqual(client.org, expected_result)

        # Assert that get_json was called once with the correct URL
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )


if __name__ == '__main__':
    unittest.main()
