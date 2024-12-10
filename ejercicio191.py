class Alumnos:

    def __init__ (self):
        self.listaAlumnos = []
        self.listaNotas = []
        self.menu()

    def menu(self):
        opcion = 0
        while opcion != 4:
            print("------------------------------------")
            print("1- cargar alumnos.")
            print("2- lista alumnos.")
            print("3- mostrar alumnos con notas mayores o igual a 7")
            print("4- finalizar el programa.")
            opcion = int(input("ingrese una de las opciones: "))
            if opcion == 1:
                self.cargar()
            else:
                if opcion == 2:
                    self.lista()
                else:
                    if opcion == 3:
                        self.mostrar_mayores()
    
    
    def cargar(self):
        for i in range(5):
            alumno = input("ingrese el nombre del alumno: ")
            self.listaAlumnos.append(alumno)
            nota = float(input("ingrese la nota: "))
            self.listaNotas.append(nota)
    
    def lista(self):
        print("listado de alumnos y sus notas..")
        for i in range(5):
            print(self.listaAlumnos[i], self.listaNotas[i])
    
    def mostrar_mayores(self):
        for i in range(5):
            if self.listaNotas[i] >= 7:
                print(self.listaAlumnos[i], self.listaNotas[i])
    
# bloque principal

alumnos1 = Alumnos()
alumnos1.menu()
