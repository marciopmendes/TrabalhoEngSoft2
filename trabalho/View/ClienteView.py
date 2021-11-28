import tkinter as tk
from tkinter import ttk
from Controller.ClienteController import ClienteCt
from tkinter import messagebox

class ClienteVw(tk.Tk):
      
    def __init__(self):
        super().__init__()
        self.controller = ClienteCt()
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
        alterar_btn = ttk.Button(alterar_frm, text='Alterar Cadastro do Cliente', command=self.alterarForm)
        alterar_btn.pack(padx=1, pady=1)
          
    def btnCadastrar(self):
        cadastrar_frm = ttk.Frame(self.main_window)
        cadastrar_frm.pack()
        cadastrar_btn = ttk.Button(cadastrar_frm, text='Cadastrar Cliente', command=self.clienteForm)
        cadastrar_btn.pack(padx=1, pady=1)

    def btnConsultar(self):
        consultar_frm = ttk.Frame(self.main_window)
        consultar_frm.pack()
        consultar_btn = ttk.Button(consultar_frm, text='Consultar Cliente', command=self.consultaForm)
        consultar_btn.pack(padx=1, pady=1)
             
    def btnDeletar(self):
        deletar_frm = ttk.Frame(self.main_window)
        deletar_frm.pack()
        deletar_btn = ttk.Button(deletar_frm, text='Apagar Cliente', command=self.deletarForm)
        deletar_btn.pack(padx=1, pady=1)
     
    def btnListar(self):
        listar_frm = ttk.Frame(self.main_window)
        listar_frm.pack()
        listar_btn = ttk.Button(listar_frm, text='Exibir Clientes Cadastrados', command=self.listarTodos)
        listar_btn.pack(padx=1, pady=1)
    
    def clienteForm(self):
        
        def validacao(nome, endereco, telefone, cpf):
            if not nome.isalpha():
                raise Exception ("Nome tem que ser somente letras")
            if not len(endereco) > 10:
                raise Exception ("Endereco nao eh tao pequeno assim")
            if not telefone.isdigit():
                raise Exception("Telefone nao tem letra, seu burro")
            else:
                if len(telefone) != 11:
                    raise Exception("Formato de telefone esta errado")
            if isinstance(cpf, int):
                if len(cpf) != 11:
                    raise Exception("CPF somente com 11 numeros")
            else:
                raise Exception("Inserir CPF somente numeros, sem pontos ou tracos")
        cadastro_window = tk.Toplevel(self)
        
        nome = tk.StringVar(cadastro_window)
        nome_lbl = ttk.Label(cadastro_window, text='Nome')
        nome_lbl.pack()
        nome_ent = ttk.Entry(cadastro_window, textvariable=nome)
        nome_ent.pack(padx=1, pady=3)
        
        endereco = tk.StringVar(cadastro_window)
        endereco_lbl = ttk.Label(cadastro_window, text='Endereco')
        endereco_lbl.pack()
        endereco_ent = ttk.Entry(cadastro_window, textvariable=endereco)
        endereco_ent.pack(padx=1, pady=3)
        
        telefone = tk.StringVar(cadastro_window)
        telefone_lbl = ttk.Label(cadastro_window, text='Telefone')
        telefone_lbl.pack()
        telefone_ent = ttk.Entry(cadastro_window, textvariable=telefone)
        telefone_ent.pack(padx=1, pady=3)
        
        cpf = tk.IntVar(cadastro_window)
        cpf_lbl = ttk.Label(cadastro_window, text='CPF')
        cpf_lbl.pack()
        cpf_ent = ttk.Entry(cadastro_window, textvariable=cpf)
        cpf_ent.pack(padx=1, pady=3)
        
        validar = ttk.Button(cadastro_window, text="Validar", command=lambda: validacao(nome.get(), endereco.get(), telefone.get(), cpf.get()))
        validar.pack()
        
        submit = ttk.Button(cadastro_window, text="Enviar", command=cadastro_window.destroy)
        submit.pack()
        self.wait_window(cadastro_window)

        self.controller.enviarCadastro(nome.get(), endereco.get(), telefone.get(), cpf.get())
        self.sucessMessage()
        
    def alterarForm(self):
        alterar_window = tk.Toplevel(self)
        
        cpf = tk.StringVar(alterar_window)
        cpf_lbl = ttk.Label(alterar_window, text='CPF')
        cpf_lbl.pack()
        cpf_ent = ttk.Entry(alterar_window, textvariable=cpf)
        cpf_ent.pack(padx=1, pady=3)
        
        nome = tk.StringVar(alterar_window)
        nome_lbl = ttk.Label(alterar_window, text='Nome')
        nome_lbl.pack()
        nome_ent = ttk.Entry(alterar_window, textvariable=nome)
        nome_ent.pack(padx=1, pady=3)
        
        endereco = tk.StringVar(alterar_window)
        endereco_lbl = ttk.Label(alterar_window, text='Endereco')
        endereco_lbl.pack()
        endereco_ent = ttk.Entry(alterar_window, textvariable=endereco)
        endereco_ent.pack(padx=1, pady=3)
        
        telefone = tk.StringVar(alterar_window)
        telefone_lbl = ttk.Label(alterar_window, text='Telefone')
        telefone_lbl.pack()
        telefone_ent = ttk.Entry(alterar_window, textvariable=telefone)
        telefone_ent.pack(padx=1, pady=3)
        
        submit = ttk.Button(alterar_window, text="Enviar", command=alterar_window.destroy)
        submit.pack()
        self.wait_window(alterar_window)

        self.controller.enviarAlteracao(int(cpf.get()), nome.get(), endereco.get(), telefone.get())
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

        listar_window = tk.Toplevel(self)
        resultado = tk.StringVar(listar_window)
        resultado.set(self.controller.enviarConsulta(int(cpf.get())))
        cliente = tk.Listbox(listar_window, selectmode='single', height=2, width=300)
        cliente.pack()
        cliente.insert('end', resultado.get())
        self.wait_window(listar_window) 

    def deletarForm(self):
        deletar_window = tk.Toplevel(self)
        cpf = tk.StringVar(deletar_window)
        cpf_lbl = ttk.Label(deletar_window, text='CPF')
        cpf_lbl.pack()
        cpf_ent = ttk.Entry(deletar_window, textvariable=cpf)
        cpf_ent.pack(padx=1, pady=3)
        
        submit = ttk.Button(deletar_window, text="Enviar", command=deletar_window.destroy)
        submit.pack()
        self.wait_window(deletar_window)
       
        self.controller.deletarCliente(int(cpf.get()))
        self.sucessMessage()
              
    def listarTodos(self):
        listar_window = tk.Toplevel(self)
        clientes = tk.Listbox(listar_window, selectmode='single', height=100, width=150)
        clientes.pack()
        clientes.insert('end', *self.controller.enviarLista())
        self.wait_window(listar_window)
              
    def sucessMessage(self):
        tk.messagebox.showinfo(title="Sucesso", message="Operacao bem sucedida!")
    
    def main(self):
        self.mainloop()