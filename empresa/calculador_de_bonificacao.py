from funcionario import Funcionario

class CalculadorDeBonificacao:

    def __init__(self):
        self._total = 0

    def registra(self, funcionario): # POLIMORFISMO, MAS no Python é Duck Type
        if hasattr(funcionario, 'bonificacao'):
            self._total += funcionario.bonificacao
            print(funcionario)
        else:
            print(f'Objeto da classe {funcionario.__class__.__name__} não é Funcionario')

    @property
    def total(self):
        return self._total
