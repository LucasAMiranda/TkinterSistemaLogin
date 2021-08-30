from tkinter import *

count = 0
def click():
   global count
   count+=1
   print(count)

window = Tk()

photo = PhotoImage(file="logo.png")

button = Button(window,
                text="Clique em mim",
                command=click,
                font=("Comic Sans", 30),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="pink",
                state=ACTIVE,
                image=photo,
                compound="bottom")

button.pack()

window.mainloop()