#tabla de multiplicar

for n in range(1,11):

  for i in range(10):
    resultado= i *n
    print(f'{i} por {n} = {resultado}')

########################################################################################################

carnet= ['EDGAR FREIRE','AUDITORIA', 'KEBAB','PASTEL']

for i in carnet: #['EDGAR FREIRE', 'AUDITORIA',....]
  print(f'----{i}----')
  for caracter in i: #'EDGAR FREIRE'
    mini= caracter.lower()
    if mini in 'aeo':
      print(mini)

print(f'fin del programa')

########################################################################################################

#LISTAS PARALELAS

#MOSTRAR LAS FRUTAS QUE TENGAN PRECIO MENOR A 1.50 DOLARES

fruitas= ['MORA', 'PERA', 'PAPAYA', 'GUINEO', 'MANZANA']
precioxlb= [1.50, 1.0, 0.5, 2.0, 1.40]

print(f'lista de frutas menor a 1.5')


for i in range(len(fruitas)): #0,1,2,3
  informacion= fruitas[i] #'MORA, 'PERA', 'PAPAYA',...
  precios= precioxlb[i] #'INDEXO LA POSICION DE LAS FRUTAS A LA POSICION DE PRECIOS'
  if precios < 1.50:
    print(informacion)


# segunda forma de hacerlo

fruitas= ['MORA', 'PERA', 'PAPAYA', 'GUINEO', 'MANZANA']
precioxlb= [1.50, 1.0, 0.5, 2.0, 1.40]

print(f'lista de frutas menor a 1.5')


for fruta in fruitas: #['MORA', 'PERA', 'PAPAYA',...]
  pos= fruitas.index(fruta) #0, 1, 2, 3
  precio= precioxlb[pos] #INDEXAMOS LA POSICION DE LA FRUTA PARA ENLAZARLO A LA LISTA DE PRECIOS
  if precio < 1.50:
    print(fruta)


#####################################################################################################

#3 LISTAS PARALELAS CON RANGE(LEN(LISTA))

fruitas= ['MORA', 'PERA', 'MORA', 'GUINEO', 'MANZANA']
cantidad= [5, 10, 3, 5, 10]
clientes= ['Axel', 'Rodrigo', 'Juan', 'Pepe', 'Mario']

#IMPRIMIR POR PANTALLA TODAS LAS PERSONAS QUE COMPRARON MORA Y LA CANTIDAD

for fruta in range(len(fruitas)): #0,1,2,3,4
  pos= fruitas[fruta] #'MORA', 'PERA', 'MORA',......
  pos_2= cantidad[fruta]
  pos_3= clientes[fruta]

  if pos == "MORA":
    print(f'{pos_3},{pos_2}')


########################################################################################################

cadena= 'piogram'

for x in range(len(cadena)):
  pos= cadena[x]
  print(pos)

##################################################################################################################################################
nomb= input('Ingrese los nombres: ') #'Xavier,Carlos,Jose'
edades= input('Ingrese las edades: ') #'21, 18, 27'

listanom= nomb.split(',')
#print(listanom)

listaed= edades.split(',')
#print(listaed)

for i in range(len(listaed)):
    listaed[i] = int(listaed[i])
    # AHORA TODA LA LISTA DE EDADES SON NUMEROS



#listanom= ['Xavier', 'Carlos', 'Jose']
#listaed= [21, 18, 27]

#ESTUDIANTE CON MAYOR DE EDAD
maxi= max(listaed)
posma= listaed.index(maxi)
ind= listanom[posma]
print(f'Estudiante con mayor edad {ind}')

#ESTUDIANTE CON MENOR EDAD
minu= min(listaed)
posmi= listaed.index(minu)
ind2= listanom[posmi]
print(f'Estudiante con menor edad {ind2}')

#PROMEDIO
suma= sum(listaed)/3
print(suma)
