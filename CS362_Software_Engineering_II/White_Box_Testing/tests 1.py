import unittest
from contrived_func import contrived_func

class TestContrivedFunc(unittest.TestCase):

    # Test a true, b true, c true, d true
    # This tests the first conditional statement, where both a and b are true,
    # c is true, and d is true, and the nested conditional is true
    def test_a_true_b_true_c_true_d_true(self):
        self.assertEqual(contrived_func(30), None)

    # Test a true, b true, c true, d false
    # This tests the first conditional statement, where both a and b are true,
    # c is true, and d is false, and the nested conditional is false
    def test_a_true_b_true_c_true_d_false(self):
        self.assertEqual(contrived_func(-1), None)

    # Test a true, b true, c false, d true
    # This tests the first conditional statement, where both a and b are true,
    # c is false, and d is true, and the nested conditional is false
    def test_a_true_b_true_c_false_d_true(self):
        self.assertEqual(contrived_func(20), None)

    # Test a true, b true, c false, d false
    # This tests the first conditional statement, where both a and b are true,
    # c is false, and d is false, and the nested conditional is false
    def test_a_true_b_true_c_false_d_false(self):
        self.assertEqual(contrived_func(-30), None)

    # Test a true, b false, c true, d true
    # This tests the first conditional statement, where a is true and b is false,
    # c is true, and d is true, and the nested conditional is true
    def test_a_true_b_false_c_true_d_true(self):
        self.assertEqual(contrived_func(16), None)

    # Test a true, b false, c true, d false
    # This tests the first conditional statement, where a is true and b is false,
    # c is true, and d is false, and the nested conditional is true
    def test_a_true_b_false_c_true_d_false(self):
        self.assertEqual(contrived_func(-16), None)

    # Test a true, b false, c false, d true
    # This tests the first conditional statement, where a is true and b is false,
    # c is false, and d is true, and the nested conditional is false
    def test_a_true_b_false_c_false_d_true(self):
        self.assertEqual(contrived_func(6), None)

    # Test a true, b false, c false, d false
    # This tests the first conditional statement, where a is true and b is false,
    # c is false, and d is false, and the nested conditional is false
    def test_a_true_b_false_c_false_d_false(self):
        self.assertEqual(contrived_func(-6), None)

    # Test a false, b true, c true, d true
    # This tests the first conditional statement, where a is false and b is true,
    # c is true, and d is true, and the nested conditional is false
    def test_a_false_b_true_c_true_d_true(self):
        self.assertEqual(contrived_func(3), None)


    # Test a false, b true, c true, d true
    # This tests the first conditional statement, where a is false and b is true,
    # c is true, and d is true, and the nested conditional is false
    def test_a_false_b_true_c_true_d_true(self):
        self.assertEqual(contrived_func(3), None)

    # Test a false, b true, c true, d false
    # This tests the first conditional statement, where a is false and b is true,
    # c is true, and d is false, and the nested conditional is false
    def test_a_false_b_true_c_true_d_false(self):
        self.assertEqual(contrived_func(-3), None)

    # Test a false, b true, c false, d true
    # This tests the first conditional statement, where a is false and b is true,
    # c is false, and d is true, and the nested conditional is false
    def test_a_false_b_true_c_false_d_true(self):
        self.assertEqual(contrived_func(8), None)

    # Test a false, b true, c false, d false
    # This tests the first conditional statement, where a is false and b is true,
    # c is false, and d is false, and the nested conditional is false
    def test_a_false_b_true_c_false_d_false(self):
        self.assertEqual(contrived_func(-8), None)

    # Test a false, b false, c true, d true
    # This tests the second conditional statement, where both a and b are false,
    # c is true, and d is true, and the nested conditional is true
    def test_a_false_b_false_c_true_d_true(self):
        self.assertEqual(contrived_func(80), None)

    # Test a false, b false, c true, d false
    # This tests the second conditional statement, where both a and b are false,
    # c is true, and d is false, and the nested conditional is false
    def test_a_false_b_false_c_true_d_false(self):
        self.assertEqual(contrived_func(-80), None)

    # Test a false, b false, c false, d true
    # This tests the second conditional statement, where both a and b are false,
    # c is false, and d is true, and the nested conditional is false
    def test_a_false_b_false_c_false_d_true(self):
        self.assertEqual(contrived_func(5), None)

    # Test a false, b false, c false, d false
    # This tests the second conditional statement, where both a and b are false,
    # c is false, and d is false, and the nested conditional is false
    def test_a_false_b_false_c_false_d_false(self):
        self.assertEqual(contrived_func(-5), None)

    # Test a false, b false, c false, d false
    # This tests the else case at the end of the function
    def test_all_false(self):
        self.assertEqual(contrived_func(0), None)

if __name__ == '__main__':
    unittest.main()
