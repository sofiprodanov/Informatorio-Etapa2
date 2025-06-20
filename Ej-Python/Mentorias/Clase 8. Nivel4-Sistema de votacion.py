# Se quiere implementar un sistema básico de votación donde cada persona puede votar una 
# sola vez por su candidato favorito
#  A- El programa debe permitir que tres personas voten
#  B- Antes de permitir votar, debe pedir el nombre del votante
#  C- Si el votante ya emitió su voto anteriormente, debe mostrar un mensaje: “Ya votaste” y 
# no permitirle votar de nuevo
#  D- Si es la primera vez que vota, el sistema debe pedir el nombre del candidato al que desea 
# votar.
#  E- Al finalizar, el programa debe mostrar los resultados con la cantidad de votos que recibió


#ES UN SET(CONJUNTO) PORQUE NO TIENE QUE REPETIRSE
votos = {} #los votos que fueron teniendo los candidatos
votantes = set() #personas que ya votaron 

for i in range(3):
    nombre = input("Tu nombre: ")
    if nombre in votantes:
        print("Ya votaste.")
    else:
        candidato = input("Vota por un cantidado: ")
        votos[nombre] = votos.get(candidato, 0) + 1
        votantes.add(nombre)
print("Resultados: ", votos)
