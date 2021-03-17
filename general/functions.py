def velocidade_media(distancia, tempo):
    return distancia / tempo


def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def calculadora(a, b):
    return soma(a, b), subtracao(a, b)


def soma_variavel(*args):
    result = 0
    for i in args:
        result += i
    return result


def passa():
    pass


def valor_carro(preco, **kwargs):
    valor_final = preco
    if 'ipi' in kwargs:
        valor_final += preco * kwargs['ipi']
    if 'desconto' in kwargs:
        valor_final -= kwargs['desconto']
    return valor_final


print(velocidade_media(100, 20))
print(velocidade_media(150, 22))
print(velocidade_media(200, 30))
print(velocidade_media(50, 3))
print(soma(10, 2))
print(subtracao(10, 2))
print(calculadora(10, 2))
print(soma_variavel(1, 2, 3))
print(soma_variavel(10, 5))
print(soma_variavel(1, 4, 5, 7, 9))
print(valor_carro(50000, ipi=0.1, desconto=500))
print(valor_carro(50000, desconto=200))
print(valor_carro(50000, ipi=0.3))
