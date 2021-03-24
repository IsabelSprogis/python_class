from analista import Analista
from gerente import Gerente
from programador import Programador
from tester import Tester
from diretor import Diretor
from funcionario import Funcionario
from calculador_de_bonificacao import CalculadorDeBonificacao


ana = Analista('ana', 6000.0)    # Analista -> 10%
bia = Gerente('bia', 12000.0, 20)   # Gerente -> 10%
caio = Programador('caio', 20000.0) # Programador -> 20%
ed = Tester('ed', 20000.0)
fab = Diretor('fab', 50000.0)

calculador = CalculadorDeBonificacao()
calculador.registra(ana)
calculador.registra(bia)
calculador.registra(caio)
calculador.registra(ed)
calculador.registra(fab)

#funcionarios = [ana, bia, caio, ed]
#for funcionario in funcionarios:
#    calculador.registra(funcionario)
#    print(f'{funcionario.nome} ({funcionario.cargo}) recebe {funcionario.salario}: bonificação é {funcionario.bonificacao}')


print(f'TOTAL DE BONIFICAÇÕES: {calculador.total}')

