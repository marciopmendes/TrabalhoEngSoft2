import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Controller.CompraController import CompraCt


class CompraVw(tk.Tk):#a classe view herda de tk.Tk, ou seja, tem todos os m�todos do tkinter
      
    def __init__(self):
        super().__init__()
        self.controller = CompraCt()
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
        alterar_btn = ttk.Button(alterar_frm, text='Alterar Cadastro da Compra', command=self.alterarForm)
        alterar_btn.pack(padx=1, pady=1)
          
    def btnCadastrar(self):
        cadastrar_frm = ttk.Frame(self.main_window)
        cadastrar_frm.pack()
        cadastrar_btn = ttk.Button(cadastrar_frm, text='Cadastrar Compra', command=self.compraForm)
        cadastrar_btn.pack(padx=1, pady=1)

    def btnConsultar(self):
        consultar_frm = ttk.Frame(self.main_window)
        consultar_frm.pack()
        consultar_btn = ttk.Button(consultar_frm, text='Consultar Compra', command=self.consultaForm)
        consultar_btn.pack(padx=1, pady=1)
             
    def btnDeletar(self):
        deletar_frm = ttk.Frame(self.main_window)
        deletar_frm.pack()
        deletar_btn = ttk.Button(deletar_frm, text='Apagar Compra', command=self.deletarForm)
        deletar_btn.pack(padx=1, pady=1)
     
    def btnListar(self):
        listar_frm = ttk.Frame(self.main_window)
        listar_frm.pack()
        listar_btn = ttk.Button(listar_frm, text='Exibir Compras Cadastradas', command=self.listarTodos)
        listar_btn.pack(padx=1, pady=1)
    
    def compraForm(self):
                
        cadastro_window = tk.Toplevel(self)
        
        matricula = tk.IntVar(cadastro_window)
        matricula_lbl = ttk.Label(cadastro_window, text='Matricula do Vendedor')
        matricula_lbl.pack()
        matricula_ent = ttk.Entry(cadastro_window, textvariable=matricula)
        matricula_ent.pack(padx=1, pady=3)
        
        cpf = tk.IntVar(cadastro_window)
        cpf_lbl = ttk.Label(cadastro_window, text='CPF do cliente')
        cpf_lbl.pack()
        cpf_ent = ttk.Entry(cadastro_window, textvariable=cpf)
        cpf_ent.pack(padx=1, pady=3)
        
        codigo = tk.IntVar(cadastro_window)
        codigo_lbl = ttk.Label(cadastro_window, text='Codigo da Compra')
        codigo_lbl.pack()
        codigo_ent = ttk.Entry(cadastro_window, textvariable=codigo)
        codigo_ent.pack(padx=1, pady=3)
        
        click = tk.IntVar(cadastro_window)
        incluir = ttk.Button(cadastro_window, text="Inserir Compra", command=lambda: click.set(1))
        incluir.pack()
        incluir.wait_variable(click)#a pessoa tem q clicar no botão pra seguir a partir daqui
        
        CompraCt.cadastraCompra(self, codigo.get(), matricula.get(), cpf.get())#cadastra a compra no banco
        incluir_window = tk.Toplevel(self)#abre a nova janela para inclusao de produtos
        
        codigoProduto = tk.IntVar(incluir_window)
        codigoProduto_lbl = ttk.Label(incluir_window, text='Codigo do Produto')
        codigoProduto_lbl.pack()
        codigoProduto_ent = ttk.Entry(incluir_window, textvariable=codigoProduto)
        codigoProduto_ent.pack(padx=1, pady=3)
        
        quantidade = tk.IntVar(incluir_window)
        quantidade_lbl = ttk.Label(incluir_window, text='Quantidade de itens')
        quantidade_lbl.pack()
        quantidade_ent = ttk.Entry(incluir_window, textvariable=quantidade)
        quantidade_ent.pack(padx=1, pady=3)

        additem = ttk.Button(incluir_window, text="Incluir Produtos", command=lambda: CompraCt.cadastraItens(CompraCt, matricula.get(), cpf.get(), codigo.get(), codigoProduto.get(), quantidade.get()))#FAZER CHAMADA DO CONTROLLER
        additem.pack()
        submit = ttk.Button(incluir_window, text="Finalizar Compra", command=incluir_window.destroy)
        submit.pack()
        self.wait_window(incluir_window)
        cadastro_window.destroy()
         
    def alterarForm(self):
        alterar_window = tk.Toplevel(self)
        
        codigoCompra = tk.IntVar(alterar_window)
        codigoCompra_lbl = ttk.Label(alterar_window, text='Codigo da Compra')
        codigoCompra_lbl.pack()
        codigoCompra_ent = ttk.Entry(alterar_window, textvariable=codigoCompra)
        codigoCompra_ent.pack(padx=1, pady=3)
        
        proximo = tk.IntVar(alterar_window)
        submit = ttk.Button(alterar_window, text="Alterar", command=lambda: proximo.set(1))
        submit.pack()
        submit.wait_variable(proximo)
        
        matricula = tk.IntVar(alterar_window)
        matricula_lbl = ttk.Label(alterar_window, text='Matricula do Vendedor')
        matricula_lbl.pack()
        matricula_ent = ttk.Entry(alterar_window, textvariable=matricula)
        matricula_ent.pack(padx=1, pady=3)
        
        cpf = tk.IntVar(alterar_window)
        cpf_lbl = ttk.Label(alterar_window, text='CPF do cliente')
        cpf_lbl.pack()
        cpf_ent = ttk.Entry(alterar_window, textvariable=cpf)
        cpf_ent.pack(padx=1, pady=3)
        
        codigoProduto = tk.IntVar(alterar_window)
        codigoProduto_lbl = ttk.Label(alterar_window, text='Codigo do Produto')
        codigoProduto_lbl.pack()
        codigoProduto_ent = ttk.Entry(alterar_window, textvariable=codigoProduto)
        codigoProduto_ent.pack(padx=1, pady=3)
        
        qtdItens = tk.IntVar(alterar_window)
        qtdItens_lbl = ttk.Label(alterar_window, text='Quantidade')
        qtdItens_lbl.pack()
        qtdItens_ent = ttk.Entry(alterar_window, textvariable=qtdItens)
        qtdItens_ent.pack(padx=1, pady=3)
        

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
        