#RETO 1: (10 minutos) Crear un programa que solicite una cantidad de elementos, un límite inicial y un límite final.
#Genere una lista con el tamaño de esta cantidad de elementos con números aleatorios enteros entre los límites. No debe incluir los límites.
import random as rd
cant = int(input("Ingrese cantidad elementos: "))
minimo = int(input("Ingrese valor mínimo: "))
maximo = int(input("Ingrese valor máximo: "))

def listaAleatoria(cantidad,limiteInicial,limiteFinal):
  lista = []
  for i in range(cantidad):
    lista.append(rd.randint(limiteInicial+1,limiteFinal-1))
  return lista
print(listaAleatoria(cant,minimo,maximo))
  
#RETO 2 (10 minutos) Crear un programa que permite generar una nueva lista con elementos únicos y ordenados de forma descendente.
listaRepetidos = [10, 27, 31, 51, 10, 30, 100, 90, 70, 80, 21]
nuevaLista = []
for i in listaRepetidos:
  if i not in nuevaLista:
    nuevaLista.append(i)
nuevaLista.sort(reverse=True)
print(nuevaLista)

#RETO 3 (10 minutos)
#Crear un programa que permite agregar números pares mientras ud no ingrese 0 o un número negativo. Antes de agregar valide que si sea un número y no tenga letras.
#Finalmente imprima la lista, la cantidad de números agregados, cuantos números fueron impares y cuantos ingresos incorrectos.
nro = 1
incorrectos = 0
impares=0
pares = []

while nro!=0 and nro>0:
  
  ingreso = input("Ingrese nro: ") #3
  if ingreso.isdigit() and ingreso!="0":
    nro = int(ingreso)
    if nro%2==0:
      pares.append(nro)
    else:
      impares+=1
  elif ingreso.lstrip("-").isdigit():
    nro= int(ingreso)
  else:
    incorrectos+=1
    
print("Lista",pares)
print("Pares", len(pares))
print("Impares", impares)
print("Incorrectos", incorrectos)
