from prepleccion2 import *

escojo=''
usuarios1=[]


while escojo not in ['4', 'Salir', 'SALIR', 'salir']:
    
    opcion1= '1'
    opcion2= '2'
    opcion3= '3'
    
    print('Sistema para administración de Usuarios')
    print(f'{opcion1}. Agregar nuevo usuario')
    print(f'{opcion2}. Eliminar usuarios')
    print(f'{opcion3}. Consultar usuarios')
    print('4. Salir')

    escojo= input('Elija una opción: ')


    if escojo == opcion1:
        nomb= input('Ingrese su nombre: ').lower() #Rodrigo
        ape= input('Ingrese su apellido: ').lower() #Saraguro
        fecha= input('Ingrese su fecha de nacimiento: ').lower() #20-09-1989

        if not (existeUsuario(generaUsuario(nomb,ape,fecha,usuarios1).split(),usuarios1)):
            agregaUsuario(generaUsuario(nomb,ape,fecha,usuarios1).split(),usuarios1)
            print('Se agrego el usuario')
        
        else:
            print('Este usuario ya existe')

    elif escojo == opcion2:
        otro1='a'
        otro2='b'
        print(f'{otro1}. Por usuario')
        print(f'{otro2}. Por indice')

        ingrese= input('Ingrese una opcion: ')

        if ingrese == otro1:
            elimino= input('Ingresa el usuario que desea eliminar: ').lower().split()
            if existeUsuario(elimino,usuarios1):
                print(eliminaUsuario(elimino,usuarios1))
                print('Se ha eliminado')
            
            else:
                print('Este usuario no existe')
        
        elif ingrese == otro2:
            indice= input('Ingrese el indice: ')
            if int(indice)<= len(usuarios1):
                print(eliminaUsuarioIndice(indice,usuarios1))
            
            else:
                print('No existe este indice')
        
        else:
            print('Opcion no valida')
    
    elif escojo == opcion3:
        imprimo= imprimeUsuarios(usuarios1)
    
    elif escojo in ['4', 'Salir', 'SALIR', 'salir']:
        print('FIN DEL PROGRAMA')

    else:
        print('Opcion no valida')



