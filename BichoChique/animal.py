from tkinter import* 
from tkinter import filedialog
import subprocess

animal=Tk()

#Configurações da tela
animal.title("Bicho chique")
animal.resizable(False, False)
width = 1000
height = 700
animal.maxsize(width, height)
animal.minsize(width, height)
animal.configure(bg='#FFC93E')

# Função para abrir a tela de menu
def abrir_tela_menu():
    subprocess.run(["python", "Menu.py"])

# Botão voltar ao menu
btn_menu = Button(animal, text="Voltar ao menu", bd=0, bg="#1D9BF0", fg="#fff", font="Helvetica 10 underline", activebackground="#FFF", activeforeground="#1D9BF0", command=abrir_tela_menu)
btn_menu.place(relx=.830, rely=.10, anchor="n")

# Título dos serviços
txt_titulo = Label(animal, text="Cadastro do Pet", bg="#FFC93E", font=("Helvetica 20 bold"))
txt_titulo.place(relx=.450, rely=.20, anchor="n")

# Campo código do serviço
txt_codigo = Label(animal, text="Código do tutor", bg="#FFC93E", font=("Helvetica 10"))
txt_codigo.place(relx=.348, rely=.30, anchor="n")
lbl_codigo = Entry(animal)
lbl_codigo.place(relx=.358, rely=.33, anchor="n", width="130", height="20")

# Campo nome
txt_nome = Label(animal, text="Nome", bg="#FFC93E", font=("Helvetica 10"))
txt_nome.place(relx=.490, rely=.30, anchor="n")
lbl_nome = Entry(animal)
lbl_nome.place(relx=.550, rely=.33, anchor="n", width="190", height="20")

# Campo data de nascimento
txt_duracao = Label(animal, text="Data de nascimento", bg="#FFC93E", font=("Helvetica 10"))
txt_duracao.place(relx=.353, rely=.40, anchor="n")
lbl_duracao = Entry(animal)
lbl_duracao.place(relx=.353, rely=.43, anchor="n", width="120", height="20")

# Campo Idade
txt_duracao = Label(animal, text="Idade", bg="#FFC93E", font=("Helvetica 10"))
txt_duracao.place(relx=.440, rely=.40, anchor="n")
lbl_duracao = Entry(animal)
lbl_duracao.place(relx=.460, rely=.43, anchor="n", width="80", height="20")

# Criando botão de rádio para a espécie
lbl_especie = Label(animal, text="Sexo", bg="#FFC93E").place(relx=.530, rely=.40, anchor="n")
var2 = StringVar()
var2.set("c")
rdb_btn_c = Radiobutton(animal, text="Macho", variable=var2, value="c", bg="#FFC93E")
rdb_btn_g = Radiobutton(animal, text="Fêmea", variable=var2, value="g", bg="#FFC93E")
rdb_btn_c.place(relx=.540, rely=.43, anchor="n")
rdb_btn_g.place(relx=.610, rely=.43, anchor="n")

#campo Especie
txt_duracao = Label(animal, text="Espécie", bg="#FFC93E", font=("Helvetica 10"))
txt_duracao.place(relx=.325, rely=.50, anchor="n")
lbl_duracao = Entry(animal)
lbl_duracao.place(relx=.338, rely=.53, anchor="n", width="80", height="20")

#Raça
txt_descricao = Label(animal, text="Raça", bg="#FFC93E", font=("Helvetica 10"))
txt_descricao.place(relx=.423, rely=.50, anchor="n")
lbl_descricao = Entry(animal)
lbl_descricao.place(relx=.453, rely=.53, anchor="n", width="120", height="20")

#Peso
txt_descricao = Label(animal, text="Peso", bg="#FFC93E", font=("Helvetica 10"))
txt_descricao.place(relx=.543, rely=.50, anchor="n")
lbl_descricao = Entry(animal)
lbl_descricao.place(relx=.563, rely=.53, anchor="n", width="90", height="20")

#Descrição
txt_descricao = Label(animal, text="Descrição", bg="#FFC93E", font=("Helvetica 10"))
txt_descricao.place(relx=.330, rely=.58, anchor="n")
lbl_descricao = Entry(animal)
lbl_descricao.place(relx=.465, rely=.61, anchor="n", width="400", height="50")

#botões de salvar alterar e excluir
btn_salvar = Button(animal, text="Salvar", bg="#1D9BF0")
btn_salvar.place(relx=.330, rely=.75, anchor="n", width="80", height="25")
btn_alterar = Button(animal, text="Alterar", bg="#1D9BF0")
btn_alterar.place(relx=.480, rely=.75, anchor="n", width="80", height="25")
btn_excluir = Button(animal, text="Excluir", bg="#1D9BF0")
btn_excluir.place(relx=.630, rely=.75, anchor="n", width="80", height="25")

#Data de cadastro
txt_descricao = Label(animal, text="Data de cadastro", bg="#FFC93E", font=("Helvetica 10"))
txt_descricao.place(relx=.855, rely=.38, anchor="n")
lbl_descricao = Entry(animal)
lbl_descricao.place(relx=.860, rely=.41, anchor="n", width="120", height="20")

animal.mainloop()
