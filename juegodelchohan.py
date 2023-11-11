#JUEGO DEL CHO HAN

#CONSISTE EN LANZAR DOS DADOS, EL JUGADOR DEBE ADIVINAR SI LA SUMA DE LOS DOS DADOS DA PAR O IMPAR (CHO O HAN)

#SIMULE EL JUEGO 'CHO HAN' DONDE UN JUGADOR INGRESARA CUANTO DINERO DESEA APOSTAR EN CADA TURNO (SUPONGA QUE EN TU BILLETERA HAY 10 DOLARES)

#SI ADIVINA: GANA EL DOBLE, ES DECIR SI TENGO 10 EN MI BILLETERA Y APOSTE 2, TENDRE 12
#NO ADIVINA: PIERDE, ES DECIR SI TENGO 10 Y APOSTE 2, TENDRE 8

#EL JUEGO TERMINA CUANDO SE QUEDE EN DINERO O CUANDO INGRESE 'no'

#SE DEBERA MOSTRAR EL RESULTADO DE CADA RONDA (SI PERDIO O GANO), EL DINERO QUE TIENE EN LA BILLETERA (TOTAL DE LO QUE SE ACUMULO EN MI BILLETERA)
#Y AL FINAL MOSTRAR CUANTAS PARTIDAS GANO EL JUGADOR (CONTADOR DE PARTIDAS)


from random import *

billetera= 10

cont=0

continuar='si'

print(f'----BIENVENIDO AL JUEGO DE CHO HAN----')
print(f' USTED TIENE {billetera}')


while billetera>0 and continuar == 'si':

    apuesta= int(input('Cuanto desea apostar: ')) #2

    if apuesta <=billetera:
        dado1= randrange(1,6) #5
        dado2= randrange(1,6) #1
        suma= dado1 + dado2 #6
        parimpar= input('Es par o impar: ') #par o impar
        print(f'salio {dado1} + {dado2} = {suma}')

        if (suma%2) == 0 and parimpar == 'par':

            print('Gana')
            billetera+=apuesta
            cont+=1 #GANA UNA JUGADA
        elif (suma%3)==0 and parimpar =='impar':

            print('Gana')
            billetera+=apuesta
            cont+=1 #GANA UNA JUGADA
        else:
            print('Pierde')
            billetera-=apuesta
            cont+=1  #GANA UNA JUGADA
        print(f'Su billetera queda en {billetera}')

        if billetera != 0:
        
            continuar= input('Desea Continuar: ') #Si o no
            print('------------------------------------')
    else:
        print('La apuesta es mayor a tu billetera')
print(f'Usted gano {cont} partida/s')
print('GRACIAS POR JUGAR')
