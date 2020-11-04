from io import open
import pickle

fichero = open('personas.txt', 'r', encoding="utf8") # utf8 nos sirve para aceptar acentos etc.
lineas = fichero.readlines()
fichero.close()

personas = []

for linea in lineas:
	# para borrar barra n
	campos = linea.replace("\n", "").split(";")
	persona = { "id" : campos[0], "nombre": campos[1], "apellido":campos[2],"nacimiento":campos[3]}
	personas.append(persona)

for p in personas:
	print("(id={}) {} {} => {}".format(p['id'],p['nombre'],p['apellido'],p['nacimiento']))