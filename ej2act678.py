
#6) Si ahora queremos saber si contiene la letra a y 
#también la letra n, cómo lo modificamos?

#palabra = input("Ingresá una palabra: ")
print('')
print('6)')
palabra = "Ingresá una palabra: "
if ("a" or "á") and "n" in palabra:
    print("Hay letras a y n.")
else:
    print("No hay letras a o no hay letras n. ")
    
#7) Dada una frase identificar mayúsculas, minúsculas y caracteres no
# letras y contar la cantidad de palabras sin distinguir entre 
# mayúsculas y minúsculas, en la frase
print('')
print('7)')
text = """
El salario promedio de un hombre en Argentina es de $60.000, mientras que
el de una mujer es de $45.000. Además, las mujeres tienen menos
posibilidades de acceder a puestos de liderazgo en las empresas.
"""
import string
from collections import Counter
all_words= text
all_words = ''.join([letter if letter in string.ascii_letters else " " for letter in all_words ])
all_words = all_words.lower().split(" ")
cnt = Counter()

for word in all_words:
    cnt[word] += 1

print(cnt)

#8  Escriba un programa que solicite que se ingrese una palabra o frase y permita identificar si la misma 
# es un [Heterograma] 
# Un Heterograma es una palabra o frase que no tiene ninguna letra repetida entre sus caracteres.

#**Tener en cuenta**
#- Lo que no se puede repetir en la frase son sólo aquellos caracteres que sean letras.
#- No se distingue entre mayúsculas y minúsculas, es decir si en la frase o palabra tenemos la letra "T" 
# y la letra "t" la misma NO será un Hererograma.
#- Para simplificar el ejercicio vamos a tomar como que las letras con tilde y sin tilde son distintas.

#cadena = input("ingresa una cadena de carácteres: ")
print('')
print('8)')
cadena = "Soy Real 100%"

cadena = ''.join([letter if letter in string.ascii_letters else "" for letter in cadena])

conj_cadena = set(cadena)

print ("ES un Heterograma" if len(conj_cadena) == len(cadena) else "NO es")
