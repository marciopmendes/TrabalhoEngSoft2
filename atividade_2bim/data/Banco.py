import MySQLdb

class Banco:
    def __init__(self):#CONSTRUTOR
        pass
    

    def criaBanco(self):
    #CRIAR O BANCO
        db = MySQLdb.connect("localhost", "root", "rkv83wwv") #host, user, senha
        cursor = db.cursor()
        cursor.execute("CREATE DATABASE BANCO") #nome do banco vai ser BANCO
        db.close()


    def criaTabelas(self):
        #CRIAR TABELA CLIENTE
        db = MySQLdb.connect("localhost", "root", "rkv83wwv", "BANCO")
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
        #------------ADICIONAR AS OUTRAS CRIAÇÕES DE TABELAS AQUI, A MEDIDA QUE FOR NECESSÁRIO--------------
        

    def inserirCliente(self): #FUNCIONANDO, O CPF É A PK
        nome = input('Digite o nome do cliente:')
        endereco = input('Digite o endereco do cliente:')
        telefone = input('Digite o telefone do cliente:')
        cpf = input('Digite o Cpf do cliente:')
        dados = (nome, endereco, telefone, cpf)
        #INSERIR UM CLIENTE NO BANCO
        db = MySQLdb.connect("localhost", "root", "rkv83wwv", "BANCO")
        cursor = db.cursor()
        sql = "INSERT INTO cliente_tbl (cliente_nome,cliente_endereco,cliente_telefone,cliente_cpf) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, dados)
        db.commit()
        db.close()
        print("O cliente foi inserido com sucesso.")


    def consultarCliente(self): #FUNCIONANDO, A BUSCA É PELO CPF
        cpf = input("Para consultar os dados de um cliente, digite o cpf: ")
        db = MySQLdb.connect("localhost", "root", "rkv83wwv", "BANCO")
        cursor = db.cursor()
        sql = "SELECT * FROM cliente_tbl WHERE cliente_cpf = %s;"%(cpf)
        cursor.execute(sql)
        result = cursor.fetchall()
        if len(result) == 0:
            print("Nenhum cliente cadastrado com o CPF informado.")
        else:
            for record in result:
                print(record)
        db.close()


    def alterarCliente(self):#FUNCIONANDO
        cpf = input("Para alterar os dados de um cliente, digite o cpf: ")
        if self.verificaExistencia(cpf):
            nome = input('Digite o nome do cliente:')
            endereco = input('Digite o endereco do cliente:')
            telefone = input('Digite o telefone do cliente:')#nao altera o cpf pq nao faz sentido
            dados = (nome, endereco, telefone, cpf)
            db = MySQLdb.connect("localhost", "root", "rkv83wwv", "BANCO")
            cursor = db.cursor()
            sql = """UPDATE cliente_tbl SET cliente_nome = %s, cliente_endereco = %s, 
            cliente_telefone = %s WHERE cliente_cpf = %s;"""
            cursor.execute(sql, dados)
            db.commit()
            db.close()
            print("Os dados do cliente foram atualizados")
        else:
            print("Não existe nenhum cliente com o CPF informado")
        

    def removerCliente(self):#FUNCIONANDO
        cpf = input("Para remover um cliente, digite o cpf: ")
        if self.verificaExistencia(cpf):
            db = MySQLdb.connect("localhost", "root", "rkv83wwv", "BANCO")
            cursor = db.cursor()
            sql = """DELETE FROM cliente_tbl WHERE cliente_cpf = %s;"""%(cpf)
            cursor.execute(sql)
            db.commit()
            db.close()
            print("Cliente removido com sucesso.")
        else:
            print("Não existe nenhum cliente com o CPF informado")
        

    def listarClientes(self): #FUNCIONANDO, PRINTA CADA UM LINHA POR LINHA
        db = MySQLdb.connect("localhost", "root", "rkv83wwv", "BANCO")
        cursor = db.cursor()
        sql = "SELECT * FROM cliente_tbl;"
        cursor.execute(sql)
        result = cursor.fetchall()
        if len(result) == 0:
            print("Nenhum cliente foi cadastrado ainda.")
        else:
            for record in result:
                print(record)
        db.close()


    def verificaExistencia(self, cpf):
        db = MySQLdb.connect("localhost", "root", "rkv83wwv", "BANCO")
        cursor = db.cursor()
        sql = "SELECT * FROM cliente_tbl WHERE cliente_cpf = %s;"%(cpf)
        cursor.execute(sql)
        result = cursor.fetchall()
        if len(result) == 0:
            db.close()
            return False
        else:
            db.close()
            return True