al_nueve = range(9)

contador1 = 0
contador2 = 0


cantidad_numeros = 0

for c in range(1,9):
    for d in range(9):
        for u in range(9):
            contador1 += 1
            if (c*100 + d*10 + u) == (c^3 + d^3 + u^3):
                cantidad_numeros += 1
                print(c*100 + d*10 + u)


print(".......................................")

print(cantidad_numeros)

print(contador1)
print(contador2)



