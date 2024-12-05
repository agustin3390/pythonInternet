class Persona():

    def inicializacion(self):
        self.nombre = input("ingrese el nombre de la persona: ")
        self.edad = int(input("ingrese la edad de la persona: "))
    
    def imprimir(self):
        print("nombre: ", self.nombre)
        print("edad: ", self.edad)

    def mayor_edad(self):
        if self.edad >= 18:
            print(self.nombre,"es mayor de edad.")
        else:
            print(self.nombre,"no es mayor de edad.")
