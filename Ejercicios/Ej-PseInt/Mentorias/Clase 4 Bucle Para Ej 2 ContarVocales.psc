Algoritmo ContarVocales
	
	//Ej 2: cuenta vocales
	
    Definir palabra Como Cadena
    Definir i, contador_vocales Como Entero
    contador_vocales <- 0
    
    Escribir "Ingrese una palabra: "
    Leer palabra
    
    Para i <- 0 Hasta Longitud(palabra) - 1 Con Paso 1 Hacer
        letra <- Subcadena(palabra, i, i)
        Si letra = "a" O letra = "e" O letra = "i" O letra = "o" O letra = "u" Entonces
            contador_vocales <- contador_vocales + 1
        FinSi
    FinPara
    
    Escribir "La palabra tiene ", contador_vocales, " vocales."
FinAlgoritmo