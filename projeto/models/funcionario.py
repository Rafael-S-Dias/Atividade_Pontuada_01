from abc import ABC
from projeto.models.fisica import Fisica
from projeto.models.enums.sexo import Sexo
from projeto.models.endereco import Endereco
from projeto.models.enums.estado_civil import EstadoCivil
from projeto.models.enums.setor import Setor

class Funcionario(Fisica, ABC):
    def __init__(self, id: int, nome: str, telefone: str, email: str, sexo: Sexo, estadoCivil: EstadoCivil, dataNascimento: str, cpf: str, rg: str, matricula: str, setor: Setor, salario: float, endereco: Endereco) -> None:
        super().__init__(id, nome, telefone, email, sexo, estadoCivil, dataNascimento, endereco)
        self.cpf = self._verificar_cpf(cpf)
        self.rg = self._verificar_rg(rg)
        self.matricula = self._verificar_matricula(matricula)
        self.setor = setor
        self.salario = self._verificar_salario(salario)


    def _verificar_cpf(self, valor):
        self._verificar_cpf_tipo_invalido(valor)
        self._verificar_cpf_vazio(valor)

        self.cpf = valor
        return self.cpf
    
    def _verificar_rg(self, valor):
        self._verificar_rg_tipo_invalido(valor)
        self._verificar_rg_vazio(valor)

        self.rg = valor
        return self.rg
    
    def _verificar_matricula(self, valor):
        self._verificar_matricula_tipo_invalido(valor)
        self._verificar_matricula_vazio(valor)

        self.matricula = valor
        return self.matricula
    
    def _verificar_salario(self, valor):
        self._verificar_salario_vazio(valor)
        
        self._verificar_salario_tipo_invalido(valor)
        self._verificar_salario_negativo(valor)

        self.salario = valor
        return self.salario
    

    def _verificar_cpf_vazio(self, valor):
        if not valor.strip():
            raise TypeError("O CPF não pode ficar vazio!")
        
    def _verificar_cpf_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O CPF deve ser um texto!")

    def _verificar_rg_vazio(self, valor):
        if not valor.strip():
            raise TypeError("O RG não pode ficar vazio!")
        
    def _verificar_rg_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O RG deve se manter como texto!")

    def _verificar_matricula_vazio(self, valor):
        if not valor.strip():
            raise TypeError("A matricula não pode ficar vazio!")
      
    def _verificar_matricula_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("A matricula deve ser um texto!")

    def _verificar_salario_vazio(self, valor):
        if valor is None:
            raise TypeError("O salário não pode ficar vazio!")   

    def _verificar_salario_tipo_invalido(self, valor):
         if not isinstance(valor, (int, float)):
            raise TypeError("O salário deve ser composto por números!")
        
    def _verificar_salario_negativo(self, valor):
        if valor < 0:
            raise ValueError("O salário não pode ser negativo!")


    def __str__(self) -> str:
        return (f"CPF: {self.cpf}\n"
                f"RG: {self.rg}\n"
                f"Numero de Matricula: {self.matricula}\n"
                f"Setor: {self.setor.value}\n"
                f"Salario: {self.salario}\n"
                f"{super().__str__()}"
        )
