from tkinter import *
import subprocess

tela = Tk()

# Funções para abrir telas
def abrir_tela_animais():
    subprocess.run(["python", "animal.py"])

def abrir_tela_clientes():
    subprocess.run(["python", "cliente.py"])

def abrir_tela_servicos():
    subprocess.run(["python", "servico.py"])

def abrir_tela_op():
    subprocess.run(["python", "operação-concluida.py"])

def logout():
    # Fechar a janela atual
    tela.destroy()

# Configurações da tela
tela.title("Bicho Chique")
tela.resizable(False, False)
width = 1000
height = 700
tela.maxsize(width, height)
tela.minsize(width, height)
tela.configure(bg='#1D9BF0')

# Barra de menu
barra_menu = Menu(tela)

opcoes_menu_arquivo = Menu(barra_menu)
opcoes_menu_gestao = Menu(barra_menu)

barra_menu.add_cascade(label="Arquivo", menu=opcoes_menu_arquivo)
barra_menu.add_cascade(label="Gestão", menu=opcoes_menu_gestao)

opcoes_menu_arquivo.add_command(label="Abrir")
opcoes_menu_arquivo.add_command(label="Salvar")
opcoes_menu_arquivo.add_command(label="Salvar como ...")
opcoes_menu_arquivo.add_separator()
opcoes_menu_arquivo.add_command(label="Sair", command=tela.quit)

opcoes_novo = Menu(opcoes_menu_arquivo)

opcoes_menu_arquivo.add_cascade(label="Novo", menu=opcoes_novo)
opcoes_menu_arquivo.add_command(label="Abrir")

opcoes_novo.add_command(label="Salvar Imagem")
opcoes_novo.add_command(label="Upload Arquivos")

tela.config(menu=barra_menu)

# Botões
foto_sair = PhotoImage(file=r"images/sair.png")
foto_animais = PhotoImage(file=r"images/animal.png")
foto_usuario = PhotoImage(file=r"images/usuario.png")
foto_serviços = PhotoImage(file=r"images/servico.png")
foto_logout = PhotoImage(file=r"images/sair.png")

# Calcula as coordenadas relativas para posicionar os botões lado a lado, com espaço entre eles
btn_animais = Button(tela, text="Animais", image=foto_animais, compound=TOP, command=abrir_tela_animais)
btn_animais.place(relx=.2, rely=.5, anchor=CENTER, width="150", height="150")

btn_clientes = Button(tela, text="Clientes", image=foto_usuario, compound=TOP, command=abrir_tela_clientes)
btn_clientes.place(relx=.4, rely=.5, anchor=CENTER, width="150", height="150")

btn_servicos = Button(tela, text="Serviços", image=foto_serviços, compound=TOP, command=abrir_tela_servicos)
btn_servicos.place(relx=.6, rely=.5, anchor=CENTER, width="150", height="150")

btn_logout = Button(tela, text="Logout", image=foto_logout, compound=TOP, command=logout)
btn_logout.place(relx=.8, rely=.5, anchor=CENTER, width="150", height="150")

tela.mainloop()
