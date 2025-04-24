class SistemaVendas:
    def __init__(self):
        self._produtos = []  # Lista de produtos cadastrados
        self._clientes = []  # Lista de clientes cadastrados
        self._vendas = []    # Lista de vendas realizadas

    @property
    def produtos(self):
        return self._produtos

    @produtos.setter
    def produtos(self, value):
        pass

    @property
    def clientes(self):
        return self._clientes

    @clientes.setter
    def clientes(self, value):
        pass

    @property
    def vendas(self):
        return self._vendas

    @vendas.setter
    def vendas(self, value):
        pass