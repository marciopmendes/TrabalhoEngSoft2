import sys
sys.path.append(r"c:\Users\Marcio Mendes\Desktop\SI\4 periodo\Eng Soft 2\atividade_2bim\\")

from model.Cliente import *
from data.Banco import *

class Model:
    def __init__(self):
        self.banco = Banco()
    
    def executarAlteracao(self, cpf, nome, endereco, telefone):
        self.banco.alterarCliente(cpf, nome, endereco, telefone)
    
    def executarCadastro(self, nome, endereco, telefone, cpf):
        self.banco.inserirCliente(nome, endereco, telefone, cpf)
        
    def executarConsulta(self, cpf):
        consultado = self.banco.consultarCliente(cpf)
        consultado_format = f"""NOME: {consultado[0]}   ENDEREÇO: {consultado[1]}   TELEFONE: {consultado[2]}   CPF: {consultado[3]}"""
        return consultado_format
        
    def deletarCliente(self, cpf):
        self.banco.deletarCliente(cpf)
        
    def executarLista(self):
        lista = self.banco.listarClientes()
        lista_format = []
        for tupla in lista:
            lista_format.append(f"""NOME: {tupla[0]}   ENDEREÇO: {tupla[1]}   TELEFONE: {tupla[2]}   CPF: {tupla[3]}""")
        return lista_format
        
    