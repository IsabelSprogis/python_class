import abc

#Superclasse, classe mãe

# sOlid: Open-Close Principle -> uma classe deve estar fechada para
#                                alteração, e aberta para extensão
class Funcionario(abc.ABC): # Não pode ser instanciada

    __slots__ = ['_nome', '_salario']

    def __init__(self, nome, salario):
        self._nome = nome
        self._salario = salario


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, salario):
        self._salario = salario

    @property
    def bonificacao(self):
        return self.salario * 0.1

    def __str__(self):
        return f'{self.nome} ({self.cargo}) recebe {self.salario}: bonificação é {self.bonificacao}'

    @property
    @abc.abstractmethod
    def cargo(self):
        pass
