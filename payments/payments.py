class Payments:

    def __init__(self, gateway):
        self.gateway = gateway

    def process_payment(self, data):
        retry = self.gateway.get_retry()
        if self.do_payment(data, self.gateway, retry):
            return

        alt_gateway_retry = self.gateway.get_alt_gateway_retry()
        print('Alternate gateway retry count {}'.format(alt_gateway_retry))

        if alt_gateway_retry:
            alt_gateway = self.gateway.get_alt_gateway()
            if self.do_payment(data, alt_gateway, alt_gateway_retry):
                return

        raise Exception("Error in processing payment")

    def do_payment(self, data, gateway, retry):
        retry_count = 0
        while retry_count < retry:
            try:
                retry_count += 1
                if gateway.is_available():
                    gateway.process_payment(data)
                    return True

            except Exception as e:
                print(e)

        return False