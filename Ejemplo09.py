"""
Se ingresa la hora y minutos en formato de 24 horas.
Hallar la hora del minuto siguiente
"""

# Metodo 1
horas   = int(input('Horas: '))
minutos = int(input('Minutos: '))

# Es el ultimo minuto de una hora
if minutos == 59:
    # Es la ultima hora
    if horas == 23:
        horas   = 0 # Reiniciamos las horas
        minutos = 0 # Reiniciamos los minutos
    elif horas < 23:
        horas  += 1 # Aumentamos las horas en 1
        minutos = 0 # Reiniciamos los minutos
elif minutos < 59:
    minutos += 1 # Aumentamos los minutos en 1, mantenemos las horas

print()
print("Hora:", horas)
print("Minuto:", minutos)

# Otro metodo
horai = horas
mini  = minutos
minF  = mini + 1
horaF = horai

if mini == 59:
    horaF = horai+1
    minF  = str(00)
    if mini == 59 and horai == 23:
        horaF = str(00)
        minF = str(00)

print()
print("Hora:", horaF)
print("Minuto:", minF)
