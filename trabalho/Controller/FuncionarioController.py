from Controller.InicioController import InicioCt
from Model.FuncionarioModel import FuncionarioMd
from DAO.InicioDAO import BancoDb
from DAO.FuncionarioDAO import FuncionarioDb


class FuncionarioCt(InicioCt):
    banco = BancoDb()
    fdao = FuncionarioDb()
    

    def __init__(self):
        pass
    
    def enviarCadastro(self, nome, endereco, telefone, cpf, matricula, salarioBase):
        funcionario = FuncionarioMd(nome, endereco, telefone, cpf, matricula, salarioBase)
        FuncionarioCt.fdao.inserirFuncionario(funcionario)
        
    def enviarAlteracao(self, matricula, nome, endereco, telefone, cpf, salarioBase):
        funcionario = FuncionarioMd(nome, endereco, telefone, cpf, matricula, salarioBase)
        FuncionarioCt.fdao.alterarFuncionario(funcionario)
        
    def enviarConsulta(self, matricula):
        consultado = FuncionarioCt.fdao.consultarFuncionario(matricula)
        return consultado
        
    def deletarFuncionario(self, matricula):
        FuncionarioCt.fdao.deletarFuncionario(matricula)
        
    def enviarLista(self):
        lista = FuncionarioCt.fdao.listarFuncionarios()
        return lista
    
    def calculaSalario(self, matricula):
        FuncionarioCt.fdao.salarioFuncionario(matricula)