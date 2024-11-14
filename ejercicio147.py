def cargar_candidatos():
    candidatos = []
    for i in range(3):
        nombre = input("ingrese el nombre del candidato: ")
        cant = int(input("ingrese la cantidad de provincias que escruto el candidato: "))
        prov = []
        for j in range(cant):
            provincia = input("ingrese el nombre de la provincia: ")
            cant_votos = int(input("ingrese la cantidad de votos: "))
            prov.append((provincia,cant_votos))
        candidatos.append((nombre, prov))
    return candidatos

def mostrar_candidatoGanador(candidatos):
    for i in range(len(candidatos)):
        for j in range(len(candidatos[i][1])):
            suma = 0
            suma += candidatos[i][1][j][1]
            print("el candidato con mayor votos es: ", candidatos[i][0], "con la cantidad de", suma, "de votos" )


#bloque principal

candidato = cargar_candidatos()
print(candidato)
mostrar_candidatoGanador(candidato)