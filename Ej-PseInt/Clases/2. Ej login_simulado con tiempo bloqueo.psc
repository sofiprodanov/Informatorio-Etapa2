Algoritmo login_simulado
    Definir usuario, contrasenia Como Cadena
    Definir intentos, i, tiempobloqueo Como Entero
    intentos = 3
	tiempobloqueo = 10 // tiempo de bloqueo en segundos
    
    Mientras intentos > 0 Hacer
		//pide ingreso de usuario -> admin  contrase�a -> dificil123 &
        Escribir 'Ingrese su Usuario:'
        Leer usuario
        
        Escribir 'Ingrese su Contrase�a:'
        Leer contrasenia
        
        // validacion
        Si usuario = "admin" y contrasenia = "dificil123" Entonces
            Escribir 'Login exitoso. Bienvenido!'
            intentos = 0
        SiNo
            Escribir 'Usuario o contrase�a incorrectos!'
            intentos =  intentos - 1
			Escribir "Le quedan " intentos " intentos."
			     // Si agota los 3 intentos + simula tiempo de espera
			     Si intentos = 0 Entonces
					Escribir "Cuenta bloqueada. Espere ", tiempobloqueo, " segundos."
					Para i = tiempobloqueo Hasta 1 Con Paso -1 Hacer
			             Escribir "Tiempo restante: ", i, " segundos."
			             Esperar 1 Segundo
		             Fin Para
		             Escribir "Cuenta desbloqueada. Intente nuevamente."
					 Esperar 3 Segundos
					 Limpiar Pantalla
					 intentos = 3 // lleva al inicio pidiendo el acceso a la cuenta
			     FinSi
		FinSi
    FinMientras
FinAlgoritmo

