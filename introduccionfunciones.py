#FUNCIONES

#SE VIENE LO BUENO

def mifuncion():
    nombre= input('Ingrese su nombre: ') #Edgar Freire
    return nombre

nombre = mifuncion()
print(f'Mi nombre es {nombre}')


#ES OBLIGATORIO USAR PARENTESIS

#######################################################

def calcular_edad(ano_nacimiento):
    edad= 2023- ano_nacimiento
    return edad #USAMOS EL RETURN PARA RETORNAR LA VARIABLE Y PODER USARLO FUERA DE MI DEF, OJO

ano_nacimiento = int(input('Ingrese su ano de nacimiento: ')) #2003
edad= calcular_edad(ano_nacimiento) #2023 - 2003 = 20
print(f'Tengo {edad} anios')


#########################################################

def mi_funcion(num1,num2):
    calculo= num1+num2 #3 + 4 == 7
    return calculo #retornamos

num1 = int(input('Ingrese su numero: ')) #3
num2 = int(input('Ingrese su numero: ')) #4
calculo= mi_funcion(num1,num2) #calculo sera la funcion implementada
print(calculo)
