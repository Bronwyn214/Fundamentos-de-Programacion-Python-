resultado = 'Resultado de Laboratorio ‘Su salud‘ Nombre del paciente: Jose Aimas E-mail del paciente: jose.aimas@gmail.com Resultados del laboratorio: INR 1.25 segundos BGT 180.12 mmol/dL HGB 13 g/dL ESR 3.2 mm/hora RBC 4000024.2 cel/uL TA 1.5 ng/dL WBC 123233.23 cel/uL. Los valores de este informe no representan un diagnóstico. Firmamédico responsable Dr. Juan Pozo'
#resultado = 'Resultado de Laboratorio ‘Sana’ Nombre del paciente: Ginger Irene Cruz Jurado Edad: 25 años E-mail: giircrju@espol.edu.ec Resultados: Azúcar BGT 180.12 mmol/dL Hemoglobina HGB 13 g/dL Hormonal TA 1.5 ng/dL. Médico responsable Dra. Karina Elizabeth Plaza'


resinv= resultado[::-1] #invierto

#print(resinv)

pos= resinv.index(' ') #pos del primer espacio
#print(pos)

pos2= resinv.index(' ', pos+1) # pos del segundo espacio

pos3= resinv.index(' ', pos2+1) #pos del tercer espacio

nombredoctorinv= resinv[ : pos3] #desde el principio hasta el tercer espacio

#print(nombredoctorinv)

nombredoctor= nombredoctorinv[::-1] #Dr. Juan Pozo y Dra. Karina Elizabeth Plaza
print(nombredoctor)

#################################################################################
variable= [] #['INR', 'BGT', 'HGB', 'ESR', 'RBC', 'TA', 'WBC'], ['BGT', 'HGB', 'TA']
caravar= [] #['1.25', '180.12', '13', '3.2', '4000024.2', '1.5', '123233.23'], ['180.12', '13', '1.5']
caravar2= [] #['segundos', 'mmol/dL', 'g/DL', 'mm/hora', 'cel/uL', 'ng/dL', 'cel/UDL'], ['mmol/dL', 'g/dL', 'ng/dL']


corteza= resultado.split(' ')

if 'INR' not in resultado:
    print('No posee esa caracteristica')
else:
    print('Si dispone esa caracteristica')
    pos= corteza.index('INR')
    ind= corteza[pos] #'INR'
    #print(ind)
    car= corteza[pos+1] #'1.25'
    #print(car)
    car2= corteza[pos+2] #'segundos'
    #print(car2)
    variable.append(ind)
    caravar.append(car)
    caravar2.append(car2)
    #print(pos)
print(variable)
print(caravar)
print(caravar2)


#######################################################################################################################


if 'BGT' not in resultado:
    print('No dispone de esta caracteristica')

else:
    print('Si dispone esa caracteristica')
    posbege= corteza.index('BGT')
    ind2= corteza[posbege] #BGT
    car_b= corteza[posbege+1] #PRIMERA CAR
    car_b2= corteza[posbege+2] #SEGUNDA CAR
    variable.append(ind2)
    caravar.append(car_b)
    caravar2.append(car_b2)
print(variable)
print(caravar)
print(caravar2)

################################################################################################################################

if 'HGB' not in resultado:
    print('No dispone de esta caracteristica')

else:
    print('Si dispone esa caracteristica')
    posache= corteza.index('HGB')
    ind3= corteza[posache]
    car_h= corteza[posache+1] #PRIMERA CAR
    car_h2= corteza[posache+2] #SEGUNDA CAR
    variable.append(ind3)
    caravar.append(car_h)
    caravar2.append(car_h2)
print(variable)
print(caravar)
print(caravar2)

################################################################################################################################

if 'ESR' not in resultado:
    print('No dispone de esta caracteristica')
else:
    print('Si dispone de esta caracteristica')
    posese= corteza.index('ESR')
    ind4= corteza[posese]
    car_es= corteza[posese+1] #PRIMERA CAR
    car_es2= corteza[posese+2] #SEGUNDA CAR
    variable.append(ind4)
    caravar.append(car_es)
    caravar2.append(car_es2)
print(variable)
print(caravar)
print(caravar2)

######################################################################################################################


if 'RBC' not in resultado:
    print('No dispone de esta caracteristica')

else:
    print('Si dispone de esta caracteristica')
    poserre= corteza.index('RBC')
    ind5= corteza[poserre]
    car_er= corteza[poserre+1]
    car_er2= corteza[poserre+2]
    variable.append(ind5)
    caravar.append(car_er)
    caravar2.append(car_er2)
print(variable)
print(caravar)
print(caravar2)

######################################################################################################################

if 'TA' not in resultado:
    print('No dispone de esta caracteristica')
else:
    print('Si dispone de esta caracteristica')
    posta= corteza.index('TA')
    ind6= corteza[posta]
    car_ta= corteza[posta+1]
    car_ta2= corteza[posta+2]
    variable.append(ind6)
    caravar.append(car_ta)
    caravar2.append(car_ta2)
print(variable)
print(caravar)
print(caravar2)

#######################################################################################################################

if 'WBC' not in resultado:
    print('No dispone de esta caracteristica')
else:
    print('Si dispone de esta caracteristica')
    posdob= corteza.index('WBC')
    ind7= corteza[posdob]
    car_w= corteza[posdob+1]
    car_w2= corteza[posdob+2]
    variable.append(ind7)
    caravar.append(car_w)
    caravar2.append(car_w2)
print(variable)
print(caravar)
print(caravar2)

#['INR', 'BGT', 'HGB', 'ESR', 'RBC', 'TA', 'WBC'], ['BGT', 'HGB', 'TA']
#['1.25', '180.12', '13', '3.2', '4000024.2', '1.5', '123233.23'], ['180.12', '13', '1.5']
#['segundos', 'mmol/dL', 'g/dL', 'mm/hora', 'cel/uL', 'ng/dL', 'cel/uL.'], ['mmol/dL', 'g/dL', 'ng/dL']

informe= 'INFORME DE LABORATORIO'
print(informe)

print(f'**********************')

for caracteristica in range(len(variable)):
    posultt= variable[caracteristica]
    posult= caravar[caracteristica]
    posult2= caravar2[caracteristica]

    print(posultt, posult, posult2)


doctor= f'Medico: {nombredoctor}'
print(doctor)
