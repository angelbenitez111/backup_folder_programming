import os
NAME_FILE = "purchase_list.txt"
SALIDA = "SALIR"
SEE_LIST = "LIST"
OPTION_BUY = ["ham", "cheese", "bread"]


def temporary_pass():
    input("Enter to continue...")


def load_create_list():
    lista = []
    question = input("Do you like to load the last purchase list? [Y/N]")
    try:
        while question != "Y" and question != "N":
            if question == "Y":
                with open(NAME_FILE, "r") as a:
                    lista = a.read().split("\n")

    except FileNotFoundError:
        print("File purchase not found")

    return lista


def question_product_user():
    response = input("Insert a product: [{} to go to out][{} see shopping list]:\n".format(SALIDA, SEE_LIST))

    while response.lower() not in OPTION_BUY and response != SALIDA and response != SEE_LIST:
        print("Your item  is not in options")
        response = input("Insert a product: [{} to go to out][{} see shopping list]:\n".format(SALIDA, SEE_LIST))
    return response


def export_list(lista):
    with open(NAME_FILE, "w") as my_file:
        my_file.write("\n".join(lista))
    # [w = write, r = read, a= append]


def main():
    shopping_list = load_create_list()
    user_input = question_product_user()

    while user_input != SALIDA:
        if user_input.lower() in [a.lower() for a in shopping_list]:
            print("The product is in the list")

        elif user_input == SEE_LIST:
            print("Options:\n" + "\n".join(OPTION_BUY))
            temporary_pass()

        else:
            shopping_list.append(user_input)
            if len(shopping_list) > 0:
                print("Products in the list:\n" + "\n".join(shopping_list))
        user_input = question_product_user()
        os.system("cls")

    export_list(shopping_list)


if __name__ == "__main__":
    main()
