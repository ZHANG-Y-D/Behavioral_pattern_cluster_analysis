import sys


def read_a_number(down=None, up=None, if_can_be_empty=True, number_type='int'):
    while True:
        number = read_a_string("Enter: ")
        if if_can_be_empty is True and number == '':
            return None
        try:
            if number_type == 'int':
                number = int(number)
            elif number_type == 'float':
                number = float(number)
            else:
                raise TypeError
        except ValueError:
            print("Please enter a " + number_type + " number.")
            continue
        if down is not None and number < down:
            print("Please enter a number larger or equal to " + str(down) + ".")
            continue
        elif up is not None and number > up:
            print("Please enter a number smaller or equal to " + str(up) + ".")
            continue
        return number


def read_a_string(hint_string=None):
    if hint_string is not None:
        print(hint_string, end='')
    try:
        return input()
    except KeyboardInterrupt:
        print("\n\nInput interrupted, Program Exit")
        sys.exit()
