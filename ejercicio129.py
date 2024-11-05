def cargar_sueldos():
    li_sueldos = []
    for i in range(10):
        sueldo = float(input("ingrese el sueldo: "))
        li_sueldos.append(sueldo)
    return li_sueldos

def imprimir_sueldos(li_sueldos):
    for i in range(len(li_sueldos)):
        print("sueldo", i + 1, ":",li_sueldos[i])

def sueldos_mayores(li_sueldos):
    contador = 0
    for i in range(len(li_sueldos)):
        if li_sueldos[i] >= 4000:
            contador += 1
    print("la cantidad de sueldos mayores son: ", contador)

def promedio_sueldos(li_sueldos):
    suma = 0
    for i in range(len(li_sueldos)):
        suma += li_sueldos[i]
    promedio = suma // len(li_sueldos)
    return promedio

def sueldos_bajo_promedio(li_sueldos, promedio):
    for i in range(len(li_sueldos)):
        if li_sueldos[i] < promedio:
            print(li_sueldos[i])



#bloque principal
lista_sueldos = cargar_sueldos()
imprimir_sueldos(lista_sueldos)
sueldos_mayores(lista_sueldos)
promedio_lista = promedio_sueldos(lista_sueldos)
sueldos_bajo_promedio(lista_sueldos, promedio_lista)