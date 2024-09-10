lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
print(lista)
print("--------------")
for k in range(len(lista[0])):
    print(lista[0][k])
print("-------------")
for k in range(len(lista)): 
    for i in range(len(lista[k])):
        print(lista[k][i]) #k columnas i filas..
