Algoritmo Calculadora_Simple
	
	Definir num1, num2, resultado Como Real
	Definir operacion Como Caracter
	
	Escribir "Ingrese el primer numero: "
    Leer num1
    
    Escribir "Ingrese el segundo numero: "
    Leer num2
	
	Escribir "¿Que operaciones queres realizar? (+, -, *, /: )"
	Leer operacion
	
	Segun operacion Hacer
		Caso "+":
			resultado = num1 + num2
			Escribir "El resultado de la suma es: ", resultado
		Caso "-":
			resultado = num1 - num2
			Escribir "El resultado de la resta es: ", resultado
		Caso "*":
			resultado = num1*num2
			Escribir "El resultado de la multiplicacion es: ", resultado
		Caso "/":
			Si num2 = 0 Entonces
				Escribir "Error: No se puede dividir por cero."
			SiNo
				resultado = num1/num2
				Escribir "El resultado de la division es: ", resultado
			FinSi
		De Otro Modo:
			Escribir "Error: Operacion no valida. Use +, -, * o /."
	Fin Segun
	
FinAlgoritmo
