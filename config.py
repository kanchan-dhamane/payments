import sys

CONFIG = {

    "cheap_gateway": {
        "max_amount": 20,
        "available": True
    },
    "expensive_gateway": {
        "max_amount": 500,
        "available": True
    },
    "premium_gateway": {
        "max_amount": sys.maxint,
        "available": True
    }

}

VISA = "4[0-9]{12}(?:[0-9]{3})?"
AMERICAN_EXPRESS = "3[47][0-9]{13}"
MASTER_CARD = "(?:5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12}"

CARD_REGEX = "^{}|{}|{}$".format(VISA, AMERICAN_EXPRESS, MASTER_CARD)

