# 1. Cadastro de Alunos (com exibição no terminal) Crie um programa utilizando o Tkinter
# que permita ao usuário cadastrar alunos. O programa deve solicitar o nome, idade e
# nota do aluno por meio de caixas de entrada (Entry) e exibir um botão para
# cadastrar. Ao cadastrar um aluno, os dados devem ser exibidos no terminal.


# from tkinter import *

# lista_alunos = []

# def cadastro_alunos():
#     nome = aluno_entre.get()
#     idade = int(idade_entre.get())
#     nota = float(nota_aluno.get())
#     lista_alunos.append({"Nome":nome,"Idade":idade,"Nota":nota})
#     print(lista_alunos)


# janela = Tk()

# titulo = Label(text="Cadastro de Alunos").pack()

# nome_aluno = Label(text="Insira o Nome Do Aluno:").pack()
# aluno_entre = Entry()
# aluno_entre.pack()

# idade_aluno = Label(text="Insira a Idade Do Aluno:").pack()
# idade_entre = Entry()
# idade_entre.pack()

# nota_aluno = Label(text="Insira a Nota Do Aluno:").pack()
# nota_aluno = Entry()
# nota_aluno.pack()

# cadastrar = Button(janela,text="Cadastrar",command=cadastro_alunos)
# cadastrar.pack()


# janela.mainloop()

# Calculadora Simples (com exibição no terminal) Desenvolva uma calculadora
# simples utilizando o Tkinter que permita ao usuário realizar operações matemáticas
# básicas, como adição, subtração, multiplicação e divisão. O programa deve exibir
# botões para os números e as operações, e ao realizar o cálculo, o resultado deve ser
# exibido no terminal.


from tkinter import *

janela = Tk()
janela.title("Calculadora")
janela.geometry("450x450")


num01 =""
num02 = ""
operacao = ""
resultado = 0


def registrar_operacao(op):
    global operacao
    operacao = op


def registrar_numero(numero):
    global num01
    global num02
    if operacao == "":
        num01 = f"{num01}{numero}"
    else:
        num02 = f"{num02}{numero}"


def calcular():
    global resultado
    if operacao == "/":
        resultado = num01 / num02
    elif operacao ==         
























botao7 = Button(janela,text="7", width=15, height=5)
botao7.grid(row=0, column=0)
botao8 = Button(janela,text="8", width=15, height=5)
botao8.grid(row=0, column=1)
botao9 = Button(janela,text="9", width=15, height=5)
botao9.grid(row=0, column=2)
botaosoma = Button(janela,text="+", width=15, height=5)
botaosoma.grid(row=0, column=3)


botao4 = Button(janela,text="4", width=15, height=5)
botao4.grid(row=1, column=0)
botao5 = Button(janela,text="5", width=15, height=5)
botao5.grid(row=1, column=1)
botao6 = Button(janela,text="6", width=15, height=5)
botao6.grid(row=1, column=2)
botaosub = Button(janela,text="-", width=15, height=5)
botaosub.grid(row=1, column=3)


botao1 = Button(janela,text="1", width=15, height=5)
botao1.grid(row=2, column=0)
botao2 = Button(janela,text="2", width=15, height=5)
botao2.grid(row=2, column=1)
botao3 = Button(janela,text="3", width=15, height=5)
botao3.grid(row=2, column=2)
botaomul = Button(janela,text="*", width=15, height=5)
botaomul.grid(row=2, column=3)

botao0 = Button(janela,text="0", width=15, height=5)
botao0.grid(row=3, column=0)
botaoigual = Button(janela,text="=", width=15, height=5)
botaoigual.grid(row=3, column=1)
botao6 = Button(janela,text="", width=15, height=5)
botao6.grid(row=3, column=2)
botaodiv = Button(janela,text="/", width=15, height=5)
botaodiv.grid(row=3, column=3)





































janela.mainloop()



































