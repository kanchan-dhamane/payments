import unittest
import sys
import json
import os

sys.path.append(os.getcwd())
from app import *
from data.payment_inputs import *


class TestAPIs(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_successful_process_payment(self):
        data = json.dumps(valid_american_express_input)
        response = self.app.post("/process_payment", headers={"Content-Type": "application/json"}, data=data)
        self.assertEqual(200, response.status_code)

    def test_bad_request_process_payment(self):
        data = json.dumps(amount_missing)
        response = self.app.post("/process_payment", headers={"Content-Type": "application/json"}, data=data)
        self.assertEqual(400, response.status_code)


if __name__ == '__main__':
    unittest.main()
