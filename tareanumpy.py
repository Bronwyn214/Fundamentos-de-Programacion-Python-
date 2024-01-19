from numpy import *

plataformas = ["Netlifx", "Spotify", "Youtube", "Disney", "HBO", "DirectvGo", "A3mediaplayer"] #filas
años = arange(2015, 2024) #columnas

print(años) #[2015 2016 2017 2018 2019 2020 2021 2022 2023]

# Pregunta 1: Crear la matriz usuarios de filas x columnas con valores enteros desde el 10000 hasta el 99999.
# Las filas representan las plataformas, las columnas son los años.

arr1= array(plataformas)
filas= arr1.size #plataformas
columnas= años.size #anos

matriz= random.randint(10000, 99999 , (filas,columnas))

print(matriz)

#[[36082 12557 18752 62419 73968 21067 37318 14009 44183] 
# [95769 81342 12749 71279 37787 33992 12195 99684 94336] 
# [50368 32081 57325 51420 92862 97595 47213 39955 10737] 
# [50286 32513 20247 80021 44504 69299 20054 44766 79710] 
# [66337 77047 78063 35388 62366 12867 79069 39262 48795] 
# [61411 37633 38204 32357 44560 26360 25206 81884 66992] 
# [31893 56977 88977 79797 75987 59094 59933 88880 58516]]




# Pregunta 2: ¿Cuál es la media de usuarios por plataforma del 2015 al 2020?

med= matriz[ :, : 6]
print(med.mean(axis=1))

#2015 2016 2017 2018 2019 2020 2021 2022 2023]
#[[43641 72290 85578 72830 65142 85897 41264 24239 19131]
# [20169 19539 50757 36465 54605 48160 29410 33962 54909]
# [98385 70571 33686 44931 28377 46597 14201 14005 60048]
# [90488 13928 64217 41387 67021 66462 65959 84637 40618]
# [29199 23910 67574 19536 12943 54256 83255 33661 85477]
# [89497 44294 10217 67149 28855 87765 98149 67763 11515]
# [93593 18817 61865 89329 81783 98330 58933 69621 30994]]
#[70896.33333333 38282.5        53757.83333333 57250.5
# 34569.66666667 54629.5        73952.83333333]


# Pregunta 3: ¿En qué año hubo la mayor cantidad de usuarios en Youtube?

print(arr1)
yout= matriz[2,:]
print(años[yout.argmax()])

#['Netlifx' 'Spotify' 'Youtube' 'Disney' 'HBO' 'DirectvGo' 'A3mediaplayer']
#filas

#[2015 2016 2017 2018 2019 2020 2021 2022 2023]
#[[68340 85776 61840 21645 11262 69112 48935 19860 12357]
# [90722 10581 97867 42659 63146 21241 55013 25179 36117]
# [11889 32775 37117 50727 91596 13935 11067 72882 10391]
# [98068 32652 98778 17239 84502 24723 36105 79608 70446]
# [63174 70097 12278 44228 88661 19983 82578 67686 88716]
# [71738 97470 88691 82531 35427 48575 35843 55109 65590]
# [32689 65517 57662 59886 26883 44792 96879 53560 48857]]

#[11889 32775 37117 50727 91596 13935 11067 72882 10391] fila de youtube
#91596
#2019 (ano)



# Pregunta 4: ¿Cuantas plataformas tuvieron mas usuarios en 2015 que en 2023?

plat= matriz[:, 0]
plat2= matriz[:, -1]
op= plat>plat2
print(op)

print(sum(op))

#[2015 2016 2017 2018 2019 2020 2021 2022 2023]
#[[97409 10342 42482 23735 74129 94551 26990 73711 99648]
# [26684 82097 40708 57838 66202 12547 73850 10213 51010]
# [60103 48034 88503 35260 82052 25417 56130 44489 66793]
# [66653 27393 50948 34491 99565 34876 85619 16765 21844]
# [14476 52940 38569 29983 35085 74731 31934 15738 93428]
# [18716 16467 25138 56901 97667 22824 87827 89043 87051]
# [72032 64098 86276 42533 61370 63130 54925 17967 59469]]

#[False False False  True False False  True]

#2 (sum cuenta solo los true en booleanos)



# Pregunta 5: Imprima las plataformas ordenadas según los usuarios del 2021.

dosmil= matriz[:, 6]

ordin= sort(dosmil, axis=0)
print(ordin)

orden= argsort(dosmil, axis=0)

print(arr1[orden])

#[2015 2016 2017 2018 2019 2020 2021 2022 2023]
#[[14105 71146 24501 41235 66330 41319 68295 50759 66615]
# [69400 68322 58178 36594 47763 21163 87519 53953 96204]
# [97620 95885 73542 81357 64125 31819 58372 67324 79234]
# [34768 27346 66885 50948 37508 80864 95724 36126 46127]
# [23111 83909 19406 12763 84291 71614 15382 27753 57120]
# [49237 93999 89709 96433 69009 93874 45381 74331 85233]
# [87033 14130 68849 93412 38492 35322 81614 71567 71755]]

#[15382 45381 58372 68295 81614 87519 95724]
#['HBO' 'DirectvGo' 'Youtube' 'Netlifx' 'A3mediaplayer' 'Spotify' 'Disney']


# Pregunta 6: Elija 2 plataformas al azar ¿Cuál de ellas tuvo más usuarios en los 3 últimos años?

ale= random.choice(plataformas,2, replace= False) #Netflix y Spotify
print(ale)

busco= where(arr1 == ale[0])
busco2= where(arr1 == ale[-1])


tres= matriz[busco, -3:]


tres2= matriz[busco2, -3: ]

suma1= sum(tres)
suma2= sum(tres2)

print(f'Suma de {ale[0]}: {suma1}')
print(f'Suma de {ale[-1]}: {suma2}')

bul= suma1>suma2

print(f'Para {ale[0]}, tuvo mas usuarios en los ultimos 3 anos? {bul}')

bul2= suma1<suma2

print(f'Para {ale[-1]}, tuvo mas usuarios en los ultimos 3 anos? {bul2}')
