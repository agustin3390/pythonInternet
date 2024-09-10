contador = 0
mail = input("ingrese el email: ")
for i in range(len(mail)):
    if mail[i] == '@':
        contador += 1


print(" el email tiene", contador, "@")
