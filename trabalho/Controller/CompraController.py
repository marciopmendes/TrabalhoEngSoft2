from Controller.InicioController import InicioCt
from Model.CompraModel import CompraMd
from DAO.InicioDAO import BancoDb
from DAO.CompraDAO import CompraDb

class CompraCt(InicioCt):
    banco = BancoDb()
    cdao = CompraDb()


    def __init__(self):
        pass
    
    def cadastraCompra(self, codigo, matricula, cpf):
        compra = CompraMd(codigo, cpf, matricula)
        CompraCt.cdao.cadastraCompra(compra)
        
    def cadastraItens(self, matricula, cpf, codigoCompra, codigoProduto, quantidade):
        CompraCt.cdao.cadastraItens(matricula, cpf, codigoCompra, codigoProduto, quantidade)
        
    def alterarCompra(self, codigoCompra, matricula, cpf):
        CompraCt.cdao.alterarCompra(codigoCompra, matricula, cpf)
        
    def alterarItens(self, matricula, cpf, codigoProduto, quantidade, codigoCompra):
        CompraCt.cdao.alterarItens(matricula, cpf, codigoProduto, quantidade, codigoCompra)
        
    def enviarConsulta(self, codigo):
        consultado = CompraCt.cdao.consultarCompra(codigo)
        return consultado
    
    def deletarCompra(self, codigo):
        CompraCt.cdao.deletarCompra(codigo)
    
    def enviarLista(self):
        lista = CompraCt.cdao.listarCompras()
        return lista