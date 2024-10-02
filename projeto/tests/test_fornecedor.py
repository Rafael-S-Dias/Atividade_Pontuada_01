import pytest
from projeto.models.fornecedor import Fornecedor
from projeto.models.endereco import Endereco
from projeto.models.enums.unidade_federativa import UnidadeFederativa

@pytest.fixture
def fornecedor_valido():
    fornecedor1 = Fornecedor(222, "Rafael", "71988...", "Rafael@...", "45800...", "5555", "Suprimentos", Endereco("Rua A", 444, "Qd 10 Lt 7", "41.....", "Salvador", UnidadeFederativa.BAHIA))
    return fornecedor1

def test_produto_valido(fornecedor_valido):
    assert fornecedor_valido.produto == "Suprimentos"

def test_pessoa_produto_vazio():
    with pytest.raises(TypeError, match = "O produto não pode ficar vazio!"):
        Fornecedor(222, "Rafael", "71988...", "Rafael@...", "45800...", "5555", " ", Endereco("Rua A", 444, "Qd 10 Lt 7", "41.....", "Salvador", UnidadeFederativa.BAHIA))

def test_pessoa_produto_invalido():
    with pytest.raises(TypeError, match = "O produto deve ser um texto!"):
        Fornecedor(222, "Rafael", "71988...", "Rafael@...", "45800...", "5555", 22, Endereco("Rua A", 444, "Qd 10 Lt 7", "41.....", "Salvador", UnidadeFederativa.BAHIA))