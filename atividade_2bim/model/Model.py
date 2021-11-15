import sys
sys.path.append(r"c:\Users\Marcio Mendes\Desktop\SI\4 periodo\Eng Soft 2\atividade_2bim\\")

from model.Cliente import *
from data.Banco import *

class Model:
    def __init__(self):
        self.banco = Banco()
    
    def executarCadastro(self, nome, endereco, telefone, cpf):
        self.banco.inserirCliente(nome, endereco, telefone, cpf)
        
    def executarConsulta(self, cpf):
        self.banco.consultarCliente(cpf)
    
"""    def executarFuncao(self, botao):
        if botao == 'Cadastrar Cliente':
            self.banco.inserirCliente()
        if botao == 'Consultar Cliente':
            self.banco.consultarCliente()
        if botao == 'Alterar Cliente':
            self.banco.alterarCliente()
        if botao == 'Listar Clientes':
            self.banco.listarClientes()
        if botao == 'Excluir Cliente':
            self.banco.removerCliente()"""
        
    