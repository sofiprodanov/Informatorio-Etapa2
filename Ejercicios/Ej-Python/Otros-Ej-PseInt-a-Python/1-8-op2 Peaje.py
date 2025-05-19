# 8. Escriba un algoritmo que determine el precio del peaje a abonar por el pasajero en función de los km que va a recorrer, sabiendo que hasta
#10 km el precio es $ 200, hasta 20 km, el precio es $ 300, hasta 40 km, el precio es $400 y hasta 80 km el precio es $500, si supera los 80 Km
#el costo es de $600.


# Diccionario con los límites y precios (orden ascendente)
tarifas = {
    10: 200,
    20: 300,
    40: 400,
    80: 500
}
precio_max = 600  # Para más de 80 km

try:
    km = float(input("Ingrese cuántos kilómetros va a recorrer: ")) #Ingreso de datos
    
    if km < 0:
        print("Error: La distancia no puede ser negativa.") #No admite nros negativos
    else:
        precio_peaje = precio_max  # Valor por defecto (si supera 80 km) - Asigna el precio máximo (600$) por defecto (si no se cumple ningún otro caso).
        
        for limite, precio in tarifas.items(): #llama  a la variable tarifas que esta al principio y recorre el diccionario
            if km <= limite: # Si los km ingresados son menores o iguales al límite actual (ej: km = 15 ≤ 20), asigna el precio correspondiente (300$).
                precio_peaje = precio
                break
        
        print(f"El costo del peaje es ${precio_peaje}.")

except ValueError:
    print("Error: Ingrese un número válido.")