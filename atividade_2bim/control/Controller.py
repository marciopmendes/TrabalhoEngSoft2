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

    def clickAlterar(self):
        self.view.alterarForm()
        
    def clickDeletar(self):
        self.view.deletarForm()
    
    def clickCadastrar(self):
        self.view.clienteForm()
        
    def clickConsultar(self):
        self.view.consultaForm()
        
    def clickListar(self):
        self.view.listarTodos()
        
    def enviarCadastro(self, nome, endereco, telefone, cpf):
        self.model.executarCadastro(nome, endereco, telefone, cpf)
        
    def enviarAlteracao(self, cpf, nome, endereco, telefone):
        self.model.executarAlteracao(cpf, nome, endereco, telefone)
        
    def enviarConsulta(self, cpf):
        consultado = self.model.executarConsulta(cpf)
        return consultado
        
    def deletarCliente(self, cpf):
        self.model.deletarCliente(cpf)
        
    def enviarLista(self):
        lista = self.model.executarLista()
        return lista

      
app = Controller()
app.main()


"""PRÓXIMOS PASSOS:
-JANELA DE SUCESSO OU ERRO NAS OPERAÇÕES (EX. CONSULTAR, DELETAR...)
-VER SE DA PRA INSERIR PLACEHOLDERS"""