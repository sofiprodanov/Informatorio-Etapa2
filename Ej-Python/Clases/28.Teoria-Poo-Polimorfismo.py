class A():
    def saludo(self):
        print("Mensaje de la clase A")

class B(A):
    def saludo(self):
        print("Mensaje de la clase B")

class C(A):
    def saludo(self):
        print("Mensaje de la clase C")

ejemplo1 = B()
ejemplo2 = C()

#Ambos tiene el mismo nombre de metodo, pero el comportamiento es distito
ejemplo1.saludo() #Mensaje desde la clase B
ejemplo2.saludo() #Mensaje desde la clase C

#Lo que estamos haciendo es sobrescribir un método heredado, de esta manera cuando instanciamos un objeto con una clase hija, podemos usar el mismo
#nombre de método, pero con distinto comportamiento debido a la clase de la que se instancia el objeto.

