notasMayores = 0
notasMenores = 0
for i in range(10):
    nota = float(input("ingrese la nota del alumno: "))
    if nota >= 7:
        notasMayores = notasMayores + 1
    else:
        notasMenores = notasMenores + 1
print("la cantidad de notas aprobadas son: ", notasMayores)
print("la cantidad de notas no aprobadas son: ", notasMenores)