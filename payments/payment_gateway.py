from abc import ABCMeta, abstractmethod


class PaymentGateway:

    __metaclass__ = ABCMeta

    def __init__(self, retry, alt_gateway, alt_gateway_retry):
        self.__retry = retry
        self.__alt_gateway = alt_gateway
        self.__alt_gateway_retry = alt_gateway_retry

    @abstractmethod
    def process_payment(self, data):
        pass

    def get_retry(self):
        return self.__retry

    def get_alt_gateway(self):
        return self.__alt_gateway

    def get_alt_gateway_retry(self):
        return self.__alt_gateway_retry


