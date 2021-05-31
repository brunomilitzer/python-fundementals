from datetime import *


def validate_card(exp_date):
    if exp_date < datetime.now().date():
        print("valid")
    else:
        print("expired")


validate_card(date(2021, 5, 30))
