Algoritmo Conexion_Internet
	
	//Ej 4: Estado de la conexion a internet
	
	Definir respuesta Como Cadena
	Definir conexion_activa, verificarconexion Como Logico
	
	conexion_activa = Falso
	verificarconexion = Falso
	
	Mientras conexion_activa = Falso Hacer
		Escribir "¿Se verifico la conexion?"
		Leer respuesta
		Si respuesta = "si" Entonces
			verificarconexion = Verdadero
		FinSi
		
        Si verificarconexion = Verdadero Entonces
            conexion_activa = Verdadero
            Escribir "Conectado."
        Sino
            Escribir "Reintentando en 5 segundos..."
            Esperar 5 segundos
        FinSi
    FinMientras
	
FinAlgoritmo
