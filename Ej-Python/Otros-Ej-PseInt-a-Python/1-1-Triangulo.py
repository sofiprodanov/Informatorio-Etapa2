#1. Elaborar un codigo para determinar el tipo de un triángulo dado el tamaño de sus lados.

print("Teniendo en cuenta que A es el lado izquierdo, B la hipotenusa y C la base: ")
print("Para determinar el tipo de triángulo, necesito que me indiques la medida de cada lado en cm:")

while True:
    try:
        a = float(input("El lado A mide: "))
        b = float(input("La hipotenusa mide: "))
        c = float(input("La base mide: "))

        if a == 0 or b == 0 or c == 0:
            print("Ingresa un numero mayor a cero.")
            continue

        break
    except ValueError:
        print("Por favor, ingresa un valor numerico valido.")

if a == b == c:
    print("El triangulo es equilatero.")
elif a == b or b == c or c == a:
    print("El triangulo es isosceles.")
else:
    print("El triangulo es escaleno.")