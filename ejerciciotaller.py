from random import *

#EJERCICIO 1

#nombre;costo;numeros-de-asientos

pasajero1= '    maria cristina lopez sanchez|200.23|A1,A2;;;;'
pasajero2= '$$$juan perez soles>20.50>A3,A4--%'
pasajero3= '..alexa andrea moran cherrez|80.10|A5=+=+'

#OBTENER LOS NOMBRES DE LOS PASAJEROS

limpieza1= pasajero1.lstrip(' ')
une= ''.join(limpieza1)

limpieza1b= une.rsplit(';')
une2= ''.join(limpieza1b) #'maria cristina lopez sanchez|200.23|A1,A2'

limpieza2= pasajero2.lstrip('$')
unee= ''.join(limpieza2)

limpieza2b= unee.rstrip('--%')
unee2= ''.join(limpieza2b) #'juan perez soles>20.50>A3,A4'

limpieza3= pasajero3.lstrip('.')
uneee= ''.join(limpieza3)

limpieza3b= uneee.rstrip('=+=+')
uneee2= ''.join(limpieza3b) #'alexa andrea moran cherrez|80.10|A5'

remp1= une2.replace('|',';') #maria cristina lopez sanchez;200.23;A1,A2
remp2= unee2.replace('>',';') #juan perez soles;20.50;A3,A4
remp3= uneee2.replace('|',';') #alexa andrea moran cherrez;80.10;A5

#DETERMINAR LOS NOMBRES DE LOS PASAJEROS (SOLO LOS NOMBRES) Y PONER SOLO LA PRIMERA LETRA EN MAYUSCULA

pos1=  remp1.index(';')
nombre1= remp1[0+1 :pos1]
mayus1= remp1[0].upper()
conc1= mayus1 + nombre1 #'Maria cristina lopez sanchez'


pos2= remp2.index(';')
nombre2= remp2[0+1:pos2]
mayus2= remp2[0].upper()
conc2= mayus2 + nombre2 #'Juan perez soles'


pos3= remp3.index(';')
nombre3= remp3[0+1 :pos3]
mayus3= remp3[0].upper()
conc3= mayus3 + nombre3 #'Alexa andrea moran cherrez'

#DETERMINAR EL TOTAL PAGADO POR TODOS LOS PASAJEROS

total=[]

pos1b= remp1.index(';', pos1+1)
precio1= remp1[pos1+1 :pos1b]

pos2b= remp2.index(';', pos2+1)
precio2= remp2[pos2+1 : pos2b]

pos3b= remp3.index(';', pos3+1)
precio3= remp3[pos3+1: pos3b]

ent1= float(precio1)
ent2= float(precio2)
ent3= float(precio3)

total.append(ent1)
total.append(ent2)
total.append(ent3)

suma= sum(total) #300.83

#DETERMINAR LOS ASIENTOS QUE RESERVARON
listreserv= []


pasinv1= remp1[::-1]
pasinv2= remp2[::-1]
pasinv3= remp3[::-1]

posinv1= pasinv1.index(';')
posinv2= pasinv2.index(';')
posinv3= pasinv3.index(';')

resinv1= pasinv1[ :posinv1]
resinv2= pasinv2[ :posinv2]
resinv3= pasinv3[ :posinv3]

reserva1= resinv1[::-1] #A1,A2
reserva2= resinv2[::-1] #A3,A4
reserva3= resinv3[::-1] #A5


listreserv.append(reserva1)
listreserv.append(reserva2)
listreserv.append(reserva3)

unereserv= ','.join(listreserv)


#OBTENER UN PASAJERO DE FORMA ALEATORIA QUIEN SE LE DARA UN OBSEQUIO

pasajeroslista= [conc1, conc2, conc3]

escojo= choice(pasajeroslista)

#FORMATO

iguales= '='*10
print(f'{iguales}+MIRABUS+{iguales}')
print(f'Pasajero1: {conc1:>20}')
print(f'Pasajero2: {conc2:>20}')
print(f'Pasajero3: {conc3:>20}')
print(f'Ganador: {escojo:>20}')
print(f'Total Pagado: {round(suma,2)}')
print(f'Asientos Reservados: {unereserv}')

#################################################################################################################################

#EJERCICIO 2

Pasajeros= [20,31,2,5,45]

#SI CADA BUS QUE TIENE CAPACIDAD DE 12, CUANTO SERIA EL EXCESO DE PASAJEROS PARA CADA BUS, PONGALO EN UNA LISTA

cap= 12

nuevopas= []
for i in range(len(Pasajeros)):

    if Pasajeros[i]>12:
        Pasajeros[i]-=cap
        nuevopas.append(Pasajeros[i])
    else:
        nuevopas.append(Pasajeros[i])
    
print(nuevopas) #[8, 19, 2, 5, 33]


#OBTENER CUAL ES EL BUS QUE TIENE MENOS PASAJEROS ASUMIENDO QUE EL NUMERO DEL BUS ES EL INDICE DE LA LISTA

minimo= min(nuevopas)
pos= nuevopas.index(minimo)
print(f'El bus con menos pasajeros es el numero: {pos}')

#DETERMINAR TOTAL DE PASAJEROS

suma= sum(nuevopas)
print(f'Total: {suma}')
