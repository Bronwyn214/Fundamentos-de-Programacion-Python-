#1.1. generaUsuario(nombre, apellido, fechaNac) que recibe nombre, apellido y fecha de nacimiento. 
#Retorna un usuario que concatena nombre y apellido separados con un punto y selecciona los 2 últimos digitos del año de nacimiento.

#generaUsuario("Rodrigo", "Saraguro", "20-09-1989") #retorna el usuario rodrigo.saraguro89

def generaUsuario(nombre, apellido, fechaNac,usuarios):
    
    usuario = nombre.lower()+'.'+apellido.lower()+fechaNac[-2:]
    return usuario



#1.2. agregaUsuario(usuario, usuarios), si el usuario NO existe se agrega a la lista usuarios, 
#en caso de que ya exista debe retornar la lista sin agregar. No es posible duplicar usuarios.

def agregaUsuario(usuario, usuarios):
    for i in usuario:
        if i not in usuarios:
            usuarios.append(i)
            return usuarios
        
        else:
            return usuarios

#1.3.1. eliminaUsuario(usuario, usuarios), si el usuario existe en usuarios se elimina de la lista usuarios, 
# solo si fue posible eliminar presente un mensaje que el usuario fue eliminado.

def eliminaUsuario(usuario,usuarios):
    for i in usuario:
        if i in usuarios:
            usuarios.remove(i)
    
    return usuarios

#eliminaUsuarioIndice(posicion, usuarios), elimina el usuario con tal indice de la lista usuarios. 
#Si fue posible borrar imprima cual usuario fue borrado. Si no existe el índice imprima un mensaje de error.

def eliminaUsuarioIndice(posicion, usuarios):
    if len(usuarios)>=int(posicion):
        elimino= usuarios.pop(int(posicion))
        print(f'El usuario {elimino} fue eliminado')
    
    else:
        print('No existe ese indice')
    
    return usuarios


#1.4. existeUsuario(usuario, usuarios), si el usuario existe en usuarios retorne True, sino existe False.

def existeUsuario(usuario, usuarios):
    for i in usuario:    
        if i in usuarios:
            return True
        else:
            return False

    
#imprimeUsuarios(usuarios), imprime los usuarios en orden de la A-Z, 
#imprima también la numeración y una tabulación. Revise el ejemplo.

def imprimeUsuarios(usuarios):
    copia= usuarios.copy()
    numero='Nro'
    persona= 'Usuario'
    print(numero,persona)

    copia.sort()

    for i in range(len(usuarios)):
        print(f'{i+1}. {usuarios[i]}')
