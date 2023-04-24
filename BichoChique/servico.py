from tkinter import *
import subprocess

# Configurações da tela
servico = Tk()
servico.title("Bicho Chique")
servico.resizable(False, False)

width = 1000
height = 700
servico.maxsize(width, height)
servico.minsize(width, height)
servico.configure(bg='#FFC93E')

# Função para voltar ao menu
def abrir_tela_menu():
    subprocess.run(["python", "Menu.py"])

# Botão para voltar ao menu
btn_menu = Button(servico, text="Voltar ao menu", bd=0, bg="#1D9BF0", fg="#fff", font="Helvetica 10 underline", 
                  activebackground="#fff", activeforeground="#1D9BF0", command=abrir_tela_menu)
btn_menu.place(relx=.830, rely=.10, anchor="n")

# Título dos serviços
txt_titulo = Label(servico, text="Cadastro dos Serviços", bg="#FFC93E", font=("Helvetica 20 bold"))
txt_titulo.place(relx=.450, rely=.20, anchor="n")

# Campo código do serviço
txt_codigo = Label(servico, text="Código do Serviço", bg="#FFC93E", font=("Helvetica 10"))
txt_codigo.place(relx=.350, rely=.30, anchor="n")
lbl_codigo = Entry(servico)
lbl_codigo.place(relx=.360, rely=.33, anchor="n", width="130", height="20")

# Campo nome
txt_nome = Label(servico, text="Nome", bg="#FFC93E", font=("Helvetica 10"))
txt_nome.place(relx=.500, rely=.30, anchor="n")
lbl_nome = Entry(servico)
lbl_nome.place(relx=.560, rely=.33, anchor="n", width="190", height="20")

# Campo valor
txt_valor = Label(servico, text="Valor", bg="#FFC93E", font=("Helvetica 10"))
txt_valor.place(relx=.320, rely=.40, anchor="n")
lbl_valor = Entry(servico)
lbl_valor.place(relx=.345, rely=.43, anchor="n", width="90", height="20")

# Campo tempo de duração
txt_duracao = Label(servico, text="Tempo de duração", bg="#FFC93E", font=("Helvetica 10"))
txt_duracao.place(relx=.525, rely=.40, anchor="n")
lbl_duracao = Entry(servico)
lbl_duracao.place(relx=.530, rely=.43, anchor="n", width="120", height="20")

# Descrição
txt_descricao = Label(servico, text="Descrição", bg="#FFC93E", font=("Helvetica 10"))
txt_descricao.place(relx=.335, rely=.50, anchor="n")
lbl_descricao = Entry(servico)
lbl_descricao.place(relx=.470, rely=.53, anchor="n", width="400", height="50")

# Botões de salvar, alterar e excluir
btn_salvar = Button(servico, text="Salvar", bg="#1D9BF0")
btn_salvar.place(relx=.330, rely=.75, anchor="n", width="80", height="25")
btn_alterar = Button(servico, text="Alterar", bg="#1D9BF0")
btn_alterar.place(relx=.480, rely=.75, anchor="n", width="80", height="25")
btn_excluir = Button(servico, text="Excluir", bg="#1D9BF0")
btn_excluir.place(relx=.630, rely=.75, anchor="n", width="80", height="25")

servico.mainloop()