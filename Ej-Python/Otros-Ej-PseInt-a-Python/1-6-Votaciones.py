# 6. Se desea calcular el promedio de votos a obtener por cinco partidos políticos. Se realiza una encuesta acumulando los votos obtenidos
# por cada partido y el número de votos indecisos. Realizar un algoritmo que determine el porcentaje de votos de cada partido y el de indecisos, 
# respecto del total de encuestados.

print("Cuantos votos tuvo el: ")
p1 = int(input("Partido 1: "))
p2 = int(input("Partido 2: "))
p3 = int(input("Partido 3: "))
p4 = int(input("Partido 4: "))
p5 = int(input("Partido 5: "))
indecisos = int(input("Indecisos: "))

total_votos = p1 + p2 + p3 + p4 + indecisos
	
p1_porcentaje = (p1 / total_votos) * 100
p2_porcentaje = (p2 / total_votos) * 100
p3_porcentaje = (p3 / total_votos) * 100
p4_porcentaje = (p4 / total_votos) * 100
p5_porcentaje = (p5 / total_votos) * 100
indecisos_porcentaje = (indecisos / total_votos) * 100
	
print("\nResultados:")
print(f"El {p1_porcentaje:.2f}% corresponde al primer partido")
print(f"El {p2_porcentaje:.2f}% corresponde al segundo partido")
print(f"El {p3_porcentaje:.2f}% corresponde al tercer partido")
print(f"El {p4_porcentaje:.2f}% corresponde al cuarto partido")
print(f"El {p5_porcentaje:.2f}% corresponde al quinto partido")
print(f"El {indecisos_porcentaje:.2f}% corresponde a votos indecisos")

# la expresión :.2f es una especificación de formato que controla cómo se muestra un número.
# : → Indica que viene un especificador de formato
# .2 → Indica que queremos 2 decimales después del punto
# f → Indica que es un número de tipo float (flotante/decimal)