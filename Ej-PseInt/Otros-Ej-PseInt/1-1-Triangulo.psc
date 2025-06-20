Algoritmo triangulo
	//1. Elaborar un algoritmo para determinar el tipo de un triángulo dado el tamaño de sus lados.
		
	Definir isosceles, equilatero, escaleno Como Caracter
	Definir a, b, c Como Real
	
	Escribir "Teniendo en cuenta que A, es el lado izquierdo, B, la hipotenusa y, C, la base: Para determinar el tipo de triangulo, necesito que me indiques la medida de cada lado en cm: "

	Repetir
		Escribir "El lado A mide:"
		Leer a
		Escribir "La hipotenusa mide: "
		Leer b
		Escribir "La base mide: "
		Leer c
		
		Si (a = 0) o (b = 0) o (c = 0) Entonces
			Escribir "Ingresa un numero mayor a cero."
		FinSi
	Hasta Que (a > 0) y (b > 0) y (c > 0)
	
	Si (a = b) y (b = c) y (a = c) Entonces // las tres condiciones deben cumplirse
		Escribir "El triangulo es equilatero."
	SiNo
		Si (a = b) o (b = c) o (c = a) Entonces // al menos una condicion debe cumplirse
			Escribir "El triangulo es isoceles."
		Sino
			Escribir "El triangulo es escaleno." // no se pone condicion ya que es por descarte (cuando ningun lado es igual)
		FinSi
	Fin Si
	
FinAlgoritmo
