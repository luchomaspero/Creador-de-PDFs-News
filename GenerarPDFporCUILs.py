import sys
import shutil
import os
from extraer_CUILs import extraerCUILs


# #################################################### #
############## PASOS PARA USO DE SCRIPT#################
# 1. descargar nomina empleados y nombrarla como "Nomina Empleados.xlsx"
# 2. Cambiar los valores de:
#     "nombrePDF": Nombre del PDF unico a multiplicar
#     "nombreCarpetaNueva": Nombre de la carpeta de destino de los Cuils.pdf
#

nombrePDF = sys.argv[1]
nombreCarpetaNueva = sys.argv[2]
########################################################
########################################################
########################################################
# #################################################### #

# Ruta del archivo PDF original
archivo_original = "C:/Users/luciomaspero/Desktop/Trabajos/Scripts/Archivos pdf Fabi/" + nombrePDF + ".pdf"


# Ruta de la carpeta donde guardar las copias
carpeta_destino = "G:/Unidades compartidas/SEGURIDAD E HIGIENE/Politicas de calidad 0823/" + nombreCarpetaNueva + "/"

if not os.path.exists(carpeta_destino):
    # Crear la carpeta de destino si no existe
    os.makedirs(carpeta_destino)

# Lista con los 500 nombres distintos para las copias (asegúrate de tener 500 nombres)
array_CUILs = extraerCUILs()
nombres_copias = array_CUILs


for i in range(len(nombres_copias)):
    nombres_copias[i] = nombres_copias[i] + ".pdf"

# Realizar las copias con los nombres diferentes
for nombre_copia in nombres_copias:
    shutil.copy(archivo_original, carpeta_destino + nombre_copia)


####### shutil.move(archivo_original, carpeta_destino)

print("Proceso completado. Se han creado las " + str(len(nombres_copias)) + " copias con nombres distintos.")