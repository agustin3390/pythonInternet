
def retorna_caracteres(tupla):
    return tupla[:3]




#bloque principla

tupla = ('enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre','noviembre', 'diciembre')

for mes in tupla:
    print(retorna_caracteres(mes))