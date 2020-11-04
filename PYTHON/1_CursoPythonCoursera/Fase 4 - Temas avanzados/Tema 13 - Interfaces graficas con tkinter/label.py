from tkinter import*
# Configuración de la raíz
root = Tk()

#root.title("label")

# Configuración de un marco
#frame = Frame(root, width=480, height=320)
#frame.pack()
"""
# Variables dinámicas
texto = StringVar()
texto.set("Un nuevo texto")

Label(root, text="Hola Mundo!").pack(anchor='nw')
label = Label(root, text="Hola Mundo!")
label.pack(anchor="center")
Label(root, text="Hola Mundo!").pack(anchor='se')


label.config(bg="green", fg="blue",font=('Verdana', 24))
label.config(textvariable=texto)
"""

imagen = PhotoImage(file="imagen.gif")
Label(root, image=imagen, bd=0).pack(side="left")

# Finalmente bucle de la aplicación
root.mainloop()