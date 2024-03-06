import os
user_input = None
number_list = []

print("Largest number and smallest number")

while user_input != "Q":
    user_input = input("insert the number to add: [Q] to exit:\n")

    if user_input == "Q":
        input("Enter to continue...")
        os.system("cls")
        break

    else:
        user_input = int(user_input)

    if user_input in number_list:
        print("the input is already in the list")
        input("Enter to continue...")
        os.system("cls")

    elif number_list not in number_list:

        if input("sure you want add {} [Y/N]:\n".format(user_input)) == "Y":
            number_list.append(user_input)
            print("added {}".format(user_input))
            input("Enter to continue...")
            os.system("cls")

        else:
            print("{} not added".format(user_input))
            input("Enter to continue...")
            os.system("cls")
            continue

print("Smallest number: {}\n"
      "Largest number: {}".format(min(number_list), max(number_list)))

input("Enter to finalize...")
