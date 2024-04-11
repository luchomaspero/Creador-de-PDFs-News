@echo off
echo RECORDAR ACTUALIZAR EL ARCHIVO DE NOMINA EMPLEADOS. MANTENER EL NOMBRE! "Nomina Empleados.xlsx"
set /p "nombrePDF=Introduce el nombre del PDF: "
set /p "nombreCarpetaNueva=Introduce el nombre de la carpeta nueva donde caeran los PDFs: "

echo Ejecutando el script de Python con los valores ingresados...
py GenerarPDFporCUILs.py "%nombrePDF%" "%nombreCarpetaNueva%"
pause

