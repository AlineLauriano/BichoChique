import tkinter as tk
from tkinter import messagebox
import os

def fazer_login():
    messagebox.showinfo("Login", "Login realizado com sucesso!")
    # Chamar a próxima tela (Menu.py)
    os.system('python Menu.py')

# Configurações da janela de login
login = tk.Tk()
login.title("Tela de Login")

# Configurar tamanho da janela
width = 400
height = 300
login.geometry(f"{width}x{height}")

login.configure(bg='#1D9BF0')

# Frame para centralizar os itens
frame = tk.Frame(login, bg='#1D9BF0')
frame.pack(expand=True)

# Labels e campos de entrada de email e senha
lbl_email = tk.Label(frame, text="Email:", bg="#1D9BF0", fg="#fff", font=("Helvetica 15 bold"))
lbl_email.pack()

ent_email = tk.Entry(frame)
ent_email.pack()

lbl_senha = tk.Label(frame, text="Senha:", bg="#1D9BF0", fg="#fff", font=("Helvetica 15 bold"))
lbl_senha.pack()

ent_senha = tk.Entry(frame, show="*")
ent_senha.pack()

# Botão de login
btn_login = tk.Button(frame, text="Login", command=fazer_login)
btn_login.pack(pady=10)  # Adicionar um espaçamento vertical entre o botão e os itens acima

# Iniciar loop de eventos
login.mainloop()