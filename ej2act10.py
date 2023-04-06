# 10. Dada una lista de nombres de estudiantes y dos listas con sus notas en un curso, escriba un
# programa que manipule dichas estructuras de datos para poder resolver los siguientes puntos:
#    1. Generar una estructura con todas las notas relacionando el nombre del estudiante con las
#       notas. Utilizar esta estructura para la resolución de los siguientes items.
#    2. Calcular el promedio de notas de cada estudiante.
#    3. Calcular el promedio general del curso.
#    4. Identificar al estudiante con la nota promedio más alta.
#    5. Identificar al estudiante con la nota más baja.


# **Nota**:
# - Las 3 estructuras están ordenadas de forma que los elementos en la misma posición corresponden a un mismo alumno.
# - Realizar funciones con cada item


nombres = """ 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín'  , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 
'Nicolás',  'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' """
notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44, 85, 73, 37, 42, 95, 18,
7, 74, 60, 9, 65, 93, 63, 74]
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
64, 13,  8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73, 95, 19, 47,
15, 31, 39, 15, 74, 33, 57, 10]

# inciso1
def generador_diccio(nombres, notas_1, notas_2):
    """ Esta funcion crea un diccionario con cada nombre como clave y sus correspondientes 
    notas dentro de una tupla """
    lista_nombres = "".join([" " if letter in "'," else letter for letter in nombres])
    lista_nombres = lista_nombres.strip()
    lista_nombres = lista_nombres.split()
    
    return {
        alumno: [nota_1, nota_2] #primero hice que las notas fueran una tupla, pero luego 
                                # me decanté por lista, por si se agregan más notas o cambian
        for alumno, nota_1, nota_2 in zip(lista_nombres, notas_1, notas_2)
    }


# inciso2
# def calcular_prom_alumno(nota_1, nota_2): decidí usar args para que se puedan agregar más notas a futuro
def calcular_prom_alumno(*args):
    """ Esta funcion calcula el promedio de los N argumentos que recibe """
    return round(sum(args) / len(args), 2)


def calcular_promedios_alumnos(registro_alumnos):
    """ Esta funcion recibe el diccionario de alumnos y sus notas y calcula el promedio 
    de las notas de cada alumno y retorna un diccionario con cada alumno y su promedio """
    return {
        alumno: (
            calcular_prom_alumno(
                registro_alumnos[alumno][0], registro_alumnos[alumno][1]
            )
        )
        for alumno in registro_alumnos
    }


# inciso3
def calcular_promedio_total(promedios):
    """ Esta función calcula el promedio total de los valores de un diccionario que se pasa 
    como parámetro """
    return round(sum(promedios.values()) / len(promedios), 2)


# inciso4 
# ver tema nombre parametro
# def identificar_alum_max_nota (alumnos_ y_notas):
#     return max(alumnos_y_notas)
def identificar_alum_max_nota(promedios):
    """ Esta función recibe como parámetro el diccionario con los promedios de los alumnos y 
    retorna la clave del alumno con el mayor promedio  """
    return (max(promedios, key = promedios.get))

#alternativa mala
    # valor_max = max(promedios.values())
    # indice = list(promedios.values()).index(valor_max)
    # return list(promedios.keys())[indice]
    #  comprimido: list(promedios.keys())[list(promedios.values()).index(max(promedios.values()))]


# inciso5
def identificar_alum_min_nota(registro_alumnos):  # analizar con map
    """ Esta función recibe como parámetro el diccionario con loas alumnos y sus notas y
    retorna la clave del alumno con la menor nota  """
    # minimos =[]
    # for alumno in registro_alumnos:
    #     minimos.append(min(registro_alumnos[alumno]))
    #return (min(registro_alumnos, key = registro_alumnos.get))  
      
    minimos = [min(registro_alumnos[alumno]) for alumno in registro_alumnos]
    valor_min = min(minimos)
    
    #valor_min = min(nota for notas in registro_alumnos.values() for nota in notas)
    #valor_min = min(map(min, [zip(*registro_alumnos.values())]))
   
    #valor_min = min(map(lambda alumno: min(alumno), registro_alumnos.values()))    
    
    indice = minimos.index(valor_min) 
    minima =list(registro_alumnos.keys())[indice] 
    # minima = list(registro_alumnos.keys())[minimos.index(min(minimos))] #comprimido de las 2 líneas de arriba
    

    return minima
 






# ---------------------------------------------------------------------------------------------------------------
# inciso1
registro_alumnos = generador_diccio(nombres, notas_1, notas_2)
print(f'Listado de alumnos y sus notas: {registro_alumnos}')
print("")
print(
    "___________________________________________________________________________________________________________"
)
# inciso2 - Calcular el promedio de notas de cada estudiante.
promedios = calcular_promedios_alumnos(registro_alumnos)
print(promedios)

print(
    "___________________________________________________________________________________________________________"
)
print("")
# inciso3 - Calcular el promedio general del curso.
promedio_total = calcular_promedio_total(promedios)
print("El promedio total de la clase es: ", promedio_total)


# inciso4 - Identificar al estudiante con la nota promedio más alta.
alumno_max = identificar_alum_max_nota(promedios)
print("El alumno con mayor promedio es: ", alumno_max)

# inciso5 - Identificar al estudiante con la nota más baja.
alumno_min = identificar_alum_min_nota(registro_alumnos)
print("El alumno con menor nota es: ", alumno_min)
