from funcionario import Funcionario

class Programador(Funcionario):

    @property
    def bonificacao(self): # SOBRESCRITA
        return self.salario * 0.2

    @property
    def cargo(self):
        return 'PROGRAMADOR'