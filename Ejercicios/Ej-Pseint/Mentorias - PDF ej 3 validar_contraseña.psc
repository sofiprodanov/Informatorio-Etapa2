Algoritmo validar_contraseña
	
	Definir password Como Caracter
	
	Escribir "Ingresa la contraseña: "
	Leer password
	
	Mientras password <> "1234" Hacer
		//Escribir el mensaje que se va a Repetir
		Escribir "Contraseña incorrecta. Intente nuevamente."
		//Para que salga el input para completar nuevamente la contraseña
		Leer password
	Fin Mientras
	
	Escribir "Acceso concedido."
	
FinAlgoritmo
