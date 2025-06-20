
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))

operacion = input("¿Qué operación quiere realizar? (+, -, *, /): ")

if operacion == "+":
    resultado = num1 + num2
    print(f"El resultado de la suma es: {resultado}")
elif operacion == "-":
    resultado = num1 - num2
    print(f"El resultado de la resta es: {resultado}")
elif operacion == "*":
    resultado = num1 * num2
    print(f"El resultado de la multiplicación es: {resultado}")
elif operacion == "/":
    if num2 == 0:
        print("Error: No se puede dividir por cero.")
    else:
        resultado = num1 / num2
        print(f"El resultado de la división es: {resultado}")
else:
    print("Error: Operación no válida. Use +, -, * o /.")