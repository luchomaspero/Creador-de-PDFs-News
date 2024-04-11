import os
import openpyxl



def extraerCUILs():
	# Abre el archivo Excel
	archivo_excel = "C:/Users/luciomaspero/Desktop/Trabajos/Scripts/Archivos pdf Fabi/Nomina Empleados.xlsx"
	libro = openpyxl.load_workbook(archivo_excel)

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
