# 5. Escriba un algoritmo que acepte tres números y luego los devuelva ordenados decrecientemente.

print("Para poder ordenar decrecientemente los numeros, necesito que me indiques tres valores: ")

v1 = float(input("Ingresa el primer numero: "))
v2 = float(input("Ingresa el segundo numero: "))
v3 = float(input("Ingresa el tercer numero: "))

if v1 > v2 and v2 > v3: #si v1 es mayor que v2 y v2 es mayor a v3
	v1 = v1
elif v2 > v1 and v1 > v3: #si v2 es mayor, v1 el del medio y v3 el mas chico
	#aux toma el valor v1, v1 toma el valor de v2 y v2 toma el valor de aux, convirtiendo a v2 en el mayor y v1 en el del medio
	aux = v1
	v1 = v2
	v2 = aux
elif v3 > v2 and v2 > v1: #si v3 es mayor, v2 el del medio y v1 el mas chico
	#aux toma el valor v1, v1 toma el valor de v3 y v3 toma el valor del aux, convirtiendo a v3 en el mayor y v1 en el mas chico
	aux = v1
	v1 = v3
	v3 = aux
elif v2 > v3 and v3 > v1: #si v2 es mayor, v3 el del medio y v1 el mas chico
	#aux toma el valor v1, v1 toma el valor de v2, v2 toma el valor de v3 y v3 toma el valor de aux, convirtiendo a v2 el mayor, v3 el del medio y v1 el mas chico		
	aux = v1
	v1 = v2
	v2 = v3
	v3 = aux	

print(f"{v1}, {v2}, {v3}")
