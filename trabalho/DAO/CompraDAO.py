import MySQLdb
from DAO.InicioDAO import BancoDb
import time

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
        dataCompra = time.strftime('%Y-%m-%d', time.localtime())
        dados = (matricula, cpf, codigoCompra, codigoProduto, qtdProduto, dataCompra)
        db = MySQLdb.connect(self.banco_host, self.banco_username, self.banco_password, self.banco_nome)
        cursor = db.cursor()
        sql = "INSERT INTO compra_produto_tbl (`funcionario_matricula`, `cliente_cpf`, `compra_codigo`, `produto_codigo`, `qtd_itens`, compra_data) VALUES (%s, %s, %s, %s, %s, %s);"
        cursor.execute(sql, dados)
        db.commit()
        db.close()
    
    def valorCompra(self, codigo):
        valor = 0
        db = MySQLdb.connect(self.banco_host, self.banco_username, self.banco_password, self.banco_nome)
        cursor = db.cursor()
        sql = f"""select cpt.compra_codigo, cpt.produto_codigo, cpt.qtd_itens, p.produto_valor
                  from compra_produto_tbl as cpt
                  inner join produto_tbl as p
                  on cpt.produto_codigo = p.produto_codigo
                  where compra_codigo = {codigo}"""
        cursor.execute(sql)
        result = cursor.fetchall()
        for linha in result:
            valor += linha[2]*linha[3]
        sql = f"update compra_tbl SET compra_valor = {valor} where compra_codigo = {codigo};"
        cursor.execute(sql)
        db.commit()
        db.close()
            
    def alterarCompra(self, codigoCompra, matricula, cpf):
        if self.verificaExistencia(codigoCompra):
            dados = (matricula, cpf, codigoCompra)
            db = MySQLdb.connect(self.banco_host, self.banco_username, self.banco_password, self.banco_nome)
            cursor = db.cursor()
            sql = "UPDATE compra_tbl SET funcionario_matricula = %s, cliente_cpf = %s WHERE compra_codigo = %s;"
            cursor.execute(sql, dados)
            db.commit()
        else:
            print("Nao existe nenhuma compra com o codigo informado")
        db.close()
            
            
    def alterarItens(self, matricula, cpf, codigoProduto, quantidade, codigoCompra):
        if self.verificaExistencia(codigoCompra):
            dados = (matricula, cpf, codigoProduto, quantidade, codigoCompra, matricula, cpf, codigoProduto)
            db = MySQLdb.connect(self.banco_host, self.banco_username, self.banco_password, self.banco_nome)
            cursor = db.cursor()
            sql = "UPDATE compra_produto_tbl SET funcionario_matricula = %s, cliente_cpf = %s, produto_codigo = %s, qtd_itens = %s WHERE (compra_codigo = %s AND funcionario_matricula = %s AND cliente_cpf = %s AND produto_codigo = %s);"
            cursor.execute(sql, dados)
            db.commit()
        else:
            print("Nao existe nenhuma compra com o codigo informado")
        db.close()
            
    def consultarCompra(self, codigo):#FORMATAR MELHOR O RESULTADO SE DER TEMPO -------------------
        db = MySQLdb.connect(self.banco_host, self.banco_username, self.banco_password, self.banco_nome)
        cursor = db.cursor()
        sql = "SELECT * FROM compra_produto_tbl WHERE compra_codigo = %s;"%(codigo)
        cursor.execute(sql)
        result = cursor.fetchall()
        if len(result) == 0:
            print("Nenhuma compra cadastrada com o codigo informado.")
        db.close()
        result_format = []
        for tupla in result:
            result_format.append(f"CPF do Cliente: {tupla[1]}   Vendedor: {tupla[2]}   Produto: {tupla[3]}   Quantidade: {tupla[4]}")
        return result_format
            
        
    def deletarCompra(self, codigo):
        if self.verificaExistencia(codigo):
            db = MySQLdb.connect(self.banco_host, self.banco_username, self.banco_password, self.banco_nome)
            cursor = db.cursor()
            sql = "DELETE FROM compra_produto_tbl WHERE compra_codigo = %s;"%(codigo)
            cursor.execute(sql)
            sql = "DELETE FROM compra_tbl WHERE compra_codigo = %s;"%(codigo)
            cursor.execute(sql)
            db.commit()
        else:
            print("Nao existe nenhuma compra com o codigo informado")
        db.close()
        
    def listarCompras(self):
        db = MySQLdb.connect(self.banco_host, self.banco_username, self.banco_password, self.banco_nome)
        cursor = db.cursor()
        sql = "SELECT * FROM compra_produto_tbl;"
        cursor.execute(sql)
        result = cursor.fetchall()
        if len(result) == 0:
            print("Nenhuma compra foi cadastrado ainda.")
        db.close()
        lista_format = []
        for tupla in result:
            lista_format.append(f"Código da Compra: {tupla[0]}   CPF do Cliente: {tupla[1]}   Vendedor: {tupla[2]}   Produto: {tupla[3]}   Quantidade: {tupla[4]}")
        return lista_format
    
    def verificaExistencia(self, codigo):
        db = MySQLdb.connect(self.banco_host, self.banco_username, self.banco_password, self.banco_nome)
        cursor = db.cursor()
        sql = "SELECT * FROM compra_tbl WHERE compra_codigo = %s;"%(codigo)
        cursor.execute(sql)
        result = cursor.fetchall()
        if len(result) == 0:
            db.close()
            return False
        else:
            db.close()
            return True
        