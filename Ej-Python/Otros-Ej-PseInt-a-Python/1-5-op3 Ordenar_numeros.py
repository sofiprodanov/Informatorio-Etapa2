# 5. Escriba un algoritmo que acepte tres números y luego los devuelva ordenados decrecientemente.

print("Para poder ordenar decrecientemente los numeros, necesito que me indiques tres valores: ")

#Se crea una lista llamada numeros que almacena los tres valores ingresados por el usuario.
numeros = [
    float(input("Ingresa el primer numero: ")),
    float(input("Ingresa el segundo numero: ")),
    float(input("Ingresa el tercer numero: "))
]

#El método .sort() ordena la lista de menor a mayor por defecto. Si usamos el argumento reverse=True, la ordena de mayor a menor (decreciente).
numeros.sort(reverse=True)

print(f"{numeros[0]}, {numeros[1]}, {numeros[2]}")