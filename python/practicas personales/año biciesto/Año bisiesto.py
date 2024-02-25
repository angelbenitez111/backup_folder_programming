print ('Ingresa el año:')
año = int(input())
if (año % 4 == 0 and año % 100 != 0) or año % 400 == 0:
    print ('El año es biciesto')
else:
    print ('El año no es bisiesto')
