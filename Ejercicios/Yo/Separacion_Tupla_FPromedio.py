n = input("Ingresa cualquier cosa separada por comas.")
separado = n.split(",")
separadoT = tuple(separado)
print(separadoT)

suma = 0
for i in separadoT: 
  suma += int(i)
promedio = suma / len(separadoT)

print(promedio)

