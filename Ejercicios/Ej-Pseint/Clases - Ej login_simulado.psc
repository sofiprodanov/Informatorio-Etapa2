Algoritmo login_simulado
	Definir usuario, contrasenia Como Cadena
	Definir intentos Como Entero
	intentos = 3
	
	Para i= 1 Hasta 3 Con Paso 1 Hacer
		Escribir "Ingrese su Usuario: "
		Leer usuario
		Escribir "Ingrese su Contraseña: "
		Leer contrasenia
		
		Si usuario == "admin" y contrasenia == "dificil123" Entonces 
			Escribir "Login Exitoso. Bienvenido!"
		SiNo
			Escribir "Usuario o contraseña incorrectos!"
		Fin Si
	Fin Para
	
FinAlgoritmo