Algoritmo validar_contraseņa
	
	Definir password Como Caracter
	
	Escribir "Ingresa la contraseņa: "
	Leer password
	
	Mientras password <> "1234" Hacer
		//Escribir el mensaje que se va a Repetir
		Escribir "Contraseņa incorrecta. Intente nuevamente."
		//Para que salga el input para completar nuevamente la contraseņa
		Leer password
	Fin Mientras
	
	Escribir "Acceso concedido."
	
FinAlgoritmo
