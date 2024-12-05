class Persona:

    def inicializacion(self,nombre):
        self.nombre = nombre

    def imprimir(self):
        print("el nombre de la persona es:", self.nombre)



#bloque principal

persona1 = Persona()
persona1.inicializacion("juan")
persona1.imprimir()

persona2 = Persona()
persona2.inicializacion("pedro")
persona2.imprimir()