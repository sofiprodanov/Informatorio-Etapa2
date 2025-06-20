# Creá un programa que guarde las notas de varios estudiantes en un diccionario.
# Luego, crea funciones para:
# A- Agregar estudiante con sus notas.
# B- Calcular el promedio de un estudiante
# C- Mostrar los estudiantes aprobados (promedio >= 6)


estudiantes = {
    'Ana': [9, 8, 10],
    'Luis': [4, 6, 5],
    'Carlos': [10, 10, 9]
}

#Funcion para agregar estudiantes:
#base es diccionario, es para hacerlo mas reutilizable por si se quiere reutilizar en otros diccionarios.
def agregar_estudiantes (base, nombre, notas):
    base[nombre] = notas

agregar_estudiantes(estudiantes, "Elias", [10, 10, 10]) #sigue los parametros
print(estudiantes)


#Funcion para obtener el promedio
def promedio_estudiante(base, nombre):
    notas = base[nombre] #se llama al valor de cada uno de los nombres.
    return sum(notas) / len(notas)

print(promedio_estudiante(estudiantes, "Ana"))


#Funcion que muestra estudiantes aprobados
# def estudiantes_aprobados(base):
#     aprobados = []
#     for nombre, notas in base.items(): #desempaquetamos y luego aplicamos el metodo que recorre el diccionario devolviendo tanto la clave como el valor asociado.
#         promedio = sum(notas) / len(notas)
#         if promedio >= 6:
#             aprobados.append(nombre)
#     return aprobados

# print(estudiantes_aprobados(estudiantes))



#Funcion que muestra los estudiantes aprobados y desaprobados
def estudiantes_aprobados(base):
    aprobados = []
    desaprobados = []
    for nombre, notas in base.items(): #desempaquetamos y luego aplicamos el metodo que recorre el diccionario devolviendo tanto la clave como el valor asociado.
        promedio = sum(notas) / len(notas)
        if promedio >= 6:
            aprobados.append(nombre)
        else:
            desaprobados.append(nombre)
    return aprobados, desaprobados

aprobados, desaprobados = estudiantes_aprobados(estudiantes)

print(f"Ha{'n' if len(aprobados) > 1 else 's'} aprobado {', '.join(aprobados)}. ¡Excelente! Continu{'en' if len(aprobados) > 1 else 'a'} asi.")
print(f"Ha{'n' if len(desaprobados) > 1 else 's'} desaprobado {', '.join(desaprobados)}. Deberia{'n' if len(desaprobados) > 1 else ''} revisar los temas.")

# .join() > convertir la lista aprobados en un string legible para humanos, ideal para mostrar en pantalla.
# Ha{'n' if len(desaprobados) > 1 else 's' > lógica para que diga "Has" o "Han" según si hay uno o varios desaprobados
# Deberia{'n' if len(desaprobados) > 1 else ''} revisar los temas > lógica para que diga "Deberia" o "Deberian" según si hay uno o varios desaprobados.
