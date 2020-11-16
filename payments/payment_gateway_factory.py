from cheap_payment_gateway import CheapPaymentGateway
from expensive_payment_gateway import ExpensivePaymentGateway
from premium_payment_gateway import PremiumPaymentGateway
from config import CONFIG


class PaymentGatewayFactory:

    def __init__(self):
        pass

    @classmethod
    def get_payment_gateway(cls, amount):
        if amount <= CONFIG["cheap_gateway"]["max_amount"]:
            return CheapPaymentGateway()
        if amount <= CONFIG["expensive_gateway"]["max_amount"]:
            cheap_gateway = CheapPaymentGateway()
            return ExpensivePaymentGateway(alt_gateway=cheap_gateway, alt_gateway_retry=1)
        else:
            return PremiumPaymentGateway(retry=3)
