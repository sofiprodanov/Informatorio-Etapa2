Algoritmo login_simulado_buclemientras
	Definir usuario, contrasenia Como Cadena
	Definir intentos Como Entero
	intentos = 3
	
	Mientras intentos > 0 Hacer
		
		Escribir "Ingrese su Usuario: "
		Leer usuario
		Escribir "Ingrese su Contrase�a: "
		Leer contrasenia
		
		//usuario --> admin / contrase�a --> dificil123
		Si usuario == "admin" y contrasenia == "dificil123" Entonces 
			Escribir "Login Exitoso. Bienvenido!"
			intentos = 0
		SiNo
			Escribir "Usuario o contrase�a incorrectos!"
			intentos = intentos - 1
			
		Fin Si
	FinMientras
	
	
FinAlgoritmo