def check_input(range_num: int):
    user_input = input('Enter your choice: ')

    if range_num != 0:
        list_range = [str(i) for i in range(1, range_num + 1)]
        while not user_input.isnumeric() or user_input not in list_range:
            user_input = input("Invalid Input. Enter a NUMBER between 1 and " + str(range_num) + ':\n')
    else:
        while not user_input.isnumeric():
            user_input = input("Invalid Input. Enter a NUMBER\n")
    return int(user_input)


