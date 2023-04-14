estado = True

num1 = int(input("Ingrese un entero positivo: "))
contador = 0

while num1 >= 0:
    # print("Dentro del bucle:", num1)
    if num1 % 2 == 0:
        # print("Numero par:", num1)
        contador = contador + 1
    num1 = num1 - 1
print("Fuera del bucle")
print("Cantidad de Pares:", contador)