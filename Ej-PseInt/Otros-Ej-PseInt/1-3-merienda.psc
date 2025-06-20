Algoritmo merienda
	
	//3. Elabore un algoritmo para representar la acción de servir la merienda. El comensal puede tomar té, café, café con leche, té con leche
	//y puede o no ponerle azúcar, si le pone puede ponerle una, dos o tres cucharadas.
	
	Definir bebida Como Caracter
	Definir op, azucar Como Entero
	
	Escribir "Hora de la merienda! Que te gustaria tomar? Las opciones son (indicar nro de opcion):"
	
	Repetir //cuando el cliente ingresa un numero de opcion fuera del rango indicado
		Escribir "1. Te"
		Escribir "2. Cafe"
		Escribir "3. Cafe c/leche" 
		Escribir "4. Te c/leche"
		Leer op
		
		Segun op Hacer
			1:
				bebida = "Te"
			2:
				bebida = "Cafe"			
			3:
				bebida = "Cafe c/leche"
			4:
				bebida = "Te c/leche"
				
			De Otro Modo:
				Escribir "La opcion que me indicas no se encuentra disponible dentro de la carta. Las opciones disponibles son (indicar con el numero):"
		Fin Segun
	Hasta Que (op >= 1) y (op <= 4)
	
	Repetir // cliente pide cantidad de cucharadas distintas a las indicadas
		Escribir "Cuantas cucharadas de azucar te gustaria? Ninguna (cero), 1, 2 o 3 cucharadas?"
		Leer azucar
		
		Si (azucar < 0) o (azucar > 3) Entonces
			Escribir "La cantidad esta fuera del rango indicado."
		FinSi
	Hasta Que (azucar >= 0) y (azucar <= 3)
		
	Si azucar = 0 Entonces // confirma la orden con la cantidad de azucar
		Escribir "Perfecto! Entonces su orden es ", bebida," sin azucar."
	SiNo
		Escribir "Perfecto! Entonces su orden es ", bebida, " con ", azucar," de azucar."
	Fin Si
	
FinAlgoritmo
