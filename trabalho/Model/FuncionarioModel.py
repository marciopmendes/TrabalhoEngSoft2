
class FuncionarioMd:

    def __init__(self, nome, endereco, telefone, cpf, matricula, salarioBase):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.cpf = cpf
        self.matricula = matricula
        self.salarioBase = salarioBase
        
    def setNome(self, nome):
        self.nome = nome

    def setEndereco(self, endereco):
        self.endereco = endereco

    def setTelefone(self, telefone):
        self.telefone = telefone

    def setCpf(self, cpf):
        self.cpf = cpf

    def getNome(self):
        return self.nome

    def getEndereco(self):
        return self.endereco

    def getTelefone(self):
        return self.telefone

    def getCpf(self):
        return self.cpf
    
    def setMatricula(self, matricula):
        self.matricula = matricula

    def getMatricula(self):
        return self.matricula
    
    def setSalarioBase(self, salarioBase):
        self.salarioBase = salarioBase
        
    def getSalarioBase(self):
        return self.salarioBase
    
    def executarCadastro(self, nome, endereco, telefone, cpf, matricula, salarioBase):
        funcionario = FuncionarioMd(nome, endereco, telefone, cpf, matricula, salarioBase)
        return funcionario