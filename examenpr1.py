from numpy import *

#1
#Implemente una funcion llamada obtenerList(nomA), que recibe el nombre del archivo.
#Retornará una lista que contiene nombres sin repetir y la nota mínima de todas las notas.

def obtenerList(nomA):
    file = open(nomA, 'r')
    #nombre|paralelo|materia|nota1,nota2,nota3,nota4

    lnombres=[]
    minimas=[]

    file.readline()

    for linea in file:
        linea= linea.strip().split('|')
        nom= linea[0]
        notas= linea[-1].split(',')
        if nom not in lnombres:
            lnombres.append(nom)
        
        for nota in notas:
            minimas.append(int(nota))


    file.close()
        
    minimo= min(minimas)
    return lnombres, minimo

    

print(obtenerList("notas.txt"))

#(['Josue', 'Gabriel', 'Carlos', 'Joice', 'Enrique', 'Roberto', 'Priscilla', 'Dayanna'], 12)


#2
#Implemente una funcion llamada obtenerDics(nomA,paralelo,materia), que recibe el nombre del archivo, un paralelo en entero y una materia. 
#Retornará un diccionario donde sus claves son nombres y sus valores serán listas de notas de ese paralelo y materia específica.


def obtenerDics(nomA,paralelo,materia):
    dic={}
    arch= open(nomA, 'r')
    arch.readline()

    #nombre|paralelo|materia|nota1,nota2,nota3,nota4

    for linea in arch:
        linea= linea.strip().split('|')
        nom= linea[0]
        para= linea[1]
        mate= linea[2]
        notas= linea[-1].split(',')

        if int(para) == paralelo and mate == materia:
            l_notas=[]
            for nota in notas:
                l_notas.append(int(nota))

                if nom not in dic:
                    dic[nom] = l_notas
    
    arch.close()

    return dic

print(obtenerDics('notas.txt',2,'matematicas'))

#{'Josue': [65, 45, 78, 89, 75], 'Joice': [65, 45, 78, 89, 100], 
#'Roberto': [65, 45, 100, 78, 96], 'Priscilla': [65, 78, 78, 71, 75], 'Dayanna': [65, 81, 100, 12, 89]}


#3
#Implemente una función llamada obtenerPromedios(nomA,paralelo,materia). que recibe el diccionario del enunciado anterior. 
#Retornará un diccionario con las notas promediadas.

def obtenerPromedios(nomA,paralelo,materia):
    d_notas= obtenerDics(nomA, paralelo, materia)
    d_promedios= {}

    for nom, nota in d_notas.items():
        prom= sum(nota)/len(nota)

        if nom not in d_promedios:
            d_promedios[nom] = prom
    
    return d_promedios

print(obtenerPromedios('notas.txt',2,'matematicas'))

#{'Josue': 70.4, 'Joice': 75.4, 'Roberto': 76.8, 'Priscilla': 73.4, 'Dayanna': 69.4}


#4
#Implemente una función llamada mayorPromedio(nomA,paralelo,materia). 
#Retornará el nombre del estudiante con mayor promedio.

def mayorPromedio(nomA,paralelo,materia):
    d_mayor= obtenerPromedios(nomA, paralelo, materia)
    v_nom= array(list(d_mayor.keys()))
    v_notas= array(list(d_mayor.values()))
    ind_max= v_nom.argmax()
    nom_max= v_nom[ind_max] #ESTUDIANTE CON MAYOR PROMEDIO

    return nom_max

print(mayorPromedio('notas.txt',2,'matematicas'))

#Roberto


#########################################################################################################################################################









dicStream = {"HBO":478569632,"Netflix":956789132,"PrimeVideo":465789123,"Star+":321654987,"Disney+":546123789}

#1

#Implemente una función llamada presentar(dic), que recibe el diccionario(dicStream). La función imprimirá de mayor a menor por consola de la siguiente manera:
#Stream            Viewers
#Netflix         956789132
#Disney+         546123789
#...

def presentar(dic):
    v_stream= array(list(dicStream.keys()))
    v_viewers= array(list(dicStream.values()))

    ind_ord= v_viewers.argsort()[::-1]
    v_stream = v_stream[ind_ord]
    v_viewers= v_viewers[ind_ord]

    print('Stream                  Viewers')

    for i in range(len(v_viewers)):
        print(f'{v_stream[i]}              {v_viewers[i]}')

presentar(dicStream) #NO ES NECESARIO MOSTRAR UN PRINT FUERA DE LA FUNCION DEBIDO A QUE NO RETORNA NADA MAS QUE
#SOLO UNA IMPRESION (NONE)

#Stream                  Viewers
#Netflix              956789132
#Disney+              546123789
#HBO              478569632
#PrimeVideo              465789123
#Star+              321654987


#2

#Ejercicio 2b. Implemente una función llamada crearArchivo(nomA,dic), que recibe el nombre del archivo y un diccionario(dicStream). Escribirá en el archivo los datos del diccionario con siguiente formato:
#Stream/Viewers
#Netflix:
#956789132
#PrimeVideo:
#465789123
#...
#winOfRating: Netflix
#nota: no importará el orden en el que se escriben las plataformas de streaming, y por ultimo escribe la plataforma con mas Viewers.


def crearArchivo(nomA,dic):

    file= open(nomA, 'w')

    vector_st= array(list(dic.keys()))
    vector_vw= array(list(dic.values()))

    orden= vector_vw.argsort()[::-1]
    vector_st= vector_st[orden]
    vector_vw= vector_vw[orden]
    posmax= vector_vw.argmax()
    stmax= vector_st[posmax]

    for i in range(len(vector_vw)):
        file.write(f'{vector_st[i]}\n{vector_vw[i]}\n')
    
    file.write(f'WinOfRating: {stmax}')

    file.close()

crearArchivo('datos.txt',dicStream)

#SALIDA DEL ARCHIVO
#Netflix
#956789132
#Disney+
#546123789
#HBO
#478569632
#PrimeVideo
#465789123
#Star+
#321654987
#WinOfRating: Netflix

    
#######################################################################################################################################







#Se tiene la siguiente matriz
m = array([["X","Y","X","X"],["Y"," ","X","X"],[" ","X","X","X"],[" ","Y","Y"," "]])

#Se desea implementar un función llamada procesar(m), que recibe la matriz y retonará cantidad de "X", 
#cantidad de "Y", cantidad total de elementos llenos y la misma matriz pero los espacios vacíos serán "0" 
#y los espacios llenos serán "1".

    
def procesar(m):
    v1= m == 'X'
    print('Cantidad de X')
    print(sum(v1)) #8

    v2= m == 'Y'
    print('Cantidad de Y')
    print(sum(v2)) #4

    v3= m==' '
    print('Cantidad de vacios')
    print(sum(v3)) #4

    suma1= sum(v1)
    suma2= sum(v2)
    suma3= sum(v3)

    v_sumas= array([suma1, suma2, suma3])


    matriz= where(m!=' ','0','1') #LOS ESPACIOS PASAN A SER 0

    #(4, 4, array([['0', '0', '0', '0'],
    #   ['0', '1', '0', '0'],
    #   ['1', '0', '0', '0'],
    #   ['1', '0', '0', '1']], dtype='<U1'))

    #LOS 0 SON LAS LETRAS X Y, Y 1 SON LOS ESPACIOS


    return suma1, suma2, suma3, matriz


print(procesar(m))

#Cantidad de X
#8
#Cantidad de Y
#4
#Cantidad de vacios
#4
#(8, 4, 4, array([['0', '0', '0', '0'],
#       ['0', '1', '0', '0'],
#       ['1', '0', '0', '0'],
#       ['1', '0', '0', '1']], dtype='<U1'))


############################################################################################################################








#Se tiene el siguiente archivo con el siguiente formato:
#almacen:ciudad:venta

#Ejercicio 4a. Implemente una función llamada obtenerEtiquetas(nomA), que recibe el nombre del archivo y retonará dos vectores, uno con el nombre de todos los almacenes sin repetir y el otro con el nombre de todas las ciudades sin repetir

def obtenerEtiquetas(nomA):
    file = open(nomA, 'r')
    file.readline()
    dic={}
    dic2={}

    for linea in file:
        linea = linea.strip().split(':')
        almacen= linea[0]
        ciudad= linea[1]
        venta= linea[-1]

        if almacen not in dic:
            dic[almacen] = venta
        
        if ciudad not in dic2:
            dic2[ciudad] = venta
    

    vector1= array(list(dic.keys()))
    vector2= array(list(dic2.keys()))

    file.close()

    return vector1, vector2

print(obtenerEtiquetas('ventas.txt'))


#Ejercicio 4b. Implemente una función llamada crearMatriz(nomA,almacenes,ciudades), 
#que recibe el nombre del archivo y vectores de la función anterior. 
#Retornará una matriz almacenes(filas)xciudades(columnas) donde cada celda representa el valor monetario.

def crearMatriz(nomA, almacenes, cities):
    file = open(nomA, 'r')
    file.readline()

    numfilas= almacenes.size
    numcol= cities.size
    matriz= ones((numfilas, numcol))


    for linea in file:
        linea = linea.strip().split(':')
        almacen= linea[0]
        ciudad= linea[1]
        venta= linea[-1]
        
        indfila= where(almacenes== almacen)[0][0]
        indcol= where(cities== ciudad)[0][0]
        matriz[indfila, indcol] = int(venta)

    file.close()
    
    return matriz

    

vector1, vector2 = obtenerEtiquetas('ventas.txt')

print(crearMatriz('ventas.txt', vector1, vector2))

#[[425678. 782134. 516249. 693521. 287943. 815372.]
# [624158. 349827. 721493. 189735. 936247. 572834.]
# [837461. 572834. 349827. 624158. 721493. 189735.]
# [287943. 815372. 693521. 936247. 624158. 349827.]
# [936247. 189735. 815372. 572834. 349827. 721493.]]





#Ejercicio 4c. Implemente una función llamada obtenerTop3almacenes(m), que recibe una matriz y 
#retonará un vector con los tres mejores almacenes que más han vendido en total de todas las ciudades.

m= crearMatriz('ventas.txt', vector1, vector2)

def obtenerTop3almacenes(m, almacenes):
    suma_almacen= m.sum(axis=1) #suma en filas
    indices_ord= suma_almacen.argsort()[::-1] #posiciones de la suma de forma ordenada de la fila
    ind_top3= indices_ord[:3]
    topalmacen= almacenes[ind_top3]

    return topalmacen

print(obtenerTop3almacenes(m, vector1)) #['GamingHouse' 'PcUPs' 'Computron']






#Ejercicio 4d. Implemente una función llamada obtenerstats(m,almacenes,ciudades), 
#que recibe los datos pertinentes y retornará una matriz de igual tamaño donde pondrá un String "mayor" 
#en aquellos mayores que el promedio total de toda la matriz.

def obtenerstats(m, almacenes, ciudades):
    numfilas= almacenes.size
    numcol= ciudades.size
    matriz= full((numfilas, numcol),'')
    prom= m.mean()
    matriz= where(m > prom, 'mayor','')

    return matriz

print(obtenerstats(m, vector1, vector2))

#[['' 'mayor' '' 'mayor' '' 'mayor']
# ['mayor' '' 'mayor' '' 'mayor' '']
# ['mayor' '' '' 'mayor' 'mayor' '']
# ['' 'mayor' 'mayor' 'mayor' 'mayor' '']
# ['mayor' '' 'mayor' '' '' 'mayor']]




#Ejercicio 4e. Implemente una función llamada obtenerTotalCiudades(vectorS,malmacenes,ciudades), 
#que recibe los datos pertinentes y un vectorS con algunas ciudades sin repetir, 
#la funcion retornará un vector paralelo al vectorS que es la suma total de esas ciudades.


def obtenerTotalCiudades(m, vectorS, ciudades):
    suma_total= m.sum(axis=0)

    ind=[]

    for i in range(len(vectorS)):
        print(vectorS[i])
        ind.append(where(ciudades == vectorS[i])[0][0])
    
    ind= array(ind)
    valores= suma_total[ind]


    return valores

print(obtenerTotalCiudades(m, array(['Guayas', 'Esmeraldas']), vector2))

#Guayas
#Esmeraldas
#[3111487. 3016495.]

