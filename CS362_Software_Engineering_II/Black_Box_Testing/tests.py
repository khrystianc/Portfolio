import unittest
from credit_card_validator import credit_card_validator


class TestCreditCardValidator(unittest.TestCase):

    # Test Case 1: Invalid length - less than 10
    # How: Guessing
    def test_invalid_length_1(self):
        self.assertFalse(credit_card_validator("99999999"))

    # Test Case 2: valid length - less than 15-16
    # How: Guessing
    def test_valid_length_2(self):
        self.assertTrue(credit_card_validator("9876543210123456"))

    # Test Case 3: Invalid length - between 10 and 14
    # How: Guessing
    def test_invalid_length_3(self):
        self.assertFalse(credit_card_validator("12345678901234"))

    # Test Case 4: Invali d length - between 17 and 18
    # Methodology: Error Guessing
    def test_invalid_length_4(self):
        self.assertFalse(credit_card_validator("123456789012345678"))

    # Test Case 5: Invalid length - greater than 19
    # Methodology: Error Guessing
    def test_invalid_length_5(self):
        self.assertFalse(credit_card_validator("12345678901234567890"))

    # Test Case 6: Invalid American Express card
    # Methodology: Partition Testing
    def test_invalid_amex_1(self):
        self.assertFalse(credit_card_validator("378282246310005"))

    # Test Case 7: Invalid American Express card
    # Methodology: Partition Testing
    def test_invalid_amex_2(self):
        self.assertFalse(credit_card_validator("371449635398431"))

    # Test Case 8: Valid American Express card
    # Methodology: Partition Testing
    def test_valid_amex_3(self):
        self.assertTrue(credit_card_validator("34343434343434"))

    # Test Case 9: Invalid MasterCard card - prefix 51
    # Methodology: Partition Testing
    def test_invalid_mc_51(self):
        self.assertFalse(credit_card_validator("5105105105105100"))

    # Test Case 10: Valid MasterCard card - prefix 52
    # Methodology: Partition Testing
    def test_valid_mc_52(self):
        self.assertTrue(credit_card_validator("5222222222222225"))

    # Test Case 11: Valid MasterCard card - prefix 53
    # Methodology: Partition Testing
    def test_valid_mc_53(self):
        self.assertTrue(credit_card_validator("5353535353535353"))

    # Test Case 12: Invalid MasterCard card - prefix 54
    # Methodology: Partition Testing
    def test_invalid_mc_54(self):
        self.assertFalse(credit_card_validator("5454545454545454"))

    # Test Case 13: Invalid MasterCard card - prefix 55
    # Methodology: Partition Testing
    def test_invalid_mc_55(self):
        self.assertFalse(credit_card_validator("5555555555554444"))

    # Test Case 14: Invalid MasterCard card - prefix 2221
    # Methodology: Partition Testing
    def test_invalid_mc_2221(self):
        self.assertFalse(credit_card_validator("2221000000000009"))

    # Test Case 15: Valid MasterCard card - prefix 2720
    # Methodology: Partition Testing
    def test_valid_mc_2720(self):
        self.assertTrue(credit_card_validator("4111111111111111"))

    # Test Case 16: Valid Visa card
    # Methodology: Partition Testing
    def test_valid_visa(self):
        self.assertTrue(credit_card_validator("4111111111111112"))

    # Test Case 16: Invalid Visa card
    # Methodology: Partition Testing
    def test_invalid_visa(self):
        self.assertFalse(credit_card_validator("4111111111111134"))

    # Test Case 17: Invalid American Express card
    # Methodology: Partition Testing
    def test_invalid_amex(self):
        self.assertFalse(credit_card_validator("378282246310006"))

    # Test Case 18: Valid MasterCard card
    # Methodology: Partition Testing
    def test_valid_mc(self):
        self.assertTrue(credit_card_validator("5105105105105106"))

    # Test Case 19: Valid Visa card with leading/trailing spaces
    # Methodology: Boundary Testing
    def test_valid_visa_spaces(self):
        self.assertTrue(credit_card_validator(" 4111111111111111 "))

    # Test Case 20: Valid Visa card with dashes
    # Methodology: Boundary Testing
    def test_valid_visa_dashes(self):
        self.assertTrue(credit_card_validator("4111-1111-1111-1111"))
        
    # Test Case 21: Valid Visa card with dots
    # Methodology: Boundary Testing
    def test_valid_visa_dots(self):
        self.assertTrue(credit_card_validator("4111.1111.1111.1111"))

    # Test Case 22: Valid Visa card with mixed delimiters
    # Methodology: Boundary Testing
    def test_valid_visa_mixed_delimiters(self):
        self.assertTrue(credit_card_validator("4111-1111.1111 1111"))

    # Test Case 23: Valid Visa card with extra digits
    # Methodology: Boundary Testing
    def test_valid_visa_extra_digits(self):
        self.assertTrue(credit_card_validator("4111-1111.1111 1111 123"))

    # Verify that credit card numbers outside of length range  return False
    def test_length_error(self):
        self.assertFalse(credit_card_validator("123456789"))
        self.assertFalse(credit_card_validator("123456789012345"))
        self.assertFalse(credit_card_validator("12345678901234567890"))

    # Verify that credit card numbers with invalid prefix return False
    def test_prefix_error(self):
        self.assertTrue(credit_card_validator("1234567890123456"))
        self.assertFalse(credit_card_validator("324567890123456"))
        self.assertTrue(credit_card_validator("5622134567890123"))

    # Verify that credit card numbers with invalid checksum return False
    def test_checksum_error(self):
        self.assertTrue(credit_card_validator("4556711111111111"))
        self.assertFalse(credit_card_validator("370000000000002"))
        self.assertTrue(credit_card_validator("6011111111111117"))

    # Verify that credit card numbers at the lower and upper bounds of length and prefix ranges work
    def test_boundary_values(self):
        # Visa
        self.assertTrue(credit_card_validator("4000000000000000"))
        self.assertTrue(credit_card_validator("4999999999999999"))
        # MasterCard
        self.assertTrue(credit_card_validator("5100000000000000"))
        self.assertTrue(credit_card_validator("5599999999999999"))
        self.assertTrue(credit_card_validator("2221000000000000"))
        self.assertTrue(credit_card_validator("2720999999999999"))
        # AmEx
        self.assertFalse(credit_card_validator("340000000000000"))
        self.assertFalse(credit_card_validator("379999999999999"))


if __name__ == '__main__':
    unittest.main()
