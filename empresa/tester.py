from funcionario import Funcionario

class Tester(Funcionario):

    @property
    def bonificacao(self):  # SOBRESCRITA
        """Método sobrescrito que altera a regra padrão
        de bonificação
        """
        return self.salario * 0.25

    @property
    def cargo(self):
        return 'TESTER'