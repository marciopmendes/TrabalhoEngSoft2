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

        