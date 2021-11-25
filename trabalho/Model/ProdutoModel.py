
class ProdutoMd:
    def __init__(self, codigo, descricao, valor, qtdEstoque, estoqueMinimo, validade):
        self.codigo = codigo
        self.descricao = descricao
        self.valor = valor
        self.qtdEstoque = qtdEstoque
        self.estoqueMinimo = estoqueMinimo
        self.validade = validade
        
    def setCodigo(self, codigo):
        self.codigo = codigo
    
    def setDescricao(self, descricao):
        self.descricao = descricao
        
    def setValor(self, valor):
        self.valor = valor
        
    def setQtdEstoque(self, qtdEstoque):
        self.qtdEstoque = qtdEstoque
        
    def setEstoqueMinimo(self, estoqueMinimo):
        self.estoqueMinimo = estoqueMinimo
        
    def setValidade(self, validade):
        self.validade = validade
        
    def getCodigo(self):
        return self.codigo
    
    def getDescricao(self):
        return self.descricao
    
    def getValor(self):
        return self.valor
    
    def getQtdEstoque(self):
        return self.qtdEstoque
    
    def getEstoqueMinimo(self):
        return self.estoqueMinimo
    
    def getValidade(self):
        return self.validade