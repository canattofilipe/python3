from datetime import datetime


class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f'nome = {self.nome}, idade = {self.idade}'

    def isAdult(self):
        return True if self.idade > 18 else False


class Vendedor(Pessoa):

    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario


class Cliente(Pessoa):

    compras = []

    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def registra_compra(self, compra):
        self.compras.append(compra)

    def total_compras(self):
        return sum([c.valor for c in self.compras])

    def get_data_ultima_compra(self):
        return self.compras[-1].data.strftime('%d/%m/%Y')


class Compra:

    def __init__(self, vendedor, data, valor):
        self.vendedor = vendedor
        self.data = data
        self.valor = valor


def main():

    vendedor = Vendedor('João', 27, 1.500)
    cliente = Cliente('José', 30)
    cliente.registra_compra(Compra(vendedor, datetime.now(), 250.00))
    cliente.registra_compra(Compra(vendedor, datetime.now(), 100.00))
    cliente.registra_compra(Compra(vendedor, datetime.now(), 50.50))
    print(cliente.total_compras())
    print(cliente.get_data_ultima_compra())


if __name__ == '__main__':
    main()
