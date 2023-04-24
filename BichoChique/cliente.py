from tkinter import *
import subprocess

cliente = Tk()

# Configurações da tela
cliente.title("Bicho Chique")
cliente.resizable(False, False)

width = 1240
height = 700

cliente.maxsize(width, height)
cliente.minsize(width, height)

cliente.configure(bg='#FFC93E')

# Função para voltar ao menu
def abrir_tela_menu():
    subprocess.run(["python", "Menu.py"])

# Botão voltar ao menu
btn_menu = Button(cliente, text="Voltar ao menu", bd=0, bg="#1D9BF0", fg="#fff", font="Helvetica 10 underline", activebackground="#FFF", activeforeground="#1D9BF0", command=abrir_tela_menu)
btn_menu.place(relx=.830, rely=.10, anchor="n")

# Título dos serviços
txt_titulo = Label(cliente, text="Cadastro do Cliente", bg="#FFC93E", font=("Helvetica 20 bold"))
txt_titulo.place(relx=.450, rely=.20, anchor="n")

# Campo código do serviço
txt_codigo = Label(cliente, text="Código do Cliente", bg="#FFC93E", font=("Helvetica 10"))
txt_codigo.place(relx=.350, rely=.30, anchor="n")
lbl_codigo = Entry(cliente)
lbl_codigo.place(relx=.360, rely=.33, anchor="n", width="130", height="20")

# Campo nome
txt_nome = Label(cliente, text="Nome", bg="#FFC93E", font=("Helvetica 10"))
txt_nome.place(relx=.500, rely=.30, anchor="n")
lbl_nome = Entry(cliente)
lbl_nome.place(relx=.560, rely=.33, anchor="n", width="190", height="20")

# Campo CPF
txt_valor = Label(cliente, text="CPF", bg="#FFC93E", font=("Helvetica 10"))
txt_valor.place(relx=.317, rely=.40, anchor="n")
lbl_valor = Entry(cliente)
lbl_valor.place(relx=.342, rely=.43, anchor="n", width="90", height="20")

# Campo data de nascimento
txt_duracao = Label(cliente, text="Data de nascimento", bg="#FFC93E", font=("Helvetica 10"))
txt_duracao.place(relx=.470, rely=.40, anchor="n")
lbl_duracao = Entry(cliente)
lbl_duracao.place(relx=.470, rely=.43, anchor="n", width="120", height="20")

# Campo Idade
txt_duracao = Label(cliente, text="Idade", bg="#FFC93E", font=("Helvetica 10"))
txt_duracao.place(relx=.560, rely=.40, anchor="n")
lbl_duracao = Entry(cliente)
lbl_duracao.place(relx=.580, rely=.43, anchor="n", width="80", height="20")

# Celular
txt_descricao = Label(cliente,text="Celular" ,bg = "#FFC93E", font=("Helvetica 10"))
txt_descricao.place(relx = .325, rely = .49, anchor = "n")
lbl_descricao = Entry(cliente)
lbl_descricao.place(relx = .355, rely = .52, anchor = "n" ,  width="120" , height="20")

# Campo cep
txt_valor = Label(cliente,text="Cep" ,bg = "#FFC93E", font=("Helvetica 10"))
txt_valor.place(relx = .317, rely = .56, anchor = "n")
lbl_valor = Entry(cliente)
lbl_valor.place(relx = .342, rely = .59, anchor = "n",  width="90" , height="20")

# Campo endereço
txt_nome = Label(cliente,text="Endereço" ,bg = "#FFC93E", font=("Helvetica 10"))
txt_nome.place(relx = .449, rely = .56, anchor = "n")
lbl_nome = Entry(cliente)
lbl_nome.place(relx = .500, rely = .59, anchor = "n" ,  width="190" , height="20")

# Campo número
txt_valor = Label(cliente,text="N°" ,bg = "#FFC93E", font=("Helvetica 10"))
txt_valor.place(relx = .593, rely = .56, anchor = "n")
lbl_valor = Entry(cliente)
lbl_valor.place(relx = .600, rely = .59, anchor = "n",  width="30" , height="20")

# Campo bairro
txt_valor = Label(cliente,text="Bairro" ,bg = "#FFC93E", font=("Helvetica 10"))
txt_valor.place(relx = .320, rely = .63, anchor = "n")
lbl_valor = Entry(cliente)
lbl_valor.place(relx = .365, rely = .66, anchor = "n",  width="150" , height="20")

# Campo cidade
txt_nome = Label(cliente,text="Cidade" ,bg = "#FFC93E", font=("Helvetica 10"))
txt_nome.place(relx = .467, rely = .63, anchor = "n")
lbl_nome = Entry(cliente)
lbl_nome.place(relx = .500, rely = .66, anchor = "n" ,  width="120" , height="20")

# Campo UF
txt_nome = Label(cliente,text="UF" ,bg = "#FFC93E", font=("Helvetica 10"))
txt_nome.place(relx = .574, rely = .63, anchor = "n")
lbl_nome = Entry(cliente)
lbl_nome.place(relx = .580, rely = .66, anchor = "n" ,  width="30" , height="20")

# Botões de salvar, alterar e excluir
btn_salvar = Button(cliente, text="Salvar", bg="#1D9BF0")
btn_salvar.place(relx=.330, rely=.75, anchor="n", width="80", height="25")

btn_alterar = Button(cliente, text="Alterar", bg="#1D9BF0")
btn_alterar.place(relx=.480, rely=.75, anchor="n", width="80", height="25")

btn_excluir = Button(cliente, text="Excluir", bg="#1D9BF0")
btn_excluir.place(relx=.630, rely=.75, anchor="n", width="80", height="25")

cliente.mainloop()