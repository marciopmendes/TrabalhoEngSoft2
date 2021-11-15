import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
#criar função para cada elemento da interface e chamar no construtor da view
#cada widget que cria, o primeiro argumento tem q ser qual o componente pai

class View(tk.Tk):#a classe view herda de tk.Tk, ou seja, tem todos os métodos do tkinter
    
    cliente_buttons = ['Cadastrar Cliente', 'Consultar Cliente', 'Alterar Cliente', 'Listar Clientes',
                       'Excluir Cliente']
    
    
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.mainWindow()
        #DESCOMENTAR ESSA LINHA PARA FUNCIONAR NO TERMINALself.criarBotoes()
        self.btnCadastrar()
        self.btnConsultar()

    def mainWindow(self):
        self.main_window = ttk.Frame(self)
        self.main_window.pack(padx=10, pady=10)
        
    def btnCadastrar(self):
        cadastrar_frm = ttk.Frame(self.main_window)
        cadastrar_frm.pack()
        cadastrar_btn = ttk.Button(cadastrar_frm, text='Cadastrar Cliente', command=self.controller.clickCadastrar)
        cadastrar_btn.pack(padx=1, pady=1)

    def btnConsultar(self):
            consultar_frm = ttk.Frame(self.main_window)
            consultar_frm.pack()
            consultar_btn = ttk.Button(consultar_frm, text='Consultar Cliente', command=self.controller.clickConsultar)
            consultar_btn.pack(padx=1, pady=1)
#DESCOMENTAR ESSA PARTE PARA FUNCIONAR PELO TERMINAL
        
    """def criarBotoes(self):
        botoes_frm = ttk.Frame(self.main_window)#esse é o frame que fica dentro da main window
        botoes_frm.pack()
        cliente_frm = ttk.Frame(botoes_frm)
        cliente_frm.pack()
        
        for botao in self.cliente_buttons:
            #alocando as funções dinamicamente na criação de cada botão
            #a função lambda joga o o botão q foi clicado para uma variável e retorna a função click naquele botão      
            botao = ttk.Button(cliente_frm, text=botao, command=(lambda button=botao: self.controller.clickButton(button)))
            botao.pack(padx=1, pady=1)"""
    
    def clienteForm(self):
        cadastro_window = tk.Toplevel(self)
        
        nome = tk.StringVar(cadastro_window)
        nome_lbl = ttk.Label(cadastro_window, text='Nome')
        nome_lbl.pack()
        nome_ent = ttk.Entry(cadastro_window, textvariable=nome)
        nome_ent.pack(padx=1, pady=3)
        
        endereco = tk.StringVar(cadastro_window)
        endereco_lbl = ttk.Label(cadastro_window, text='Endereço')
        endereco_lbl.pack()
        endereco_ent = ttk.Entry(cadastro_window, textvariable=endereco)
        endereco_ent.pack(padx=1, pady=3)
        
        telefone = tk.StringVar(cadastro_window)
        telefone_lbl = ttk.Label(cadastro_window, text='Telefone')
        telefone_lbl.pack()
        telefone_ent = ttk.Entry(cadastro_window, textvariable=telefone)
        telefone_ent.pack(padx=1, pady=3)
        
        cpf = tk.StringVar(cadastro_window)
        cpf_lbl = ttk.Label(cadastro_window, text='CPF')
        cpf_lbl.pack()
        cpf_ent = ttk.Entry(cadastro_window, textvariable=cpf)
        cpf_ent.pack(padx=1, pady=3)
        
        submit = ttk.Button(cadastro_window, text="Enviar", command=cadastro_window.destroy)
        submit.pack()
        self.wait_window(cadastro_window)

        self.controller.enviarCadastro(nome.get(), endereco.get(), telefone.get(), cpf.get())
        self.sucessMessage()
    
    def consultaForm(self):
        consulta_window = tk.Toplevel(self)
        
        cpf = tk.StringVar(consulta_window)
        cpf_lbl = ttk.Label(consulta_window, text='CPF')
        cpf_lbl.pack()
        cpf_ent = ttk.Entry(consulta_window, textvariable=cpf)
        cpf_ent.pack(padx=1, pady=3)
        
        submit = ttk.Button(consulta_window, text="Enviar", command=consulta_window.destroy)
        submit.pack()
        self.wait_window(consulta_window)

        self.controller.enviarConsulta(cpf.get())
        
    def fecharJanela(self):
        self.destroy()
        
    def sucessMessage(self):
        tk.messagebox.showinfo(title="Sucesso", message="Operação bem sucedida!")
    
    def main(self):
        self.mainloop()#iniciando método do tkinter, é um loop infinito que termina quando fecha a janela
        
    