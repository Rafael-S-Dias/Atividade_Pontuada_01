from models.endereco import Endereco
from models.enums.sexo import Sexo
from models.enums.setor import Setor
from models.funcionario import Funcionario
from models.enums.estado_civil import EstadoCivil

class Medico(Funcionario):
    def __init__(self, id: int, nome: str, telefone: str, email: str, sexo: Sexo, estadoCivil: EstadoCivil, dataNascimento: str, cpf: str, rg: str, matricula: str, setor: Setor, salario: float, crm: str, endereco: Endereco) -> None:
        super().__init__(id, nome, telefone, email, sexo, estadoCivil, dataNascimento, cpf, rg, matricula, setor, salario, endereco)
        self.crm = self._verificar_crm(crm)

    def _verificar_crm(self,valor):
        self._verificar_crm_vazio(valor)
        self._verificar_crm_tipo_invalido(valor)

        self.crm = valor
        return self.crm
    

    def _verificar_crm_vazio(self, valor):
        if not valor.strip():
            raise TypeError("O CRM não pode ficar vazio!")

    def _verificar_crm_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("O CRM deve se manter como texto!")


    def __str__(self) -> str:
        return (f"CRM: {self.crm}\n"
               f"{super().__str__()}"
        ) 