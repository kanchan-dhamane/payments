import unittest
import sys
import os

sys.path.append(os.getcwd())

from data.payment_inputs import *
from input_schema.payment_input_schema import PaymentInputSchema


class TestPaymentInputSchema(unittest.TestCase):

    def setUp(self):
        self.input_schema = PaymentInputSchema()

    def test_valid_input(self):
        # American Express card
        data = valid_american_express_input
        errors = self.input_schema.validate(data)
        self.assertDictEqual(errors, {})

        # Visa card
        data = valid_visa_card
        errors = self.input_schema.validate(data)
        self.assertDictEqual(errors, {})

        # Master card
        data = valid_master_card
        errors = self.input_schema.validate(data)
        self.assertDictEqual(errors, {})

    def test_invalid_card(self):
        data = invalid_card
        errors = self.input_schema.validate(data)
        self.assertDictEqual(errors, {'card_number': [u'String does not match expected pattern.']})

    def test_card_holder_missing(self):
        data = card_holder_missing
        errors = self.input_schema.validate(data)
        self.assertDictEqual(errors, {'card_holder': [u'Missing data for required field.']})

    def test_expiration_date_in_past(self):
        data = expiration_date_in_past
        errors = self.input_schema.validate(data)
        self.assertDictEqual(errors, {'expiration_date': ['Expiry date can not be in the past!']})

    def test_security_code_missing(self):
        data = security_code_missing
        errors = self.input_schema.validate(data)
        self.assertDictEqual(errors, {})

    def test_invalid_security_code(self):
        data = invalid_security_code
        errors = self.input_schema.validate(data)
        self.assertDictEqual(errors, {'security_code': [u'Length must be between 3 and 3.']})

    def test_amount_missing(self):
        data = amount_missing
        errors = self.input_schema.validate(data)
        self.assertDictEqual(errors, {'amount': [u'Missing data for required field.']})

    def test_invalid_amount(self):
        data = invalid_amount
        errors = self.input_schema.validate(data)
        self.assertDictEqual(errors, {'amount': ['Value must be greater than 0']})


if __name__ == '__main__':
    unittest.main()