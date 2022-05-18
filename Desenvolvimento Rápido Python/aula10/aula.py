import tkinter
import sqlite3

class App:
    def __init__(self, master=None):
        janela.title("Trabalhando GUI em Python")
        janela.geometry("640x480")
        janela.resizable(True, True)

        tkinter.Label(janela, text="Nome:", justify=tkinter.LEFT).grid(row=0)

        self.txtNomeAluno = tkinter.Entry(janela)
        self.txtNomeAluno.grid(row=0, column=1)

        tkinter.Label(janela, text="Matrícula:", justify=tkinter.LEFT).grid(row=2)

        self.txtMatriculaAluno = tkinter.Entry(janela)
        self.txtMatriculaAluno.grid(row=2, column=1)

        tkinter.Label(janela, text="Idade:", justify=tkinter.LEFT).grid(row=4)

        self.txtIdadeAluno = tkinter.Entry(janela)
        self.txtIdadeAluno.grid(row=4, column=1)

        self.botaoAdicionarAluno = tkinter.Button(janela)
        self.botaoAdicionarAluno['text'] = "Adicionar Aluno"
        self.botaoAdicionarAluno['command'] = lambda: adicionaAluno(self.txtNomeAluno.get().title().strip(), self.txtMatriculaAluno.get().strip(), self.txtIdadeAluno.get())
        self.botaoAdicionarAluno.grid(row=6, column=0)

        self.botaoVisualizarAluno = tkinter.Button(janela)
        self.botaoVisualizarAluno['text'] = "Visualizar Alunos"
        self.botaoVisualizarAluno['command'] = lambda: visualizarTabela("alunos")
        self.botaoVisualizarAluno.grid(row=6, column=1)

def iniciaBanco():
    global connection
    connection = sqlite3.connect('tkinter.db')
    global tabela
    tabela = connection.cursor()

def adicionaAluno(nome, matricula, idade):
    iniciaBanco()
    tabela.execute("""CREATE TABLE IF NOT EXISTS alunos (nome, matricula, idade);""")
    tabela.execute("""INSERT INTO alunos VALUES (?, ?, ?);""", (nome, matricula, idade))
    connection.commit()
    labelConfimacao = tkinter.Label(janela)
    labelConfimacao['text'] = 'Aluno adicionado com sucesso!'
    labelConfimacao.grid(row=10, column=0)

def visualizarTabela(tabelaConsulta):
    dados = []
    for i in tabela.execute(f"SELECT rowid, * FROM {tabelaConsulta} ORDER BY nome"):
        dados.append(i)
    labelAlunos = tkinter.Label(janela)
    labelAlunos['text'] = tuple(dados)
    labelAlunos.grid(row=10, column=0)


janela = tkinter.Tk()
App(janela)

janela.mainloop()