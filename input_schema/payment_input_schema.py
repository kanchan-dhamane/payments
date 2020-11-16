from marshmallow import Schema, fields, validate, validates, ValidationError
from datetime import datetime

from config import CARD_REGEX


class PaymentInputSchema(Schema):
    card_number = fields.Str(required=True,validate=validate.Regexp(CARD_REGEX))
    card_holder = fields.Str(required=True)
    expiration_date = fields.DateTime(required=True)
    security_code = fields.Str(validate=validate.Length(min=3, max=3))
    amount = fields.Decimal(required=True, validate=[validate.Range(min=1, error="Value must be greater than 0")])

    @validates('expiration_date')
    def is_not_in_future(self, value):
        now = datetime.now()
        if value <= now:
            raise ValidationError("Expiry date can not be in the past!")