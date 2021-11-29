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

        db = MySQLdb.connect(self.banco_host, self.banco_username, self.banco_password)
        cursor = db.cursor()
        cursor.execute(f"USE {self.banco_nome}")#MEXER NESSA PARTE PRA USAR O BANCO SE JÁ EXISTIR, SENAO, CRIAR
#        cursor.execute(f"CREATE DATABASE {self.banco_nome}") 
        db.close()

    def criaTabelas(self):
        db = MySQLdb.connect(self.banco_host, self.banco_username, self.banco_password, self.banco_nome)
        cursor = db.cursor()
        sql = f"""        -- Schema banco3
        -- -----------------------------------------------------
        CREATE SCHEMA IF NOT EXISTS `{self.banco_nome}` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
        USE `{self.banco_nome}` ;
        
        -- -----------------------------------------------------
        -- Table `{self.banco_nome}`.`cliente_tbl`
        -- -----------------------------------------------------
        CREATE TABLE IF NOT EXISTS `{self.banco_nome}`.`cliente_tbl` (
          `cliente_nome` VARCHAR(100) NOT NULL,
          `cliente_endereco` VARCHAR(300) NOT NULL,
          `cliente_telefone` VARCHAR(11) NOT NULL,
          `cliente_cpf` INT NOT NULL,
          PRIMARY KEY (`cliente_cpf`),
          UNIQUE INDEX `cliente_cpf_UNIQUE` (`cliente_cpf` ASC) VISIBLE)
        ENGINE = InnoDB
        DEFAULT CHARACTER SET = utf8mb4
        COLLATE = utf8mb4_0900_ai_ci;
        
        
        -- -----------------------------------------------------
        -- Table `{self.banco_nome}`.`funcionario_tbl`
        -- -----------------------------------------------------
        CREATE TABLE IF NOT EXISTS `{self.banco_nome}`.`funcionario_tbl` (
          `funcionario_nome` VARCHAR(100) NOT NULL,
          `funcionario_endereco` VARCHAR(300) NOT NULL,
          `funcionario_telefone` VARCHAR(11) NOT NULL,
          `funcionario_cpf` VARCHAR(11) NOT NULL,
          `funcionario_matricula` INT NOT NULL,
          `funcionario_salarioBase` FLOAT(8,2) NOT NULL,
          `funcionario_salarioFinal` FLOAT(8,2) NOT NULL DEFAULT 0,
          PRIMARY KEY (`funcionario_matricula`),
          UNIQUE INDEX `funcionario_matricula_UNIQUE` (`funcionario_matricula` ASC) VISIBLE)
        ENGINE = InnoDB
        DEFAULT CHARACTER SET = utf8mb4
        COLLATE = utf8mb4_0900_ai_ci;
        
        
        -- -----------------------------------------------------
        -- Table `{self.banco_nome}`.`produto_tbl`
        -- -----------------------------------------------------
        CREATE TABLE IF NOT EXISTS `{self.banco_nome}`.`produto_tbl` (
          `produto_codigo` INT NOT NULL,
          `produto_descricao` VARCHAR(300) NOT NULL,
          `produto_valor` FLOAT(8,2) NOT NULL,
          `produto_qtdEstoque` INT NOT NULL,
          `produto_estoqueMinimo` INT NOT NULL,
          `produto_validade` VARCHAR(10) NOT NULL,
          PRIMARY KEY (`produto_codigo`),
          UNIQUE INDEX `produto_codigo_UNIQUE` (`produto_codigo` ASC) VISIBLE)
        ENGINE = InnoDB
        DEFAULT CHARACTER SET = utf8mb4
        COLLATE = utf8mb4_0900_ai_ci;
        
        
        -- -----------------------------------------------------
        -- Table `{self.banco_nome}`.`compra_tbl`
        -- -----------------------------------------------------
        CREATE TABLE IF NOT EXISTS `{self.banco_nome}`.`Compra` (
          `compra_codigo` INT NOT NULL,
          `cliente_cpf` INT NOT NULL,
          `funcionario_matricula` INT NOT NULL,
          `compra_valor` FLOAT(10,2) NOT NULL DEFAULT 0,
          PRIMARY KEY (`compra_codigo`, `cliente_cpf`, `funcionario_matricula`),
          UNIQUE INDEX `codigo_UNIQUE` (`compra_codigo` ASC) VISIBLE,
          INDEX `fk_Compra_cliente_tbl_idx` (`cliente_cpf` ASC) VISIBLE,
          INDEX `fk_Compra_funcionario_tbl1_idx` (`funcionario_matricula` ASC) VISIBLE,
          CONSTRAINT `fk_Compra_cliente_tbl`
            FOREIGN KEY (`cliente_cpf`)
            REFERENCES `{self.banco_nome}`.`cliente_tbl` (`cliente_cpf`)
            ON DELETE NO ACTION
            ON UPDATE NO ACTION,
          CONSTRAINT `fk_Compra_funcionario_tbl1`
            FOREIGN KEY (`funcionario_matricula`)
            REFERENCES `{self.banco_nome}`.`funcionario_tbl` (`funcionario_matricula`)
            ON DELETE NO ACTION
            ON UPDATE NO ACTION)
        ENGINE = InnoDB;
        
        
        -- -----------------------------------------------------
        -- Table `{self.banco_nome}`.`compra_produto_tbl`
        -- -----------------------------------------------------
        CREATE TABLE IF NOT EXISTS `{self.banco_nome}`.`compra_produto_tbl` (
          `compra_codigo` INT NOT NULL,
          `cliente_cpf` INT NOT NULL,
          `funcionario_matricula` INT NOT NULL,
          `produto_codigo` INT NOT NULL,
          `qtd_itens` INT NOT NULL,
          `compra_data` DATE NOT NULL,
          PRIMARY KEY (`compra_codigo`, `cliente_cpf`, `funcionario_matricula`, `produto_codigo`),
          INDEX `fk_Compra_has_produto_tbl_produto_tbl1_idx` (`produto_codigo` ASC) VISIBLE,
          INDEX `fk_Compra_has_produto_tbl_Compra1_idx` (`compra_codigo` ASC, `cliente_cpf` ASC, `funcionario_matricula` ASC) VISIBLE,
          CONSTRAINT `fk_Compra_has_produto_tbl_Compra1`
            FOREIGN KEY (`compra_codigo` , `cliente_cpf` , `funcionario_matricula`)
            REFERENCES `{self.banco_nome}`.`compra_tbl` (`compra_codigo` , `cliente_cpf` , `funcionario_matricula`)
            ON DELETE NO ACTION
            ON UPDATE NO ACTION,
          CONSTRAINT `fk_Compra_has_produto_tbl_produto_tbl1`
            FOREIGN KEY (`produto_codigo`)
            REFERENCES `{self.banco_nome}`.`produto_tbl` (`produto_codigo`)
            ON DELETE NO ACTION
            ON UPDATE NO ACTION)
        ENGINE = InnoDB;
        
        
        SET SQL_MODE=@OLD_SQL_MODE;
        SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
        SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;"""

        cursor.execute(sql)
        db.close()

        
    def setBanco(self, host, username, password, nome):
        self.setHost(self, host)
        self.setUsername(self, username)
        self.setPassword(self, password)
        self.setNome(self, nome)
        self.criaBanco(self)#MEXER NESSA PARTE PRA CHECAR SE AS TABELAS EXISTEM
#        self.criaTabelas(self)
