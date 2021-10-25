# Pedimos al usuario que introduzca un
n=int(input("Escribe el número: "))
print("\nPerfecto! Se va a calcular los números primos comprendidos entre 2 y {}".format(n))

# Declaración función que calcula la Criba de Eratóstenes
def criba_eratostenes(n):
    multiplos=[]
    for i in range(2,n+1):
        if i not in multiplos:
            print(i)
            for j in range(i*i,n+1,i):
                multiplos.append(j)
 
criba_eratostenes(n)
