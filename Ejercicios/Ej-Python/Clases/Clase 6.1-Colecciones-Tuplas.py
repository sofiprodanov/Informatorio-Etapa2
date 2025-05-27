#Se definen con () y pueden contener cualquier tipo de elementos inlcuido otras colecciones o listas.
#Son ordenadas (sus elementos tienen indices) y son inmutables (no se puede modificar).

numeros_tupla = (1, 2, 3, 4, 5)
print(f"Numeros (tupla): {numeros_tupla}, tipo: {type(numeros_tupla)}")


#primer elemento
print(numeros_tupla[0])

#ultimo elemento
print(numeros_tupla[-1])


#sublista(slicing)
print(f"Primeros 3 elementos: {numeros_tupla[:3]}")
print(f"Ultimos 2 elementos: {numeros_tupla[-2:]}")
print(f"Elementos del medio: {numeros_tupla[1:-1]}")

print(f"Longitud de la tupla: {len(numeros_tupla)}")

#Desempaquetado de tuplas
a, b, c, d, e = numeros_tupla #a corresponde a 1, b a 2, 3 a c, 4 a d y 5 a e.
print(f"Desempaquetado: a={a}, b={b}, c={c}, d={d}, e={e}")


#El asterisco significa multiples elementos (los separa de los que si vamos a usar)
primer_elemento, *resto_elementos = numeros_tupla
print(f"Desempaquetado: primero ={primer_elemento}\nResto={resto_elementos}")

_, segundo_elemento, *resto_elementos = numeros_tupla
print(f"Desempaquetado: primero ={segundo_elemento}\nResto={resto_elementos}")


print("### MATRIZ ###") #LISTA DE LISTA
matriz = [
       [1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]
]

print(f"Matriz: {matriz}")
print(f"Elemento [2][2]: {matriz[1][1]}")

persona=("Juan", 23, 1.85, True)
print(f"Persona: {persona}")

print(f"El elemento con valor 'Juan' esta en la tupla?: {"SI" if 'Juan' in persona else "NO"}")
print(f"El elemento con valor '10' esta en la numeros_tupla?: {"SI" if 10 in numeros_tupla else "NO"}")
print(f"Tupla original: {numeros_tupla}")


#CONVIERTO A LISTA
lista_numeros = list(numeros_tupla)
print(f"Tupla convertida a lista: {lista_numeros}")

#En este punto como se convirtio a lista se pueden hacer modificaciones
lista_numeros.append(88)
print(f"Tupla convertida a lista: {numeros_tupla}")

tupla_numeros = tuple(lista_numeros)
print(f"Lista convertida a tupla: {tupla_numeros}")
