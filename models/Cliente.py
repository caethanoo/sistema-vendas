class Cliente:
    def __init__(self):
        self._nome = None
        self._cpf = None
        self._email = None
        self._telefone = None

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        pass

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, value):
        pass

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        pass

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, value):
        pass