def fibonacci(a):
    fibonacci_list = []
    for a in range(a):
        if a == 0:
            fibonacci_list.append(0)
        elif a == 1 or a == 2:
            fibonacci_list.append(1)
        else:
            c = (fibonacci_list[-1])
            fibonacci_list.append(c + c)
    return print(fibonacci_list)


def main():
    number = None

    while not (isinstance(number, int)):
        try:
            number = int(input("Insert the amount of numbers fibonacci: "))
        except ValueError:
            pass

    fibonacci(number)


if __name__ == "__main__":
    main()
