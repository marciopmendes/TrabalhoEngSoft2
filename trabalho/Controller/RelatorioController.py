from Controller.InicioController import InicioCt
from DAO.InicioDAO import BancoDb
from DAO.RelatorioDAO import RelatorioDb

class RelatorioCt(InicioCt):
    banco = BancoDb()
    rdao = RelatorioDb()
    

    def __init__(self):
        pass
    
    def clienteCompra(self):
        lista = RelatorioCt.rdao.clienteCompra()
        return lista
    
    def estoqueMinimo(self):
        lista = RelatorioCt.rdao.estoqueMinimo()
        return lista
    
    def compraPeriodo(self, anoInicial, anoFinal):
        consultado = RelatorioCt.rdao.compraPeriodo(anoInicial, anoFinal)
        return consultado