nom=input('Nombres: ') #Andres Pablo
ap=input('Apellidos: ') #Pena Bravo
edad= int(input('Edad: ')) #34
pais= input('Pais: ').title() #Ecuador
cor= input('Correo: ') #micorreo@gmail.com
tit= input('Titulo: ') #Ing. Telematica
prom= float(input('Promedio: ')) #7.8

#EL POSTULANTE DEBE DE TENER DE 18-40 ANOS
cond= 18<edad<40

#SER DE UNO DE LOS DE LOS PAISES DE: ECUADOR, PERU, COLOMBIA, CHILE
pais1= pais == 'Ecuador'
pais2= pais == 'Peru'
pais3= pais == 'Colombia'
pais4= pais == 'Chile'

cond2= pais1 or pais2 or pais3 or pais4

#TENER PROMEDIO DE AL MENOS(>=) 8.0

cond3= prom >= 8.0

condfin= cond and cond2 and cond3

print(f'Cumple requisitos? {condfin}')

######################################################################

print('***Agencia Avianca travel***')

cedula= int(input('Cedula: ')) #0292928283
fecha= input('Fecha: ') #'15-10-2023'
destino= input('Destino: ') #'Paris'
dias= int(input('Dias: ')) #10
gente= int(input('Nro de personas: ')) #3
vuelo= int(input('Vuelo: ')) #2000
hotel= int(input('Hotel: ')) #50
trans= int(input('Transporte: ')) #20
alim= int(input('Alimentación: ')) #30
gastos= int(input('Otros gastos: ')) #200

vu= vuelo*gente #6000
ho= dias*hotel*gente #1500
tr= dias*trans*gente #600
al= dias*alim*gente #900
ot= gastos*gente #600

total= vu + ho+ tr+al+ ot #9600
per= int(total/gente) #3200

print(f'Subtotal Vuelo: {vu}')
print(f'Subtotal Hotel: {ho} ')
print(f'Subtotal Transporte: {tr} ')
print(f'Subtotal Alimentación: {al} ')
print(f'Subtotal Otros gastos: {ot}')
print(f'Total: {total} ')
print(f'Pago por persona: {per}')
print(f'**Los valores de esta plataforma solo aplican desde el {fecha} hasta 3 dias posteriores.')


################################################################################################################

#TAREA 2

#CODIGO POSTAL

post= input('Ingrese su codigo postal: ') #EC029293

cond= post[0:2].isupper()
cond2= post[2:]
cond2plus= 5<=len(cond2)<=7

condfin= cond and cond2plus
print(condfin)

#CANCION

cancion= input('Ingresa su verso de una cancion: ').lower() #'que encontraste una chica y ahora estás casado'

vocal1= cancion.count('a')
vocal2= cancion.count('e')
vocal3= cancion.count('i')
vocal4= cancion.count('o')
vocal5= cancion.count('u')

tilde1= cancion.count('á')
tilde2= cancion.count('é')
tilde3= cancion.count('í')
tilde4= cancion.count('ó')
tilde5= cancion.count('ú')

vocaltotal= vocal1+vocal2+vocal3+vocal4+vocal5+tilde1+tilde2+tilde3+tilde4

print(f'Numero de vocales {vocaltotal}')

#bcdfghjklmnñpqrstvxyz

suma= len(cancion.replace(' ',''))-vocaltotal


print(f'Numero de consonantes {suma}')


conteo3= vocaltotal + suma
print(f'Numero de palabras {conteo3}')

#Articulos

primer= cancion.count('el')
segundo= cancion.count('la')
tercero= cancion.count('los')
cuarto= cancion.count('las')
quinto= cancion.count('lo')
sexto= cancion.count('un')
sep= cancion.count('uno')
octav= cancion.count('una')
noven= cancion.count('unos')
dec= cancion.count('unas')

contt= primer+segundo+tercero+cuarto+quinto+sexto+sep+octav+noven+dec

print(f'Numero de articulos {contt}')

##################################################################

#CEDULA

cedula= input('Ingrese su cedula: ') #'0951994508'

cond= len(cedula) ==10
cond2= cedula.isdigit()

num1= cedula[0:2]=='01'
num2= cedula[0:2]=='02'
num3= cedula[0:2]=='03'
num4= cedula[0:2]=='04'
num5= cedula[0:2]=='05'
num6= cedula[0:2]=='06'
num7= cedula[0:2]=='07'
num8= cedula[0:2]=='08'
num9= cedula[0:2]=='09'

numplus= 10<=int(cedula[0:2])<=24

condplus= num1 or num2 or num3 or num4 or num5 or num6 or num7 or num8 or num9 or numplus

condfin= cond and cond2 and condplus
print(f'Cumple con todo {condfin}')

########################################

#CLAVE

clave= input('Ingrese su clave: ') #abr1l2104#

cod= len(clave)>5

#vocales
vocal1= clave.count('a')>=1
vocal2= clave.count('e')>=1
vocal3= clave.count('i')>=1
vocal4= clave.count('o')>=1
vocal5= clave.count('u')>=1

tilde1= clave.count('á')>=1
tilde2= clave.count('é')>=1
tilde3= clave.count('í')>=1
tilde4= clave.count('ó')>=1
tilde5= clave.count('ú')>=1

verificar= vocal1 or vocal2 or vocal3 or vocal4 or vocal5 or tilde1 or tilde2 or tilde3 or tilde4 or tilde5

#especial

esp1= clave.count('#')>=1
esp2= clave.count('$')>=1
esp3= clave.count('-')>=1

verificar2= esp1 or esp2 or esp3

cod2= clave.replace('#','').replace('$','').replace('-','').isalnum()

confirmar= cod and verificar and verificar2 and cod2
print(f'Cumple con todo {confirmar}')


#TWEET

tweet= input('Ingrese su tweet: ')

cd= len(tweet) == 140

conteo1= tweet.count('@fifa')==1
conteo2= tweet.count('@conmebol')==1
conteopl= conteo1 or conteo2

contec= tweet.count('Ecuador')==1

confinn= cd and conteo1 and conteo2 and conteopl and contec

print(f'Cumple con todo {confinn}')