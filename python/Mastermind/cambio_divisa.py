
dollar_guarani = 6905.90
libra_guarani = 8407.92

conversion = int(input("What conversion do you want:\n"
                       "1- Convart Dollar to Guarani\n"
                       "2- Convart Libra to Guarani\n"
                       "3- Convart Guarani to Dollar\n"
                       "4- Convart Guarani to Libra\n"
                       "Response: "))

if conversion == 1:
    name_currency = "Dollar"
elif conversion == 2:
    name_currency = "Libra"
elif conversion == 3 or conversion == 4:
    name_currency = "Guarani"
else:
    print("an error occurred\n"
          "Your option is invalid")
    exit()


amout = float(input("Insert amout in {}: ".format(name_currency)))

if conversion == 1:
    money = amout * dollar_guarani
elif conversion == 2:
    money = amout * libra_guarani
elif conversion == 3:
    money = amout / dollar_guarani
elif conversion == 4:
    money = amout / libra_guarani
else:
    print("an error occurred")
    exit()

print("The change is: {}".format(money))
