class Cliente:
    def __init__(self, nome : str, cpf : str, email : str, telefone : str):
        if not isinstance(nome, str) or not isinstance(cpf, str) or not isinstance(email, str) or not isinstance(telefone, str):
            raise TypeError("Todos os parâmetros devem ser do tipo string.")
        
    
        self.nome =  nome.title()
        self._cpf = cpf
        self._email = email
        self._telefone = telefone

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, value):
        if not isinstance(value, str):
            raise TypeError("O CPF deve ser uma string.")
        if len(value) != 11 or not value.isdigit():
            raise ValueError("O CPF deve ter 11 dígitos.")
        self._cpf = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not isinstance(value, str):
            raise TypeError("O email deve ser uma string.")
        if "@" not in value or "." not in value:
            raise ValueError("Email inválido.")
        self._email = value

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, value):
        if not isinstance(value, str):
            raise TypeError("O telefone deve ser uma string.")
        if len(value) < 10 or not value.isdigit():
            raise ValueError("O telefone deve ter pelo menos 10 dígitos.")
        self._telefone = value
    
    def exibir_informacoes(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}, Email: {self.email}, Telefone: {self.telefone}"
    
    def atualizar_informacoes(self, nome=None, email=None, telefone=None):
        if nome:
            self.nome = nome.title()
        if email:
            self.email = email
        if telefone:
            self.telefone = telefone
    
    def validar_cpf(self, cpf):
        if len(cpf) != 11 or not cpf.isdigit():
            return False
        # Aqui você pode implementar uma validação mais robusta, como o cálculo do dígito verificador.
        return True
    
    def cliente_valido(self):
        return all([self.nome, self.cpf, self.email, self.telefone])
    
    def enviar_mensagem(self, mensagem):
        return f"Mensagem enviada para {self.nome} ({self.telefone}): {mensagem}"
    
    def validar_email(self, email):
        return "@" in email and "." in email

    def adicionar_compra(self, compra):
        if not hasattr(self, "_compras"):
            self._compras = []
        self._compras.append(compra)

    def listar_compras(self):
        return getattr(self, "_compras", [])








