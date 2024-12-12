class Agenda:

    def __init__ (self):
        self.contactos = {}

    def menu(self):
        opcion = 0
        while opcion != 5:
            print("-------------------------------------")
            print("1- cargar un contacto en la agenda.")
            print("2- listado completo de la agenda.")
            print("3- consulta ingresando el nombre de la persona.")
            print("4- modificacion de su telefono y mail.")
            print("5- finalizacion del programa.")
            opcion = int(input("ingrese una de las opciones: "))
            if opcion == 1:
                self.cargar()
            else:
                if opcion == 2:
                    self.listado()
                else:
                    if opcion == 3:
                        self.consulta_nombre()
                    else:
                        if opcion == 4:
                            self.modificacion()
                        else:
                            if opcion == 5:
                                print("finalizacion del programa.")
                            else:
                                print("error. vuelva a intentar.")
    
    def cargar(self):
        nombre = input("ingrese el nombre de la persona: ")
        telefono = input("ingrese el telefono: ")
        mail = input("ingrese el mail de la persona.")
        self.contactos[nombre]= (telefono, mail)

    
    def listado(self):
        print("listado de contactos.")
        for nombre in self.contactos:
            print(nombre ,self.contactos[nombre][0], self.contactos[nombre][1])
    
    def consulta_nombre(self):
        nombre = input("ingrese el nombre a buscar: ")
        if nombre in self.contactos:
            print(nombre, self.contactos[nombre][0], self.contactos[nombre][1])
        else:
            print("no se encuentra el nombre ingresado.")
    
    def modificacion(self):
        nombre = input("ingrese el nombre de la agenda que quiere modificar: ")
        if nombre in self.contactos:
            telefono = input("ingrese el nuevo telefono: ")
            mail = input("ingrese el nuevo mail: ")
            self.contactos[nombre] = (telefono, mail)

    

#bloque principal

agenda1 = Agenda()
agenda1.menu()