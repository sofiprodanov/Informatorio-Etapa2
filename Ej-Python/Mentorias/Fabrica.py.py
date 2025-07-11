# Una fábrica desea llevar un control de la cantidad de piezas producidas en distintos turnos de trabajo a lo largo del día. Cada ingreso por teclado 
# representa la cantidad total de piezas fabricadas en un turno determinado. El programa debe permitir ingresar por teclado los valores de producción
# para cada turno (Mañana, tarde, Noche). La carga de datos finalizará cuando se ingrese un valor negativo.
# Al finalizar la carga, el sistema debe:
# 1) Informar la cantidad total de turnos registrados.
# 2) Calcular el total de piezas producidas.
# 3) Indicar cuántos turnos tuvieron una producción entre 200 y 500 piezas.
# 4) Contar cuántos turnos registraron exactamente 600, 800 o 1000 piezas.
# 5) Informar si existió algún turno con menos de 100 piezas producidas.

totalTurnos= 0
producbaja=0
producexacta =0 
producmedia =0
totalPiezasProducidas =0




print ("Ingrese se la cantidad de produccion por turno (mañana,tarde,noche) o ingrese un valor negativo para finalizar") 
while True : # crea un bucle infinito
 turno = input ("Ingrese el turno (mañana, tarde, noche): ")
 if turno != "" : # si el turno no esta vacio, entonces
  cantidadPiezas = int (input("ingrese la cantidad de piezas producidas en el turno: "))
 if cantidadPiezas > 0 :
    totalTurnos = totalTurnos + 1 
    totalPiezasProducidas <- totalPiezasProducidas + cantidadPiezas
 if cantidadPiezas >= 200 and cantidadPiezas <= 500 :
    producmedia = producmedia + 1
 if cantidadPiezas == 600 and cantidadPiezas == 800 and cantidadPiezas == 1000 :
    producexacta= producexacta + 1
 if cantidadPiezas < 100 :
   producbaja = producbaja + 1
 if cantidadPiezas < 0:
   break 

print ("fin de la carga de datos")
print ("cantidad de turnos registrados : " , totalTurnos)
print ("total de piezas producidas :" , totalPiezasProducidas)
print ("total de turnos con produccion media :" , producmedia)
print ("total de turnos con produccion exacta " , producexacta)

if producbaja > 0 : 
 print ("total de turnos con produccion baja :" , producbaja)
else : 
   print ("no se registraron turnos con produccion baja")