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
