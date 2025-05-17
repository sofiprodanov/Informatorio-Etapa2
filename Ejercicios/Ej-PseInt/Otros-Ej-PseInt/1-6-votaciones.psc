Algoritmo votaciones
	
	// Se desea calcular el promedio de votos a obtener por cinco partidos políticos. 
	//Se realiza una encuesta acumulando los votos obtenidos por cada partido y el número de votos indecisos. 
	//Realizar un algoritmo que determine el porcentaje de votos de cada partido y el de indecisos, respecto del total de encuestados.
	
	Definir p1, p2, p3, p4, indecisos, total_votos Como Entero
	
	Escribir "Cuantos votos tuvo el: "
	Escribir "Partido 1:"
	Leer p1
	Escribir "Partido 2:"
	Leer p2
	Escribir "Partido 3:"
	Leer p3
	Escribir "Partido 4:"
	Leer p4
	Escribir "Partido 5:"
	Leer p5
	Escribir "Indecisos:"
	Leer indecisos
	
	total_votos = p1 + p2 + p3 + p4 + indecisos
	
	p1pond = (p1 * total_votos)/100
	p2pond = (p2 * total_votos)/100
	p3pond = (p3 * total_votos)/100
	p4pond = (p4 * total_votos)/100
	p5pond = (p5 * total_votos)/100
	indecisospond = (indecisos * total_votos)/100
	
	Escribir "El ",p1pond,"% corresponde al primer partido, el ",p2pond,"% corresponde al segundo, el ",p3pond,"% corresponde al tercero, el ",p4pond,"% corresponde al cuarto,  el ",p5pond,"% corresponde al quinto, el ",indecisospond,"% a los votos indecisos."	
FinAlgoritmo
