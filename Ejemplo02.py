# Mayor de tres numeros
num1 = int(input("Ingrese numero 1: "))
num2 = int(input("Ingrese numero 2: "))
num3 = int(input("Ingrese numero 3: "))

# Metodo 1
if(num1 > num2 and num1 > num3):
    print("El numero mayor es " + str(num1))
else:
    if(num2 > num1 and num2 > num3):
        print("El numero mayor es " + str(num2))
    else:
        print("El numero mayor es " + str(num3))

# Metodo 2
mayor = num1
if mayor < num2:
    mayor = num2
if mayor < num3:
    mayor = num3
print("El numero mayor es:", mayor)

# Otro metodo
if (num1 > num2):
    mayor = num1
else:
    mayor = num2

if (num3 > mayor):
    mayor = num3
print("El numero mayor es:", mayor)