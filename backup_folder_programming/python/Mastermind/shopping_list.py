

shopping_list = []
user_input = None

print("Shopping list program")

while user_input != "Q":
    user_input = input("what do you wish a purchase? ([Q] to exit):\n")

    if user_input == "Q":
        break

    if user_input not in shopping_list:

        confirmation = input("sure you want add {} [Y/N]:\n".format(user_input))
        if confirmation == "Y":
            shopping_list.append(user_input)
            print("added {}".format(user_input))

    if user_input in shopping_list:
        print("the input is already in the list")

print("The shopping list is: \n"
      "{}".format(shopping_list))
