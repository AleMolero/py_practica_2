# 4. Para la aceptación de un artículo en un congreso se definen las siguientes especificaciones que deben cumplir y recomendaciones de escritura:
# * **título**: 10 palabras como máximo
# * cada oración del **resumen**:
#     * hasta 12 palabras: fácil de leer
#     * entre 13-17 palabras:  aceptable para leer
#     * entre 18-25 palabras: difícil de leer
#     * mas de 25 palabras: muy difícil

# Dado un artículo en formato string, defina si cumple las especificaciones del título y cuántas oraciones tiene de cada categoría.

evaluar0=""" título: Experiences in Developing a Distributed Agent-based Modeling Toolkit with Python
resumen: Distributed agent-based modeling (ABM) on high-performance computing resources provides the promise of capturing unprecedented details of large-scale complex systems. However, the specialized knowledge required for developing such ABMs creates barriers to wider adoption and utilization. Here we present our experiences in developing an initial implementation of Repast4Py, a Python-based distributed ABM toolkit. We build on our experiences in developing ABM toolkits, including Repast for High Performance Computing (Repast HPC), to identify the key elements of a useful distributed ABM toolkit. We leverage the Numba, NumPy, and PyTorch packages and the Python C-API to create a scalable modeling system that can exploit the largest HPC resources and emerging computing architectures.
"""
evaluar = evaluar0

#evaluar = input('ingrese texto del artículo: ')

#separo en líneas
evaluar =evaluar.splitlines()
evaluar[0] =evaluar[0].strip('título: ')
#evaluar[0] =evaluar[0].split()
#print ( evaluar[0])

#evaluo titulo
if (len(evaluar[0].split())<=10):
    print('El titulo cumple con lo pedido ')
else:
    print('El titulo NO cumple con lo pedido ')
    
#separo en oraciones
evaluar[1] =evaluar[1].strip('resumen: ')
evaluar[1] =evaluar[1].split('.')
#print ( evaluar)

#armo estructura 
tipo_oracion = {}
# tipo_oracion[('fácil de leer', range(1,12))]= 0
# tipo_oracion[('aceptable para leer', range(13,17))]= 0
# tipo_oracion[('difícil de leer', range(18,25))]= 0
# tipo_oracion[('muy difícil', range(26,99999))]= 0

tipo_oracion['fácil de leer']= 0
tipo_oracion['aceptable para leer']= 0
tipo_oracion['difícil de leer']= 0
tipo_oracion['muy difícil']= 0

evaluar[1].remove("")
#como evito contar oraciones con largo =0?
#evaluo oraciones
for oration in evaluar[1]:
    long=len(oration.split())
    #print(long) 
    match long:
        case long if long in range(1,13):
            tipo_oracion['fácil de leer']+=1
            #print(1) 
        case long if long in range(13,18):
            tipo_oracion['aceptable para leer']+=1
            #print(2)
        case long if long in range(18,26):
            tipo_oracion['difícil de leer']+=1
            #print(3)
        case long if long >25:
            tipo_oracion['muy difícil']+=1
            #print(4)
#en el rango la cota superior no se incluye
print (tipo_oracion)
#hay que contar el título??

# longitudes = [len(oration.split()) for oration in evaluar[1]]
# tipo_oracion = {
#     'fácil de leer': longitudes.count(long) for long in range(1, 12)
# }
# tipo_oracion.update({
#     'aceptable para leer': longitudes.count(long) for long in range(13, 17)
# })
# tipo_oracion.update({
#     'difícil de leer': longitudes.count(long) for long in range(18, 25)
# })
# tipo_oracion.update({
#     'muy difícil': longitudes.count(long) for long in longitudes if long >= 25
# })