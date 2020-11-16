import unittest
import sys
import os

sys.path.append(os.getcwd())
from payments.payment_gateway_factory import *


class TestPaymentGatewayFactory(unittest.TestCase):

    def test_get_payment_gateway(self):
        gateway = PaymentGatewayFactory.get_payment_gateway(CONFIG["cheap_gateway"]["max_amount"])
        self.assertIsInstance(gateway, CheapPaymentGateway)

        gateway = PaymentGatewayFactory.get_payment_gateway(CONFIG["expensive_gateway"]["max_amount"])
        self.assertIsInstance(gateway, ExpensivePaymentGateway)

        gateway = PaymentGatewayFactory.get_payment_gateway(CONFIG["expensive_gateway"]["max_amount"] + 1)
        self.assertIsInstance(gateway, PremiumPaymentGateway)


if __name__ == '__main__':
    unittest.main()