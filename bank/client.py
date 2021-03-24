class Client:
    def __init__(self, cpf, name):
        self.cpf = cpf
        self.name = name

    def print_data(self):
        print(f'{self.name} {self.cpf}')