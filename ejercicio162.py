def meses(tupla, mes):
    print(tupla[mes:])




#bloque principal

tupla = ('enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre','noviembre', 'diciembre')
mes = int(input("ingrese el mes desea: "))
meses(tupla, mes)