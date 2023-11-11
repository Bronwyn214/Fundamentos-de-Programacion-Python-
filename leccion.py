#Nombre
#Matricula
#Carrera

instituciones="""Escuela Superior Politécnica del Litoral,
Universidad Católica Santiago de Guayaquil, 
Universidad de Especialidades Espíritu Santo,
Universidad Internacional del Ecuador,
Instituto Tecnológico Superior Sudamericano,
Instituto de Altos Estudios Nacionales,
Instituto Ecuatoriano de Seguridad Social,
Universidad Técnica Particular de Loja,
Universidad Técnica de Ambato,
Universidad Ténica de Manabí,
Universidad Politécnica de Madrid,
Massachusetts Institute of Technology,
National Aeronautics and Space Administration"""

print("Inicio de ejercicio 1") #Usando la variable instituciones, imprima todos los Institutos en letras MAYÚSCULAS y las Universidades en letras minúsculas.

cortada= instituciones.split(',')

print('Insitutos')

cont=0
cont2=0

contin=0
contotro=0

palcort=0


for institucion in cortada:
  if 'Instituto' in institucion or 'Institute' in institucion or 'National' in institucion:
    conteo= institucion.count('Instituto') + institucion.count('Institute') + institucion.count('National')
    cont+=conteo
    conteoins= institucion.count('Instituto')
    contin+= conteoins
    conteotro= institucion.count('Institute') + institucion.count('National')
    contotro+=conteotro
    print(institucion.upper())

print('Universidades')

for universidad in cortada:
  if 'Universidad' in universidad or 'Escuela' in universidad:
    conteo2= universidad.count('Universidad') + universidad.count('Escuela')
    cont2+=conteo2
    print(universidad.lower())


#print("Fin de ejercicio 1")


print("Inicio de ejercicio 2") #Usando la variable instituciones imprima los siguientes datos:

#Cantidad de instituciones total
#Cantidad de universidades
#Cantidad de 'institutos'
#Cantidad de otras instituciones
#Instituto con el nombre más corto


if cont>0:
  print(f'Cantidad de instituciones totales: {cont}')

if cont2>0:
  print(f'Cantidad de universidades: {cont2}')

if contin>0:
  print(f'Cantidad de institutos: {contin}')
  
if contotro>0:
  print(f'Cantidad de otras instituciones: {contotro}')

cort=100
palcort=''

for escuela in cortada:
  if 'Instituto' in escuela or 'Institute' in escuela or 'National' in escuela:
    if len(escuela)<cort:
      cort= len(escuela)
      palcort = escuela
  

print(f'Instituto con el nombre más corto {palcort}')

#print("Fin de ejercicio 2")


print("Inicio de ejercicio 3") #Crear un juego para adivinar nombres de Universidades. Las reglas son las siguientes:

#Dispone de 5 intentos, siempre se repite 5 veces.
#Solicite el nombre de una universidad. En cada intento debe imprimir su nro de vez.
#Formatee el nombre a MAYÚSCULAS y aplique el mismo formato a la variables instituciones.
#Valide si se encuentra la universidad en la variable instituciones. Si la encuentra debe borrarla de la cadena para evitar repetir y sumar 1 acierto, si no se encuentra suma 1 error.
#Imprima cuantos aciertos tuvo y cuantos errores.
#Si acertó 3 o más veces imprima "ERES UN CRACK ACADÉMICO", si es inferior a 3 imprima "PARA LA PRÓXIMA CAMPEÓN".

int=0
ac=0
er=0

cambio= instituciones.upper()

for i in range(5):
  solic= input('Ingrese el nombre de universidad: ').upper()
  
  if solic in cambio and 'UNIVERSIDAD' in solic or 'ESCUELA' in solic:
    print('Encontrado')
    reemp= cambio.replace(solic,'')
    ac+=1
    int+=1
    print(reemp)
  
  else:
    print('No encontrado')
    er+=1
    int+=1

print(f'Aciertos: {ac}')
print(f'Errores: {er}')
print(f'Intentos: {int}')

if ac>=3:
  print('ERES UN CRACK ACADÉMICO')
else:
  print(f'PARA LA PRÓXIMA CAMPEÓN')
#print("Fin de ejercicio 3")