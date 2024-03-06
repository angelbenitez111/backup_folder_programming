number_chose_by_the_user = int(input("What number do you want its multiplication?: "))

for number_multiply_variable in range(1, 11):
    if number_multiply_variable % 2 == 0:
        print("{} * {} = {}".format(number_chose_by_the_user, number_multiply_variable,
                                    number_chose_by_the_user * number_multiply_variable))
