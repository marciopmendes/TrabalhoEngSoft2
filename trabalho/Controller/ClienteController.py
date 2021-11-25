from Model.ClienteModel import ClienteMd
from DAO.InicioDAO import BancoDb
from DAO.ClienteDAO import ClienteDb
from Controller.InicioController import InicioCt


class ClienteCt(InicioCt):
    
    banco = BancoDb()
    cdao = ClienteDb()
    
    def __init__(self):
        pass
        
    def enviarCadastro(self, nome, endereco, telefone, cpf):
        cliente = ClienteMd(nome, endereco, telefone, cpf)
        ClienteCt.cdao.inserirCliente(cliente)
        
    def enviarAlteracao(self, cpf, nome, endereco, telefone):
        cliente = ClienteMd(nome, endereco, telefone, cpf)
        ClienteCt.cdao.alterarCliente(cliente)
        
    def enviarConsulta(self, cpf):
        consultado = ClienteCt.cdao.consultarCliente(cpf)
        return consultado
        
    def deletarCliente(self, cpf):
        ClienteCt.cdao.deletarCliente(cpf)
        
    def enviarLista(self):
        lista = ClienteCt.cdao.listarClientes()
        return lista
   
    def getBanco(self):
        return ClienteCt.banco
        


"""
PRÓXIMOS PASSOS:
-VALIDAÇÃO NO FORMULÁRIO DO TKINTER
-SPRINT 2 E 3
-VALIDAÇÃO DE DADOS EM GERAL
"""