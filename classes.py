# NOTE: acesso public, protected, private

# class Pessoa:
#   def __init__(self, nome, idade, email):
#       self.nome = nome  # public
#       self._idade = idade # protected
#       self.__email = email # private


class Pessoa:
    def __init__(self, nome, idade, email):
        self.__nome = nome  
        self.__idade = idade 
        self.__email = email 

# NOTE: metodos de acesso

    """def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome

    def get_idade(self):
        return self.__idade
    
    def set_idade(self, idade):
        self.__idade = idade

    def get_email(self):
        return self.__email
    
    def set_email(self, email):
        self.__email = email"""
    
# metedo get nome

    @property
    def nome(self):
        return self.__nome
    
# metodo set nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        self.__email = email