import unittest

from src.com.jalasoft.compiler.common.invalid_data_error import InvalidDataError
from src.com.jalasoft.compiler.common.util import Util


class TestUtil(unittest.TestCase):
    def test_sum_list_valid_data(self):
        util = Util()
        util.sum_list([1, 2, 3])

    def test_sum_list_valid_data_invalid(self):
        util = Util()
        with self.assertRaises(InvalidDataError):
            util.sum_list([1, 2, 'hi'])

    def test_sum_list_none(self):
        util = Util()
        with self.assertRaises(InvalidDataError):
            util.sum_list(None)
