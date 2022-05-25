import appbd as appbd
import tkinter as tk

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
    
    def defineMensagemOperacao(self, msgOperacao):
        self.lblMensagemOperacao.configure(text=msgOperacao)
    
    def cadastrar(self):
        try:
            if self.txtCodigo.get() == "":
                raise Exception("Código não informado!")
            codigo, nome, preco = self.lerCampos()
            record = self.objBD.inserirDados(codigo, nome, preco)
            self.limpar()
            self.defineMensagemOperacao(f"Cadastro realizado com sucesso! {record}")
        except Exception as error:
            self.defineMensagemOperacao(f"Falha ao cadastrar: {error}")


    def atualizar(self):
        try:
            if self.txtCodigo.get() == "":
                raise Exception("Código não informado!")
            codigo, nome, preco = self.lerCampos()
            record = self.objBD.atualizarDados(codigo, nome, preco)
            self.limpar()
            self.defineMensagemOperacao(f"Produto atualizado com sucesso! {record}")
        except Exception as error:
            self.defineMensagemOperacao(f"Falha ao atualizar: {error}")

    def excluir(self):
        try:
            if self.txtCodigo.get() == "":
                raise Exception("Código não informado")
            if self.txtNome.get() == "":
                self.txtNome.insert(0, "Não informado")
            if self.txtPreco.get() == "":
                self.txtPreco.insert(0, 0)
            codigo, nome, preco = self.lerCampos()
            self.objBD.excluirDados(codigo)
            self.limpar()
            self.defineMensagemOperacao("Produto excluído com sucesso!")
        except Exception as error:
            self.defineMensagemOperacao(f"Falha ao excluir: {error}")

    def limpar(self):
        try:
            self.txtCodigo.delete(0, tk.END)
            self.txtNome.delete(0, tk.END)
            self.txtPreco.delete(0, tk.END)
            self.lblMensagemOperacao["text"] = ""
        except Exception as error:
            self.defineMensagemOperacao(f"Falha ao limpar: {error}")
    
    def lerCampos(self):
        try:
            codigo = int(self.txtCodigo.get())
            nome = (self.txtNome.get()).strip().capitalize()
            preco = float(self.txtPreco.get())
        except Exception as error:
            self.defineMensagemOperacao(f"Não foi possível ler os dados: {error}")
        return codigo, nome, preco

def main():
    janela = tk.Tk()
    principal = PrincipalBD(janela)
    janela.title("Cadastro de Produtos")
    janela.geometry("600x400")
    janela.mainloop()

if __name__ == "__main__":
    main()