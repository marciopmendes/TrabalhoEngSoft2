from DAO.InicioDAO import BancoDb


class InicioCt:
    

    def __init__(self):
        pass
        
    def setBanco(self, host, username, password, nome):
        BancoDb.setBanco(BancoDb, host, username, password, nome)
        
        
