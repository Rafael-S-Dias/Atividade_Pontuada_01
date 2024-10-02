from projeto.models.endereco import Endereco
from projeto.models.enums.sexo import Sexo
from projeto.models.enums.setor import Setor
from projeto.models.funcionario import Funcionario
from projeto.models.enums.estado_civil import EstadoCivil

class Engenheiro(Funcionario):
    def __init__(self, id: int, nome: str, telefone: str, email: str, sexo: Sexo, estadoCivil: EstadoCivil, dataNascimento: str, cpf: str, rg: str, matricula: str, setor: Setor, salario: float, crea: str, endereco: Endereco) -> None:
        super().__init__(id, nome, telefone, email, sexo, estadoCivil, dataNascimento, cpf, rg, matricula, setor, salario, endereco)
        self.crea = self._verificar_crea(crea)

    def _verificar_crea(self,valor):
        self._verificar_crea_tipo_invalido(valor)
        self._verificar_crea_vazio(valor)

        self.crea = valor
        return self.crea
    
    def _verificar_crea_vazio(self, valor):
        if not valor.strip():
            raise TypeError("O CREA não pode ficar vazio!")

    def _verificar_crea_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O CREA deve ser um texto!")

    def __str__(self) -> str:
        return (f"CREA: {self.crea}\n"
               f"{super().__str__()}"
        )