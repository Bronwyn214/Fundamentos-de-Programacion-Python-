#Nombres
#Matrícula
#Carrera


#Lectura del archivo data.csv, se crean las siguientes listas y array.
import numpy as np

file = open("data.csv", encoding="utf8")
columnas = file.readline().strip().split(",")
listaDatos = []
paises = []
for line in file:
  separate = line.strip().split(",")
  listaDatos.append(separate[1:])
  paises.append(separate[0].split("(")[0].strip())
file.close()
matriz = np.array(listaDatos,int)

for pais in paises:
  print(pais)
  
print(columnas)
print(matriz)
print(matriz.shape)

#1. Copiar pregunta
#Imprimir el total de medallas de Ecuador y el general.

#filas son los paises
#columnas son las caracteristicas (country, summer, etc)
#01 es oro, 02 es plata, 03 es bronce
#total es total de medallas

arreglo= np.array(paises)

print(arreglo)


busco= np.where(arreglo=="Ecuador")
print(busco)

uno= matriz[busco ,14][0][0] #Columna 14 seria Combined total (o el -1)

print(uno) #Imprime el total de medallas de Ecuador SOLAMENTE HACIENDO SLICING CON LA MATRIZ, 2

print(matriz[:,14].sum()) #17579

#2. Copiar pregunta
##2. Imprimir la suma de medallas de plata en Winter.

print(matriz[:,7].sum())


#958


#3. Copiar pregunta
##3. Imprimir el nombre de los países que superan el total de medallas de plata de Argentina.

arg= arreglo=="Argentina"
sumita= matriz[arg ,2] + matriz[arg ,7]

sumplat= matriz[:,1] + matriz[:,6]

print(arreglo[sumplat>sumita])

#4. Copiar pregunta
##4. Imprimir cuantos países han ganado más de una medalla de bronce en Summer.

bro= matriz[:, 3]
ver= bro>0 #mayor o igual a 1
print(sum(ver))

#5. Copiar pregunta
##5. Imprimir el top 5 de países con más medallas

medallas= matriz[:,4] + matriz[:, 9]

orden= arreglo[medallas.argsort()][::-1]

print(f"El top 5 de paises con mas medallas es: {orden[:5]}")


#6. Copiar pregunta
#Imprima el país con más juegos y el país con menos juegos.


jueg= matriz[:, 10]

ord1= jueg.argmin()
ord2= jueg.argmax()

print(f'El pais con menos juegos es: {arreglo[ord1]}')
print(f'El pais con mas juegos es: {arreglo[ord2]}')