import random

dado1 = random.randint(1,6)
dado2 = random.randint(1,6)
suma = dado1 + dado2
print("dado 1: ", dado1)
print("dado 2: ", dado2)
if suma == 7:
    print("gano la partida.")
else:
    print("perdio la partida")