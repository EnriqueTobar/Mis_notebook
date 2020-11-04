from tkinter import*
# Configuración de la raíz
root = Tk()

label = Label(root, text="Nombre asdasdasd")
label.grid(row=0, column=0, sticky="W", padx=5, pady=5)

entry = Entry(root)
entry.grid(row=0, column=1, padx=5, pady=5)
entry.config(justify="right", state="normal")

label2 = Label(root, text="Constraseña")
label2.grid(row=1, column=0, sticky="W", padx=5, pady=5)

entry2 = Entry(root)
entry2.grid(row=1, column=1, padx=5, pady=5)
entry2.config(justify="center", show="*")



# Finalmente bucle de la aplicación
root.mainloop()