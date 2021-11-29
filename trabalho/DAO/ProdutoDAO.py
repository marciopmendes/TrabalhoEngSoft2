import MySQLdb
from DAO.InicioDAO import BancoDb

class ProdutoDb(BancoDb):

    def __init__(self):
        pass
    
    def inserirProduto(self, produto):
        if (produto.getCodigo() == "" or produto.getDescricao() == "" or produto.getValor() == "" or produto.getQtdEstoque() == "" or produto.getEstoqueMinimo() == "" or produto.getValidade() == ""):#nao aceita campo nulo
            raise "All fields must be entered"
        else:
            dados = (produto.getCodigo(), produto.getDescricao(), produto.getValor(), produto.getQtdEstoque(), produto.getEstoqueMinimo(), produto.getValidade())
            db = MySQLdb.connect(self.banco_host, self.banco_username, self.banco_password, self.banco_nome)
            cursor = db.cursor()
            sql = "INSERT INTO produto_tbl (produto_codigo, produto_descricao, produto_valor, produto_qtdEstoque, produto_estoqueMinimo, produto_validade) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, dados)
            db.commit()
            db.close()    
            
    def alterarProduto(self, produto):
        if (produto.getDescricao() == "" or produto.getValor() == "" or produto.getQtdEstoque() == "" or produto.getEstoqueMinimo() == "" or produto.getValidade() == ""):#nao aceita campo nulo
            raise "All fields must be entered"
        dados = (produto.getDescricao(), produto.getValor(), produto.getQtdEstoque(), produto.getEstoqueMinimo(), produto.getValidade(), produto.getCodigo())
        db = MySQLdb.connect(self.banco_host, self.banco_username, self.banco_password, self.banco_nome)
        cursor = db.cursor()
        sql = """UPDATE produto_tbl SET produto_descricao = %s, produto_valor = %s, produto_qtdEstoque = %s, produto_estoqueMinimo = %s, produto_validade = %s WHERE produto_codigo = %s;"""
        cursor.execute(sql, dados)
        db.commit()
        db.close()
            
    def consultarProduto(self, codigo):
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
            
        
    def deletarProduto(self, codigo):
        if self.verificaExistencia(codigo):
            db = MySQLdb.connect(self.banco_host, self.banco_username, self.banco_password, self.banco_nome)
            cursor = db.cursor()
            sql = f"select produto_tbl.produto_codigo from produto_tbl inner join compra_produto_tbl on produto_tbl.produto_codigo = compra_produto_tbl.produto_codigo where produto_tbl.produto_codigo = {codigo}"
            cursor.execute(sql)
            result = cursor.fetchall()
            if len(result) == 0:
                sql = """DELETE FROM produto_tbl WHERE produto_codigo = %s;"""%(codigo)
                cursor.execute(sql)
                db.commit()
            else:
                print("Existem compras cadastradas relacionadas a esse produto. Impossível excluir.")
        else:
            print("Nao existe nenhum produto com o codigo informado")
        db.close()
        
    def listarProdutos(self):
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
        