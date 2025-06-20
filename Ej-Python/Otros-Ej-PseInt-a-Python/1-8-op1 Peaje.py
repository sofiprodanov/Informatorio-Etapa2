# 8. Escriba un algoritmo que determine el precio del peaje a abonar por el pasajero en función de los km que va a recorrer, sabiendo que hasta
#10 km el precio es $ 200, hasta 20 km, el precio es $ 300, hasta 40 km, el precio es $400 y hasta 80 km el precio es $500, si supera los 80 Km
#el costo es de $600.

km = float(input("Ingrese cuantos kilometros va a recorrer:"))

if km < 10:
	print("El costo del peaje es $200.")
elif km < 20:
	print("El costo del peaje es $300.")
elif km < 40:
	print("El costo del peaje es $400.")
elif km < 80:
	print("El costo del peaje es $500.")
else:
	print("El costo del peaje es $600.")



	
