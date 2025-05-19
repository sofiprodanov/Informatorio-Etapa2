# 2. Elaborar un codigo para determinar el mayor de cuatro valores.

#.append() Toma el número ingresado (valor) y lo añade al final de la lista valores.

print("Para indicar cuál de los números es el mayor, necesito que me indiques cuatro valores:")

valores = [] #Se inicializa una lista llamada valores que almacenará los números ingresados por el usuario.


for i in range(4):
    while True:
        try:
            valor = float(input(f"Ingresa el {i+1}° valor: ")) # muestra un mensaje como "Ingresa el 1° valor: ", "Ingresa el 2° valor: ", etc.
            valores.append(valor) #Si la conversión a float es exitosa, el valor se agrega a la lista valores con valores.append(valor) y se rompe el bucle (break).
            break
        except ValueError:
            print("Error: Debes ingresar un número válido.")

# Encontramos el mayor valor usando la función max()
mayor_valor = max(valores) #La función max() recibe la lista valores y devuelve el número más grande.

print(f"El {mayor_valor} es el mayor de los cuatro valores.")