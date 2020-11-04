from io import open
import sys

fichero = open("contador.txt", "a+") # lo abrimos en modo apertura y para editar
fichero.seek(0) # volvemos a poner el puntero en el inicio
contenido = fichero.readline()

if len(contenido) == 0:
	contenido = "0"
	fichero.write(contenido)

fichero.close()

# Vamos a intentar transformar el texto a un número
# Puede dar error así que agregamos un try
try:
	contador = int(contenido)

	# En función de lo que el usuario quiera...
	if len(sys.argv) == 2:
		if sys.argv[1] == "inc":
			contador += 1
		elif sys.argv[1] == "dec":
			contador -= 1

	print(contador)

	# Finalmente volvemos a escribir los cambios en el fichero
	fichero = open("contador.txt", "w")
	fichero.write(str(contador))
	fichero.close()

except:
	print("Error: Fichero corrupto.")