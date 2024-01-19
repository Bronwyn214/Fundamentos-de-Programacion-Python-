#Nombre: Edgar Freire
#Matrícula
#Carrera: Auditoría y Control de Gestión


#Ejercicio 1
#Lea el archivo pokemon.csv y cree una lista con los tipos de pokemon sin repetirse.

#Ejercicio 2


tiposPokemon= {}

gen1={}


archivo= open('pokemon.csv', 'r')

salto1= archivo.readline()
salto2= archivo.readline()

for salto2 in archivo:

  pokes=[]
  
  corte= salto2.split(',')
  pok= corte[1]
  tipo1= corte[2]
  tipo2= corte[3]

  gen= corte[-2]

  if pok not in pokes:
    pokes.append(pok)

    valor1= tiposPokemon.get(tipo1, [])
    valor1.append(pok)
    tiposPokemon[tipo1]= valor1

    valor2= tiposPokemon.get(tipo2, [])
    valor2.append(pok)
    tiposPokemon[tipo2]= valor2

  if pok not in gen:
    gen1[pok] = [tipo1,gen]

print(tiposPokemon)

  


archivo.close()





#Ejercicio 3

datosPokemon={}

archivo2= open('pokemon.csv', 'r')

salto3= archivo2.readline()
salto4= archivo2.readline()

for salt4 in archivo2:
  corte2= salt4.split(',')
  pok2= corte2[1]
  leg= corte2[-2]
  total= corte2[4]

  if pok2 not in datosPokemon:
    datosPokemon[pok2]= [total,leg]

print(datosPokemon)

archivo2.close()


#Ejercicio 4

tipo= input('Ingrese un tipo: ').capitalize() #Water
gen= input('Ingrese generation: ') #2

archivo3= open(tipo+'-'+gen+'.csv', 'w')


for clave, valores in gen1.items():
  if tipo == valores[0] and gen == valores[-1]:
    archivo3.write(clave+','+valores[0]+','+valores[-1]+'\n')

archivo3.close()



#Ejercicio 5

llaves1= tiposPokemon.keys()
lista1= list(llaves1)

valores1= tiposPokemon.values()
lista2= list(valores1)

llaves2= datosPokemon.keys()
lista3= list(llaves2)

valores2= datosPokemon.values()
lista4= list(valores2)

print(lista4)

unicos=[]

for i in range(len(lista1)):
  if lista1[i] not in unicos:
    unicos.append(lista1[i])

numero=0

for i in range(len(lista1)):
  total= int(lista4[i][0])

  if total < numero:
    numero = total
    print(lista3[i], unicos[i])
