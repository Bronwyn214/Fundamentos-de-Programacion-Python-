from random import *

temp= input('ingrese una palabra: ') #temporizador

cond= randrange(len(temp)) #0,1,2,3,...
#print(cond)
enlace= temp[cond]
print(enlace)

cond2= randrange(len(temp)) #0,1,2,3,...
#print(cond2)
enlace2= temp[cond2]
print(enlace2)

cond3= randrange(len(temp)) #0,1,2,3,...
#print(cond3)
enlace3= temp[cond3]
print(enlace3)

cond4= randrange(len(temp)) #0,1,2,3,...
#print(cond4)
enlace4= temp[cond4]
print(enlace4)

cond5= randrange(len(temp)) #0,1,2,3,...
#print(cond5)
enlace5= temp[cond5]
print(enlace5)

vinc= enlace + '-'+ enlace2 + '-' + enlace3 + '-' + enlace4 + '-' + enlace5

print(f'los caracteres aleatorios son {vinc}')

###############################################################################

lpalabras = ['alejandro','fundamentos','escritura','python','ayudante']

escojo= choice(lpalabras) #'alejandro'
palmay= escojo.upper() #'ALEJANDRO'

#REEMPLACE LOS CARACTERES LAS PALABRA CON ASTERISCOS, EXCEPTO LOS CARACTERES DE LOS EXTREMOS (EL PRIMER INDICE Y EL ULTIMO):

lon= len(palmay)
lon2= (len(palmay)-2)* '*'

prim= palmay[0]
con1= prim + lon2 #A********
#print(con1)

ult= palmay[-1]
con2= lon2 + ult #********O

confin= con1 + con2
print(confin) #A*******O

#########

pal= input('ingrese un tamano de palabra: ').upper() #'programacion'
condfin= len(pal) == lon

print(f'Acerto {condfin}')

###################################################################################################################################

datos= [10, 40, 25, 50]

pos= int(input('Ingrese una posicion: ')) #1

vinculo= datos[pos] #40
print(vinculo)

aleatorio= randint(5,10)
print(f'Numero aleatorio {aleatorio}')

if vinculo in datos:
    datos[pos] = aleatorio
    print(datos)

#[10, 40, 25, 50]
#[10, 6, 25, 50]

########################################################

aleatorio2= randint(-30,-1)
randomo= choice(datos)
posrandom= datos.index(randomo) #posicion aleatoria
print(f'Posicion aleatoria: {posrandom}')
print(f'Numero aleatorio {aleatorio2}')

vinculo2= datos[posrandom]
#print(vinculo2)

if vinculo2 in datos:
    datos[posrandom] = aleatorio2
    print(datos)

#############################################################################################################################3

empleados= ['Xavier Pauta', 'Edgar Freire', 'Willy Fernandez', 'Antonia Alvarez']

correos=[]

for i in range(len(empleados)):
    
    empleado= empleados[i]
    print(empleado)

    dos= empleado[0:2].lower() #'xa'
    ap= empleado[-2:].lower() #'ta'
    
    #dos letras aleatorias del nombre (tanto mi nombre y apellido)
    esp= empleado.index(' ')
    nombre= empleado[ :esp].lower() #'xavier'
    nomesc= sample(nombre,2)
    une= ''.join(nomesc)



    apellido= empleado[esp+1:].lower() #'pauta'
    apesc= sample(apellido,2)
    une2=''.join(apesc)


    dominio= '@espol.edu.ec'
    correo= dos + ap+ une + une2 + dominio
    correos.append(correo)

print(correos)
