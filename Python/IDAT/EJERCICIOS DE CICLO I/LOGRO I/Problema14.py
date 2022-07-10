# para usar timedelta hay que importarla

from datetime import datetime, timedelta
 
def sumar_hora(hora1,hora2):
    formato = "%H:%M:%S"
    lista = hora2.split(":")
    hora=int(lista[0])
    minuto=int(lista[1])
    segundo=int(lista[2])
    h1 = datetime.strptime(hora1, formato)
    dh = timedelta(hours=hora) 
    dm = timedelta(minutes=minuto)          
    ds = timedelta(seconds=segundo) 
    resultado1 =h1 + ds
    resultado2 = resultado1 + dm
    resultado = resultado2 + dh
    resultado=resultado.strftime(formato)
    return str(resultado)

print(sumar_hora("04:36:55","10:24:28"))