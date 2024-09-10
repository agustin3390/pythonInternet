lista = []
for i in range(5):
    nombre = input("ingrese el nombre de la persona: ")
    lista.append(nombre)
    nombreMenor = lista[0]
    if lista[i] < nombreMenor:
        nombreMenor = lista[i]
print("lista completa: ", lista)
print("nombre menor alfabeticamente: ", nombreMenor)