#ELABORE UN PROGRAMA QUE PIDA AL USUARIO UNA CANTIDAD DE SEGUNDOS Y MUESTRE CUANTAS HORAS, MINUTOS Y SEGUNDOS SON:

num= int(input('ingrese por teclado los segundos')) #3665
segundos= num%60 #5
horas= num//3600 #1
sobra_horas= num%3600 #65
minutos= sobra_horas//60 #1

print(f'resultado de segundos queda {segundos}, horas queda en {horas} y minutos en {minutos}')

###############################################################

#ESCRIBA POR TECLADO DOS NUMEROS Y MUESTRE POR PANTALLA TRUE SI EL PRIMER #NUMERO ES DIVISIBLE PARA EL SEGUNDO, CASO CONTRARIO SERIA FALSE

num_1= int(input('ingrese el numero')) #5
num_2= int(input('ingrese el numero')) #2
residuo= num_1%num_2 #1

condicion= residuo == 0

print(f'el primer numero es divisible con el segundo numero? {condicion}')


###############################################################################################
nota1= float(input('ingrese nota1: '))
nota2= float(input('ingrese nota2: '))

promedio= (nota1+nota2)/2 #float

print(f'el promedio es {promedio}')

#aprueba o no

ap= promedio>=60
rp= 60<promedio

cond= ap or rp

print(f'aprobo? {cond}')

print(f'aprobo? {ap}') #SI SOLO ME INTERESA LA PRIMERA PARTE LA CUAL ES AP

#######################################################
num= int(input('ingrese un numerito'))
cond= not(10<num<100)
print(f'no esta entre 10 y 100 {cond}')

############################################################

num= int((input('ingrese numero 3 cifras')))
num_2= int((input('ingrese numero 1 cifra')))

cond= num%100 #460%100 = 60
cond_2= cond%num_2 == 0
cond_3= ((num_2)**2) < cond

ultcom= cond_2 and cond_3

print(f'cumple condicion {ultcom}')

############################################################

num= int(input('ingrese numero de x')) #2
cond= 4*(num**2)+((3/2)*num)-5

print(f'resultado {cond}')

######################################################
producto= 'Capucchino'
valor= 2.60
iva= 0.12
total= valor + (valor*iva)

print(f'producto es {producto} y total es {total:0.2f}')

#producto es Capucchino y total es 2.91
# PRODUCTO ES CAPUCCHINO, Y SI QUIERO REDONDEARLO EN DOS DECIMALES SERIA PRESENTAR LA VARIABLE CON DOS PUNTOS Y 0.2FLOAT
