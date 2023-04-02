# No se porque primero lo fui pensando para cambiar solo las letras considerandolas todas 
# minúsculas, tal vez por los ejercicios que estuve haciendo que iban por ese lado.
# Dejé todo lo que fui probando proque me pareció interesante y útil como aprendizaje 
# pero la versión que realmente responde a lo pedido (usar lambda y realizar un corrimiento 
# de caracter al siguiente de la lista ascii ) está al final de todo

import string

print (string.ascii_letters)
# dos formas de quedarme solo con minúsculas
#       me quedo con la mitad de ascii_letters
solo_minusculas1 = string.ascii_letters[:int(len(string.ascii_letters)/2)]
print(solo_minusculas1)
solo_minusculas2 = ''.join(set(string.ascii_letters.lower())) 
#  ORDEN RANDOM :D no sirve para esto, pero bueno recordar que no hay orden en un conjunto
print(solo_minusculas2)
# o investigo un poco más y uso cosas disponibles en python
print(string.ascii_lowercase)

#cadena= 'abC cde Zotaz'
cadena = input ('ingrese una cadena de carácteres: ')

abc = string.ascii_lowercase
bcd = abc[1:] + abc[0]#[0:1]

cadena_traducida = ''.join([bcd[string.ascii_lowercase.index(letra)] if letra in string.ascii_lowercase  else letra for letra in cadena.lower()])
print(cadena_traducida)

print('---------------------------------------------')

#print(bcd)
mytable = str.maketrans(abc, bcd)
print(cadena.lower().translate(mytable))

print('------+++++---------EJERCICIO---------+++++------')

# este resuelve lo pedido... CASI
# si se ingresa el último símbolo ASCII '~'... pone una "casita" (pensé q se iba a romper), o sea... sigue con otros por fuera de ASCII?
#con chr() y ord()

corrimiento = 1
#corrimiento = int(input('ingrese valor para el corrimiento: '))
cadena_codificada = ''.join(map(lambda letra: chr(ord(letra)+corrimiento), cadena))
print(cadena_codificada)