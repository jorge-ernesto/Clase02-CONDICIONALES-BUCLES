"""
Se ingresa una base y su exponente. Calcular la potencia. No usar el operador potencia
base=2 y exponente=5 => base**expo=32
"""

"""
Resolucion del ejercicio
https://parzibyte.me/blog/2019/05/27/potencia-python-ciclo-while/
"""
base = int(input("Ingresa base: "))
exponente = int(input("Ingresa exponente: "))
contador = 1
elevado = 1

while contador <= exponente:
    elevado *= base # contador
    contador += 1 # contador

print(elevado)
