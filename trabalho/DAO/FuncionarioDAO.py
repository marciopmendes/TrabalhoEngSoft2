from DAO.InicioDAO import BancoDb
import MySQLdb

class FuncionarioDb(BancoDb):
    

    def __init__(self):
        pass
        
    def inserirFuncionario(self, funcionario):
        if (funcionario.getNome() == "" or funcionario.getEndereco() == "" or funcionario.getTelefone() == "" or funcionario.getCpf() == "" or funcionario.getMatricula() == "" or funcionario.getSalarioBase() == ""):#nao aceita campo nulo
            raise "All fields must be entered"
        else:
            dados = (funcionario.getNome(), funcionario.getEndereco(), funcionario.getTelefone(), funcionario.getCpf(), funcionario.getMatricula(), funcionario.getSalarioBase())
            db = MySQLdb.connect(self.banco_host, self.banco_username, self.banco_password, self.banco_nome)
            cursor = db.cursor()
            sql = "INSERT INTO funcionario_tbl (funcionario_nome,funcionario_endereco,funcionario_telefone,funcionario_cpf, funcionario_matricula, funcionario_salarioBase) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, dados)
            db.commit()
            db.close()    
            
    def alterarFuncionario(self, funcionario):
        if (funcionario.getNome() == "" or funcionario.getEndereco() == "" or funcionario.getTelefone() == "" or funcionario.getCpf() == "" or funcionario.getSalarioBase() == ""):#nao aceita campo nulo
            raise "All fields must be entered"
        if self.verificaExistencia(funcionario.getMatricula()):
            dados = (funcionario.getNome(), funcionario.getEndereco(), funcionario.getTelefone(), funcionario.getCpf(), funcionario.getSalarioBase(), funcionario.getMatricula())
            db = MySQLdb.connect(self.banco_host, self.banco_username, self.banco_password, self.banco_nome)
            cursor = db.cursor()
            sql = """UPDATE funcionario_tbl SET funcionario_nome = %s, funcionario_endereco = %s, 
            funcionario_telefone = %s, funcionario_cpf = %s, funcionario_salarioBase = %s WHERE funcionario_matricula = %s;"""
            cursor.execute(sql, dados)
            db.commit()
            db.close()
        else:
            print("Não existe nenhum funcionario com a matricula informada.")
            
    def consultarFuncionario(self, matricula):
        db = MySQLdb.connect(self.banco_host, self.banco_username, self.banco_password, self.banco_nome)
        cursor = db.cursor()
        sql = "SELECT * FROM funcionario_tbl WHERE funcionario_matricula = %s;"%(matricula)
        cursor.execute(sql)
        result = cursor.fetchone()
        if len(result) == 0:
            print("Nenhum funcionario cadastrado com a matricula informada.")
        db.close()
        result_format = f"""NOME: {result[0]}   ENDERECO: {result[1]}   TELEFONE: {result[2]}   CPF: {result[3]}   Salario Base: {result[5]}"""
        return result_format
            
        
    def deletarFuncionario(self, matricula):
        if self.verificaExistencia(matricula):
            db = MySQLdb.connect(self.banco_host, self.banco_username, self.banco_password, self.banco_nome)
            cursor = db.cursor()
            sql = """DELETE FROM funcionario_tbl WHERE funcionario_matricula = %s;"""%(matricula)
            cursor.execute(sql)
            db.commit()
        else:
            print("Nao existe nenhum funcionario com a matricula informada")
        db.close()
        
    def salarioFuncionario(self, matricula):
        db = MySQLdb.connect(self.banco_host, self.banco_username, self.banco_password, self.banco_nome)
        cursor = db.cursor()
        sql = f"""select cpt.funcionario_matricula, pt.produto_valor, cpt.qtd_itens
                 from compra_produto_tbl as cpt inner join produto_tbl as pt
                 on pt.produto_codigo = cpt.produto_codigo
                 where cpt.funcionario_matricula = {matricula}"""
        cursor.execute(sql)
        result = cursor.fetchall()
        vendaTotal = 0
        for linha in result:
            vendaTotal += linha[1]*linha[2]
        sql = f"""select funcionario_salarioBase
                  from funcionario_tbl
                  where funcionario_matricula = {matricula};""" 
        cursor.execute(sql)
        salarioBase = cursor.fetchone()
        if vendaTotal < 10000:
            salarioFinal = salarioBase[0]*1.05
        else:
            salarioFinal = salarioBase[0]*1.07
        sql = f"UPDATE funcionario_tbl SET funcionario_salarioFinal = {salarioFinal} WHERE funcionario_matricula = {matricula};"
        cursor.execute(sql)      
        db.commit()
        db.close()
            
    def listarFuncionarios(self):
        db = MySQLdb.connect(self.banco_host, self.banco_username, self.banco_password, self.banco_nome)
        cursor = db.cursor()
        sql = "SELECT * FROM funcionario_tbl;"
        cursor.execute(sql)
        result = cursor.fetchall()
        if len(result) == 0:
            print("Nenhum funcionario foi cadastrado ainda.")
        db.close()
        lista_format = []
        for tupla in result:
            lista_format.append(f"""NOME: {tupla[0]}   ENDERECO: {tupla[1]}   TELEFONE: {tupla[2]}   CPF: {tupla[3]}   Matricula: {tupla[4]}   Salario Base: {tupla[5]}""")
        return lista_format

    def verificaExistencia(self, matricula):
        db = MySQLdb.connect(self.banco_host, self.banco_username, self.banco_password, self.banco_nome)
        cursor = db.cursor()
        sql = "SELECT * FROM funcionario_tbl WHERE funcionario_matricula = %s;"%(matricula)
        cursor.execute(sql)
        result = cursor.fetchall()
        if len(result) == 0:
            db.close()
            return False
        else:
            db.close()
            return True