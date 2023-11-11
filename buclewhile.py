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

######################################################################################################################################################
productos= ['monitor', 'mouse', 'teclado', 'microfono', 'camara', 'audifonos']
precios= [200, 15, 25, 5 , 40, 80]


#Nombre del producto con menor precio

minimo= min(precios) #5 
posmin= precios.index(minimo) #posicion del minimo
prodmin= productos[posmin]


print(f'El nombre del producto con el menor precio es {prodmin}')

#EL PRECIO DE UN MOUSE

posmouse= productos.index('mouse') #pos del mouse
preciomouse= precios[posmouse]

print(f'El precio del mouse es {preciomouse}')

#HACER UN RANKING DE TOP 5 EN ORDEN A MAYOR SU PRECIO

iteracion=0

info= 'PRODUCTO'
info2= 'PRECIO'


print(f'{info:<20}{info2:20} ')


while iteracion<5: #0<5 == true

    maximo= max(precios) #precio maximo
    posmax= precios.index(maximo)
    vinc= productos[posmax]

    print(f'{vinc:<20}{maximo:<20}')

    del productos[posmax]
    del precios[posmax]

    iteracion+=1
    
    #monitor 200
    #audifonos 80
    #camara 40
    #teclado 25
    #mouse 15

################################################################################################################################################

password= input('Ingrese su contra: ') #'Xavier'
pass2= input('Ingrese su contra otra vez: ') #'1234', tiene que ser igual a 'Xavier' para salir del bucle
cont=1 #Comienza en uno porque al ingresar una contrasena incorrecta, cuenta como mi primer intento


while password!=pass2:
    print('No coincide, ingrese otra vez')
    cont+=1
    pass2= input('Ingrese su contra otra vez: ') #'1234'

print('Coinciden')
print(f'Te ha tomado {cont} intentos')

##################################################################################################################################################

ahorro= int(input('Cuanto desea ahorrar: ')) #40

suma=0

while ahorro>suma:

    alcancia= int(input('Ingrese dinero a la alcancia: '))
    suma+=alcancia

print(f'Objetivo alcanzado, se ha ahorrado {suma}')

