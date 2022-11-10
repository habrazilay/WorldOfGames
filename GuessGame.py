import random
from CheckInput import check_input


def generate_number(difficulty: int):
    secret_number = random.randrange(1, difficulty)
    return int(secret_number)


def get_guess_from_user(difficulty: int):
    print("Guess a number between 1 and " + str(difficulty) + '\n')
    user_number = check_input(difficulty)
    return user_number


def compare_results(a: int, b: int):
    print(f"The number: {a} \nYour guess: {b}")
    if a == b:
        return True
    else:
        return False


def play(difficulty: int):
    return compare_results(generate_number(difficulty), get_guess_from_user(difficulty)
)
