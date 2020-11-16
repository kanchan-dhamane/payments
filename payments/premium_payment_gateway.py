from payment_gateway import PaymentGateway
from config import CONFIG


class PremiumPaymentGateway(PaymentGateway):

    def __init__(self, retry=0, alt_gateway=None, alt_gateway_retry=0):
        PaymentGateway.__init__(self, retry, alt_gateway, alt_gateway_retry)

    def process_payment(self, data):
        print("PremiumPaymentGateway process_payment successfully")

    def is_available(self):
        available = CONFIG["premium_gateway"]["available"]
        print("PremiumPaymentGateway available: {}".format(available))
        return available

