from tkinter import *
from tkinter import PhotoImage
from functools import partial

window = Tk()
window.geometry("320x110")
window.title("Lschool Info Tech")

icon = PhotoImage(file="logo.png")
window.iconphoto(True, icon)
window.config(background="#0fcdd0")


def validateLogin(nome, senha):
    print("Informe seu nome:", nome.get())
    print("Informe sua senha:", senha.get())
    return


nomeLabel = Label(window, text="Nome").grid(row=1, column=1)
nome = StringVar()
nomeEntry = Entry(window, textvariable=nome).grid(row=1, column=2)

senhaLabel = Label(window, text="Senha").grid(row=2, column=1)
senha = StringVar()
passwordEntry = Entry(window, textvariable=senha, show='*').grid(row=2, column=2)

validacao = partial(validateLogin, nome, senha)

loginButton = Button(window, text="Login", command=validateLogin).grid(row=4, column=2)

window.mainloop()
