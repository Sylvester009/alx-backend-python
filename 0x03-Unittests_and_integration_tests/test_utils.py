#!/usr/bin/env python3
"""A Module to test utils file"""
from parameterized import parameterized
import unittest
from unittest.mock import patch


def access_nested_map(nested_map, path):
    """Access a nested dictionary with a sequence of keys.

    Args:
        nested_map (dict): The nested dictionary to access.
        path (tuple): A sequence of keys to access the nested dictionary.

    Returns:
        The value associated with the given path in the nested dictionary.
    """
    for key in path:
        if not isinstance(nested_map, dict) or key not in nested_map:
            raise KeyError(key)
        nested_map = nested_map[key]
    return nested_map


def get_json(url):
    """Fetch JSON data from a remote URL.

    Returns:
        JSON data retrieved from the remote URL.
    """
    import requests
    response = requests.get(url)
    return response.json()


class TestAccessNestedMap(unittest.TestCase):
    """Test class for the access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test that access_nested_map returns expected value."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """Test that access_nested_map raises KeyError for paths that are
        invalid."""
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual(f"KeyError('{expected}')", repr(e.exception))


class TestGetJson(unittest.TestCase):
    """Test class for the get_json function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """Test that get_json returns the expected JSON data."""
        config = {'return_value.json.return_value': test_payload}
        patcher = patch('requests.get', **config)
        p_mock = patcher.start()
        self.assertEqual(get_json(test_url), test_payload)
        p_mock.assert_called_once()
        patcher.stop()


if __name__ == '__main__':
    unittest.main()
