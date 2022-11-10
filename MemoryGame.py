import random
from CheckInput import check_input
import time


def generate_sequence(difficulty: int):
    num_list = [random.randrange(1, 101) for num in range(difficulty)]
    # print('Try to remember this list ', num_list)
    print('Try to remember this list ', num_list, end="")
    time.sleep(1)
    # print("\n"*100)
    print("\r", end="")
    return num_list


def get_list_from_user(difficulty: int):
    user_number_list = []
    for i in range(difficulty):
        print("Guess the number " + str(i + 1) + " of the previous list: \n")
        user_number = check_input(101)
        user_number_list.append(user_number)
    return user_number_list


def is_list_equal(list_a, list_b):
    list_a.sort()
    list_b.sort()
    print(f"The numbers: {list_a} \nYour guess: {list_b}")
    if list_a == list_b:
        return True
    else:
        return False


def play(difficulty: int):
    return is_list_equal(generate_sequence(difficulty), get_list_from_user(difficulty))
