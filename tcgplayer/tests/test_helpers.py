import types

import unittest

from src.api.helpers import encode_query_params, convert_list_to_string


class EncodeParamsTestCase(unittest.TestCase):
    def test_exists(self):
        self.assertIsNotNone(encode_query_params)

    def test_is_function(self):
        self.assertIsInstance(encode_query_params, types.FunctionType)

    def test_single_param(self):
        expected = 'https://api.test.com/endpoint?foo=bar'
        self.assertEqual(encode_query_params('https://api.test.com/endpoint', {'foo': 'bar'}), expected)

    def test_multi_param(self):
        expected = 'https://api.test.com/endpoint?foo=bar&baz=qux'
        self.assertEqual(encode_query_params('https://api.test.com/endpoint', {'foo': 'bar', 'baz': 'qux'}), expected)


class ConvertListToStringTestCase(unittest.TestCase):
    def test_exists(self):
        self.assertIsNotNone(convert_list_to_string)

    def test_is_function(self):
        self.assertIsInstance(convert_list_to_string, types.FunctionType)

    def test_default_separator(self):
        expected = 'first,second,third'
        self.assertEqual(convert_list_to_string(['first', 'second', 'third']), expected)

    def test_separator_argument(self):
        expected = 'first/second/third'
        self.assertEqual(convert_list_to_string(['first', 'second', 'third'], '/'), expected)
