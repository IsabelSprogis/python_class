from funcionario import Funcionario

# Subclasse
class Analista(Funcionario):

    @property
    def cargo(self):
        return 'ANALISTA'
