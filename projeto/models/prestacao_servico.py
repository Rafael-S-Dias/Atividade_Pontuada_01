from projeto.models.endereco import Endereco
from projeto.models.juridica import Juridica

class PrestacaoServico(Juridica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, cnpj: str, inscricaoEstadual: str, contratoInicio: str, contratoFim: str, endereco: Endereco) -> None:
        super().__init__(id, nome, telefone, email, cnpj, inscricaoEstadual, endereco)
        self.contratoInicio = self._verificar_contrato_inicio(contratoInicio)
        self.contratoFim = self._verificar_contrato_fim(contratoFim)


    def _verificar_contrato_inicio(self, valor):
        self._verificar_contrato_inicio_vazio(valor)
        self._verificar_contrato_inicio_tipo_invalido(valor)

        self.contratoInicio = valor
        return self.contratoInicio

    def _verificar_contrato_fim(self, valor):
        self._verificar_contrato_fim_vazio(valor)
        self._verificar_contrato_fim_tipo_invalido(valor)

        self.contratoFim = valor
        return self.contratoFim


    def _verificar_contrato_inicio_vazio(self, valor):
        if not valor.strip():
            raise TypeError("O inicio do contrato não pode ficar vazio!")
        
    def _verificar_contrato_inicio_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O inicio de contrato deve ser um texto!")
        
    def _verificar_contrato_fim_vazio(self, valor):
        if not valor.strip():
            raise TypeError("O fim de contrato não pode ficar vazio!")
        
    def _verificar_contrato_fim_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O fim de contrato deve ser um texto!")
        

    def __str__(self) -> str:
        return (f"Inicio de Contrato: {self.contratoInicio}\n"
                f"Final de Contrato: {self.contratoFim}\n"
                f"{super().__str__()}"
        )

