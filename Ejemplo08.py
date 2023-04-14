# Range: Valor inicial, Valor final, Incremento
print(range(3,10,2))

for i in range(3,10,2):
    print("i =", i)

for i in range(1,6):
    for j in range(1,13):
        print(str(i) + " * " + str(j) + " = " + str(i*j))
    print()
print("Fin del programa")