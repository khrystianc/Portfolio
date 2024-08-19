import unittest
from contrived_func import contrived_func


class TestContrivedFunc(unittest.TestCase):
    # Test if only A, B, and D are true
    def test_ABD_true(self):
        self.assertEqual(contrived_func(9), None)

    # Test if only B, C, and D are true
    def test_BCD_true(self):
        self.assertEqual(contrived_func(20), None)

    # Test if A and B are not true
    def test_AB_false(self):
        self.assertEqual(contrived_func(-8), None)

    # Test if only A or B is true
    def test_AorB_true(self):
        self.assertEqual(contrived_func(2), None)

    # Test if only A or C is true
    def test_AorC_true(self):
        self.assertEqual(contrived_func(25), None)

    # Test if only B or C is true
    def test_BorC_true(self):
        self.assertEqual(contrived_func(18), None)

    # Test if only B or C is true
    def test_BC_true(self):
        self.assertEqual(contrived_func(19), None)

    # Test if all are false
    def test_ABCD_false(self):
        self.assertEqual(contrived_func(-5), None)


if __name__ == '__main__':
    unittest.main()
