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
	
	p1_porcentaje = (p1 / total_votos) * 100
	p2_porcentaje = (p2 / total_votos) * 100
	p3_porcentaje = (p3 / total_votos) * 100
	p4_porcentaje = (p4 / total_votos) * 100
	p5_porcentaje = (p5 / total_votos) * 100
	indecisos_porcentaje = (indecisos / total_votos) * 100
	
	Escribir "El ",p1_porcentaje,"% corresponde al primer partido.
	Escribir "El ",p2_porcentaje,"% corresponde al segundo."
	Escribir "El ",p3_porcentaje,"% corresponde al tercero."
	Escribir "El ",p4_porcentaje,"% corresponde al cuarto."
	Escribir "El ",p5_porcentaje,"% corresponde al quinto."
	Escribir "El ",indecisos_porcentaje,"% a los votos indecisos."	
FinAlgoritmo
