from tkinter import *

window = Tk()

photo = PhotoImage(file="conhecimento.png")

label = Label(window,
              text="Programe ou seja Programado",
              font=("Arial", 40, "bold"),
              fg="#00FF00",
              bg="#000000",
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound="bottom")
label.pack()
#label.place(x=0, y=2)

window.mainloop()