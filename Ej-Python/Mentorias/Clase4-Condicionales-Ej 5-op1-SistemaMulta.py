#Ej 5: Sistema de multas por exceso de velocidad en zonas urbanas

#.lower() hace que no diferencie las mayusculas y minusculas
#.strip() elimina espacios accidentales

max_calle = 40
max_av = 60

try:
    vias = input("¿Vas por calle o avenida? \n").lower().strip()
    velocidad = int(input("¿A que velocidad vas? \n"))

    if vias == "calle" or vias == "avenida":
        if velocidad <= max_calle or velocidad <= max_av:
            print("Cumple con las normas.")
        elif velocidad > max_calle or velocidad > max_av:
            print("Tiene una multa por exceso de velocidad.")
  
except ValueError:
    print("Error: Por favor ingresa un dato valido.")