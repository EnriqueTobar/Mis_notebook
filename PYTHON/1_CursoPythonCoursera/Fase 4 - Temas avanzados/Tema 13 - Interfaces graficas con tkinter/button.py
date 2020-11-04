from tkinter import*

def sumar():
	r.set( float(n1.get()) + float(n2.get()) )


# Configuración de la raíz
root = Tk()
root.config(bd=15)

n1 = StringVar()
n2 = StringVar()
r = StringVar()

Label(root, text="Número 1").pack()
Entry(root, justify="center", textvariable=n1).pack() # primer número
Label(root, text="Número 2").pack()
Entry(root, justify="center", textvariable=n2).pack() # segundo número
Label(root, text="\nResultado").pack()
Entry(root, justify="center", textvariable=r).pack() # resultado

Button(root, text="Sumar", command=sumar).pack()

# Finalmente bucle de la aplicación
root.mainloop()