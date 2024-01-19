#Matricula
#Nombre EDGAR FREIRE
#Carrera AUDITORIA


#Ejercicio 1

archivo= open('gifts.csv','r')

linea= archivo.readline()

dic={}

for linea in archivo:
  corte= linea.strip().split(',')
  nro= corte[0]
  pers= corte[1]
  cont= corte[2]
  reg= corte[4]
  cost= corte[-1]
  ciudad= corte[-4]
  categoria= 'Moda'
  cat= corte[-2]

  if nro not in dic and cat == categoria:
    dic[nro]=[pers,cont,reg,cost,cat,ciudad]

print(dic)

archivo.close()

#Ejercicio 2

#Crear una lista con los regalos que son de Sudamérica y cuestan menos de $100, imprima la ciudad, nombre de persona, regalo. Use el diccionario anterior.

# {'95': ['Florencia', 'Sudamérica', 'Sombrero de diseñador', '60']}
# {NroDeseo: [NombrePersona,Continente, NombreRegalo, Costo]}

lista=[]

for clave,valor in dic.items():
  if valor[1] == 'Sudamérica' and int(valor[-3]) < 100:
    lista.append(valor[2])
    print(f'Nombre: {valor[0]}, Ciudad: {valor[-1]}, Regalo: {valor[-4]}')

print(lista)



#Ejercicio 3

continente= input('Ingrese un continente: ').capitalize() #Europa

archivo3= open(f'{continente}.csv','w')

# {NroDeseo: [NombrePersona,Continente, NombreRegalo, Costo]}
# Nro Deseo,Nombre de Persona,Continente,Ciudad,Nombre de Regalo,Categoría,Costo aproximado
# dic[nro]=[pers,cont,reg,cost,cat,ciudad]

for keya, valuep in dic.items():
  if valuep[1] == continente:
    archivo3.write(f'{keya}, {valuep[0]}, {valuep[1]}, {valuep[-1]}, {valuep[-4]}, {valuep[-2]}, {valuep[-3]} \n')

archivo3.close()
