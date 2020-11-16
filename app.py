from flask import Flask, request
import json
from input_schema.payment_input_schema import PaymentInputSchema
from payments.payments import Payments
from payments.payment_gateway_factory import PaymentGatewayFactory

app = Flask(__name__)


@app.route('/process_payment', methods=['POST'])
def process_payment():
    process_paymnet = PaymentInputSchema()
    data = request.get_json()
    print("Recivied request: {}".format(data))
    errors = process_paymnet.validate(data)
    if errors:
        return errors, 400

    success = False
    status_code = 200
    gateway = PaymentGatewayFactory.get_payment_gateway(data["amount"])
    payment = Payments(gateway)
    try:
        response = payment.process_payment(data)
        success = True
    except Exception as e:
        print("Error {}".format(e))
        status_code = 500

    return json.dumps({"success": success}), status_code


if __name__ == '__main__':
    app.run()