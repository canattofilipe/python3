from .pessoa import Pessoa


def get_data(compra):
    return compra.data


class Cliente(Pessoa):

    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.compras = []

    def registra_compra(self, compra):
        self.compras.append(compra)

    def total_compras(self):
        return sum([c.valor for c in self.compras])

    def get_data_ultima_compra(self):
        return None if not self.compras else \
            sorted(self.compras, key=get_data)[-1].data
