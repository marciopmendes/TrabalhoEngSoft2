import tkinter as tk
from tkinter import ttk
from View.ClienteView import ClienteVw
from View.CompraView import CompraVw
from View.FuncionarioView import FuncionarioVw
from View.ProdutoView import ProdutoVw
from Controller.InicioController import InicioCt
from tkinter import messagebox
from View.RelatorioView import RelatorioVw

class InicioVw(tk.Tk):
      
    def __init__(self):
        super().__init__()
        self.controller = InicioCt()
        self.mainWindow()
        self.btnConectar()
        self.btnCliente()
        self.btnFuncionario()
        self.btnProduto()
        self.btnCompra()
        self.btnRelatorio()

        
    def mainWindow(self):
        self.main_window = ttk.Frame(self)
        self.main_window.pack(padx=10, pady=10)
        
    def sucessMessage(self):
        tk.messagebox.showinfo(title="Sucesso", message="Operacao bem sucedida!")
        
    def btnConectar(self):
        conectar_frm = ttk.Frame(self.main_window)
        conectar_frm.pack()
        conectar_btn = ttk.Button(conectar_frm, text='Conectar ao Banco de Dados', command=self.conectarForm)
        conectar_btn.pack(padx=1, pady=1)
        
    def btnRelatorio(self):
        relatorio_frm = ttk.Frame(self.main_window)
        relatorio_frm.pack()
        relatorio_btn = ttk.Button(relatorio_frm, text='Relatorios', command=RelatorioVw)
        relatorio_btn.pack(padx=1, pady=1)
        
    def conectarForm(self): 
        conexao_window = tk.Toplevel(self)
        
        host = tk.StringVar(conexao_window)
        host_lbl = ttk.Label(conexao_window, text='Host')
        host_lbl.pack()
        host_ent = ttk.Entry(conexao_window, textvariable=host)
        host_ent.pack(padx=1, pady=3)

        usuario = tk.StringVar(conexao_window)
        usuario_lbl = ttk.Label(conexao_window, text='Username')
        usuario_lbl.pack()
        usuario_ent = ttk.Entry(conexao_window, textvariable=usuario)
        usuario_ent.pack(padx=1, pady=3)

        password = tk.StringVar(conexao_window)
        password_lbl = ttk.Label(conexao_window, text='Password')
        password_lbl.pack()
        password_ent = ttk.Entry(conexao_window, textvariable=password, show="*")
        password_ent.pack(padx=1, pady=3)

        nome = tk.StringVar(conexao_window)
        nome_lbl = ttk.Label(conexao_window, text='Nome do Banco')
        nome_lbl.pack()
        nome_ent = ttk.Entry(conexao_window, textvariable=nome)
        nome_ent.pack(padx=1, pady=3)
        
        conectar = ttk.Button(conexao_window, text="Conectar", command=conexao_window.destroy)
        conectar.pack()
        self.wait_window(conexao_window)

        self.controller.setBanco(host.get(), usuario.get(), password.get(), nome.get())
        self.sucessMessage()
        
    def btnCliente(self):
        cliente_frm = ttk.Frame(self.main_window)
        cliente_frm.pack()
        cliente_btn = ttk.Button(cliente_frm, text='Clientes', command=ClienteVw)
        cliente_btn.pack(padx=1, pady=1)
        
    def btnCompra(self):
        compra_frm = ttk.Frame(self.main_window)
        compra_frm.pack()
        compra_btn = ttk.Button(compra_frm, text='Compras', command=CompraVw)
        compra_btn.pack(padx=1, pady=1)
        
    def btnFuncionario(self):
        funcionario_frm = ttk.Frame(self.main_window)
        funcionario_frm.pack()
        funcionario_btn = ttk.Button(funcionario_frm, text='Funcionarios', command=FuncionarioVw)
        funcionario_btn.pack(padx=1, pady=1)
        
    def btnProduto(self):
        produto_frm = ttk.Frame(self.main_window)
        produto_frm.pack()
        produto_btn = ttk.Button(produto_frm, text='Produtos', command=ProdutoVw)
        produto_btn.pack(padx=1, pady=1)
        
    def main(self):
        self.mainloop()

app = InicioVw()
app.main()