class Punto:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def imprimir(self):
        print("puntos en el plano: ")
        print("x:", self.x)
        print("y:", self.y)
        if self.x > 0 and self.y > 0:
            print("el punto se encuentra en el primer plano.")
        else:
            if self.x < 0 and self.y > 0:
                print("el punto se encuentra en el segundo plano")
            else:
                if self.x < 0 and self.y < 0:
                    print("el punto se encuentra en el tercer cuadrante")
                else:
                    if self.x > 0 and self.y < 0:
                        print("el punto se encuentra en el cuarto cuadrante")
                    else:
                        print("el punto se encuentra en linea")


# bloque principal
x = int(input("ingrese el numero X: "))
y = int(input("ingrese el numero Y: "))
punto1 = Punto(x, y)
punto1.imprimir()

