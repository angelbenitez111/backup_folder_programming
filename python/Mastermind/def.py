def empowerment(number, number2):
    if number2:
        number ** number2
        return number ** number2
    return number ** 2


def convert_to_int():
    a = None

    while not (isinstance(a, int) and isinstance(a, int)):
        try:
            a = int(input("Number: "))
        except ValueError:
            pass
    return a


def main():
    number = convert_to_int()

    response = None
    while not (response == "Y" or response == "N"):
        response = input("Do you want raise it to another number [Y/N]: ")

    number_to_raise = None
    if response == "Y":
        number_to_raise = convert_to_int()

    result = empowerment(number, number_to_raise)

    if response == "Y":
        print(number, "**", number_to_raise, "=", result)
    else:
        print(number, "** 2 =", result)


if __name__ == "__main__":
    main()
