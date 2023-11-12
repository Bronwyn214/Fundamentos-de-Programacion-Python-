lista= [0,1,2,3,4,5,6,7,8,9]

for i in lista:
  print(f'iteracion {i}') #i son los nombres de los elementos dentro de la lista

#tienda de pinturas

lista_2= ['rojo', 'verde', 'amarillo', 'azul', 'plateado', 'dorado']

for i in lista_2:
  print(f'hay pintura color {lista_2}')

indice=0


while indice < len(lista_2):
  index= lista_2[indice]
  print(f'hay pintura color {index}')
  indice+=1

#######################################################################

#EJERCICIO DE VOTOS

pollos= ['Angie', 'Andres', 'Gabriela', 'Oscar', 'Kevin', 'Victor', 'Gustavo', 'Annie', 'Maria']
#EN MI LISTA PUEDEN HABER MAS NOMBRES

cont_votos = [0]* len(pollos)

#LE SACO UNA LISTA DE 0 DEL TAMANO DE LOS POLLOS

print(pollos)
print(cont_votos)

nombre= input('Ingrese el nombre del estudiante que quiera votar: ').capitalize() #'Angie'


while nombre != 'Fin':
    if nombre in pollos:

        busco= pollos.index(nombre) #busco angie
    
        cont_votos[busco]+=1
        print(f'Votos totales: {cont_votos}')

        
    else:
        print('Voto no valido')
    
    nombre= input('Ingrese el nombre del estudiante que quiera votar: ').capitalize() #'Victor'

print('Fin')

#TOTAL DE ESTUDIANTES QUE VOTARON
suma= sum(cont_votos)
print(f'Total de estudiantes que votaron {suma}')

#GANADOR
maxi= max(cont_votos)
posmaxi= cont_votos.index(maxi)
ganador= pollos[posmaxi]
print(f'GANADOR {ganador}')

#VOTOS DEL GANADOR
print(f'Con total de votos de {maxi}')

######################################################################################################################

frase= input('Ingrese la frase: ') #'Esto de la programacion es genial'



while frase!= 'fin':
    corteza= frase.split(' ')
    for i in range((len(corteza))):
        pos= corteza[i]

        #print(pos)

        if len(pos) >=5:
            print(pos)

    frase= input('Ingrese la frase: ') #'fundamentos asegura un AP'
print('BYE')

 #############################################################################3

ingrese= ''


uno= '1'
dos='2'
tres= '3'

while ingrese!='paso':
    print('Menu')   
    print('Seleccione una opcion')   
    print(f'{uno}: Dividir entre dos numeros')
    print(f'{dos}: Verificar si es par')
    print(f'{tres}: Verificar si es infinitivo ')  
    ingrese= input('Elija una opcion: ') #'1','2','3'

    if ingrese == uno:
        num1= int(input('Ingrese su numero: ')) #2
        num2= int(input('Ingrese su otro numero: ')) #2
        cond= num1//num2
        print(f'Division: {cond}')
    
    elif ingrese == dos:
        num1= int(input('Ingrese su numero: ')) #2
        cond= num1%2==0
        print(f'Es par {cond}')

    elif ingrese==tres:
        pal1= input('Ingrese su palabra: ')
        cond= pal1[-2:] == 'ar'
        cond2= pal1[-2:] == 'er'
        cond3= pal1[-2:] == 'ir'
        condplus= cond or cond2 or cond3
        print(f'Es infinitivo {condplus}')

print('ERROR')


#SEGUNDA VERSION PERO SIN CICLO WHILE
#####

uno= '1'
dos='2'
tres= '3'


print('Menu')   
print('Seleccione una opcion')   
print(f'{uno}: Dividir entre dos numeros')
print(f'{dos}: Verificar si es par')
print(f'{tres}: Verificar si es infinitivo ')  
ingrese= input('Elija una opcion: ') #'1','2','3'

if ingrese.isdigit():
    if ingrese == uno:
        num1= int(input('Ingrese su numero: ')) #2
        num2= int(input('Ingrese su otro numero: ')) #2
        cond= num1//num2
        print(f'Division: {cond}')
    
    elif ingrese == dos:
        num1= int(input('Ingrese su numero: ')) #2
        cond= num1%2==0
        print(f'Es par {cond}')

    elif ingrese==tres:
        pal1= input('Ingrese su palabra: ')
        cond= pal1[-2:] == 'ar'
        cond2= pal1[-2:] == 'er'
        cond3= pal1[-2:] == 'ir'
        condplus= cond or cond2 or cond3
        print(f'Es infinitivo {condplus}')

else:
  print('ERROR')
