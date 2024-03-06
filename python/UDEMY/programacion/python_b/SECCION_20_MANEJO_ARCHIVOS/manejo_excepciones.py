from NumerosIdenticosException import NumerosIdenticosException

resultado = None

try:
    a = int(input('Primer número: '))
    b = int(input('Segundo número: '))
    if a == b:
        raise NumerosIdenticosException('números indénticos')
    resultado = a / b

# Tambien se podria poner ZeroDivisionError
except ZeroDivisionError as e:
    print(f"ZeroDivisionError - Ocurrio un error: {e}, {type(e)}")
except TypeError as e:
    print(f"TypeError - Ocurrio un error: {e}, {type(e)}")
except Exception as e:
    print(f"Exception - Ocurrio un error: {e}, {type(e)}")
else:
    print('No se arrojó ninguna excepción')
finally:
    print('Ejecución del bloque finally')

print(f"Resultado: {resultado}")
print("Continuamos...")
