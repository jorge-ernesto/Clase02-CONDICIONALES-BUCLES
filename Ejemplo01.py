print("Ejemplo01")

num1 = int(input("Ingrese primer numero"))
num2 = int(input("Ingrese segundo numero"))

estado = num1 == num2
print("Estado:", estado)

if estado:
    print("La condicion es verdad")
    if num1 % num2:
        print(str(num1) + "no es multiplo de " + str(num2))
    else:
        print(str(num1) + "es multiplo de " + str(num2))
else:
    print("La condicion es falsa")

if 0:
    print("cero")
elif 1:
    print("uno")
else:
    print("La condificon es falsa")

print("Se continua con el programa")
print("Fuera del if")