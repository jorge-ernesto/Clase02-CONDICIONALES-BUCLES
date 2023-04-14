"""
Suma de los primeros 100 numeros, no usar formula
s = 1 + 2 + 3 + 4 + .... + 100
Metodo de Gauss
5050 = 100 * (101/2)
Total = n * (n+1/2)
"""

num = 100
con = 1 # variable contador
sum = 0 # variable acumulador

while con <= 100:
    con = con + 1   # contador: Siempre suma una constante, puede ser 1, 2, 3 o lo que sea
    sum = sum + con # acumulador: Siempre suma una variable, no sabemos cuanto vale
print("Suma:", sum)