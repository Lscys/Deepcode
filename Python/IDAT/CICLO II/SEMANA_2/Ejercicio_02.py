"""
Implemente un reloj que muestre la hora, minutos y segundos utilizando el módulo datetime.
"""

import datetime

horaActual = datetime.datetime.now()

hora = horaActual.hour         
minutos = horaActual.minute    
segundos = horaActual.second   

print("Hora actual: {}:{}:{}".format(hora, minutos, segundos))