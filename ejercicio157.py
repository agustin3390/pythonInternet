def cargar():
    alumnos = {}
    
    for i in range(3):
        dni = int(input("ingrese el dni del alumno: "))
        cant_materias = int(input("ingrese la cantidad de materias: "))
        lista = []
        for j in range(cant_materias):
            materia = input("ingrese el nombre de la materia: ")
            nota = float(input("ingrese la nota de la materia: "))
            lista.append((materia,nota))
        alumnos[dni] = lista
    return alumnos

def imprimir(alumnos):
    print("lista completa de alumnos.")
    for dni in alumnos:
        print(dni)
        for materia,notas in alumnos[dni]:
            print(materia, notas)
        

def consulta_dni(alumnos):
    dni = int(input("ingrese el dni que desea buscar: "))
    if dni in alumnos:
        for materia,notas in alumnos[dni]:
            print(materia, notas)


#bloque principal

alumnos = cargar()
imprimir(alumnos)
consulta_dni(alumnos)