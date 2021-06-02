import unittest
from creditcardvalidation import *


class CreditCardValidationTest(unittest.TestCase):
    def setUp(self):
        print("Setup")

    def test_validate_card(self):
        result = validate_card(date(2021, 5, 30))
        self.assertEqual("valid", result)

    def test_validate_card_expired(self):
        with self.assertRaises(RuntimeError):
            validate_card(date(2022, 5, 30))

    def tearDown(self):
        print("TearDown")


if __name__ == '__main__':
    unittest.main()
