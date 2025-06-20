Algoritmo cambio_de_letras
	
	Definir  a, b, c, aux Como Caracter
	
	Imprimir 'En este programa veremos como en la ejecucion del programa los valores de las variables cambian, pero con letras.'
	Imprimir 'Ingrese un numero: '
	Leer a
	
	Imprimir 'Ingrese otro numero: '
	Leer b
	
	Imprimir 'Ingrese otro numero mas: '
	Leer c
	
	Imprimir 'Los valores ingresados son, variable a: ', a, ', variable b: ', b, ', variable c: ', c
	
	aux = a //utilizamos aux para guardar el valor de la variable A para no perderlo en las asignaciones
	a = b // a ocupa el valor de b
	b = c // b ocupa el valor de c
	c = aux // c ocupa el valor que tenia a al principio, pero que lo guardamos en la variable aux 
	
	Imprimir 'Ahora probamos intercambiar los valores: variable a: ', a, ', variable b: ', b, ', variable c: ', c

	
	
FinAlgoritmo
