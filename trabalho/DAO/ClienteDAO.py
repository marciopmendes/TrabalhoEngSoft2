import MySQLdb
from DAO.BancoDAO import BancoDb


class ClienteDb(BancoDb):
   
    def __init__(self):
        pass
    
    def inserirCliente(self, cliente):#PEGANDO INPUT DO FORM
        if (cliente.getNome() == "" or cliente.getEndereco() == "" or cliente.getTelefone() == "" or cliente.getCpf() == ""):#nao aceita campo nulo
            raise "All fields must be entered"
        else:
            dados = (cliente.getNome(), cliente.getEndereco(), cliente.getTelefone(), cliente.getCpf())
            db = MySQLdb.connect(self.banco_host, self.banco_username, self.banco_password, self.banco_nome)
            cursor = db.cursor()
            sql = "INSERT INTO cliente_tbl (cliente_nome,cliente_endereco,cliente_telefone,cliente_cpf) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, dados)
            db.commit()
            db.close()    
            
    def alterarCliente(self, cliente):#PEGANDO INPUT DO FORM
        if (cliente.getNome() == "" or cliente.getEndereco() == "" or cliente.getTelefone() == ""):#nao aceita campo nulo
            raise "All fields must be entered"
        if self.verificaExistencia(cliente.getCpf()):
            dados = (cliente.getNome(), cliente.getEndereco(), cliente.getTelefone(), cliente.getCpf())
            db = MySQLdb.connect(self.banco_host, self.banco_username, self.banco_password, self.banco_nome)
            cursor = db.cursor()
            sql = """UPDATE cliente_tbl SET cliente_nome = %s, cliente_endereco = %s, 
            cliente_telefone = %s WHERE cliente_cpf = %s;"""
            cursor.execute(sql, dados)
            db.commit()
            db.close()
        else:
            print("Não existe nenhum cliente com o CPF informado")
            
    def consultarCliente(self, cpf): #CONSULTA PEGANDO INPUT DO FORM
        db = MySQLdb.connect(self.banco_host, self.banco_username, self.banco_password, self.banco_nome)
        cursor = db.cursor()
        sql = "SELECT * FROM cliente_tbl WHERE cliente_cpf = %s;"%(cpf)
        cursor.execute(sql)
        result = cursor.fetchone()
        if len(result) == 0:
            print("Nenhum cliente cadastrado com o CPF informado.")
        db.close()
        result_format = f"""NOME: {result[0]}   ENDERECO: {result[1]}   TELEFONE: {result[2]}   CPF: {result[3]}"""
        return result_format
            
        
    def deletarCliente(self, cpf):#FUNCIONANDO
        if self.verificaExistencia(cpf):
            db = MySQLdb.connect(self.banco_host, self.banco_username, self.banco_password, self.banco_nome)
            cursor = db.cursor()
            sql = """DELETE FROM cliente_tbl WHERE cliente_cpf = %s;"""%(cpf)
            cursor.execute(sql)
            db.commit()
            db.close()
        else:
            print("N�o existe nenhum cliente com o CPF informado")
        
    def listarClientes(self): #FUNCIONANDO, PRINTA CADA UM LINHA POR LINHA NUMA LISTBOX
        db = MySQLdb.connect(self.banco_host, self.banco_username, self.banco_password, self.banco_nome)
        cursor = db.cursor()
        sql = "SELECT * FROM cliente_tbl;"
        cursor.execute(sql)
        result = cursor.fetchall()
        if len(result) == 0:
            print("Nenhum cliente foi cadastrado ainda.")
        db.close()
        lista_format = []
        for tupla in result:
            lista_format.append(f"""NOME: {tupla[0]}   ENDERE�O: {tupla[1]}   TELEFONE: {tupla[2]}   CPF: {tupla[3]}""")
        return lista_format

    def verificaExistencia(self, cpf):
        db = MySQLdb.connect(self.banco_host, self.banco_username, self.banco_password, self.banco_nome)
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