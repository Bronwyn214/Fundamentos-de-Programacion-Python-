#CREE UN PROGRAMA QUE PERMITA IDENTIFICAR SI UN NUMERO INGRESADO POR EL
#USUARIO ES PRIMO

#UN NUMERO PRIMO ES:
#QUE SEA NATURAL (ENTERO)
#MAYOR A 1
#DIVISIBLE SOLO PARA SI MISMO Y PARA 1



#PRIMERA MANERA: HACERLO CON FOR

num= int(input('ingrese su numero ')) #5

if num >1: #SI EL NUMERO QUE INGRESE ES MAYOR A 1, PUEDO CONTINUAR

    cont=0
    for i in range(2,num): # del 2 hasta el numero que ingreso
        #ejemplo: del 2 hasta el 5 sin incluir (2,4) OJO
    
        resto=num%i

        #5 % 2
        #5 % 3
        #5 % 4
       
        print(f'{num} % {i} = {resto}')

        #5 % 2 = 1
        #5 % 3 = 2
        #5 % 4 = 1
        #5 % 5 = 0 (YA NO ENTRARIA)
       
        if resto ==0: # SI MI MODULO DE MI OPERACION DA 0, CONTARIA
            #COMO NO NUMERO PRIMO
       
            cont+=1
    
    if cont==0: #SI MI CONTADOR ES 0, OSEA QUE NO HAYA CONTADO UN NO NUMERO PRIMO
        
        print(f'el numero {num} es un numero primo')
    
    else: # SI MI CONTADOR ES DIFERENTE DE 0, ENTONCES TENGO UN NO NUMERO PRIMO
        print(f'el numero {num} NO es un numero primo')


else: #SI NO LO ES, PUES AUTOMATICAMENTE NO ES UN NUMERO PRIMO
    print(f'el numero {num} NO es un numero primo')


#SEGUNDA MANERA: HACERLO CON WHILE

num= int(input('ingrese su numero: ')) #5

if num >1:

    cont=0
    i= 2
    while i<num and cont==0: 
        # 2< 5 = true
        # 2< 4 = true
        # 2< 3 = true
        # 2 <2 = false

        print(i)
        resto= num%i

        print(f'{num} % {i} = {resto}')
        
        if resto ==0:
            cont+=1
        i+=1
        
    if cont == 0:
        print(f'EL {num} ES UN NUMERO PRIMO')
    else:
        print(f'EL {num} NO ES UN NUMERO PRIMO')


else:
    print('EL 1 NO ES UN NUMERO PRIMO')


###############################################################################
