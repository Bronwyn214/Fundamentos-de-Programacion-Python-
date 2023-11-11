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
