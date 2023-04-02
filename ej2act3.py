#3. Dado el siguiente texto guardado en la varible *jupyter_info*,  solicite por teclado **una letra** e
# #imprima las palabras que comienzan con dicha letra. En caso que no se haya inrgesado un letra, indique 
# el error. *Ver: módulo string*
jupyter_info = """ JupyterLab is a web-based interactive development environment for Jupyter notebooks, 
code, and data. JupyterLab is flexible: configure and arrange the user interface to support a wide range 
of workflows in data science, scientific computing, and machine learning. JupyterLab is extensible and
modular: write plugins that add new components and integrate with existing ones.
"""


import string
jupyter_info_words =  ''.join([letter if letter in string.ascii_letters else " " for letter in jupyter_info ])
jupyter_info_words = set(jupyter_info_words.lower().split(" "))
#filtered_words = [word for word in jupyter_info_words if word.startswith(letter)]

letter = input ('ingrese una letra: ')
if letter in string.ascii_letters:
    print ([word for word in jupyter_info_words if word.startswith(letter)])
else:
    print ('No ha ingresado un caracter válido')
    

    
    
    
    