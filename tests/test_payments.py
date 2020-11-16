import sys
import os
import unittest
from mock import patch

sys.path.append(os.getcwd())
from data.payment_inputs import valid_visa_card
from payments.payments import Payments


class TestAPIs(unittest.TestCase):

    @patch('payments.cheap_payment_gateway.CheapPaymentGateway')
    def test_cheap_payment_success(self, mock_cheap_gateway):
        mock_cheap_gateway.get_retry.return_value = 1
        mock_cheap_gateway.is_available.return_value = True

        data = valid_visa_card
        payment = Payments(mock_cheap_gateway)
        payment.process_payment(data)

        mock_cheap_gateway.is_available.assert_called_once()
        mock_cheap_gateway.process_payment.assert_called_once()

    @patch('payments.cheap_payment_gateway.CheapPaymentGateway')
    def test_cheap_payment_failed(self, mock_cheap_gateway):
        mock_cheap_gateway.get_retry.return_value = 1
        mock_cheap_gateway.is_available.return_value = False

        data = valid_visa_card
        payment = Payments(mock_cheap_gateway)

        self.assertRaises(Exception, payment.process_payment, data)
        mock_cheap_gateway.is_available.assert_called_once()
        mock_cheap_gateway.process_payment.assert_not_called()

    @patch('payments.expensive_payment_gateway.ExpensivePaymentGateway')
    def test_expensive_payment_success(self, mock_expensive_gateway):
        mock_expensive_gateway.get_retry.return_value = 1
        mock_expensive_gateway.is_available.return_value = True

        data = valid_visa_card
        payment = Payments(mock_expensive_gateway)
        payment.process_payment(data)

        mock_expensive_gateway.is_available.assert_called_once()
        mock_expensive_gateway.process_payment.assert_called_once()

    @patch('payments.cheap_payment_gateway.CheapPaymentGateway')
    @patch('payments.expensive_payment_gateway.ExpensivePaymentGateway')
    def test_expensive_unavailable_cheap_payment_success(
            self, mock_expensive_gateway, mock_cheap_gateway):
        mock_cheap_gateway.is_available.return_value = True
        mock_expensive_gateway.get_retry.return_value = 1
        mock_expensive_gateway.is_available.return_value = False
        mock_expensive_gateway.get_alt_gatway.retun_value = mock_cheap_gateway
        mock_expensive_gateway.get_alt_gateway_retry.return_value = 1

        data = valid_visa_card
        payment = Payments(mock_expensive_gateway)
        payment.process_payment(data)

        mock_expensive_gateway.is_available.assert_called_once()
        mock_expensive_gateway.process_payment.assert_not_called()

    @patch('payments.cheap_payment_gateway.CheapPaymentGateway')
    @patch('payments.expensive_payment_gateway.ExpensivePaymentGateway')
    def test_expensive_payment_failed(
            self, mock_cheap_gateway, mock_expensive_gateway):
        mock_cheap_gateway.is_available.return_value = False
        mock_expensive_gateway.get_retry.return_value = 1
        mock_expensive_gateway.is_available.return_value = False
        mock_expensive_gateway.get_alt_gatway.retun_value = mock_cheap_gateway
        mock_expensive_gateway.get_alt_gateway_retry.return_value = 0

        data = valid_visa_card
        payment = Payments(mock_expensive_gateway)

        self.assertRaises(Exception, payment.process_payment, data)
        mock_expensive_gateway.is_available.assert_called_once()
        mock_expensive_gateway.process_payment.assert_not_called()

    @patch('payments.premium_payment_gateway.PremiumPaymentGateway')
    def test_premium_payment_success(self, mock_premium_gateway):
        mock_premium_gateway.is_available.return_value = True
        mock_premium_gateway.get_retry.return_value = 3

        data = valid_visa_card
        payment = Payments(mock_premium_gateway)
        payment.process_payment(data)

        mock_premium_gateway.is_available.assert_called_once()
        mock_premium_gateway.process_payment.assert_called_once()

    @patch('payments.premium_payment_gateway.PremiumPaymentGateway')
    def test_premium_payment_success(self, mock_premium_gateway):
        mock_premium_gateway.is_available.return_value = False
        mock_premium_gateway.get_retry.return_value = 3
        mock_premium_gateway.get_alt_gateway_retry.return_value = 0

        data = valid_visa_card
        payment = Payments(mock_premium_gateway)

        self.assertRaises(Exception, payment.process_payment, data)
        self.assertEqual(mock_premium_gateway.is_available.call_count, 3)


if __name__ == '__main__':
    unittest.main()
