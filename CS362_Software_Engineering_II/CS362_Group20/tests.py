import unittest
from task import *


class TestCase(unittest.TestCase):

    def test1(self):
        self.assertTrue(True)


class TestConvNum(unittest.TestCase):

    # Tests for integer strings
    def test_pos_int(self):
        self.assertEqual(conv_num('12345'), 12345)

    def test_neg_int(self):
        self.assertEqual(conv_num('-6789'), -6789)

    def test_zero_int(self):
        self.assertEqual(conv_num('0'), 0)

    # Tests for floating point strings
    def test_pos_float(self):
        self.assertAlmostEqual(conv_num('123.45'), 123.45)

    def test_neg_float(self):
        self.assertAlmostEqual(conv_num('-0.123'), -0.123)

    def test_empty_dec(self):
        self.assertAlmostEqual(conv_num('10.'), 10.0)

    # Tests for hexadecimal strings
    def test_pos_hexadecimal(self):
        self.assertEqual(conv_num('0xFF'), 255)

    def test_neg_hexadecimal(self):
        self.assertEqual(conv_num('-0xABC'), -2748)

    def test_zero_hexadecimal(self):
        self.assertEqual(conv_num('0x0'), 0)

    # Tests for invalid inputs or strings
    def test_invalids(self):
        self.assertIsNone(conv_num('12.34.56'))
        self.assertIsNone(conv_num('0xAZ4'))
        self.assertIsNone(conv_num('12345A'))
        self.assertIsNone(conv_num('.'))
        self.assertIsNone(conv_num(''))

    # Tests for the edge cases
    def test_edges(self):
        self.assertIsNone(conv_num(None))
        self.assertIsNone(conv_num(12345))
        self.assertIsNone(conv_num([]))
        self.assertIsNone(conv_num('0xFF.02'))
        self.assertIsNone(conv_num('-0x'))

    # Sample cases fromt the assignment
    def test_samples(self):
        self.assertEqual(conv_num('12345'), 12345)
        self.assertEqual(conv_num('-123.45'), -123.45)
        self.assertEqual(conv_num('.45'), 0.45)
        self.assertEqual(conv_num('123.'), 123.0)
        self.assertEqual(conv_num('0xAD4'), 2772)
        self.assertEqual(conv_num('0xAZ4'), None)
        self.assertEqual(conv_num('12345A'), None)
        self.assertEqual(conv_num('12.3.45'), None)


if __name__ == '__main__':
    unittest.main()
