from funcionario import Funcionario

class Gerente(Funcionario):

    def __init__(self, nome, salario, quantidade_de_funcionarios):
        super().__init__(nome, salario)
        self._quantidade_de_funcionarios = quantidade_de_funcionarios

    @property
    def cargo(self):
        return 'GERENTE'