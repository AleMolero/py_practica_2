import string
def codificador_cadena(cadena):
    return ''.join(map(lambda letra: chr(ord(letra) + 1), cadena))
   