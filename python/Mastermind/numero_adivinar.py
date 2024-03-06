import random

number = random.randint(1, 10)

print("divine the number is between 1 and 10")
participant_number: int = int(input("insert a number:"))

if number == participant_number:
    print("you guessed the number")

if number < 1:
    print("you fell short")

if number > 10:
    print("you already passed")

if number != participant_number:
    print("it's wrong number")

print("the number is {}".format(number))