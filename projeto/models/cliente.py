from projeto.models.fisica import Fisica
from projeto.models.enums.sexo import Sexo
from projeto.models.endereco import Endereco
from projeto.models.enums.estado_civil import EstadoCivil

class Cliente(Fisica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, sexo: Sexo, estadoCivil: EstadoCivil, dataNascimento: str, protocoloAtendimento: int, endereco: Endereco) -> None:
        super().__init__(id, nome, telefone, email, sexo, estadoCivil, dataNascimento, endereco)
        self.protocoloatendimento = self._verificar_protocolo_de_atendimento(protocoloAtendimento)


    def _verificar_protocolo_de_atendimento(self,valor):
        self._verificar_protocolo_de_atendimento_vazio(valor)
        self._verificar_protocolo_de_atendimento_tipo_invalido(valor)

        self.protocoloAtendimento = valor
        return self.protocoloAtendimento
    

    def _verificar_protocolo_de_atendimento_vazio(self, valor):
        if valor is None:
            raise TypeError("O protocolo de atendimento não pode ficar vazio!")
        
    def _verificar_protocolo_de_atendimento_tipo_invalido(self, valor):
        if not isinstance(valor, int):
            raise TypeError("O protocolo de atendimento deve ser composto por números inteiros!")


    def __str__(self) -> str:
        return (f"Protocolo de Atendimento: {self.protocoloAtendimento}\n"
                f"{super().__str__()}"
        )