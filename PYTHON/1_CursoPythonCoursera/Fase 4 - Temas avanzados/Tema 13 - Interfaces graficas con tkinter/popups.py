from tkinter import*
from tkinter import messagebox as Messagebox
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog

# Configuración de la raíz
root = Tk()

def test():
	#Messagebox.showinfo("Hola","Hola Mundo")
	#Messagebox.showwarning("Alerta","Sección sólo para administradores")
	#Messagebox.showerror("Error","Ha ocurrido un error inesperado.")
	#resultado = Messagebox.askquestion("Salir","¿Estás seguro que quieres salir sin guardar?")
	#if resultado == "yes":
	#	root.destroy()
	#resultado = Messagebox.askokcancel("Salir","¿Estás seguro que sobreescribir salir sin guardar?")
	#if resultado:
	#	root.destroy()

	#resultado = Messagebox.askyesno("Salir","¿Estás seguro que quieres salir sin guardar?")
	#if resultado:
	#	root.destroy()

	#Messagebox.askretrycancel("Reintentar", "No se puede conectar")
	#if resultado:
	#	root.destroy()
	
	#color=ColorChooser.askcolor(title="Elige un color")
	#print(color)

	ruta = FileDialog.askopenfilename(title="Abrir un fichero", initialdir="C:") # devulve la ruta
	print(ruta)




Button(root, text="Clícame", command=test).pack()

#abajo de todo
root.mainloop()