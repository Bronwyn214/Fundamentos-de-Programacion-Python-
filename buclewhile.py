#Sistema contraseña: haga un sistema en donde le permita ingresar una contraseña y al tercer intento, se cierra el programa.

con= 'marzo20'
contador= 0
user=''
while user != con and contador != 3:
  user= input('ingrese su contraseña: ')
  contador+=1
  if user != con:
    print('no se pudo ingresar ')

if contador < 3:
    print('ingresaste')
else:
    print('los intentos se caducaron')

#ESCRIBIR UN PROGRAMA QUE PERMITA AL USUARIO EL INGRESO DE N NUMEROS

#PRIMERO DEBE PREGUNTAR AL USUARIO CUANTOS NUMEROS DESEA INGRESAR
#AL FINAL DEL PROGRAMA PRESENTE LA SUMATORIA DE DICHOS NUMEROS


num= int(input('cuantos numeros desea ingresar ')) #3
contador=0
ciclo=0


while ciclo < num: #0<3, 1<3, 2<3
  numero= int(input('ingrese su numero '))#12, 12, 23
  contador+=numero
  ciclo+=1

print(f'total: {contador}')

##############################################################################################################################################
#ELABORE UNA CALCULADORA CON ESE MENU

#PEDIR AL USUARIO QUE OPCION DESEA USAR SEA 1 PARA SUMA, 2 PARA RESTA O 3 PARA FINALIZAR EL PROGRAMA.
#SI EL USUARIO INGRESA 1 O 2, PIDA DOS NUMEROS Y REALICE LA OPERACION. EL PROGRAMA DEBERA SEGUIR MOSTRANDO EL MENU HASTA QUE EL USUARIO COLOCE EL 3

opcion= ''

while opcion !='3':


  plus='1'
  minus= '2'

  bienvenida= 'Bienvenido a tu calculadora'
  sum= f'{plus}.- SUMA'
  rest= f'{minus}.- RESTA'
  exit= f'3.- SALIR'

  print(f'{bienvenida:<20}')
  print(f'{sum:<20}')
  print(f'{rest:<20}')
  print(f'{exit:<20}')

  opcion= input('Ingrese una opcion: ')

  if opcion == plus:
    n1= int(input('ingrese su primer numero: '))
    n2= int(input('ingrese su segundo numero: '))
    total= n1+n2
    print(total)

  elif opcion == minus:
    n_1= int(input('ingrese su primer numero'))
    n_2= int(input('ingrese su segundo numero'))
    totall= n_1-n_2
    print(totall)

  elif opcion == '3':
    print('FIN DEL PROGRAMA')

  else:
    print('INCORRECTO')

################################################################################################################################################################
#EJEMPLO DE WHILE CON CONTADOR

contador= 0

while contador <10:
  print(f'ITERACION {contador}')
  # es 0 menor a 10 == true
  # es 1 menor a 10 == true
  #.......
  # es 10 menor a 10 == false
  contador +=1 #contador= contador + 1
  # 0+1 == 1
  # 1+1 == 2
  #......
  # HASTA 9 ACABA EL CICLO
print('TERMINA EJECUCION')

#SI YO QUIERO INGRESAR NUMEROS HASTA CIERTA CANTIDAD DE VECES Y ESOS NUMEROS INGRESADOS SE ME SUMAN

total= 0 #acumulador que guardara la suma

num_sum= 5

contador=0

###############################################################################################################################################

while contador < num_sum:
  num= int(input('ingrese su numero: '))
  total= total + num
  contador +=1
print(f'el total de la suma es {total}')

#####################################################################################################################################################
#VALIDACION DE CONTRASENA

autorizacion= False

while autorizacion == False:
  contra= input('ingrese su contrasena ')
  if contra == 'marzo20':
    autorizacion = True
  else:
    print('Acceso denegado')

print('acceso correcto')

#####################################################################################################################################################
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

