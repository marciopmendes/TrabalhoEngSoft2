import MySQLdb
from DAO.InicioDAO import BancoDb

class RelatorioDb(BancoDb):

    def __init__(self):
        pass
    
    def clienteCompra(self):
        db = MySQLdb.connect(self.banco_host, self.banco_username, self.banco_password, self.banco_nome)
        cursor = db.cursor()
        sql = """select distinct cliente_nome from cliente_tbl as cli
                 inner join compra_tbl as c
                 on cli.cliente_cpf = c.cliente_cpf"""
        cursor.execute(sql)
        result = cursor.fetchall()
        db.close()
        return result
    
    def estoqueMinimo(self):
        db = MySQLdb.connect(self.banco_host, self.banco_username, self.banco_password, self.banco_nome)
        cursor = db.cursor()
        sql = """select p.produto_descricao, p.produto_qtdEstoque, p.produto_estoqueMinimo
                 from produto_tbl as p
                 where p.produto_qtdEstoque < p.produto_estoqueMinimo"""
        cursor.execute(sql)
        result = cursor.fetchall()
        db.close()
        lista_format = []
        for tupla in result:
            lista_format.append(f"Descricao: {tupla[0]}   Qtd_Estoque: {tupla[1]}   Estoque Minimo: {tupla[2]}")
        return lista_format
    
    def compraPeriodo(self, anoInicial, anoFinal):
        db = MySQLdb.connect(self.banco_host, self.banco_username, self.banco_password, self.banco_nome)
        cursor = db.cursor()
        sql = f"""select distinct c.compra_codigo from compra_tbl as c
              inner join compra_produto_tbl as cpt
              on c.compra_codigo = cpt.compra_codigo
              where year(cpt.compra_data) >= {anoInicial} and year(cpt.compra_data) < {anoFinal}"""
        cursor.execute(sql)
        result = cursor.fetchall()
        db.close()
        lista_format = []
        if len(result) == 0:
            print("Nenhuma compra no periodo informado")
        else:
            for tupla in result:
                lista_format.append(f"Codigo da Compra: {tupla[0]}")
        return lista_format