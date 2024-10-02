from projeto.models.endereco import Endereco
from projeto.models.juridica import Juridica

class Fornecedor(Juridica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, cnpj: str, inscricaoEstadual: str, produto: str, endereco: Endereco) -> None:
        super().__init__(id, nome, telefone, email, cnpj, inscricaoEstadual, endereco)
        self.produto = self._verificar_produto(produto)


    def _verificar_produto(self, valor):
        self._verificar_produto_tipo_invalido(valor)
        self._verificar_produto_vazio(valor)

        self.produto = valor
        return self.produto
    

    def _verificar_produto_vazio(self, valor):
        if not valor.strip():
            raise TypeError("O produto não pode ficar vazio!")
        
    def _verificar_produto_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O produto deve ser um texto!")


    def __str__(self) -> str:
        return (f"Produto: {self.produto}\n"
                f"{super().__str__()}"
        )