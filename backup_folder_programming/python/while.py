a = 10
b = 7
c = -3
e_1 = ((b * (-1)) < (c)) and (a * (-1) > b * -1)
e_2 = b + c <= c + b and not (a < b + c * (-1))
e_3 = ((a > c) and ((a+c) == b)) or (b > (a+c))
e_4 = ((b * c) > b+c or b*c < a*c)

if e_1:
    print("1")
if e_2:
    print("2")
if e_3:
    print("3")
if e_4:
    print("4")
