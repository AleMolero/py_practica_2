
# 5. Dada una frase y un string ingresados por teclado (en ese orden),
# genere una lista de palabras, y sobre ella, informe la cantidad de palabras 
# en las que se encuentra el string. No distingir entre mayúsculas y minúsculas.

oration = input('ingrese oracion: ').lower()
letras = input ('Ingrese cadena de caracteres: ').lower()

word_list = oration.split()
#print(word_list)
print('la cantidad de palabras que incluyen la cadena ingresada es: ', len([ word for word in word_list if letras in word]))