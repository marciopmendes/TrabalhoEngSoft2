import MySQLdb

class BancoDb:
    
    banco_host = ""
    banco_username = ""
    banco_password = ""
    banco_nome = ""
    
    def __init__(self):
        pass

    def getHost(self):
        return self.banco_host
    
    def getUsername(self):
        return self.banco_username

    def getPassword(self):
        return self.banco_password

    def getNome(self):
        return self.banco_nome

    def setHost(self, host):
        self.banco_host = host
    
    def setUsername(self, username):
        self.banco_username = username

    def setPassword(self, password):
        self.banco_password = password

    def setNome(self, nome):
        self.banco_nome = nome 

    def criaBanco(self):
    #CRIAR O BANCO
        db = MySQLdb.connect(self.banco_host, self.banco_username, self.banco_password) #host, user, senha
        cursor = db.cursor()
        cursor.execute(f"CREATE DATABASE {self.banco_nome}") 
        db.close()

    def criaTabelas(self):
        #CRIAR TABELA CLIENTE
        db = MySQLdb.connect(self.banco_host, self.banco_username, self.banco_password, self.banco_nome)
        cursor = db.cursor()
        sql = """CREATE TABLE cliente_tbl(
                    cliente_nome VARCHAR(100) NOT NULL,
                    cliente_endereco VARCHAR(300) NOT NULL,
                    cliente_telefone VARCHAR(11) NOT NULL,
                    cliente_cpf VARCHAR(11) NOT NULL,
                    PRIMARY KEY (cliente_cpf));"""
        cursor.execute(sql)
        db.close()
        print("Tabela criada com sucesso.")
        #------------ADICIONAR AS OUTRAS CRIA��ES DE TABELAS AQUI, A MEDIDA QUE FOR NECESS�RIO--------------
        
    def setBanco(self, host, username, password, nome):#pega os dados do form na view para criar e conectar ao banco
        self.setHost(host)
        self.setUsername(username)
        self.setPassword(password)
        self.setNome(nome)
        self.criaBanco()
        self.criaTabelas()