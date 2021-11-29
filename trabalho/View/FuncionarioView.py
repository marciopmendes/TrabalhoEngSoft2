import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Controller.FuncionarioController import FuncionarioCt

class FuncionarioVw(tk.Tk):
      
    def __init__(self):
        super().__init__()
        self.controller = FuncionarioCt()
        self.mainWindow()
        self.btnCadastrar()
        self.btnConsultar()
        self.btnAlterar()
        self.btnListar()
        self.btnDeletar()
        self.btnSalario()

    def mainWindow(self):
        self.main_window = ttk.Frame(self)
        self.main_window.pack(padx=10, pady=10)
    
    def btnAlterar(self):
        alterar_frm = ttk.Frame(self.main_window)
        alterar_frm.pack()
        alterar_btn = ttk.Button(alterar_frm, text='Alterar Cadastro do Funcionario', command=self.alterarForm)
        alterar_btn.pack(padx=1, pady=1)
          
    def btnCadastrar(self):
        cadastrar_frm = ttk.Frame(self.main_window)
        cadastrar_frm.pack()
        cadastrar_btn = ttk.Button(cadastrar_frm, text='Cadastrar Funcionario', command=self.funcionarioForm)
        cadastrar_btn.pack(padx=1, pady=1)
        
    def btnSalario(self):
        salario_frm = ttk.Frame(self.main_window)
        salario_frm.pack()
        salario_btn = ttk.Button(salario_frm, text='Calcular Salario', command=self.salarioForm)
        salario_btn.pack(padx=1, pady=1)

    def btnConsultar(self):
        consultar_frm = ttk.Frame(self.main_window)
        consultar_frm.pack()
        consultar_btn = ttk.Button(consultar_frm, text='Consultar Funcionario', command=self.consultaForm)
        consultar_btn.pack(padx=1, pady=1)
             
    def btnDeletar(self):
        deletar_frm = ttk.Frame(self.main_window)
        deletar_frm.pack()
        deletar_btn = ttk.Button(deletar_frm, text='Apagar Funcionario', command=self.deletarForm)
        deletar_btn.pack(padx=1, pady=1)
     
    def btnListar(self):
        listar_frm = ttk.Frame(self.main_window)
        listar_frm.pack()
        listar_btn = ttk.Button(listar_frm, text='Exibir Funcionarios Cadastrados', command=self.listarTodos)
        listar_btn.pack(padx=1, pady=1)
    
    def funcionarioForm(self):
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
        
        cpf = tk.StringVar(cadastro_window)
        cpf_lbl = ttk.Label(cadastro_window, text='CPF')
        cpf_lbl.pack()
        cpf_ent = ttk.Entry(cadastro_window, textvariable=cpf)
        cpf_ent.pack(padx=1, pady=3)

        matricula = tk.StringVar(cadastro_window)
        matricula_lbl = ttk.Label(cadastro_window, text='Matricula')
        matricula_lbl.pack()
        matricula_ent = ttk.Entry(cadastro_window, textvariable=matricula)
        matricula_ent.pack(padx=1, pady=3)
        
        salarioBase = tk.StringVar(cadastro_window)
        salarioBase_lbl = ttk.Label(cadastro_window, text='Salario Base')
        salarioBase_lbl.pack()
        salarioBase_ent = ttk.Entry(cadastro_window, textvariable=salarioBase)
        salarioBase_ent.pack(padx=1, pady=3)
        
        submit = ttk.Button(cadastro_window, text="Enviar", command=cadastro_window.destroy)
        submit.pack()
        self.wait_window(cadastro_window)

        self.controller.enviarCadastro(nome.get(), endereco.get(), telefone.get(), cpf.get(), int(matricula.get()), float(salarioBase.get()))
        self.sucessMessage()
        
    def alterarForm(self):
        alterar_window = tk.Toplevel(self)
        
        matricula = tk.StringVar(alterar_window)
        matricula_lbl = ttk.Label(alterar_window, text='Matricula')
        matricula_lbl.pack()
        matricula_ent = ttk.Entry(alterar_window, textvariable=matricula)
        matricula_ent.pack(padx=1, pady=3)
        
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
        
        cpf = tk.StringVar(alterar_window)
        cpf_lbl = ttk.Label(alterar_window, text='CPF')
        cpf_lbl.pack()
        cpf_ent = ttk.Entry(alterar_window, textvariable=cpf)
        cpf_ent.pack(padx=1, pady=3)
        
        salarioBase = tk.StringVar(alterar_window)
        salarioBase_lbl = ttk.Label(alterar_window, text='Salario Base')
        salarioBase_lbl.pack()
        salarioBase_ent = ttk.Entry(alterar_window, textvariable=salarioBase)
        salarioBase_ent.pack(padx=1, pady=3)
        
        submit = ttk.Button(alterar_window, text="Enviar", command=alterar_window.destroy)
        submit.pack()
        self.wait_window(alterar_window)

        self.controller.enviarAlteracao(int(matricula.get()), nome.get(), endereco.get(), telefone.get(), cpf.get(), salarioBase.get())
        self.sucessMessage()
    
    def consultaForm(self):
        consulta_window = tk.Toplevel(self)
        
        matricula = tk.StringVar(consulta_window)
        matricula_lbl = ttk.Label(consulta_window, text='Matricula')
        matricula_lbl.pack()
        matricula_ent = ttk.Entry(consulta_window, textvariable=matricula)
        matricula_ent.pack(padx=1, pady=3)
        
        submit = ttk.Button(consulta_window, text="Enviar", command=consulta_window.destroy)
        submit.pack()
        self.wait_window(consulta_window)

        listar_window = tk.Toplevel(self)
        resultado = tk.StringVar(listar_window)
        resultado.set(self.controller.enviarConsulta(int(matricula.get())))
        funcionario = tk.Listbox(listar_window, selectmode='single', height=2, width=300)
        funcionario.pack()
        funcionario.insert('end', resultado.get())
        self.wait_window(listar_window) 

    def salarioForm(self):
        salario_window = tk.Toplevel(self)
        
        matricula = tk.IntVar(salario_window)
        matricula_lbl = ttk.Label(salario_window, text='Matricula')
        matricula_lbl.pack()
        matricula_ent = ttk.Entry(salario_window, textvariable=matricula)
        matricula_ent.pack(padx=1, pady=3)
        
        submit = ttk.Button(salario_window, text="Calcular", command=lambda: FuncionarioCt.calculaSalario(self, matricula.get()))
        submit.pack()
        self.wait_window(salario_window)
        salario_window.destroy()

    def deletarForm(self):
        deletar_window = tk.Toplevel(self)
        matricula = tk.StringVar(deletar_window)
        matricula_lbl = ttk.Label(deletar_window, text='Matricula')
        matricula_lbl.pack()
        matricula_ent = ttk.Entry(deletar_window, textvariable=matricula)
        matricula_ent.pack(padx=1, pady=3)
        
        submit = ttk.Button(deletar_window, text="Enviar", command=deletar_window.destroy)
        submit.pack()
        self.wait_window(deletar_window)
       
        self.controller.deletarFuncionario(int(matricula.get()))
        self.sucessMessage()
              
    def listarTodos(self):
        listar_window = tk.Toplevel(self)
        funcionarios = tk.Listbox(listar_window, selectmode='single', height=100, width=150)
        funcionarios.pack()
        funcionarios.insert('end', *self.controller.enviarLista())
        self.wait_window(listar_window)
              
    def sucessMessage(self):
        tk.messagebox.showinfo(title="Sucesso", message="Operacao bem sucedida!")
    
    def main(self):
        self.mainloop()