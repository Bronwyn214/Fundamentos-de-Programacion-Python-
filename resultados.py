#resultado = 'Resultado de Laboratorio ‘Su salud‘ Nombre del paciente: Jose Aimas E-mail del paciente: jose.aimas@gmail.com Resultados del laboratorio: INR 1.25 segundos BGT 180.12 mmol/dL HGB 13 g/dL ESR 3.2 mm/hora RBC 4000024.2 cel/uL TA 1.5 ng/dL WBC 123233.23 cel/uL. Los valores de este informe no representan un diagnóstico. Firmamédico responsable Dr. Juan Pozo'
resultado = 'Resultado de Laboratorio ‘Sana’ Nombre del paciente: Ginger Irene Cruz Jurado Edad: 25 años E-mail: giircrju@espol.edu.ec Resultados: Azúcar BGT 180.12 mmol/dL Hemoglobina HGB 13 g/dL Hormonal TA 1.5 ng/dL. Médico responsable Dra. Karina Elizabeth Plaza'

cortada= resultado.split(' ') #['Resultado', 'de', 'Laboratorio',....]

variables= []
numeros= []
carac= []

if 'INR' in resultado:
    posine= cortada.index('INR')

    indine= cortada[posine]
    #print(indine) #'INR'
    variables.append(indine)

    numinde= cortada[posine+1]
    #print(numinde) #1.25
    numeros.append(numinde)

    caraine= cortada[posine+2]
    #print(caraine) #'segundos'
    carac.append(caraine)

    print(variables)
    print(numeros)
    print(carac)

else:
    print('No posee esta caracteristica')


if 'BGT' in resultado:
    posbege= cortada.index('BGT')

    indbege= cortada[posbege]
    variables.append(indbege)

    numbege= cortada[posbege+1]
    numeros.append(numbege)

    carabege= cortada[posbege+2]
    carac.append(carabege)

    print(variables)
    print(numeros)
    print(carac)
else:
    print('No posee esta caracteristica')


if 'HGB' in resultado:
    posache= cortada.index('HGB')

    indache= cortada[posache]
    variables.append(indache)

    numache= cortada[posache+1]
    numeros.append(numache)

    caraache= cortada[posache+2]
    carac.append(caraache)

    print(variables)
    print(numeros)
    print(carac)

else:
    print('No posee esta caracteristica')


if 'ESR' in resultado:
    posere= cortada.index('ESR')

    indere= cortada[posere]
    variables.append(indere)

    numere= cortada[posere+1]
    numeros.append(numere)

    caraere= cortada[posere+2]
    carac.append(caraere)

    print(variables)
    print(numeros)
    print(carac)

else:
    print('No posee esta caracteristica')


if 'RBC' in resultado:
    posbece= cortada.index('RBC')

    indece= cortada[posbece]
    variables.append(indece)

    numbece= cortada[posbece+1]
    numeros.append(numbece)

    carabece= cortada[posbece+2]
    carac.append(carabece)

    print(variables)
    print(numeros)
    print(carac)

else:
    print('No posee esta caracteristica')


if 'TA' in resultado:
    posta= cortada.index('TA')

    indta= cortada[posta]
    variables.append(indta)

    numta= cortada[posta+1]
    numeros.append(numta)

    carata= cortada[posta+2]
    carac.append(carata)

    print(variables)
    print(numeros)
    print(carac)

else:
    print('No posee esta caracteristica')


if 'WBC' in resultado:
    postdob= cortada.index('WBC')

    indob= cortada[postdob]
    variables.append(indob)

    numdob= cortada[postdob+1]
    numeros.append(numdob)

    caradob= cortada[postdob+2]
    carac.append(caradob)

    print(variables)
    print(numeros)
    print(carac)

else:
    print('No posee esta caracteristica')


################################################################################################

#PARA EL PRIMER RESULTADO

#['INR', 'BGT', 'HGB', 'ESR', 'RBC', 'TA', 'WBC']
#['1.25', '180.12', '13', '3.2', '4000024.2', '1.5', '123233.23']
#['segundos', 'mmol/dL', 'g/dL', 'mm/hora', 'cel/uL', 'ng/dL', 'cel/uL.']

#PARA EL SEGUNDO RESULTADO

#['BGT', 'HGB', 'TA']
#['180.12', '13', '1.5']
#['mmol/dL', 'g/dL', 'ng/dL.']

info= 'INFORME DE LABORATORIO'
print(f'{info:<20}')

ast= len(info)* '*'
print(f'{ast:<20}')



for caracteristica in range(len(variables)):
    posvar= variables[caracteristica]
    posnum= numeros[caracteristica]
    poscarac= carac[caracteristica]

    print(posvar, posnum, poscarac)


if 'Dr.' in cortada:
    pos= cortada.index('Dr.')
    ind= cortada[pos :]
    #print(ind)
    une= ' '.join(ind)
    print(f'Medico: {une}') #Dr. Juan Pozo


elif 'Dra.' in cortada:
    pos2= cortada.index('Dra.')
    ind2= cortada[pos2: ]
    #print(ind2)
    une2= ' '.join(ind2)
    print(f'Medico: {une2}') #Dra. Karina Elizabeth Plaza

else:
    print('No posee doctor para tu informe')


##########################################################################################
