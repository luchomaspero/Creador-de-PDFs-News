import os
import openpyxl

carpeta_de_proyecto = os.path.dirname(os.path.abspath(__file__))
archivos_en_carpeta = os.listdir(carpeta_de_proyecto)

def buscar_archivo_en_carpeta(archivo_buscado):
    carpeta_de_proyecto = os.path.dirname(os.path.abspath(__file__))
    archivos_en_carpeta = os.listdir(carpeta_de_proyecto)
    
    for archivo in archivos_en_carpeta:
        if archivo.startswith(archivo_buscado):
            archivo_buscado = archivo
            break

    if archivo_buscado:
        # Construir la ruta completa del archivo
        ruta_completa_archivo_buscado = os.path.join(carpeta_de_proyecto, archivo_buscado)
        # Aquí puedes continuar con el procesamiento de df_COMPLEGA
    else:
        print("No se encontraron archivos que comiencen con {archivo_buscado}.")
    
    return ruta_completa_archivo_buscado



# # Buscar el primer archivo que comience con "COMPLEGA"
# archivo_nomina = None
# for archivo in archivos_en_carpeta:
#     if archivo.startswith("Nomina"):
#         archivo_nomina = archivo
#         break

# if archivo_nomina:
#     # Construir la ruta completa del archivo
#     ruta_completa_nomina = os.path.join(carpeta_de_proyecto, archivo_nomina)
#     # Aquí puedes continuar con el procesamiento de df_COMPLEGA
# else:
#     print("No se encontraron archivos que comiencen con 'Nomina'.")



def extraerCUILs():
    # Abre el archivo Excel
    carpeta_de_proyecto = os.path.dirname(os.path.abspath(__file__))
    nomina = os.path.join(carpeta_de_proyecto,"Nomina Empleados.xlsx")
    
    #archivo_excel = "C:/Users/luciomaspero/Desktop/Trabajos/Scripts/Archivos pdf Fabi/Nomina Empleados.xlsx"
    libro = openpyxl.load_workbook(nomina)
    
    # Selecciona la hoja en la que deseas trabajar
    hoja = libro.active  # Puedes cambiarlo si tienes un nombre específico para la hoja
    
    # Obtén las columnas D y J
    columna_d = hoja['D']
    columna_j = hoja['J']
    
	# Inicializa una lista para almacenar los datos filtrados
    array_CUILs = []

    	# Recorre las celdas de las columnas D y J simultáneamente
    for celda_d, celda_j in zip(columna_d, columna_j):
        if celda_j.value is None:  # Si la celda en columna J está vacía
            array_CUILs.append("{}".format(str(celda_d.value)))

    	# Cierra el archivo Excel
    libro.close()
    array_CUILs = array_CUILs[1:]
    return array_CUILs

