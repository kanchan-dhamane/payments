import unittest
import sys
import json
import os
from mock import patch

sys.path.append(os.getcwd())
import app
from data.payment_inputs import *


class TestAPIs(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()

    def test_successful_process_payment(self):
        data = json.dumps(valid_american_express_input)
        response = self.app.post("/process_payment", headers={"Content-Type": "application/json"}, data=data)
        self.assertEqual(200, response.status_code)

    def test_bad_request_process_payment(self):
        data = json.dumps(amount_missing)
        response = self.app.post("/process_payment", headers={"Content-Type": "application/json"}, data=data)
        self.assertEqual(400, response.status_code)

    @patch('app.Payments.process_payment', return_value=400)
    def test_server_error(self, mock_payment):
        mock_payment.side_effect = Exception()
        data = json.dumps(valid_american_express_input)
        response = self.app.post("/process_payment", headers={"Content-Type": "application/json"}, data=data)
        self.assertEqual(500, response.status_code)


if __name__ == '__main__':
    unittest.main()
