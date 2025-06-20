# 7. La nota final en la escuela de informática se obtiene en función de 3 notas. La nota final del primer examen, la nota del segundo examen y 
# una nota de concepto del profesor. La nota del primer examen se pondera como 30% de la nota final, la del segundo examen como el 50% y la de 
# concepto como el 20% de la nota final. Elabore un algoritmo que en base a esas tres notas calcule la nota final.


#Validaciones
while True:
    try:
        nota1 = float(input("Nota del primer examen: "))
        if 0 <= nota1 <= 100:
            break
        else:
            print("Error: La nota debe estar entre 0 y 100.")
    except ValueError:
        print("Error: Ingrese un numero valido.")

while True:
    try:
        nota2 = float(input("Nota del segundo examen: "))
        if 0 <= nota2 <= 100:
            break
        else:
            print("Error: La nota debe estar entre 0 y 100.")
    except ValueError:
        print("Error: Ingrese un número válido.")

while True:
    try:
        concepto = float(input("Nota de concepto del profesor: "))
        if 0 <= concepto <= 100:
            break
        else:
            print("Error: La nota debe estar entre 0 y 100.")
    except ValueError:
        print("Error: Ingrese un número válido.")

#Calculo
nota_final = (nota1 * 0.30) + (nota2 * 0.50) + (concepto * 0.20)

# round(nota_final, 2) muestra el resultado con 2 decimales (más legible).
print(f"\nLa nota final es: {round(nota_final, 2)}%") 