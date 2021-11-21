from Model.ClienteModel import ClienteMd
from View.ClienteView import ClienteVw
from DAO.BancoDAO import BancoDb
from DAO.ClienteDAO import ClienteDb

class ClienteCt:
    
    banco = BancoDb()
    cdao = ClienteDb()
    
    def __init__(self):
        self.view = ClienteVw(self)

    def main(self):
        self.view.main()
        
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

    def setBanco(self, host, username, password, nome):
        self.cdao.setBanco(host, username, password, nome)
        
    def getBanco(self):
        return ClienteCt.banco
        
app = ClienteCt()
app.main()