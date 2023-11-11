from random import *

lista=['rueda']*4

lista2= ['x']*11


conc= lista + lista2

shuffle(conc) #['x', 'x', 'x', 'x', 'rueda', 'rueda', 'x', 'rueda', 'x', 'rueda', 'x', 'x', 'x', 'x', 'x']

print(conc)

indice= ''

cont=0
intento=0
ruedas=0

while intento != 7 and ruedas!=4:
    
    indice= input('Ingrese su indice: ') #'4'


    if not indice.isdigit():
        print('Indice no encontrado')
        intento+=1
    
    else:

        ente= int(indice)
        intento+=1


        if 0<=ente<=14:
            enlace= conc[ente] #'rueda'

            if enlace == 'rueda':
                print('Encontrado')

                cont+=1000
                ruedas+=1
                

                ruedita= conc[ente].count('rueda')
                print(f'Rueda encontrada: {ruedita}')
                conc[ente] = '*'
                
            else:
                print('No encontrado')
        
        else:
            print('Indice no encontrado')

if ruedas ==4:
    print(f'Has acumulado {cont} de dinero, GANASTE UN CARRO')

else:
    print(f'Has acumulado {cont} de dinero, NO GANASTE NADA')
