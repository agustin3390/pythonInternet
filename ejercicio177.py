class Alumno:

    def inicializacion(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print("nombre:",self.nombre)
        print("nota:",self.nota)

    def regularidad(self):
        if self.nota >= 4:
            print("el alumno esta regular..")
        else:
            print("el alumno no esta regular..")


#bloque principal

alumno1 = Alumno()
alumno1.inicializacion("pedro", 10)
alumno1.imprimir()
alumno1.regularidad()

alumno2 = Alumno()
alumno2.inicializacion("Ana", 3)
alumno2.imprimir()
alumno2.regularidad()