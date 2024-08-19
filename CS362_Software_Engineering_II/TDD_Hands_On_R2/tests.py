import unittest
from check_pwd import check_pwd


class TestCase (unittest.TestCase):
    
    def test_length(self):
        input = 'ABcd1!@'
        expected = False
        self.assertEqual(check_pwd(input), expected)
        input = 'ABcdefghijklmnopqrstu12@!'
        expected = False
        self.assertEqual(check_pwd(input), expected)
        input = 'ABcd12@!'
        expected = True
        self.assertEqual(check_pwd(input), expected)
        input = 'ABcd12789101214161@!'
        expected = True
        self.assertEqual(check_pwd(input), expected)


    def test_lowercase(self):
        input = 'password'
        expected = False
        self.assertEqual(check_pwd(input), expected)
        input = 'PASSWORD'
        expected = False
        self.assertEqual(check_pwd(input), expected)


    def test_uppercase(self):
        input = 'abcd12@#'
        expected = False
        self.assertEqual(check_pwd(input), expected)
        input = 'ABcd12@#'
        expected = True
        self.assertEqual(check_pwd(input), expected)


    def test_digit(self):
        input = 'ABcdefg@#'
        expected = False
        self.assertEqual(check_pwd(input), expected)
        input = 'ABcd123@#'
        expected = True
        self.assertEqual(check_pwd(input), expected)
        input = '12345678'
        expected = False
        self.assertEqual(check_pwd(input), expected)

    def test_symbol(self):
        input = 'ABcd1234@#'
        expected = True
        self.assertEqual(check_pwd(input), expected)
        input = 'ABcdefg1234'
        expected = False
        self.assertEqual(check_pwd(input), expected)
        input = '!@#$%^&*~'
        expected = False
        self.assertEqual(check_pwd(input), expected)


if __name__ == '__main__':
    unittest.main()
