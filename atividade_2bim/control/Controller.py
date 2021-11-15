import sys
sys.path.append(r"c:\Users\Marcio Mendes\Desktop\SI\4 periodo\Eng Soft 2\atividade_2bim\\")

from model.Model import *
from data.Banco import *
from view.View import *

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)
        self.data = Banco()

    def main(self):
        self.view.main()
        
#DESCOMENTAR ESSA PARTE PARA FUNCIONAR PELO TERMINAL       
#   def clickButton(self, botao):
#        self.model.executarFuncao(botao)

    def clickCadastrar(self):
        self.view.clienteForm()
        
    def clickConsultar(self):
        self.view.consultaForm()
        
    def enviarCadastro(self, nome, endereco, telefone, cpf):
        self.model.executarCadastro(nome, endereco, telefone, cpf)
        
    def enviarConsulta(self, cpf):
        self.model.executarConsulta(cpf)

        
        
app = Controller()
app.main()


"""PRÓXIMOS PASSOS:
-EXIBIR OS DADOS DA CONSULTA EM UMA JANELA SEPARADA (USANDO TEXT WIDGET)
-CRIAR FUNCIONALIDADE DE ALTERAR CLIENTE
-CRIAR FUNCIONALIDADE DE LISTAR TODOS OS CLIENTES
-CRIAR FUNCIONALIDADE DE DELETAR CLIENTE
-VER SE DA PRA INSERIR PLACEHOLDERS"""