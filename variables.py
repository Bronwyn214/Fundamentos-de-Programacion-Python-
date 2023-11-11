import math
print(22)
print(1.5)
print('Hola mundo')
print(True)
print(False)

#######################################################

nombre= 'soy edgar'
edad= 20

presentate=(f'Me presento, {nombre}')
print(presentate)

ed_pre= (f'Tengo {edad}')
print(ed_pre)

base,altura,color= 5,7,"verde"

print(base)
print(altura)
print(color)

################################################################

lado_1= 3
lado_2= 5
lado_3= 12

perimetro= lado_1 + lado_2 + lado_3
print(f'el perimetro es {perimetro}')

################################################################
# FORMULA GENERAL

valor_A= 7
valor_b= -13
valor_c= 6

formula= (-valor_b + ((valor_b**2)-(4*valor_A*valor_c))**(1/2))/(2*valor_A)

print(f'mi resultado es {int(formula)}')

##########################################

num_1= 45
num_2= 32

ultimo= num_1 % 10
ultimo_2= num_2 % 10

print(ultimo) #5
print(ultimo_2) #2


re=ultimo == ultimo_2
ree=ultimo > ultimo_2
reee=ultimo >= ultimo_2
reeee=ultimo <= ultimo_2

print(f'Resultados: {re}, {ree}, {reee}, {reeee}')

#COMPARAR SI EL ULTIMO NUMERO DE NUM1 ES DIFERENTE AL ULTIMO NUMERO DE NUM2

rep= ultimo != ultimo_2

print(rep)

##############################################################################################################################
p= 'PRODUCTO'
v= 'VALOR SIN IVA'
t= 'TOTAL'

producto= 'Capucchino'
valor= 2.60
iva= 0.12
total= valor + (valor*iva)

producto_2= 'Expresso'
valor_2= 1.1
iva_2= 0.12
total_2= valor_2 + (valor_2*iva_2)

producto_3= 'Mocaccino'
valor_3= 2.95
iva_3= 0.12
total_3= valor_3 + (valor_3*iva_3)


print(f'{p:^20}{v:^20}{t:^20}')
print(f'{producto:^20}{valor:^20}{total:^20,.2f}')
print(f'{producto_2:^20}{valor_2:^20}{total_2:^20,.2f}')
print(f'{producto_3:^20}{valor_3:^20}{total_3:^20,.2f}')

##########################################################################################################################

num= float(input('ingrese num'))
num_2=float(input('ingrese num segundo'))

cond= (num**2 + num_2**2)
cond_2= math.sqrt(cond)
print(f'{cond_2:.3f}') #0.3, en 3 decimales

##############################################################
av= (num**2 + num_2**2)**(1/2)
print(f'{av:.3f}') #0.3 en 3 decimales
