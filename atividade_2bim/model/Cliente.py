class Cliente:
    def __init__(self, nome, endereco, telefone, cpf):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.cpf = cpf

    def setNome(self, nome):
        self.nome = nome

    def setEndereço(self, endereco):
        self.endereco = endereco

    def setTelefone(self, telefone):
        self.telefone = telefone

    def setCpf(self, cpf):
        self.cpf = cpf

    def getNome(self):
        return self.nome

    def getEndereço(self):
        return self.endereco

    def getTelefone(self):
        return self.telefone

    def getCpf(self):
        return self.cpf