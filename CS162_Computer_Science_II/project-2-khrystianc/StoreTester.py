# Author: Khrystian Clark
# Date: 10/7/2020
# Description: The UnitTester for the Store Simulator

import unittest
from Store import Product, Customer


class Project2TestCases(unittest.TestCase):
    def test_1(self):
        p1 = Product("889", "Rodent of unusual size", "when a rodent of the usual size just won't do", 33.45, 8)
        result = p1.get_product_id()
        self.assertEqual(result, "889")

    def test_2(self):
        c1 = Customer("Yinsheng", "QWF", False)
        result = c1.is_premium_member()
        self.assertTrue(result)

    def test_3(self):
        c1 = Customer("Yinsheng", "QWF", False)
        result = c1.is_premium_member()
        self.assertFalse(result)

    def test_4(self):
        p1 = Product("889", "Rodent of unusual size", "when a rodent of the usual size just won't do", 33.45, 8)
        result = p1.get_title()
        self.assertIn(result, p1.get_description())

    def test_5(self):
        p1 = Product("889", "Rodent of unusual size", "when a rodent of the usual size just won't do", 33.45, 8)
        result = p1.get_title()
        self.assertNotIn(result, p1.get_description())


if __name__ == '__main__':
    unittest.main()
