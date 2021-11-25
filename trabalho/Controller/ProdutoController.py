from Controller.InicioController import InicioCt
from DAO.InicioDAO import BancoDb
from DAO.ProdutoDAO import ProdutoDb
from Model.ProdutoModel import ProdutoMd


class ProdutoCt(InicioCt):
    banco = BancoDb()
    pdao = ProdutoDb()
    

    def __init__(self):
        pass
    
    def enviarCadastro(self, codigo, descricao, valor, qtdEstoque, estoqueMinimo, validade):
        produto = ProdutoMd(codigo, descricao, valor, qtdEstoque, estoqueMinimo, validade)
        ProdutoCt.pdao.inserirProduto(produto)
                
    def enviarAlteracao(self, codigo, descricao, valor, qtdEstoque, estoqueMinimo, validade):
        produto = ProdutoMd(codigo, descricao, valor, qtdEstoque, estoqueMinimo, validade)
        ProdutoCt.pdao.alterarProduto(produto)
        
    def enviarConsulta(self, codigo):
        consultado = ProdutoCt.pdao.consultarProduto(codigo)
        return consultado
        
    def deletarProduto(self, codigo):
        ProdutoCt.pdao.deletarProduto(codigo)
        
    def enviarLista(self):
        lista = ProdutoCt.pdao.listarProdutos()
        return lista