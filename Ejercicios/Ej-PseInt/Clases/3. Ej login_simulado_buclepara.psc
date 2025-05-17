Algoritmo login_simulado_buclepara
	Definir usuario, contrasenia Como Cadena
	Definir intentos Como Entero
	intentos = 3
	
	
	Para i = 0 Hasta intentos Con Paso 1 Hacer
		Escribir "Ingrese su Usuario: "
		Leer usuario
		Escribir "Ingrese su Contraseña: "
		Leer contrasenia
		
		//usuario --> admin / contraseña --> dificil123
		Si usuario == "admin" y contrasenia == "dificil123" Entonces 
			Escribir "Login Exitoso. Bienvenido!"
			i = intentos // seria lo mismo poner i = 3, pero es mejor usar la variable
		SiNo
			Escribir "Usuario o contraseña incorrectos!"
		Fin Si
	Fin Para
	
	//Para simplificarlo mas podemos eliminar la variable intentos = 3, y completar:
	//En la linea 6 "Para i = 0 Hasta 3 Con Paso 1 Hacer";
	//En la linea 14 poner "i = 3"	
	//Dentro del bucle Para si i = 0, va a ejecutar 4 veces (0, 1, 2, 3).
	//Se puede reemplazar el iterador (i) por cualquier otro valor (se debe cambiar administrador el usuario de pseint)
	
FinAlgoritmo
