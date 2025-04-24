class Produto:
    def __init__(self, id, nome, preco, quantidade):
        self.__id = id
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        pass  # você completa depois

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco):
        pass  # lógica depois

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        pass  # lógica depois
