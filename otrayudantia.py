#PRIMER EJERCICIO


def buscar_palindromo(mensaje):
    mini= mensaje.lower()
    corte= mini.split(' ')
    nuevo=[]
    for i in corte:
        if i == i[::-1] and len(i)>=3:
            nuevo.append(i)
    
    return nuevo

print(buscar_palindromo('ana y yo somos amigos y trabajamos en la torre del radar'))
#['ana', 'somos', 'radar']

####################################################################################

#SEGUNDO EJERCICIO

palabra= input('Ingrese su palabra: ').lower() #hola

ingrese=''

total=0


while ingrese!='final':
    ingrese= input('Ingrese una frase: ').lower()

    ingrese= ingrese.replace('.','').replace(',','')

    if ingrese!='final':
        corte= ingrese.split(' ')
        total+=corte.count(palabra)


print(f'La palabra {palabra} se ha repetido {total} veces en las frases ingresadas')

#Ingrese su palabra: hola
#Ingrese una frase: Hola, estoy bien
#Ingrese una frase: Hola. No me gusta saludar diciendo hola
#Ingrese una frase: final
#La palabra hola se ha repetido 3 veces en las frases ingresadas


###################################################################################

#TERCER EJERCICIO

def siglas(frase, palabras_comunes):
    lista=[]

    corte= frase.lower().split(' ')
    primero= corte[0]

    lista.append(primero[0])

    for i in corte[1:-1]:
        if i not in palabras_comunes:
            lista.append(i[0])

    ultimo= corte[-1]

    lista.append(ultimo[0])

    return ''.join(lista).upper()

frase= 'el yin y el yang son conceptos filosoficos de la cultura china'

palabras_comunes= ['el', 'y', 'de', 'la', 'son']

print(siglas(frase,palabras_comunes)) #EYYCFCC



####################################################################################

#CUARTO EJERCICIO (CAMBIO DE ORDEN DE POSICIONES DE UNA LISTA MEDIANTE UN K NUMERO)

def rotacion_parcial(numeros,k):
    numeritos= numeros.copy()

    if k>0 and k<len(numeros):
        k_elemento = numeritos.pop(k-1)
        numeritos.insert(0, k_elemento )
        return numeritos




lista= [110,202,343,40,52]

print(rotacion_parcial(lista,3))

#SI ES DE 3...

#[110, 202, 343, 40,52]

#[343, 110, 202, 40, 52]


#######################################################################################

#QUINTO EJERCICIO

from random import *

def buscar_divisibles(numeros, divisor):
    lista=[]

    for i in numeros:
        if i%divisor == 0:
            lista.append(i)
    
    return lista


numeros_aleatorios= [228,213,277,169,230,168,110,225,162,198,90]
divisor= 9

print(buscar_divisibles(numeros_aleatorios, divisor)) #[225, 162, 198, 90]

nuevo=[]

for i in range(32):
    aleatorio= randint(5,42)
    nuevo.append(aleatorio)

genero= randint(6,19)

llamo= buscar_divisibles(nuevo,genero)

print(llamo)