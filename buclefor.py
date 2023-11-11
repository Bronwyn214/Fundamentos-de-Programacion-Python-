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

##################################################################################################################
paginas= ['www.espol.edu.ec', 'www.google.com', 'www.UCSG.edu.ec', 'www.fcnm.espol.edu.ec', 'www.uess.edu.ec', 'www.Stanford.edu', 'www.ucsg.edu.ec', 'www.harvard.edu']

universidades=[]

for i in range(len(paginas)):
    pagina= paginas[i]
    
    if '.edu' not in pagina:
        print('No es un URL educativo')
    
    else:
        if 2<=pagina.count('.')<=3:
            punto= pagina.index('.')
            edu= pagina.index('.edu')
            universidad= pagina[punto+1 :edu]
            universidades.append(universidad)
        
        elif pagina.count('.')>=4:
            otropunto= pagina.index('.')
            punto2= pagina.index('.', otropunto+1)
            edu2= pagina.index('.edu')
            universidad2= pagina[punto2+1: edu2]
            universidades.append(universidad2)

print(universidades)

unicos=[]

for i in range(len(universidades)):
    universidades[i] = universidades[i].lower()
    
    if universidades[i] not in unicos:
        unicos.append(universidades[i])


print(unicos)

############################################################################################################################################

lst_personas= ['Frank Malo', 'Pedro Peralta', 'Mercede Malo', 'Carlos Andrade', 'Humberto Coto', 'Manuel Andrade' ]

nom= input('Ingrese el nombre y apellido: ') #Frank Malo

esp2= nom.index(' ')
nombre2= nom[ :esp2]
apellido2= nom[esp2+1:]

print('Posibles parientes:')

for i in range(len(lst_personas)):
    persona= lst_personas[i]
    esp= persona.index(' ')
    nombre= persona[ :esp]
    apellido= persona[esp+1: ]

    if apellido2== apellido and nom.lower()!=persona.lower(): #PARA QUE NO SALGA FRANK MALO REPETIDO, HAY QUE HACER LA CONDICION DE VERIFICAR SI MI NOMBRE INTRODUCIDO ES DIFERENTE A LA PERSONAS QUE SE RECORREN
        print(persona)
