#Escriba un programa que solicite por teclado una palabra y calcule el valor de la misma dada la siguiente tabla de valores del juego Scrabble:


# |Letra                       |valor|
# |-----                       |-----|
# |A, E, I, O, U, L, N, R, S, T|1|
# |D, G                        |2|
# |B, C, M, P                  |3|
# |F, H, V, W, Y               |4|
# |K                           |5|
# |J, X                        |8|
# |Q, Z                        |10|



word = input("Ingresá una palabra: ").upper()
puntajes = {('A','E','I','O','U','L','N','R','S','T'):1,
            ('D','G'):2,
            ('B','C','M','P'):3,
            ('F','H','V','W','Y'):4,
            ('K'):5,
            ('J','X'):8,
            ('Q','Z'):10}

#print(puntajes)

suma=0

#print(puntajes[('K')])
for letter in word:
    #found= False
    for clave in puntajes:
        if letter in clave:
            suma+= puntajes[clave]
            break
print (suma)

#solución sin break?