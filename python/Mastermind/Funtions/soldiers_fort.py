from random import choice

NUMBER_SOLDIERS = 30


def number_generator(number_soldiers):
    soldiers = list(range(number_soldiers))
    for i in range(number_soldiers - 1):
        soldiers.remove(choice(soldiers))
    return int(soldiers[0]) + 1


def main():
    soldier = number_generator(NUMBER_SOLDIERS)
    print("The selected soldier is {}". format(soldier))


if __name__ == "__main__":
    main()
