from random import *

polloasado= ['edgar', 'castro', 'adrian', 'tinoco', 'andy', 'juan', 'diego', 'rafael']

ayu= polloasado[0:3] # de edgar hasta adrian, NO CUENTA A TINOCO
est= polloasado[3:] #DE TINOCO HACIA EL INFINITO

print(f'{ayu} y {est}')

########################################################################################################################################

lista= ['capuchino', 'edgar', 'julio', 'hamburguesa', 'comida', 'pollos']

escojo= choice(lista).upper() #JULIO
print(escojo)

escojo_2 = choice(escojo) #I
print(escojo_2)

indice= escojo.index(escojo_2) #3
print(indice)

restante= escojo[ indice +1 :  ] # DESDE LA LETRA QUE YO SAQUE VA A RECORRER LO QUE ESTA DESPUES
print(restante)

tamano= len(restante) #LE SACO EL TAMANO DEL RESTANTE

pista= (' _ ' * indice) + escojo_2 + (" _ " * tamano)

print(pista)

user= input('ingrese su palabra ').upper()
cond= user == escojo

print(f'gano {cond}')

#####################################################################################################################

lista= ['pollos', 'edgar', 'adrian', 'willy', 'gravy']

escojo= choice(lista).upper() #'WILLY'
slice= escojo[0] #'W'
slice_2= escojo[-1] #'Y'

subguiones= '_' * (len(escojo)-2)

#SE VA A CONSIDERAR TODAS LAS LETRAS DE LA PALAABRA PARA CONVERTIRLAS EN SUBGUIONES A EXCEPCION DE 2

unir= slice + subguiones + slice_2

#'W___Y'

print(unir)

user(input('ingrese su palabra: '))

#####################################################################################################################
pokemones= ['Pikachu', 'Braixen', 'Primarina', 'Lucario'] #nombre de los pokemon
niveles= [15, 50, 20, 30 ] #poderes de los pokemon

poke= input('Ingrese el nombre de un pokemon: ') #'Braixen'
print(poke)


escojo= choice(pokemones) #'Lucario'
print(f'Pokemon rival {escojo}')

poder1= pokemones.index(poke)
poderdef= niveles[poder1]
print(f'Poder del primer poke {poderdef}')

poder2= pokemones.index(escojo)
poderdef2= niveles[poder2]
print(f'Poder del segundo poke {poderdef2}')

cond= poderdef > poderdef2
cond2= poderdef2 > poderdef

condfin= cond or cond2

print(f'Ganaste {condfin}')

cond= user == escojo

print(f'gano {cond}')

#####################################################################################################################################

personas= ['Juan Perez', 'Carlos Leon', 'Francisco Leon', 'CARLOS MALDONADO']

escojo= sample(personas, 2)
print(escojo) #['CARLOS MALDONADO', 'Juan Perez']

primer= escojo[0].title() #'Carlos Maldonado'
segundo= escojo[-1].title() #'Juan Perez'

pos= primer.index(' ')
ind= primer[pos+1 :] #'Maldonado'
#print(ind)


pos2= segundo.index(' ')
ind2= segundo[pos2+1 :] #'Perez'
#print(ind2)

print(f'Persona 1: {primer}')
print(f'Persona 2: {segundo}')


if ind == ind2:
    print('Son parientes')
else:
    print('No son parientes')
