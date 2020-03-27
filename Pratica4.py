import datetime
from time import ctime
import ntplib
import os

t1 = datetime.datetime.now()

print ("Hora de inicio de peticion = %s" % t1)

servidor_de_tiempo = "pool.ntp.org"

cliente_ntp = ntplib.NTPClient()
respuesta = cliente_ntp.request(servidor_de_tiempo)
hora_servidor = datetime.datetime.strptime(ctime(respuesta.tx_time), "%a %b %d %H:%M:%S %Y")
t2 = datetime.datetime.now()

print ("Hora de llegada de peticion = %s" % t2)

print("Hora de servidor de tiempo = " +  str(hora_servidor) + "\n")

ajuste = ( t2 - t1 ) / 2

print("Ajuste = %s" % ajuste)

nueva_hora = hora_servidor + ajuste

print("Nueva fecha y hora = " +  str(nueva_hora) + "\n")
print("\nAjustando tiempo:")

conver = nueva_hora.strftime("%m%d%H%M%Y")
os.system(f"date -u {conver}")
