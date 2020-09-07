print("hello world")
# Soy un comentario

'''
un texto que no 
se va a mostrar
'''
texto = 'Repaso de Python con victor'
nombre = 'Victor Robles'
altura = 1.68
year = 2020

print(texto)
'''
# Condiciones 
altura = int(input("¿Cuál es tu añtura altura?"))



if altura >= 180:
    print('Eres una persona alta!!')
elif altura <180 and altura >=150:
    print("Eres una persona baja")
else:
    print('Eres un enanito')
'''

# Funciones

var_altura = int(input("¿Cuál es tu altura?"))

def mostrarAltura(altura):
    if var_altura >= 180:
        resultado = 'Eres una persona alta!!'
    elif var_altura <180 and var_altura >=150:
        resultado = "Eres una persona baja"
    else:
        resultado = 'Eres un enanito'
    return resultado

print(mostrarAltura(var_altura))

# Listas

personas = ['enrique', 'lala']
print(personas[0])

import math 
print(math.pi)