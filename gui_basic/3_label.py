from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("480x360+1050+400") 
# //////////////////////////////////////////

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="C://nado_python//nodo_python-1//gui_basic//irene_20x20.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="또만나요")

btn = Button(root, text="클릭", command=change)
btn.pack()


root.mainloop()
