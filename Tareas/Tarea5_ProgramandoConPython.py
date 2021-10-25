# 1. Crea una función que reciba los tres coeficientes a, b y c para resolver una ecuación de segundo grado. 
# Muestra la solución por pantalla y ayúdate de la librería Math para acceder a la función raíz cuadrada.
# Crea una función que reciba los tres coeficientes a, b y c para resolver una ecuación de segundo grado. 
# Muestra la solución por pantalla y ayúdate de la librería Math para acceder a la función raíz cuadrada.

import math 
def  second_grade(a, b, c):
    s1 = (((-1)*b)+ math.sqrt((b**2)-(4*a*c)))/(2*a)
    s2 = (((-1)*b)- math.sqrt((b**2)-(4*a*c)))/(2*a)
    return("x1 is %s and x2 is %s:"%(s1, s2))

second_grade(1, 2, 1)


# 2. Crea una función que lea una frase de teclado y nos diga si es o no un palíndromo (frase que se lee igual 
# de izquierda a derecha o al revés como por ejemplo La ruta nos aportó otro paso natural.)

def palindromo():
  
  l = []
  ent = input("Ingresa tu frase, evita usar caracteres especiales como:, . ñ - o acentos: ")
  ent = ent.replace(" ", "").lower()
  
  for i in ent:
    l.append(i)
  
  l_rv = l.copy()
  l_rv.reverse()
  
  if (l == l_rv):
      return("Tu frase " + ent + " es un PALINDROMO")
  else:
      return("Tu frase " + ent + " no es un PALINDROMO")
      
palindromo()


# 3. Crea un diccionario que tenga por claves los números del 1 al 10 y como valores sus raíces cuadradas

import math 

keys = list(range(1,11))
keys_str = [str(x) for x in keys]
values = list(map(lambda x: round(math.sqrt(x),2), keys)) 
dic = dict(zip(keys_str, values))

# 4. Crea un diccionario que tenga como claves las letras del alfabeto castellano y como valores 
# los símbolos del código morse (los tienes todos en la Wikipedia). A continuación crea un programa 
# que lea una frase del teclado y te la convierta a Morse utilizando el diccionario anterior.

def to_morse():
  a = input("Escribe tu frase para convertirla en codigo morse: ")
  a = a.lower()
  morse = {'a' : '. -', 'b' : '- . . .', 'c' : '- . - .', 'd' : '- . .', 'e' : '.',
  'f' : '. . - .', 'g' : '- - .', 'h' : '. . . .', 'i' : '. .', 'j' : '. - - -',
  'k' : '- . -', 'l' : '. - . .', 'm' : '- -', 'n' : '- .', 'ñ' : '- - . - -', 
  'o' : '- - -', 'p' : '. - - .', 'q' : '- - . -', 'r' : '. - .', 's' : '. . .', 
  't' : '-', 'u' : '. . -', 'v' : '. . . -', 'w' : '. - -', 'x' : '- . . -', 
  'y' : '- . - -', 'z' : '- - . .'}   
  li = []
  for letra in a:
    li.append(morse[letra])
  
  print("<<%s>> en codigo morse es: %s"%(a, li))
  
to_morse()

# 5. Crea una función que dados dos diccionarios nos diga que claves están presentes en ambos.

dic1 = {1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,11:11}
dic2 = {10:1,11:2,12:3,13:4,14:5,15:6,16:7,17:8,18:9,19:10}

def keys_d(dic1, dic2):
  for i in list(dic1.keys()):
    for j in list(dic2.keys()):
      if i == j:
        l_keys.append(i)
  return("Claves repetidas en ambos diccionarios %s"%(set(l_keys))) 

keys_d(dic1, dic2)


# 6. Crea una función que dado un número N nos diga si es primo o no (tiene que ir dividiendo por 
# todos los números x comprendidos entre 2 y el propio número N menos uno y ver si el cociente 
# de N/x tiene resto cero o no).

def def_primo(q):
  div = []
  for i in range(2, q):
    div.append(q%i)
  
  if (0 in div):
    print("El numero %d no es primo"%q) 
  else:
    print("El numero %d es primo"%q)  
    
def_primo(8)  


# 7. Investiga la documentación de la clase string y crea un método que lea una frase del teclado y 
# escriba la primera letra de cada palabra en Mayúscula.

def oracion():
  p = input("Ingresa tu frase para convertir cada palabra en Title: ")
  return(p.title())
    
oracion() 


# 8. Crea una función que calcule el máximo común divisor de dos números introducidos por el usuario por teclado.

def mcd(ns):
  mlt = []
  for j in ns:
    for i in range(1, j+1):
      if j % i == 0:
        # print(i)
        mlt.append(i)
  d = dict(zip(mlt,map(lambda x: mlt.count(x),mlt))) 
  key_list = list(d.keys())
  val_list = list(d.values())
  position = val_list.count(len(ns)) - 1
  return("Maximo Comun Divisor de %s y %s  es: %s"%(ns[0], ns[1], key_list[position]))

mcd([12, 36])

# 9. Investiga el Cifrado del César y crea una función que lo reproduzca en Python. 
# Cada letra del mensaje original se desplaza tres posiciones en el alfabeto estándar. 
# La A se convierte en la D, la B se convierte en la E, la C se convierte en la F... y cuando se acaba 
# el alfabeto se le vuelve a dar la vuelta: la X se convierte en la A, la Y en la B y la X en la C. 
# Los números no sufren ninguna modificación.

from string import ascii_lowercase, ascii_uppercase

def cifrado_cesar(texto, pasos):
  resultado = []
  for c in texto:
    if c in ascii_lowercase:
      indice = ascii_lowercase.index(c)
      nuevo_indice = (indice + pasos)%len(ascii_lowercase)
      resultado.append(ascii_lowercase[nuevo_indice])
    elif c in ascii_uppercase:
      indice = ascii_uppercase.index(c)
      nuevo_indice = (indice + pasos)%len(ascii_uppercase)
      resultado.append(ascii_uppercase[nuevo_indice])
    else:
      resultado.append(c)
  return ''.join(resultado)
cifrado_cesar("Hola mundo", 3)



# 10. Dado una lista de nombres de persona, escribe un algoritmo que los ordene de tres formas diferentes:
# A. De forma alfabética
# B. De forma alfabética invertida
# C. De nombre más corto al más largo.

import numpy as np

lista_nbr = ["ricardo", "alan", "rosa", "miguel"]

def wrd_sort(lista):
    
    alista_nbr = lista.copy()
    blista_nbr = lista.copy()
    alista_nbr.sort()
    blista_nbr.sort(reverse = True)
    
    lenlist=[]   
    for x in lista:
          lenlist.append(len(x))     
    index = np.argsort(lenlist)  
    lst2 = ['val']*len(lista)   
    for i in range(len(lista)):    
        lst2[i] = lista[index[i]] 
    print(f"Lista en forma alfabetica {alista_nbr}")
    print(f"Lista en forma alfabetica invertida {blista_nbr}")
    print(f"Lista por numero de caracteres{lst2}")
  
wrd_sort(lista_nbr)
