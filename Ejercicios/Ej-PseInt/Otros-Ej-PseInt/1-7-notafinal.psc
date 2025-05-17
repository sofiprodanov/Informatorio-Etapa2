Algoritmo notafinal
	
	Definir nota1, nota2, notaconcep, notapond1, notapond2, notapondconcep, notafinalpond Como Real
	
	Escribir "Para determinar la nota final tengo que saber las notas (en porcentaje):"
	Escribir "Del primer examen:"
	Leer nota1
	Escribir "Del segundo examen:"
	Leer nota2
	Escribir "Del concepto del profe:"
	Leer notaconcep
	
	//nota1 > 1°ex 30% , nota2 > 2°ex 50%, nota3 > concep. profesor 20%.	
	notapond1 = (nota1 * 30)/100
	notapond2 = (nota2 * 50)/100
	notapondconcep = (notaconcep * 20)/100
	
	notafinalpond = notapond1 + notapond2 + notapondconcep
	
	Escribir "La nota final es ",notafinalpond,"%."
	
FinAlgoritmo
