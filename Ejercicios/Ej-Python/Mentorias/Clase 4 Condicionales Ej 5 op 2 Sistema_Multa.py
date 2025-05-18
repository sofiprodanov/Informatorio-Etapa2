#Ej 5: Sistema de multas por exceso de velocidad en zonas urbanas

#.lower() hace que no diferencie las mayusculas y minusculas
#.strip() 

max_calle = 40
max_avenida = 60

try:
    tipo_via = input("¿Vas por calle o avenida? ").lower().strip()
    velocidad = int(input("¿A qué velocidad vas? "))
    
    # Validación de tipo de vía
    if tipo_via not in ["calle", "avenida"]:
        print("Error: Debes especificar 'calle' o 'avenida'")
    else:
        # Determinación del límite según tipo de vía
        limite = max_calle if tipo_via == "calle" else max_avenida
        
        # Evaluación de velocidad
        if velocidad <= limite:
            print("Vas a una velocidad adecuada. ¡Buen viaje!")
        else:
            print(f"¡ALERTA! Exceso de velocidad. Límite: {limite} km/h")
            
except ValueError:
    print("Error: La velocidad debe ser un número entero válido.")