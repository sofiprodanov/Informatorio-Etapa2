# 5. Escriba un algoritmo que acepte tres números y luego los devuelva ordenados decrecientemente.

print("Para poder ordenar decrecientemente los numeros, necesito que me indiques tres valores: ")

v1 = float(input("Ingresa el primer numero: "))
v2 = float(input("Ingresa el segundo numero: "))
v3 = float(input("Ingresa el tercer numero: "))

# Ordenar los valores
if v1 < v2:
    v1, v2 = v2, v1  #Si v2 es mayor que v1, se intercambian sus valores.
if v1 < v3:
    v1, v3 = v3, v1  #Si v3 es mayor que v1, se intercambian.
if v2 < v3:
    v2, v3 = v3, v2  #Falta ordenar v2 y v3 (porque v1 ya es el mayor). Si v3 es mayor que v2, se intercambian.

print(f"{v1}, {v2}, {v3}")