from tkinter import*

def seleccionar():
	cadena = ""
	if(leche.get()):
		cadena += "Con leche"
	else:
		cadena += "Sin leche"

	if(azucar.get()):
		cadena += " y con azúcar"
	else:
		cadena += " y sin azúcar"

	monitor.config(text=cadena)


# Configuración de la raíz
root = Tk()
root.title("Cafetería")
root.config(bd=15)

leche = IntVar()
azucar = IntVar()

imagen = PhotoImage(file="imagen.gif")
Label(root, image=imagen).pack(side="left")

frame = Frame(root)
frame.pack(side="right")

Label(root, text="¿Cómo quieres el café").pack(anchor="w")
Checkbutton(root, text="Con leche", variable=leche, onvalue=1, offvalue=0, command=seleccionar).pack()
Checkbutton(root, text="Con Azúcar", variable=azucar, onvalue=1, offvalue=0, command=seleccionar).pack()

monitor = Label(frame)
monitor.pack()

#abajo de todo
root.mainloop()