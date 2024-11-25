import random

dado1 = random.randint(1,6)
dado2 = random.randint(1,6)
print("el resultado del dado 1: ", dado1)
print("el resultado del dado 2: ", dado2)
if dado1 + dado2 == 7:
    print("gano")
else:
    print("perdio")