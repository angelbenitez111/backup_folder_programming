post = 0
actual = 1
iteration = 3
i = 0
while i <= iteration:
    nextNumber = post + actual

    post = actual
    actual = nextNumber

    print(nextNumber)
    i += 1
