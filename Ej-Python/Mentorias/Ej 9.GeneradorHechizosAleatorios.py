# Escribe una función que combine aleatoriamente un prefijo y sufijo de listas dadas y cree un hechizo mágico
#(Usar módulo random)

import random

def generar_hechizos():
    prefijos = ['Abra', 'Alakaza', 'Zendo', 'Foco', 'Magi']
    sufijos = ['cadabra', 'lumos', 'mora', 'nox', 'flama']
    prefijo_aleatorio = random.choice(prefijos)
    sufijos_aleatorio = random.choice(sufijos)
    hechizo = f"{prefijo_aleatorio}-{sufijos_aleatorio}" #tambien se puede hacer hechizo = f"{prefijo_aleatorio}+{sufijos_aleatorio}"
    return hechizo #si el print no esta dentro de la funcion hay que retornar para poder reutilizar la funcion

print(generar_hechizos())