
from credit_card_validator import credit_card_validator
import random
import unittest


class TestCase(unittest.TestCase):
    pass


def test_func(expected, test_case, func_under_test, message):
    def test(self):
        result = func_under_test(test_case)
        self.assertEqual(expected, result, message.format(test_case, expected, result))
    return test


def testcases(tests_to_generate=80000):
    """
    Formatted to follow the readings, but with my own adjustments to show credit card requirements.
    """
    for i in range(tests_to_generate):
        expected = True
        # prefix and length
        prefix, length = _card_params()
        # random credit card number with the prefix and length
        number = prefix + ''.join(random.choice('0123456789') for _ in range(length - len(prefix) - 1))
        # check digit wityh Luhn's algorithm
        check_digit = _generate_check_digit(number)
        # putnit ll together with valid check digit = valid CCN
        valid_card_number = number + check_digit
        # begin CCN checks based on issuer requirements
        if length < 15 or length > 16:
            expected = False
        if prefix not in ['4'] + [str(i) for i in range(51, 56)] + [str(i) for i in range(2221, 2721)] + ['34', '37']:
            expected = False
        message = 'Test case: {}, Expected: {}, Result: {}'
        new_test = test_func(expected, valid_card_number, credit_card_validator, message)
        setattr(TestCase, 'test_{}'.format(i), new_test)

        # corner cases
        if length == 16:
            if prefix == '4':
                # Visa length with valid prefix and check digit
                invalid_length = valid_card_number[:-1] + str(random.choice([1, 2, 3, 5, 6, 7, 8, 9]))
                expected = False
                new_test = test_func(expected, invalid_length, credit_card_validator, message)
                setattr(TestCase, 'test_{}_corner_case'.format(i), new_test)
                # Visa length with valid prefix and invalid check digit
                invalid_check_digit = valid_card_number[:-1] + str(random.randint(0, 9))
                expected = False
                new_test = test_func(expected, invalid_check_digit, credit_card_validator, message)
                setattr(TestCase, 'test_{}_corner_case_2'.format(i), new_test)
            elif prefix in [str(i) for i in range(51, 56)] + [str(i) for i in range(2221, 2721)]:
                # Mastercard invalid length with valid prefix and check digit
                invalid_length = valid_card_number[:-1] + str(random.choice([1, 2, 3, 5, 6, 7, 8, 9]))
                expected = False
                new_test = test_func(expected, invalid_length, credit_card_validator, message)
                setattr(TestCase, 'test_{}_corner_case'.format(i), new_test)
                # Mastercard length with valid prefix and invalid check digit
                invalid_check_digit = valid_card_number[:-1] + str(random.randint(0, 9))
                expected = False
                new_test = test_func(expected, invalid_check_digit, credit_card_validator, message)
                setattr(TestCase, 'test_{}_corner_case_2'.format(i), new_test)
        else:
            if prefix in ['34', '37']:
                # Amex invalid length with valid prefix and check digit
                invalid_length = valid_card_number[:-1] + str(random.choice([1, 2, 3, 5, 6, 7, 8, 9]))
                expected = False
                new_test = test_func(expected, invalid_length, credit_card_validator, message)
                setattr(TestCase, 'test_{}_corner_case'.format(i), new_test)
                # Amex length with valid prefix and invalid check digit
                invalid_check_digit = valid_card_number[:-1] + str(random.randint(0, 9))
                expected = False
                new_test = test_func(expected, invalid_check_digit, credit_card_validator, message)
                setattr(TestCase, 'test_{}_corner_case_2'.format(i), new_test)


def _card_params():
    """
    Select card issuer prefix and length
    """
    visa_prefix = '4'
    mastercard_prefixes = [str(i) for i in range(51, 56)] + [str(i) for i in range(2221, 2721)]
    amex_prefixes = ['34', '37']

    issuer = random.choice(['visa', 'mastercard', 'amex'])
    if issuer == 'visa':
        prefix = visa_prefix
        length = random.choice([10, 16, 19])
    elif issuer == 'mastercard':
        prefix = random.choice(mastercard_prefixes + [str(i) for i in range(51, 56)] + [str(i) for i in range(2221, 2721)])
        length = random.choice([10, 16, 19])
    else:
        prefix = random.choice(amex_prefixes + ['34', '37'])
        length = random.choice([10, 15, 19])
    return prefix, length


def _generate_check_digit(number):
    """
    Generate a check digit using the Luhn algorithm for a given credit card number. Same check code from my black box testing assignment
    """
    digits = [int(digit) for digit in number]
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits + [sum(divmod(2 * digit, 10)) for digit in even_digits])
    return str((10 - checksum % 10) % 10)


if __name__ == '__main__':
    testcases()
    unittest.main()
