from datetime import *


def validate_card(exp_date):
    if exp_date < datetime.now().date():
        return "valid"
    else:
        raise RuntimeError("Card has expired")
