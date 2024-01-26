import numpy as np

paises = np.array(["USA", "China", "Russia", "Germany", "Japan", "France", "United Kingdom", "Italy", "Canada", "Brazil", 
  "Australia", "South Korea", "India", "Mexico", "Argentina", "South Africa", "Nigeria", "Egypt", "Spain", "Netherlands", "Argentina", "USA"])

olimpiadas = {2000: "Sídney, Australia",
2004: "Atenas, Grecia",
2008: "Pekín, China",
2012: "Londres, Reino Unido",
2016: "Río de Janeiro, Brasil",
2020: "Tokio, Japón",
2024: "París, Francia"}

paisesUnicos = np.unique(paises)
columnasAnio = np.array(list(olimpiadas.keys()))

nroFil = paisesUnicos.size
nroCol = columnasAnio.size
print("Estas son las filas: ", paisesUnicos)
print("Estas son las columnas: ", columnasAnio)
m = np.random.randint(40,200,(nroFil,nroCol))
print(m)

#Para resolver los ejercicios, ud contará con una matriz con valores enteros aleatorios, las filas son los países que han ganado medallas y las columnas corresponden al año cuándo  se desarrolló la olimpiada. Tenga en consideración que los países podrían estar en cualquier orden (no se acepta índice de la fila).

#Estas son las filas:  ['Argentina' 'Australia' 'Brazil' 'Canada' 'China' 'Egypt' 'France'
# 'Germany' 'India' 'Italy' 'Japan' 'Mexico' 'Netherlands' 'Nigeria'
# 'Russia' 'South Africa' 'South Korea' 'Spain' 'USA' 'United Kingdom']

#Estas son las columnas:  [2000 2004 2008 2012 2016 2020 2024]

#FILAS

#[[ 52 116 174 152  56 155 144]
# [129 101  74  57  71 139 186]
# [105  48 186 159  69 183 181]
# [192 152 155 173  43 124 165]
# [102  96 146 107 102 198 150]
# [170 151  98 141  67  40 145]
# [139 192  80 129 160  84 194]
# [ 47 156  93 187  84 167  51]
# [ 46  81  82 120  60 110 155]
# [ 40  50 103  64 100 174  97]
# [142 185  44 187 165  58 181]
# [192  82 129 168  59 162 195]
# [156  41 107 123  41  68  44]
# [118  80 186 132  51  87  75]
# [133 151  49 174 168 144 132]
# [129  68 149  44 173 121  99]
# [125 137 109  96  61  62 103]
# [130 121  64  44 105 103  85]
# [180 146 170 162  84  40  78]
# [ 58 193 161 193 177 151  80]]



#Copiar Pregunta 1: 5 ptos
"""
Imprimir el país que obtuvo menor número de medallas en 2008.

"""
busco= np.where(columnasAnio==2008)
dosmil= m[ : , busco]
print(paisesUnicos[dosmil.argmin()])


#Copiar Pregunta 2: 6 ptos
"""
Calcular el promedio de medallas de Mexico entre los años 2008 al 2016.

"""

busco2= np.where((columnasAnio>=2008) & (columnasAnio<=2016))
mexico= m[paisesUnicos=="Mexico",busco2]
print(mexico.mean())


#Copiar Pregunta 3: 9 ptos
"""
Obtenga el máximo de medallas de France en todas las ediciones, indique en qué año fue y cuantos países superaron este máximo en el mismo año.

"""

busco3= np.where(paisesUnicos=="France")
frances= m[busco3,:]
anio= columnasAnio[frances.argmax()]

print(anio)

buscoano= np.where(columnasAnio== anio)
print(buscoano)

paisitos= m[:, buscoano]


francita= m[busco3,buscoano]


ver= (paisitos>francita)
print(ver)

print(f'Cuantos paises: {sum(ver)}')

#ver= (paisitos>valor)[0][0]
#print(ver)

#Pregunta extra: 2 ptos
"""
Imprima el top 10 países ordenados según su promedio de las 3 últimas olimpiadas

"""
suma= m[:,-3] + m[:,-2] + m[:,-1]

orden= paisesUnicos[suma.argsort()][::-1]

print(orden[:10])