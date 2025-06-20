Crearemos una clase Persona en la cual guardaremos la
información general de cada persona, y una clase
Estudiante que heredará los atributos y métodos de la
clase anterior con información más precisa sobre la
carrera que está estudiando.

-> En la clase Persona() indicaremos los atributos
nombre y apellido.
Además, definimos un método el cual nos muestre
ambos atributos en un mismo mensaje
(nombre_completo()).
-> En la clase Estudiante() heredamos de Persona() sus
atributos y métodos, por eso mismo, en el constructor
requerimos los datos de nombre y apellido nuevamente,
lo que nos permite pasar dichos valores a su clase padre
mediante super() pero agregando el nuevo atributo carrera.
Por último, definimos un método que nos devuelva que
carrera estudia actualmente el estudiante.
