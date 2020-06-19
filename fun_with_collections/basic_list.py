def make_list():
    user_input_list = []
    for x in range(3):
        user_input = get_input()
        if not user_input.isnumeric():
            raise ValueError
        else:
            user_input_list.append(int(user_input))
    return user_input_list


def get_input():
    return str
