import sys

sys.path.insert(1, '..') # dos puntos hace referencia al directorio anterior
						 # un punto hace referencia al mismo
#print(sys.path)
from saludos import Saludo

Saludo()
