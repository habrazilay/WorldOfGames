from currency_converter import CurrencyConverter
import random
from CheckInput import check_input
c = CurrencyConverter()


def get_money_interval(v: float, d: int, t: int):
    us_to_ils_value = c.convert(v, 'USD', 'ILS')
    a = t - (5 - d)
    b = t + (5 - d)
    print(f"The real value: {us_to_ils_value}, \n Your guess: {t}")
    if a <= us_to_ils_value <= b:
        return True
    else:
        return False


def get_guess_from_user(d: int):
    random_value = random.randrange(1, 100)
    print("What is the value of US$ " + str(random_value) + " in ILS currency?\n")
    guess_from_user = check_input(0)
    return get_money_interval(int(random_value), d, int(guess_from_user))


def play(difficulty: int):
    return get_guess_from_user(difficulty)
