import unittest
from conv_num import *

class ConvNumTestCase(unittest.TestCase):
    def test_integer(self):
        self.assertEqual(conv_num('12345'), 12345)
        self.assertEqual(conv_num('-6789'), -6789)
        self.assertEqual(conv_num('0'), 0)

    def test_float(self):
        self.assertAlmostEqual(conv_num('123.45'), 123.45)
        self.assertAlmostEqual(conv_num('-0.123'), -0.123)
        self.assertAlmostEqual(conv_num('10.'), 10.0)

    def test_hexadecimal(self):
        self.assertEqual(conv_num('0xFF'), 255)
        self.assertEqual(conv_num('-0xABC'), -2748)
        self.assertEqual(conv_num('0x0'), 0)

    def test_invalid_formats(self):
        self.assertIsNone(conv_num('12.34.56'))
        self.assertIsNone(conv_num('0xAZ4'))
        self.assertIsNone(conv_num('12345A'))
        self.assertIsNone(conv_num('.'))
        self.assertIsNone(conv_num(''))

    def test_edge_cases(self):
        self.assertIsNone(conv_num(None))
        self.assertIsNone(conv_num(12345))
        self.assertIsNone(conv_num([]))
        self.assertIsNone(conv_num('0xFF.02'))
        self.assertIsNone(conv_num('-0x'))
        self.assertIsNone(conv_num('-.123'))

if __name__ == '__main__':
    unittest.main()
