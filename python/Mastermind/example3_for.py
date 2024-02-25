user_input = input("Insert the numbers separate for a comma: ")
user_numbers = [int(numbers) for numbers in user_input.split(",")]

largest_number = user_numbers[0]
smallest_number = user_numbers[0]

for number in user_numbers[1:]:
    if largest_number < number:
        largest_number = number

    if smallest_number > number:
        smallest_number = number

print("The smallest number is: {}\n"
      "The largest number is: {}".format(smallest_number, largest_number))
