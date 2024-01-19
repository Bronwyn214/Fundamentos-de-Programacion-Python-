estudiantes= 'Maria;Juan;Pepe;Luis;Jorge'
notasMat= [20, 10, 4, 12, 9]
notasFisica= [3, 2, 5, 3, 4]

#primer ejercicio

corte= estudiantes.split(';') #['Maria','Juan','Pepe',...]

companeros={}


for i in range(len(corte)):
    if corte[i] not in companeros:
        companeros[corte[i]] = notasMat[i]

print(companeros)

#{'Maria': 20, 'Juan': 10, 'Pepe': 4, 'Luis': 12, 'Jorge': 9}


#segundo ejercicio

companeros2={}

for estudiante, notas in zip(corte, notasMat):
    if estudiante not in companeros2:
        companeros2[estudiante] = notas

print(companeros2) #{'Maria': 20, 'Juan': 10, 'Pepe': 4, 'Luis': 12, 'Jorge': 9}



#tercer ejercicio

companeros3={}

prom=[]

for k in range(len(corte)):
    suma= (notasMat[k] + notasFisica[k])//2
    prom.append(suma)

for a in range(len(corte)):
    notitas=[]

    if notasMat[a] and notasFisica[a] and prom not in notitas:
        notitas.append(notasMat[a])
        notitas.append(notasFisica[a])
        notitas.append(prom[a])

        valorcito= companeros3.get(corte[a],[])

        valorcito.append(notasMat[a])
        valorcito.append(notasFisica[a])
        valorcito.append(prom[a])

        #[20,3]
        #[10,2]
        #...

        if corte[a] not in companeros3:
            companeros3[corte[a]] = valorcito

print(companeros3) #{'Maria': [20, 3], 'Juan': [10, 2], 'Pepe': [4, 5], 'Luis': [12, 3], 'Jorge': [9, 4]}

#{'Maria': [20, 3, 11], 'Juan': [10, 2, 6], 'Pepe': [4, 5, 4], 'Luis': [12, 3, 7], 'Jorge': [9, 4, 6]}




