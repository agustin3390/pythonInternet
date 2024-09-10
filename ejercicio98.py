lista = [[4,12,5,66],[14,6,25],[3,4,5,67,89,23,1],[78,56]]
print(lista)
for k in range(len(lista)):
    for i in range(len(lista[k])):
        if lista[k][i] > 10:
            lista[k][i] = 0
print("-----------------------------")
print(lista)