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

cond= user == escojo

print(f'gano {cond}')
