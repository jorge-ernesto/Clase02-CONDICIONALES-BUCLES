"""
Año bisiesto es el divisible entre 4, salvo que sea año secular -último de cada siglo, terminado en «00»-,
en cuyo caso también ha de ser divisible entre 400.
https://es.wikipedia.org/wiki/A%C3%B1o_bisiesto
"""

"""
Resolucion del ejercicio
https://www.mclibre.org/consultar/python/ejercicios/ej-funciones-2-soluciones.html
"""
anio = int(input("Escribe un año: "))
print(anio % 400 == 0 or (anio % 100 != 0 and anio % 4 == 0))