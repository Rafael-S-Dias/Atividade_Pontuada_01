from abc import ABC
from projeto.models.endereco import Endereco

class Pessoa(ABC):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        self.id = self._verificar_id(id)
        self.nome = self._verificar_nome(nome)
        self.telefone = self._verificar_telefone(telefone)
        self.email = self._verificar_email(email)
        self.endereco = endereco


    def _verificar_id(self, valor):
        self._verificar_id_vazio(valor)
        self._verificar_id_tipo_invalido(valor)

        self.id = valor
        return self.id

    def _verificar_nome(self, valor):
        self._verificar_nome_vazio(valor)
        self._verificar_nome_tipo_invalido(valor)

        self.nome = valor
        return self.nome
    
    def _verificar_telefone(self, valor):
        self._verificar_telefone_vazio(valor)
        self._verificar_telefone_tipo_invalido(valor)

        self.telefone = valor
        return self.telefone

    def _verificar_email(self, valor):
        self._verificar_email_vazio(valor)
        self._verificar_email_tipo_invalido(valor)

        self.email = valor
        return self.email
    
    
    def _verificar_id_vazio(self, valor):
        if valor is None:
            raise TypeError("O ID não pode ficar vazio!")
        
    def _verificar_id_tipo_invalido(self, valor):
        if not isinstance(valor, int):
            raise TypeError("O ID deve ser composto por números inteiros!")
        
    def _verificar_nome_vazio(self, valor):
        if not valor.strip():
            raise TypeError("O nome não pode ficar vazio!")
             
    def _verificar_nome_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O nome deve ser um texto!")
         
    def _verificar_telefone_vazio(self, valor):
         if not valor.strip():
            raise TypeError("O telefone não pode ficar vazio!")
        
    def _verificar_telefone_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O telefone deve ser um texto!")
        
    def _verificar_email_vazio(self, valor):
         if not valor.strip():
            raise TypeError("O email não pode ficar vazio!")
        
    def _verificar_email_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O email deve ser um texto!")

    def __str__(self) -> str:
        return ( f"Id: {self.id}\n"
                 f"Nome: {self.nome}\n"
                 f"Telefone: {self.telefone}\n"
                 f"Email: {self.email}\n"
                 f"=== Endereço === {self.endereco}"
        )