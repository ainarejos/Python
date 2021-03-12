"""
Este proyecto es una recopilacion de pruebas, esta se realizaron a medida
que se fueron aprendiendo nuevos conceptos del lenguaje python.

Desarrollador: Adán Inarejos.
Fecha Inicio: 12/03/2021.
Fecha Final: --/--/--.
ID: PyCharm.
"""

#Creación de una clase.
class HelloWorld:

    #Variables/Atributos.
    a="Hello World"

    #Matriz.
    array = ["Carlos", "Joshua", "Ismael"]

    #Añadir itema a raiz
    array.append("Adan")

    #Metodo de una clase.
    def mostrar_pantalla(self):
        # Print Simple.
        print("Hello World!")

        #Mostar items de la matriz.
        print(self.array[1] + ", " + self.array[2])

        #Bucle para mostrar todos los items de una matriz.
        for x in self.array:
            print(x)

#Finalización de la clase.

#Intanciar una clase y utilizar un metodo.
x = HelloWorld
x.mostrar_pantalla(x)