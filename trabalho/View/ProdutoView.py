import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Controller.ProdutoController import ProdutoCt

class ProdutoVw(tk.Tk):#a classe view herda de tk.Tk, ou seja, tem todos os m�todos do tkinter
      
    def __init__(self):
        super().__init__()
        self.controller = ProdutoCt()
        self.mainWindow()
        self.btnCadastrar()
        self.btnConsultar()
        self.btnAlterar()
        self.btnListar()
        self.btnDeletar()

    def mainWindow(self):
        self.main_window = ttk.Frame(self)
        self.main_window.pack(padx=10, pady=10)
    
    def btnAlterar(self):
        alterar_frm = ttk.Frame(self.main_window)
        alterar_frm.pack()
        alterar_btn = ttk.Button(alterar_frm, text='Alterar Cadastro do Produto', command=self.alterarForm)
        alterar_btn.pack(padx=1, pady=1)
          
    def btnCadastrar(self):
        cadastrar_frm = ttk.Frame(self.main_window)
        cadastrar_frm.pack()
        cadastrar_btn = ttk.Button(cadastrar_frm, text='Cadastrar Produto', command=self.produtoForm)
        cadastrar_btn.pack(padx=1, pady=1)

    def btnConsultar(self):
        consultar_frm = ttk.Frame(self.main_window)
        consultar_frm.pack()
        consultar_btn = ttk.Button(consultar_frm, text='Consultar Produto', command=self.consultaForm)
        consultar_btn.pack(padx=1, pady=1)
             
    def btnDeletar(self):
        deletar_frm = ttk.Frame(self.main_window)
        deletar_frm.pack()
        deletar_btn = ttk.Button(deletar_frm, text='Apagar Produto', command=self.deletarForm)
        deletar_btn.pack(padx=1, pady=1)
     
    def btnListar(self):
        listar_frm = ttk.Frame(self.main_window)
        listar_frm.pack()
        listar_btn = ttk.Button(listar_frm, text='Exibir Produtos Cadastrados', command=self.listarTodos)
        listar_btn.pack(padx=1, pady=1)
    
    def produtoForm(self):
        cadastro_window = tk.Toplevel(self)
        
        codigo = tk.StringVar(cadastro_window)
        codigo_lbl = ttk.Label(cadastro_window, text='Codigo')
        codigo_lbl.pack()
        codigo_ent = ttk.Entry(cadastro_window, textvariable=codigo)
        codigo_ent.pack(padx=1, pady=3)
        
        descricao = tk.StringVar(cadastro_window)
        descricao_lbl = ttk.Label(cadastro_window, text='Descricao')
        descricao_lbl.pack()
        descricao_ent = ttk.Entry(cadastro_window, textvariable=descricao)
        descricao_ent.pack(padx=1, pady=3)
        
        valor = tk.StringVar(cadastro_window)
        valor_lbl = ttk.Label(cadastro_window, text='Valor')
        valor_lbl.pack()
        valor_ent = ttk.Entry(cadastro_window, textvariable=valor)
        valor_ent.pack(padx=1, pady=3)
        
        qtdEstoque = tk.StringVar(cadastro_window)
        qtdEstoque_lbl = ttk.Label(cadastro_window, text='Quantidade Estoque')
        qtdEstoque_lbl.pack()
        qtdEstoque_ent = ttk.Entry(cadastro_window, textvariable=qtdEstoque)
        qtdEstoque_ent.pack(padx=1, pady=3)
        
        estoqueMinimo = tk.StringVar(cadastro_window)
        estoqueMinimo_lbl = ttk.Label(cadastro_window, text='Estoque Minimo')
        estoqueMinimo_lbl.pack()
        estoqueMinimo_ent = ttk.Entry(cadastro_window, textvariable=estoqueMinimo)
        estoqueMinimo_ent.pack(padx=1, pady=3)
        
        validade = tk.StringVar(cadastro_window)
        validade_lbl = ttk.Label(cadastro_window, text='Validade')
        validade_lbl.pack()
        validade_ent = ttk.Entry(cadastro_window, textvariable=validade)
        validade_ent.pack(padx=1, pady=3)
        
        submit = ttk.Button(cadastro_window, text="Enviar", command=cadastro_window.destroy)
        submit.pack()
        self.wait_window(cadastro_window)

        self.controller.enviarCadastro(int(codigo.get()), descricao.get(), float(valor.get()), int(qtdEstoque.get()), int(estoqueMinimo.get()), validade.get())
        self.sucessMessage()
        
    def alterarForm(self):
        alterar_window = tk.Toplevel(self)
        
        codigo = tk.StringVar(alterar_window)
        codigo_lbl = ttk.Label(alterar_window, text='Codigo')
        codigo_lbl.pack()
        codigo_ent = ttk.Entry(alterar_window, textvariable=codigo)
        codigo_ent.pack(padx=1, pady=3)
        
        descricao = tk.StringVar(alterar_window)
        descricao_lbl = ttk.Label(alterar_window, text='Descricao')
        descricao_lbl.pack()
        descricao_ent = ttk.Entry(alterar_window, textvariable=descricao)
        descricao_ent.pack(padx=1, pady=3)
        
        valor = tk.StringVar(alterar_window)
        valor_lbl = ttk.Label(alterar_window, text='Valor')
        valor_lbl.pack()
        valor_ent = ttk.Entry(alterar_window, textvariable=valor)
        valor_ent.pack(padx=1, pady=3)
        
        qtdEstoque = tk.StringVar(alterar_window)
        qtdEstoque_lbl = ttk.Label(alterar_window, text='Quantidade Estoque')
        qtdEstoque_lbl.pack()
        qtdEstoque_ent = ttk.Entry(alterar_window, textvariable=qtdEstoque)
        qtdEstoque_ent.pack(padx=1, pady=3)
        
        estoqueMinimo = tk.StringVar(alterar_window)
        estoqueMinimo_lbl = ttk.Label(alterar_window, text='Estoque Minimo')
        estoqueMinimo_lbl.pack()
        estoqueMinimo_ent = ttk.Entry(alterar_window, textvariable=estoqueMinimo)
        estoqueMinimo_ent.pack(padx=1, pady=3)
        
        validade = tk.StringVar(alterar_window)
        validade_lbl = ttk.Label(alterar_window, text='Validade')
        validade_lbl.pack()
        validade_ent = ttk.Entry(alterar_window, textvariable=validade)
        validade_ent.pack(padx=1, pady=3)
        
        submit = ttk.Button(alterar_window, text="Enviar", command=alterar_window.destroy)
        submit.pack()
        self.wait_window(alterar_window)

        self.controller.enviarAlteracao(int(codigo.get()), descricao.get(), float(valor.get()), int(qtdEstoque.get()), int(estoqueMinimo.get()), validade.get())
        self.sucessMessage()
    
    def consultaForm(self):
        consulta_window = tk.Toplevel(self)
        
        codigo = tk.StringVar(consulta_window)
        codigo_lbl = ttk.Label(consulta_window, text='Codigo')
        codigo_lbl.pack()
        codigo_ent = ttk.Entry(consulta_window, textvariable=codigo)
        codigo_ent.pack(padx=1, pady=3)
        
        submit = ttk.Button(consulta_window, text="Enviar", command=consulta_window.destroy)
        submit.pack()
        self.wait_window(consulta_window)

        listar_window = tk.Toplevel(self)
        resultado = tk.StringVar(listar_window)
        resultado.set(self.controller.enviarConsulta(int(codigo.get())))
        produto = tk.Listbox(listar_window, selectmode='single', height=2, width=300)
        produto.pack()
        produto.insert('end', resultado.get())
        self.wait_window(listar_window) 

    def deletarForm(self):
        deletar_window = tk.Toplevel(self)
        codigo = tk.StringVar(deletar_window)
        codigo_lbl = ttk.Label(deletar_window, text='Codigo')
        codigo_lbl.pack()
        codigo_ent = ttk.Entry(deletar_window, textvariable=codigo)
        codigo_ent.pack(padx=1, pady=3)
        
        submit = ttk.Button(deletar_window, text="Enviar", command=deletar_window.destroy)
        submit.pack()
        self.wait_window(deletar_window)
       
        self.controller.deletarProduto(int(codigo.get()))
        self.sucessMessage()
              
    def listarTodos(self):
        listar_window = tk.Toplevel(self)
        produtos = tk.Listbox(listar_window, selectmode='single', height=100, width=150)
        produtos.pack()
        produtos.insert('end', *self.controller.enviarLista())#VER ESSA FUNCAO NO CONTROLLER
        self.wait_window(listar_window)
              
    def sucessMessage(self):
        tk.messagebox.showinfo(title="Sucesso", message="Operacao bem sucedida!")
    
    def main(self):
        self.mainloop()