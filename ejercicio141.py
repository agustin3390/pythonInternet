def empaquetamiento():
    dia = 17
    mes = 3
    año = 1990
    return (dia, mes, año)

def desempaquetar(tupla):
    lista1 = list(tupla)
    dia = lista1[0]
    mes = lista1[1]
    año = lista1[2]
    return dia, mes, año



tupla1 = (10,8,15)
print(tupla1)
lista1 = list(tupla1)
lista1[0] = 45
lista1[1] = 100
lista1[2] = 70
tupla1 = tuple(lista1)
print(tupla1)

tupla2 = empaquetamiento()
dia_1, mes_1, año_1 = desempaquetar(tupla2)
print(dia_1, mes_1,año_1)

