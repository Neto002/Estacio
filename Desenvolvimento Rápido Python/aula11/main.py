import appbd
import tkinter as tk
from tkinter import ttk

class PrincipalBD:
    def __init__(self, win):
        self.objBD = appbd.AppBD()

        self.lblCodigo = tk.Label(win, text="Código do produto:")
        self.lblNome = tk.Label(win, text="Nome do produto:")
        self.lblPreco = tk.Label(win, text="Preço do produto:")
        self.lblMensagemOperacao = tk.Label(win, text="")

        self.txtCodigo = tk.Entry(bd=3)
        self.txtNome = tk.Entry()
        self.txtPreco = tk.Entry()

        self.btnCadastrar = tk.Button(win, text="Cadastrar", command=self.cadastrar)
        self.btnAtualizar = tk.Button(win, text="Atualizar", command=self.atualizar)
        self.btnExcluir = tk.Button(win, text="Excluir", command=self.excluir)
        self.btnLimpar = tk.Button(win, text="Limpar", command=self.limpar)

        self.lblCodigo.place(x=100, y=50)
        self.txtCodigo.place(x=250, y=50)

        self.lblNome.place(x=100, y=100)
        self.txtNome.place(x=250, y=100)

        self.lblPreco.place(x=100, y=150)
        self.txtPreco.place(x=250, y=150)

        self.btnCadastrar.place(x=100, y=200)
        self.btnAtualizar.place(x=200, y=200)
        self.btnExcluir.place(x=300, y=200)
        self.btnLimpar.place(x=400, y=200)

        self.lblMensagemOperacao.place(x=100, y=250)
    
    def limpaMensagemOperacao(self, msgOperacao):
        self.lblMensagemOperacao["text"] = ""
    
    def cadastrar(self):
        pass

    def atualizar(self):
        pass

    def excluir(self):
        pass

    def limpar(self):
        pass

janela = tk.Tk()
principal = PrincipalBD(janela)
janela.title("Cadastro de Produtos")
janela.geometry("600x500")
janela.mainloop()