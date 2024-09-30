from models.endereco import Endereco
from models.enums.sexo import Sexo
from models.enums.setor import Setor
from models.funcionario import Funcionario
from models.enums.estado_civil import EstadoCivil

class Advogado(Funcionario):
    def __init__(self, id: int, nome: str, telefone: str, email: str, sexo: Sexo, estadoCivil: EstadoCivil, dataNascimento: str, cpf: str, rg: str, matricula: str, setor: Setor, salario: float, oab: str, endereco: Endereco) -> None:
        super().__init__(id, nome, telefone, email, sexo, estadoCivil, dataNascimento, cpf, rg, matricula, setor, salario, endereco)
        self.oab = self._verificar_oab(oab)


    def _verificar_oab(self,valor):
        self._verificar_oab_vazio(valor)
        self._verificar_oab_tipo_invalido(valor)

        self.oab = valor
        return self.oab
    
    
    def _verificar_oab_vazio(self, valor):
        if not valor.strip():
            raise TypeError("O OAB não pode ficar vazio!")
        
    def _verificar_oab_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("O OAB deve ser um texto!")

    def __str__(self) -> str:
        return (f"OAB: {self.oab}\n"
               f"{super().__str__()}"
        ) 