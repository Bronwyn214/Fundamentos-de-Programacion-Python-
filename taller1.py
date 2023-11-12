#Matricula
#Nombre
#Carrera


#Ejercicio 1
print('Bienvenido al sistema XYZ')
usuario= input('Ingrese usuario: ').lower() #javier

if usuario.isalpha() and usuario!='admin' and len(usuario)>=6:
    clave= input('Ingrese contraseña: ') #3920dmdmdf
    
    if len(clave)>=8 and clave.isalnum():
        if '123' not in clave and 'abc' not in clave and 'hola'          not in clave and 'contrasena' not in clave:
          print('Registro realizado exitosamente.')

        else:
          print(f'La contraseña {clave} no es correcta. No fue             posible hacer el registro.')
    else:
      print(f'La contraseña {clave} no es correcta. No fue             posible hacer el registro.')



else:  
  print(f'El usuario {usuario} no es correcto. No fue posible hacer el registro')


#Ejercicio 2

print('¡Hola soy Siri!')

deseo= input('Deseas una recomendación de clima? ')

if deseo== 'Si' or deseo == 'SI':

  clima= input('Ingrese el clima: ')

  if clima == 'soleado':
    print('Si hace sol usa protector solar y gafas de sol')
    print('Gracias por usar Siri, hasta pronto.')

  elif clima == 'nevado':
    print('Si está nevando abrígate y usa ropa abrigada.')
    print('Gracias por usar Siri, hasta pronto.')

  elif clima == 'lluvioso':
    print('Si está lloviendo no olvides llevar un paraguas.')
    print('Gracias por usar Siri, hasta pronto.')

  elif clima == 'nublado':
    print('Si está nublado es un buen día para caminar.')
    print('Gracias por usar Siri, hasta pronto.')

  else:
    print('No me es posible dar una recomendación. Inténtalo más tarde')
    print('Gracias por usar Siri, hasta pronto.')




else:
  print('Gracias por usar Siri, hasta pronto.')



#Ejercicio 3

print('Postula a una BECA SANTANDER')

cedula= input('Ingrese su cédula: ') #'0705795219'

nombres= input('Ingrese nombre y apellido: ') #'Rodrigo Saraguro'


if cedula.isdigit() and len(cedula)==10 and nombres.count(' ')==1 and nombres.replace(' ','').isalpha() and nombres.title():

  print('Cédula correcta')
  print('Nombres correctos')

  ano= input('Ingrese año de nacimiento: ')#1989

  if len(ano)==4 and ano.isdigit() and (2023-int(ano))<=40:
    print('Cumple edad')

    pais= input('Ingrese país de origen: ')#'Ecuador'

    if pais.title() and pais.isalpha():
      print('Pais elegible')

      titulo= input('Ingrese titulo: ') #'Ingeniería en Sistemas'

      if titulo == 'Ingeniería en Sistemas' and titulo.replace(' ','').isalpha():
        print('Titulo correcto')

        prom= float(input('Ingrese promedio: ')) #8.6

        if prom>= 8.5:
          print('Cumple promedio minimo')

          print(f'El postulante {nombres.upper()} con DNI {cedula} de {2023-(int(ano))} anos con titulo {titulo} y promedio de {prom} puede postular a la BECA SANTANDER')

        else:
          print('No cumple promedio minimo')

      else:
        print('Título incorrecto')  
      


    else:
      print('País incorrecto')  

    

  else:
    print('No Cumple edad')

  

else:
  print('Cédula y/o Nombre incorrecta')
  print('No fue posible realizar la postulación.')