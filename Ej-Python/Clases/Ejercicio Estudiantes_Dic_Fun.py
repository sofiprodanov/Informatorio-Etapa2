#Verificar si aprobo la materia sacando el promedio de los 3 meses por materia a partir del sig. diccionario

#NO ES UN DICCIONARIO SIMPLE, ES UN DICCIONARIO DENTRO DE LISTAS.

estudiantes = [
    {
        "nombre": "Juan",
        "notas": {
            "mate": {
                "trimestre_uno": 10,
                "trimestre_dos": 5,
                "trimestre_tres": 8,
            },
            "castellano": {
                "trimestre_uno": 10,
                "trimestre_dos": 5,
                "trimestre_tres": 8,
            },
            "ingles": {
                "trimestre_uno": 10,
                "trimestre_dos": 5,
                "trimestre_tres": 8,
            }
        }
    },
    {
        "nombre": "Pablo",
        "notas": {
            "mate": {
                "trimestre_uno": 10,
                "trimestre_dos": 5,
                "trimestre_tres": 8,
            },
            "castellano": {
                "trimestre_uno": 10,
                "trimestre_dos": 5,
                "trimestre_tres": 8,
            },
            "ingles": {
                "trimestre_uno": 10,
                "trimestre_dos": 5,
                "trimestre_tres": 8,
            }
        }
    }
]

# Puntos:
# 1. Consultar alumno.
# 2. Consultar materia.
# 3. Si el alumno no figura en el diccionario, que se agregue a la lista junto a la materia a consultar
# 4. Sacar promedio de los 3 meses por materia
# 5. Verificar si aprobo la materia segun el promedio

#FUNCION CONSULTA ESTUDIANTE
def buscar_estudiante(nombre):
    for i, estudiante in enumerate(estudiantes): #enumerate > para obtener tanto el indice como el estudiante. Ignorando mayusculas y minusculas
        if estudiante["nombre"].lower() == nombre.lower():
            return i, estudiante #devuelve indice y estudiante
    return None, None

#FUNCION PARA AGREGAR ESTUDIANTE
def agregar_estudiante(nombre):
    """Agrega un nuevo estudiante"""

    nuevo_estudiante = {
        "nombre": nombre,
        "notas": {}
    }
    estudiantes.append(nuevo_estudiante)
    return len(estudiantes) - 1, nuevo_estudiante #Devuelve el índice del nuevo estudiante y el estudiante mismo

#FUNCION PARA AGREGAR MATERIA
def agregar_materia(estudiante, materia):
    """Agrega una nueva materia al estudiante con notas en 0"""

    if materia not in estudiante["notas"]: #VERIFICA SI LA MATERIA EXISTE. SI NO EXISTE, LA AGREGA Y PIDE SUS NOTAS
        estudiante["notas"][materia] = { 
            "trimestre_uno": float(input("Nota del primer trimestre: ")),
            "trimestre_dos": float(input("Nota del segundo trimestre: ")),
            "trimestre_tres": float(input("Nota del tercer trimestre: ")),
        }
        return True #SI AGREGO LA MATERA
    return False #SI YA EXISTIA

#FUNCION PARA CALCULAR PROMEDIO Y APROBACION
def calcular_promedio(notas_materia):
    """Calcula el promedio de una materia"""
    """Verifica si el promedio aprueba la materia (>=6)"""
    
    promedio = round(sum(notas_materia.values()) / 3, 2) #SUMA LOS VALORES, DIVIDE POR 3 Y REONDEA CON 2 DECIMALES
    print(f"El promedio es {promedio}.")

    if promedio >= 6:
        print("Materia aprobada!")
    else:
        print("Materia desaprobada.")

def main():
    #1. Consultar estudiante
    nombre_estudiante = input("Ingrese el nombre del estudiante: ")
    indice, estudiante = buscar_estudiante(nombre_estudiante)

    if estudiante is None:
        print(f"Estudiante {nombre_estudiante} no encontrado. Vamos a agregarlo!")
        indice, estudiante = agregar_estudiante(nombre_estudiante)
    
    #2. Consultar materia
    materia = input("Ingrese la materia a consultar: ").lower()

    #Verifica si la materia existe. Si no existe, la agrega
    if materia not in estudiante["notas"]:
        print(f"Materia {materia} no encontrada. Agregando nueva materia con sus notas.")
        agregar_materia(estudiante, materia)
    
    #4. Sacar promedio de los 3 meses por materia e indicar si aprobo o no
    notas = estudiante["notas"][materia] #llama al diccionario dentro de la lista
    print(f"\nNotas en {materia}: {notas}") #muestra las notas de la materia que se llamo
    promedio = calcular_promedio(notas) 

if __name__ == "__main__":
    main()


    
