#EJERCICIOS PRACTICOS

#PRIMER EJERCICIO

def listarjugadores(ldatos,pais):
    jugadores=[]

    for i in jugadores:
        jugador, nacion= i.split('|')
        if nacion == pais:
            jugadores.append(jugador)
    
    return jugadores







#SEGUNDO EJERCICIO

from random import *

def mostrarTopAlmacenamiento(lapps,entero):
    apps=[]
    datos=[]

    for i in lapps:
        aplicacion, dato = i.split('-')
        numero= dato.replace('MB','')
        ente= int(numero)
        apps.append(aplicacion)
        datos.append(ente)
    
    print(f'Top {entero} aplicaciones con mayor consumo')

    for i in range(entero):
        maximo= max(datos)
        pos= datos.index(maximo)
        print(f'{i + 1}. {apps[pos]}: {maximo} MB')
        apps.pop(pos) #Elimina el resto de los maximos de los nombres de las aplicaciones
        datos.pop(pos) #Elimina el resto de los maximos de los datos de la aplicaciones
    

apps= ['Teams-520MB', 'ACADEMICO-38MB', 'FACEBOOK-366MB','WSAPP-1500MB', 'TIKTOK-1200MB']
aleatorio= randint(3,len(apps)-1)

mostrarTopAlmacenamiento(apps,aleatorio)







#TERCER EJERCICIO

def siglas(frase, palabras_comunes):
    palabritas=[]
    corte= frase.lower().split(' ')
    prim= corte[0]
    palabritas.append(prim[0])

    for i in corte[1:-1]:
        if i not in palabras_comunes:
            palabritas.append(i[0])

    ult= corte[-1]
    palabritas.append(ult[0])

    return ''.join(palabritas).upper()

comunes= ['el', 'de', 'a', 'un', 'para']

print(siglas('para todo epsilon mayor a cero existe un delta mayor a cero', comunes)) #PTEMCEDMC








#CUARTO EJERCICIO

from random import *

aleatorio= randint(20,50)

lista=[]

for i in range(aleatorio):
    aleatorio2= randint(100,5500)  
    lista.append(aleatorio2)

print(lista)


ingrese= int(input(f'Ingrese un numero entre el {min(lista)} y {max(lista)}: '))

while not (min(lista)<=ingrese<=max(lista)):
    ingrese= int(input(f'Ingrese un numero entre el {min(lista)} y {max(lista)}: '))

print(f'Numeros divisibles para el {ingrese}')

divisibles=[]

for i in lista:
    if i%ingrese==0:
        divisibles.append(i)


print(divisibles)











#QUINTO EJERCICIO

from random import *

def crearCarta(lsimbolos, lvalores):
    lcartas=[]

    while len(lcartas) <5:
        escojo1= choice(lvalores)
        escojo2= choice(lsimbolos)
        formato= escojo1 + '-' + escojo2

        if formato not in lcartas:
            lcartas.append(formato)
    
    return lcartas
    
    

lsimb= ['T', 'E', 'C', 'D']
lval= ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

cartas= crearCarta(lsimb, lval)

shuffle(cartas)

print(cartas)

escoje= choice(cartas)

ingrese= input('Ingrese su carta: ')

if ingrese == escoje:
    print(f'Adivinaste! {escoje}')

else:
    print(f'{escoje}')
    print('Para la proxima campeon')