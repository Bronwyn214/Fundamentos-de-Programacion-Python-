#Nombre
#Matricula
#Carrera


#Ejercicio 1, De la siguiente lista, clasifique en una nueva lista (correosEdu) 
#todos los correos que empiecen con una vocal, que sean educativos. Presente la lista ordenada de la z-a.

#correos = ["abc1@espol.edu.ec", "elcorreo@gmail.com", "info@udla.edu.cl", "correo@ugedu.ec", "info@sri.gob.ec", "oui@mit.edu", "correo10@hotmail.com", "opqr@sfq.edu.ec", "edu@bbva.fin.es", "omg@uba.edu.ar"]
#Resultado: correosEdu = [ "oui@mit.edu", "opqr@sfq.edu.ec", "omg@uba.edu.ar", "info@udla.edu.cl", "abc1@espol.edu.ec"]


print("Inicio ejercicio 1")
correos = ["abc1@espol.edu.ec", "elcorreo@gmail.com", "info@udla.edu.cl", "correo@ugedu.ec", "info@sri.gob.ec", "oui@mit.edu", "correo10@hotmail.com", "opqr@sfq.edu.ec", "edu@bbva.fin.es", "omg@uba.edu.ar"]
vocales=['a','e','i','o','u']
nuevos=[]
def correosEdu(nuevos):
  correos.sort(reverse=True)
  for i in correos:
    
    if i[0] in vocales and i not in nuevos and '.edu' in i:
      nuevos.append(i)
      
    
  return nuevos
print(correosEdu(nuevos)) #['oui@mit.edu', 'opqr@sfq.edu.ec', 'omg@uba.edu.ar', 'info@udla.edu.cl', 'abc1@espol.edu.ec']



#print("Fin ejercicio 1")


#Ejercicio 2, Crear una función denominada generaCorreo(nombre, apellido, empresa, tipo) que recibe 
#nombre, apellido, empresa, tipo y permite retornar una cadena que representa un correo según las siguientes reglas.

#1) El usuario se conforma de las 2 primeras letras del nombre, guión bajo y las 5 primeras letras del apellido.

#2) El proveedor se conforma con cada primera letra del nombre de la empresa en el caso de que la palabra sea mayor a 12 caracteres. 
#Si es menor a 12 caracteres elimine los espacios y convierta a minúscula.

#3) El tipo permite establecer como finaliza el correo, establezca los siguientes 4 casos: 
#educación -> edu, organización -> org, comercio -> com, gobierno -> gov, .

#4) Todos los correos son de Ecuador así que deben terminar en ec.

#generaCorreo("Carlos", "Perez", "Universidad de las Américas", "educación") #retornaría ca_perez@udla.edu.ec

#generaCorreo("Ana", "Mena", "Patitas Gye", "organización") #retornaría an_mena@patitasgye.org.ec

#generaCorreo("Xavier", "Lopez", "Barcabi", "comercio") #retornaría xa_lopez@barcabi.com.ec


print("Inicio ejercicio 2")

def generaCorreo(nombre, apellido, empresa, tipo):
  part=''
  if len(empresa)>12:
    corte= empresa.split(' ')
    
    for i in corte:
      part+= i[0]
  
  else:
    part = empresa.lower()
  
  if tipo == 'educación':
    tipo = '.edu.ec'
  
  elif tipo == 'organización':
    tipo= '.org.ec'
  
  elif tipo == 'comercio':
    tipo= '.com.ec'
  
  usuario= nombre[0:2]+"_" + apellido[0:5]+'@'+part + tipo
  
  return usuario.replace(' ','').lower()

print(generaCorreo("Carlos", "Perez", "Universidad de las Américas", "educación"))
#ca_perez@udla.edu.ec
print(generaCorreo("Ana", "Mena", "Patitas Gye", "organización"))
#an_mena@patitasgye.org.ec
print(generaCorreo("Xavier", "Lopez", "Barcabi", "comercio"))
#xa_lopez@barcabi.com.ec



#print("Fin ejercicio 2")


#Ejercicio 3, Escriba un programa que solicite nombre y apellido (1 solo input) de una persona para los próximos estudiantes de la ESPOL. 
#Mientras el usuario no ingrese la palabra cierre almacene cada dato en la lista de inscritos.

#Cuando finalice genere una lista de correos con todos los inscritos. 
#Use la función del ejercicio 2, envíe de la lista nombre, apellido, "ESPOL" y "educación".

#Imprima todos los correos generados.
#[ro_sarag@espol.edu.ec, fe_cresp@espol.edu.ec, ca_rodri@espol.edu.ec,] #version 2

print("Inicio ejercicio 3")

ingrese=''
lista=[]

while ingrese!='cierre':
  ingrese= input('Ingrese su nombre y su apellido: ') #Rodrigo Saraguro
  if ingrese.replace(' ','').isalpha() and ingrese !='cierre':
    lista.append(ingrese)
    print(lista)
  else:
    print('Introduce otra vez')

for i in range(len(lista)):
  nombres= lista[i]
  cortesito= nombres.split(' ')
  nombre= cortesito[0]
  apellido= cortesito[1]

  print(generaCorreo(nombre,apellido,"Espol", 'educación'))
  
  #ro_sarag@espol.edu.ec
  #fe_cresp@espol.edu.ec
  #ca_rodri@espol.edu.ec


#print("Fin ejercicio 3")