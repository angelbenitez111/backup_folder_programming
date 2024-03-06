def print_list(lista):
    if isinstance(lista, list):
        for element in lista:
            print(element)


def fibonacci(number):
    fibonacci_list = []
    for a in range(number):
        if a == 0:
            fibonacci_list.append(0)
        elif a == 1 or a == 2:
            fibonacci_list.append(1)
        else:
            c = (fibonacci_list[-1])
            fibonacci_list.append(c + c)
    return fibonacci_list


def main():
    number = None

    while not (isinstance(number, int)):
        try:
            number = int(input("Insert the amount of numbers fibonacci: "))

        except ValueError:
            pass

    list_fibonacci = fibonacci(number)

    print_list(list_fibonacci)


if __name__ == "__main__":
    main()
