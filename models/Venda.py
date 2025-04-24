class Venda:
    def __init__(self):
        self._id = None
        self._data = None
        self._cliente = None
        self._itens = None
        self._valor_total = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        pass

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        pass

    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, value):
        pass

    @property
    def itens(self):
        return self._itens

    @itens.setter
    def itens(self, value):
        pass

    @property
    def valor_total(self):
        return self._valor_total

    @valor_total.setter
    def valor_total(self, value):
        pass
    