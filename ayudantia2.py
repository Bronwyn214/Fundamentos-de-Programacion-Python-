#PRIMER EJERCICIO

lista= ['carbon:58', 'oro:74', 'diamante:12','hierro:85','diamante:5']

minerales=[]
datos=[]

ingrese= input('Ingrese su elemento: ') #diamante

acum=0
carbones=0

for i in lista:
    mineral, dato= i.split(':')
    entero= int(dato)
    if mineral not in minerales:
        minerales.append(mineral)
    
    if entero not in datos:
        datos.append(entero)
    
    if ingrese == mineral:
        acum+=entero #12 + 5 == 17
    
    if mineral == 'carbon':
        carbones+=entero


#cantidad total de todos los elementos juntos
print(sum(datos)) #234


#total de un elemento en especifico elegido por el usuario
print(acum) #17

#valor en dolares del carbon sabiendo que cada unidad cuesta 4.5 dolares
print(carbones*4.5) #261.0


#######################################################################################################################################################################################

#SEGUNDO EJERCICIO

#1) haga una funcion que recibe una lista con sus elementos y un elemento en especifico, retornara la cantidad total de ese elemento

def contarElemento(elemento,lista):
    acum=0
    for i in lista:
        material, unidad= i.split('|')
        limpio= unidad.lstrip('<')
        limpio2= limpio.rstrip('>')
        entero= int(limpio2)
        if elemento == material:
            acum+=entero
    
    return acum

#2) haga una funcion que recibe la lista con sus elementos , retornara el valor verdadero si el elemento esta al menos UNA sola vez en la lista, caso contario FALSE

def existeElemento(elemento,lista):
    for a in lista:
        if a.startswith(elemento):
            return True
        
        else:
            return False

#De esta lista...
adquisicion= ['perno|<5>', 'perno|<4>', 'tornillo|<2>', 'clavo|<7>', 'remache|<11>']

ing= input('Ingresa un material: ')

print(contarElemento(ing,adquisicion)) #9

print(existeElemento(ing,adquisicion)) #True o false

#3) En el programa principal el usuario ingresa su elemento, si se encuentra en la lista imprime la cantidad total de ese elemento, y sino imprimira que el
# elemento no se encuentra registrado

if existeElemento(ing,adquisicion):
    total= contarElemento(ing,adquisicion)
    print(f'El total de {ing} es {total}') #el total de perno es 9

else:
    print('No se encuentra registrado')


#####################################################################################################################################################################################################

#TERCER EJERCICIO

palabras= ['eventos', 'socrates', 'matematicas', 'automovil', 'elevaciones','elevaciones']

max=0
l=[]

for pal in palabras:

    if len(pal)> max:
        max=len(pal)
        l.clear()

    if max == len(pal) and pal.upper() not in l:
        l.append(pal.upper())

print(l) #['MATEMATICAS', 'ELEVACIONES']


###########################################################################################################################################################

#CUARTO EJERCICIO

nombres=['jorge', 'eduardo','andres','jose']

ingrese=''

cont=0

while ingrese!='---':
    ingrese=input('Ingrese su nombre: ')

    if ingrese!='---':
        cont+=1
        
        if ingrese in nombres:
            print('Esta en la lista')
            
        
        else:
            print('No esta en la lista')

print(f'Ha introducido {cont} nombres')


########################################################################################################################################################################

#QUINTO EJERCICIO

from random import *

palabras=['hola','online','futbol']

puntos=0
int=0

while puntos<50 and int!=5:
    ing= input('Ingrese una palabra: ') #'hola'
    escojo= choice(palabras) #'hola'

    if ing == escojo:
        print('Es igual')
        puntos+=5
        int+=1
    
    elif ing in palabras:
        print('Si esta en la lista')
        puntos+=1
        int+=1
    
    else:
        print('No es igual ni esta en la lista')
        puntos+=0
        int+=1


print(f'Intentos: {int}')
print(f'Puntos: {puntos}')

##########################################################################################################################################################################

#SEXTO EJERCICIO

def numero(ingreso):
    while not ingreso.isdigit():
        print('Por favor introduce un numero')
        ingreso= input('Ingrese un numero: ') #5678946893

    acum=0

    for i in ingreso:
        acum+=int(i)


    if ingreso.isdigit() and len(ingreso)==10 and acum>45:
        return True
    
    else:
        return False


entro=''

print(numero(entro))

######################################################################################################################################################################################

#SEPTIMO EJERCICIO

acum=1

while acum<1000:
    numero= input('Ingrese un numero: ')

    acum*=int(numero)
    print(acum)


print('Finalizado: limite alcanzado')

#funcion inputNum()

def inputNum():
    numero=''

    while not numero.isdigit():
        numero= input('Ingrese un numero: ')
    
    entero= int(numero)
    return entero

print(inputNum())


##################################################################################################################################################################################################

#OCTAVO EJERCICIO

def agregar(nombre,edad,lista):

    formato= nombre+':'+edad
    lista.append(formato)
    print(lista)  
    return lista

def mostrar(lista):
    if len(lista)!=0:
        print('Nombre, edad')
        for i in lista:
            nombre, edad = i.split(':')
            print(nombre,edad)
                
    else:
        print('No existen datos para presentar')


nombres=[]

def menu():
    ingreso=''

    while ingreso not in ['3','Salir']:
        uno= '1'
        dos='2'
        tres='3'

        print(f'{uno}. Agregar')
        print(f'{dos}. Mostrar')
        print(f'{tres}. Salir')

        ingreso= input('Ingrese una opcion: ')

        if ingreso == uno:
            nom= input('Ingrese su nombre: ')
            num= input('Ingrese su edad: ')
            agrego= agregar(nom,num,nombres)
            
        elif ingreso == dos:
            muestro= mostrar(nombres)
            
            
        elif ingreso in ['3', 'Salir']:
            muestro= mostrar(nombres)
            print('FIN DEL PROGRAMA')
        
        else:
            print('Opcion invalida')


print(menu())




