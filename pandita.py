import pandas as pd

serie = pd.Series([1,2,4,5,6], index=['a','b','c','d','e'])
#print(serie['e'])

equipoFutbol = pd.DataFrame({'nombres':["Enner Valencia", "Kendry Paez", "Moises Ramirez"], 'club': ["Inter Porto Alegre", "Independiente del Valle", "Independiente del Valle"], "posicion":['delantero', 'media punta', 'portero'], 'goles':[13, 2, 0], 'faltas':[1,1,2]}, index=[31,10,1], columns=['posicion','nombres','goles','club','faltas'])

#print(equipoFutbol)

#print("La selección actualmente tiene ",equipoFutbol['goles'].sum(), "goles")

#print("Jugadores de IDV", equipoFutbol[equipoFutbol.club=="Independiente del Valle"].nombres)

#print("Jugadores con una falta", equipoFutbol[equipoFutbol.faltas==1].nombres)

#print(equipoFutbol.describe())

#print(serie)

#Leer datos
datosOlimpiadas = pd.read_csv("datos.csv")
print(datosOlimpiadas)

#1. Imprimir el total de medallas de Ecuador y el total general.

medallasEc = datosOlimpiadas[datosOlimpiadas.Country=='Ecuador']['Total General'].values[0]

print(f"Ecuador ha ganado {medallasEc} medallas en los Juegos.")

medallasTotal = datosOlimpiadas['Total General'].sum()
print(f"Medallas totales: {medallasTotal}")

#2. Imprimir la suma de medallas de plata en Invierno de todos los países.

medallasTotal = datosOlimpiadas['Total Invierno'].sum()
print(f"Medallas invierno: {medallasTotal}")

medallasTotal = datosOlimpiadas['Total Verano'].sum()
print(f"Medallas verano: {medallasTotal}")

medallasTotal = datosOlimpiadas['Plata Invierno'].sum()
print(f"Medallas plata invierno: {medallasTotal}")

#3. Imprimir el nombre de los países que superan el total de medallas de plata de Argentina.

medallasArg = datosOlimpiadas[datosOlimpiadas.Country=='Argentina']['Plata Invierno'].values[0] + datosOlimpiadas[datosOlimpiadas.Country=='Argentina']['Plata Verano'].values[0]

totalPlatatodosP = datosOlimpiadas['Plata Verano']+ datosOlimpiadas['Plata Invierno']
print(datosOlimpiadas[totalPlatatodosP>medallasArg].Country)


#4. Imprimir cuantos países han ganado más de una medalla de bronce en Verano.

filtro = datosOlimpiadas[datosOlimpiadas['Bronce Verano'] > 1]
print('Países que han ganado más de una medalla de bronce de Verano: ',len(filtro))


#5. Imprimir el top 5 de países con más medallas

top5 = datosOlimpiadas.nlargest(10, 'Total General')

print("Top 5 países con más medallas en Total General:")
print(top5[['Country', 'Total General']])

#6. Imprima el país con más juegos y el país con menos juegos.

paisMax = datosOlimpiadas.loc[datosOlimpiadas['Nro Olimpiadas'].idxmax(), 'Country']
paisMin = datosOlimpiadas.loc[datosOlimpiadas['Nro Olimpiadas'].idxmin(), 'Country']

print(f"País con más juegos: {paisMax} ({datosOlimpiadas['Nro Olimpiadas'].max()} juegos)")
print(f"País con menos juegos: {paisMin} ({datosOlimpiadas['Nro Olimpiadas'].min()} juegos)")