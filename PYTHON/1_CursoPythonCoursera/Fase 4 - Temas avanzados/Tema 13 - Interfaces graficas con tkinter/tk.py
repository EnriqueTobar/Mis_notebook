from tkinter import*

root = Tk()

# Título de la Ventana
root.title("Hola Mundo")
root.resizable(1,1) # para evitar que se modifique la ventana
root.iconbitmap('hola.ico')

frame = Frame(root, width=480, height=320)
frame.pack(fill='both', expand=1)
frame.config(cursor="pirate")
frame.config(bg="lightblue")
frame.config(bd=25)
frame.config(relief="sunken")

root.config(cursor="arrow")
root.config(bg="blue")
root.config(bd=15)
root.config(relief="ridge")




#abajo de todo
root.mainloop()