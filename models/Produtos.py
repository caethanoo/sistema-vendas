class Produto:
    def __init__(self, id, nome, preco, quantidade):
        if preco < 0:
            raise ValueError("O preço não pode ser negativo.")
        if quantidade <0:
            raise ValueError("A quantidade não pode ser negativa.")
        
        self.__id = id
        self. nome = nome.title()
        self.__preco = preco
        self.__quantidade = quantidade

    @property
    def id(self):
        return self.__id
 

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco):
       if preco <0:
           raise ValueError("O preço não pode ser negativo.")
       self.__preco = preco

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
       if quantidade < 0 :
        raise ValueError("A quantidade não pode ser negativa.")
        self.__quantidade = quantidade


    def calcular_valor_estoque(self):
        return self.__preco * self.__quantidade
    
    def atualizar_estoque(self,quantidade):
        if self.__quantidade + quantidade < 0 :
            raise ValueError("A quantidade não pode ser negativa.")
        self.__quantidade += quantidade
        
    def registrar_vendas(self,quantidade):
        if quantidade < 0:
            raise ValueError("A quantidade não pode ser negativa.")
        if quantidade > self.__quantidade:
            raise ValueError("Quantidade insuficiente em estoque.")
        self.__quantidade -= quantidade
        
    def informacoes_produto(self):
        return f"ID: {self.__id}, Nome: {self.nome}, Preço: {self.__preco}, Quantidade: {self.__quantidade}"