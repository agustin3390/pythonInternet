class Cliente:

    def __init__ (self, nombre):
        self.nombre = nombre
        self.monto = 0

    def depositar(self, monto):
        self.monto = self.monto + monto
    
    def extraer(self, monto):
        self.monto = self.monto - monto
    
    def retornar_monto(self):
        return self.monto

    def imprimir(self):
        print("el cliente", self.nombre,"tiene un monto de:",self.monto)
    

class Banco:

    def __init__ (self):
        self.cliente1 = Cliente("juan")
        self.cliente2 = Cliente("lucas")
        self.cliente3 = Cliente("pedro")
    
    def operar(self):
        
        self.cliente1.depositar(300)
        self.cliente2.depositar(500)
        self.cliente3.depositar(400)
        self.cliente2.extraer(100)
        self.cliente1.imprimir()
        self.cliente2.imprimir()
        self.cliente3.imprimir()
    
    def depositos_totales(self):
        suma = self.cliente1.retornar_monto() + self.cliente2.retornar_monto() + self.cliente3.retornar_monto()
        print("la saldo total del dia es:", suma)
    
# bloque principal

banco1 = Banco()
banco1.operar()
banco1.depositos_totales()
