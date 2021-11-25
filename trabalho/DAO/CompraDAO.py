import MySQLdb
from DAO.InicioDAO import BancoDb

class CompraDb(BancoDb):

    def __init__(self):
        pass
    
    def cadastraCompra(self, compra):
        dados = (compra.getCodigo(), compra.getCpfCliente(), compra.getMatriculaFuncionario())
        db = MySQLdb.connect(self.banco_host, self.banco_username, self.banco_password, self.banco_nome)
        cursor = db.cursor()
        sql = "INSERT INTO compra_tbl (compra_codigo, cliente_cpf, funcionario_matricula) VALUES (%s, %s, %s)"
        cursor.execute(sql, dados)
        db.commit()
        db.close()
            
    def cadastraItens(self, matricula, cpf, codigoCompra, codigoProduto, qtdProduto):
        dados = (matricula, cpf, codigoCompra, codigoProduto, qtdProduto)
        db = MySQLdb.connect(self.banco_host, self.banco_username, self.banco_password, self.banco_nome)
        cursor = db.cursor()
        sql = "INSERT INTO compra_produto_tbl (`funcionario_matricula`, `cliente_cpf`, `compra_codigo`, `produto_codigo`, `qtd_itens`) VALUES (%s, %s, %s, %s, %s);"
        cursor.execute(sql, dados)
        db.commit()
        db.close()
          
            
    def alterarCompra(self, compra, codigoProduto, qtdItens):#PEGANDO INPUT DO FORM
        if self.verificaExistencia(compra.getCodigo()):
            dados = (compra.getMatriculaFuncionario(), compra.getCpfCliente(), compra.getCodigo(), compra.getMatriculaFuncionario(), compra.getCpfCliente(), codigoProduto, qtdItens, compra.getCodigo())
            db = MySQLdb.connect(self.banco_host, self.banco_username, self.banco_password, self.banco_nome)
            cursor = db.cursor()
            sql = """UPDATE compra_tbl SET funcionario_matricula = %s, cliente_cpf = %s WHERE compra_codigo = %s;
                     UPDATE compra_produto_tbl SET funcionario_matricula = %s, cliente_cpf = %s, produto_codigo = %s, qtd_itens = %s WHERE compra_codigo = %s;"""
            cursor.execute(sql, dados)
            db.commit()
            db.close()
        else:
            print("Nao existe nenhuma compra com o codigo informado")
            
    def consultarProduto(self, codigo): #CONSULTA PEGANDO INPUT DO FORM
        db = MySQLdb.connect(self.banco_host, self.banco_username, self.banco_password, self.banco_nome)
        cursor = db.cursor()
        sql = "SELECT * FROM produto_tbl WHERE produto_codigo = %s;"%(codigo)
        cursor.execute(sql)
        result = cursor.fetchone()
        if len(result) == 0:
            print("Nenhum produto cadastrado com o codigo informado.")
        db.close()
        result_format = f"""Codigo: {result[0]}   Descricao: {result[1]}   Valor: {result[2]}   Qtd Estoque: {result[3]}   Estoque Minimo: {result[4]}   Validade: {result[5]}"""
        return result_format
            
        
    def deletarProduto(self, codigo):#FUNCIONANDO
        if self.verificaExistencia(codigo):
            db = MySQLdb.connect(self.banco_host, self.banco_username, self.banco_password, self.banco_nome)
            cursor = db.cursor()
            sql = """DELETE FROM produto_tbl WHERE produto_codigo = %s;"""%(codigo)
            cursor.execute(sql)
            db.commit()
            db.close()
        else:
            print("N�o existe nenhum produto com o codigo informado")
        
    def listarProdutos(self): #FUNCIONANDO, PRINTA CADA UM LINHA POR LINHA NUMA LISTBOX
        db = MySQLdb.connect(self.banco_host, self.banco_username, self.banco_password, self.banco_nome)
        cursor = db.cursor()
        sql = "SELECT * FROM produto_tbl;"
        cursor.execute(sql)
        result = cursor.fetchall()
        if len(result) == 0:
            print("Nenhum produto foi cadastrado ainda.")
        db.close()
        lista_format = []
        for tupla in result:
            lista_format.append(f"""Codigo: {tupla[0]}   Descricao: {tupla[1]}   Valor: {tupla[2]}   Qtd Estoque: {tupla[3]}   Estoque Minimo: {tupla[4]}   Validade: {tupla[5]}""")
        return lista_format
    
    def verificaExistencia(self, codigo):
        db = MySQLdb.connect(self.banco_host, self.banco_username, self.banco_password, self.banco_nome)
        cursor = db.cursor()
        sql = "SELECT * FROM produto_tbl WHERE produto_codigo = %s;"%(codigo)
        cursor.execute(sql)
        result = cursor.fetchall()
        if len(result) == 0:
            db.close()
            return False
        else:
            db.close()
            return True
        