from funcionario import Funcionario

class Diretor(Funcionario):

    @property
    def bonificacao(self):
        return 100_000.0

    @property
    def cargo(self):
        return 'DIRETOR'