from abc import ABC
from projeto.models.pessoa import Pessoa
from projeto.models.endereco import Endereco

class Juridica(Pessoa, ABC):
    def __init__(self, id: int, nome: str, telefone: str, email: str, cnpj: str, inscricaoEstadual: str, endereco: Endereco) -> None:
        super().__init__(id, nome, telefone, email, endereco)
        self.cnpj = self._verificar_cnpj(cnpj)
        self.inscricaoEstadual = self._verificar_inscricao_estadual(inscricaoEstadual)


    def _verificar_cnpj(self, valor):
        self._verificar_cnpj_tipo_invalido(valor)
        self._verificar_cnpj_vazio(valor)

        self.cnpj = valor
        return self.cnpj

    def _verificar_inscricao_estadual(self, valor):
        self._verificar_inscricao_estadual_tipo_invalido(valor)
        self._verificar_inscricao_estadual_vazio(valor)

        self.inscricaoEstadual = valor
        return self.inscricaoEstadual
    
    def _verificar_cnpj_vazio(self, valor):
        if not valor.strip():
            raise TypeError("O CNPJ não pode ficar vazio!")
        
    def _verificar_cnpj_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O CNPJ deve ser um texto!")
        
    def _verificar_inscricao_estadual_vazio(self, valor):
        if not valor.strip():
            raise TypeError("A inscrição estadual não pode ficar vazio!")
        
    def _verificar_inscricao_estadual_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("A inscrição estadual deve ser um texto!")


    def __str__(self) -> str:
        return (f"CNPJ: {self.cnpj}\n"
                f"Inscrição Estadual: {self.inscricaoEstadual}\n"
                f"{super().__str__()}"
        )