from payment_gateway import PaymentGateway
from config import CONFIG


class CheapPaymentGateway(PaymentGateway):

    def __init__(self, retry=1, alt_gateway=None, alt_gateway_retry=0):
        PaymentGateway.__init__(self, retry, alt_gateway, alt_gateway_retry)

    def process_payment(self, data):
        print("CheapPaymentGateway process_payment successfully")

    def is_available(self):
        available = CONFIG["cheap_gateway"]["available"]
        print("CheapPaymentGateway available: {}".format(available))
        return available
