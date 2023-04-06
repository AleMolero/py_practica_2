from codificador import codificador_cadena as codificador 

cadena = input ("Ingrese una cadena de caracteres o '-1' para salir: ")
while (cadena != '-1'):    
    cadena_codificada = codificador(cadena)
    print(f'la cadena de caracteres "{cadena}" ha sido codificada como "{cadena_codificada}".')
    cadena = input ("Ingrese una cadena de caracteres o '-1' para salir: ")
