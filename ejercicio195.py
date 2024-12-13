class Socio:

    def __init__ (self):
        self.nombre = input("ingrese el nombre del socio:")
        self.antiguedad = int(input("ingrese la antiguedad del mismo: "))
    
    def imprimir(self):
        print(self.nombre,"tiene", self.antiguedad,"de antiguedad.")

    def retornar_antiguedad(self):
        return self.antiguedad
    
class Club:

    def __init__ (self):
        self.socio1 = Socio()
        self.socio2 = Socio()
        self.socio3 = Socio()
    
    def imprimir(self):
        self.socio1.imprimir()
        self.socio2.imprimir()
        self.socio3.imprimir()
    
    def mayor_antiguedad(self):
        if self.socio1.retornar_antiguedad() > self.socio2.retornar_antiguedad() and self.socio1.retornar_antiguedad() > self.socio3.retornar_antiguedad():
            print(self.socio1.nombre,"es el socio con mas antiguedad con:", self.socio1.antiguedad)
        else:
            if self.socio2.retornar_antiguedad() > self.socio3.retornar_antiguedad():
                print(self.socio2.nombre,"es el socio con mas antiguedad con:", self.socio2.antiguedad)
            else:
                print(self.socio3.nombre,"es el socio con mas antiguedad con:", self.socio3.antiguedad)

# bloque principal

club1 = Club()
club1.imprimir()
club1.mayor_antiguedad()