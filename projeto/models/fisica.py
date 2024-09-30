from abc import ABC
from models.pessoa import Pessoa
from models.enums.sexo import Sexo
from models.endereco import Endereco
from models.enums.estado_civil import EstadoCivil

class Fisica(Pessoa, ABC):
    def __init__(self, id: int, nome: str, telefone: str, email: str, sexo: Sexo, estadoCivil: EstadoCivil, dataNascimento: str, endereco: Endereco) -> None:
        super().__init__(id, nome, telefone, email, endereco)
        self.sexo = sexo
        self.estadoCivil = estadoCivil
        self.dataNascimento = self._verificar_data_de_nascimento(dataNascimento)

    def _verificar_data_de_nascimento(self, valor):
        self._verificar_data_de_nascimento_vazio(valor)
        self._verificar_data_de_nascimento_tipo_invalido(valor)

        self.dataNascimento = valor
        return self.dataNascimento


    def _verificar_data_de_nascimento_vazio(self, valor):
        if not valor.strip():
            raise TypeError("A data de nascimento não pode ficar vazio!")

    def _verificar_data_de_nascimento_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("A data de nascimento deve ser um texto!")


    def __str__(self) -> str:
        return (f"Sexo: {self.sexo.caractere} / {self.sexo.texto}\n"
                f"Estado Civil: {self.estadoCivil.value}\n"
                f"Data de Nascimento: {self.dataNascimento}\n"
                f"{super().__str__()}"
        )