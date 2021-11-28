

class CompraMd:
    
    produtos = []
    
    def __init__(self, codigo, cpfCliente, matriculaFuncionario):
        self.codigo = codigo
        self.cpfCliente = cpfCliente
        self.matriculaFuncionario = matriculaFuncionario
  
    def setCodigo(self, codigo):
        self.codigo = codigo
        
    def setCpfCliente(self, cpf):
        self.cpfCliente = cpf
        
    def setMatriculaFuncionario(self, matricula):
        self.matriculaFuncionario = matricula
        
    def getCodigo(self):
        return self.codigo
    
    def getCpfCliente(self):
        return self.cpfCliente
    
    def getMatriculaFuncionario(self):
        return self.matriculaFuncionario