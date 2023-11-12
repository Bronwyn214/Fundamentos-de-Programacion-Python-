url= input('ingrese su url ') #'www.yahoo.com'
nom= input('ingrese su nombre ') #'kevin'
seg= input('ingrese su segundo nombre ') #'axell'
apellido= input('ingrese su apellido ') #'concha'
ano= input('ingrese el ano de nacimiento ') #'1997'

#DEBE IMPRIMIR: kaconcha97@yahoo.com

cond= url[4:] #yahoo.com
cond_2= nom[0] #k
cond_3= seg[0] #a
cond_4= apellido[::] #concha
cond_5= ano[-2:] #97

cond_fin= cond_2 + cond_3 +cond_4 + cond_5 + '@' + cond

print(f'su correo empresarial es: {cond_fin}')


######################################################################

tweet= 'el dia de ayer hubo ayudantias con #Joel de FP y #Kevin de CUV ya se divertieron los pollos, ahora le toca a los gallos con #Axell B)'

#MOSTRAR EL NOMBRE DEL PRIMER AYUDANTE
#MOSTAR EL NOMBRE DEL SEGUNDO AYUDANTE
#MOSTAR EL NOMBRE DEL TERCER AYUDANTE

pos1= tweet.index('#')
print(pos1) #35ava posicion en la que busco el primer hashtag

subtuit= tweet[pos1+1 : ] #Joel de FP.....
print(subtuit)

#HAY QUE HALLAR EL ESPACIO QUE ESTA DESPUES DE JOEL

subesp= subtuit.index(' ') ##Joel
ayu1= subtuit[ : subesp] #JOEL

print(ayu1) #Joel


pos_2= subtuit.index('#') #13AVA POSICION

print(pos_2) #13ava posicion desde #Joel en la que esta el siguiente hashtag

subtuit_2= subtuit[pos_2+1 : ] #Kevin de CUV....

print(subtuit_2) #Kevin de CUV......

#HALLAMOS EL ESPACIO DESPUES DE KEVIN

subesp_2= subtuit_2.index(' ') ###Kevin
ayu2= subtuit_2[ : subesp_2] #KEVIN

print(ayu2) #Kevin

tweetinv= tweet[::-1] #INVERTIMOS PARA DESCUBRIR EL ULTIMO, NO EL TERCERO, OJO CON ESO

 #)B llexA# noc sollag sol a acot el aroha ,sollop sol noreitrevid es ay VUC ed niveK# y PF ed leoJ# noc saitnaduya obuh reya ed aid le

pos_3= tweetinv.index('#')
subtuit_3= tweetinv[ : pos_3] #)B llexA
print(subtuit_3)

ordenar= subtuit_3[::-1]
subtuit_4= ordenar.index(' ')

ayu3= ordenar[ :subtuit_4]
print(ayu3)

print(f'primer ayudante es: {ayu1}, segundo ayudante es: {ayu2}, ultimo ayudante es {ayu3}')

#primer ayudante es: Joel, segundo ayudante es: Kevin, ultimo ayudante es Axell

################################################################################################################################################

tweet= "This is Google #AI that sounds RT @rajat_shrimal #ArtificialIntelligence #NLU #NLP #DigitalAssistant @MikeQuindazzi @evankirstel @kuriharan"

lo= len(tweet) #cantidad
ha= tweet.index('#')
ind= tweet[ha]
con= tweet.count(ind) #cuenta cuantos hashtags hay en el tuit
print(con)

me= tweet.index('@')
ind2= tweet[me]
con2= tweet.count(ind2) #cuenta cuantas menciones hay en el tuit
print(con2)

tuit= tweet[me+1 : ] #rajat_shrimal.....
arroba= tuit.index('@')
tuit2= tuit[arroba +1 : ] #MikeQuindazzi...
print(tuit2)

esp= tuit2.index(' ')
primero= tuit2[ :esp] #MikeQuindazzi
print(primero)

otroarr= tuit2.index('@')
pos3= tuit2[ otroarr+1:] #evankirstel....

esp2= pos3.index(' ')
segundo= pos3[ :esp2] #evankirstel

print(segundo)

tuitinv= tweet[::-1]
posarroba= tuitinv.index('@')

posult= tuitinv[ :posarroba]

ultimo= posult[::-1] #kuriharan
print(ultimo)

##############################################################################################################################################################################################

s= 'ACGT'
r= 'CG'


ese= input('ingrese su secuencia s: ') #'AGCTTGCTAAGCA'

inv= ese[::-1]

print(inv)

pos= inv.index(r) #hallas las posiciones del CG

pos2= inv.index(r, pos+1) #halla la posicion del primer CG en la segunda mitad

ind= inv[pos2 :] #CGTTCGA


print(ind)

conteo= ind.count(r) #hay 2 en la segunda mitad

print(conteo)

verifica= conteo ==2 #verificamos si tiene 2 CG

cond= inv.count(r) >=3 #VERIFICAMOS SI EN TOTAL HAY 3 CG EN LA CADENA INVERTIDA

confin= verifica and cond 

print(f'La secuencia AGCTTGCTAAGCA pertenece a la especie buscada: {confin}')
print(f'total de hashtags: {con}')
print(f'total de menciones: {con2}')
print(f' segunda mencion {segundo}')
print(f' tercera mencion {ultimo}')
