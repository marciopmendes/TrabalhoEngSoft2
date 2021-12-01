import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Controller.RelatorioController import RelatorioCt

class RelatorioVw(tk.Tk):

      
    def __init__(self):
        super().__init__()
        self.controller = RelatorioCt()
        self.mainWindow()
        self.btnClienteCompra()
        self.btnCompraPeriodo()
        self.btnEstoqueMinimo()
        
    def mainWindow(self):
        self.main_window = ttk.Frame(self)
        self.main_window.pack(padx=10, pady=10)      
    
    def btnClienteCompra(self):
        cliente_compra_frm = ttk.Frame(self.main_window)
        cliente_compra_frm.pack()
        cliente_compra_btn = ttk.Button(cliente_compra_frm, text='Exibir Clientes com Compras', command=self.clienteCompra)
        cliente_compra_btn.pack(padx=1, pady=1)
        
    def btnCompraPeriodo(self):
        compra_periodo_frm = ttk.Frame(self.main_window)
        compra_periodo_frm.pack()
        compra_periodo_btn = ttk.Button(compra_periodo_frm, text='Exibir Compras Por Periodo', command=self.compraPeriodo)
        compra_periodo_btn.pack(padx=1, pady=1)
        
    def btnEstoqueMinimo(self):
        estoque_minimo_frm = ttk.Frame(self.main_window)
        estoque_minimo_frm.pack()
        estoque_minimo_btn = ttk.Button(estoque_minimo_frm, text='Produtos Abaixo Do Estoque', command=self.estoqueMinimo)
        estoque_minimo_btn.pack(padx=1, pady=1) 
              
    def clienteCompra(self):
        cc_window = tk.Toplevel(self)
        clientes = tk.Listbox(cc_window, selectmode='single', height=100, width=150)
        clientes.pack()
        clientes.insert('end', *self.controller.clienteCompra())
        self.wait_window(cc_window)
        
    def estoqueMinimo(self):
        em_window = tk.Toplevel(self)
        estoque = tk.Listbox(em_window, selectmode='single', height=100, width=150)
        estoque.pack()
        estoque.insert('end', *self.controller.estoqueMinimo())
        self.wait_window(em_window)
        
    def compraPeriodo(self):
        cp_window = tk.Toplevel(self)
        
        anoInicial = tk.StringVar(cp_window)
        anoInicial_lbl = ttk.Label(cp_window, text='Ano Inicial')
        anoInicial_lbl.pack()
        anoInicial_ent = ttk.Entry(cp_window, textvariable=anoInicial)
        anoInicial_ent.pack(padx=1, pady=3)
        
        anoFinal = tk.StringVar(cp_window)
        anoFinal_lbl = ttk.Label(cp_window, text='Ano Final')
        anoFinal_lbl.pack()
        anoFinal_ent = ttk.Entry(cp_window, textvariable=anoFinal)
        anoFinal_ent.pack(padx=1, pady=3)
        
        submit = ttk.Button(cp_window, text="Listar", command=cp_window.destroy)
        submit.pack()
        self.wait_window(cp_window)
        
        compras_window = tk.Toplevel(self)
        compras = tk.Listbox(compras_window, selectmode='single', height=100, width=150)
        compras.pack()
        compras.insert('end', *self.controller.compraPeriodo(anoInicial.get(), anoFinal.get()))
        self.wait_window(compras_window)
    
    def main(self):
        self.mainloop()