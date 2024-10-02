import pytest
from projeto.models.juridica import Juridica
from projeto.models.endereco import Endereco
from projeto.models.enums.unidade_federativa import UnidadeFederativa

@pytest.fixture
def pessoa_juridica_valida():
    pessoa_juridica1 = Juridica(222, "Rafael", "71988...", "Rafael@...", "45800...", "5555", Endereco("Rua A", 444, "Qd 10 Lt 7", "41.....", "Salvador", UnidadeFederativa.BAHIA))
    return pessoa_juridica1

def test_cnpj_valido(pessoa_juridica_valida):
    assert pessoa_juridica_valida.cnpj == "45800..."

def test_inscricao_estadual_valido(pessoa_juridica_valida):
    assert pessoa_juridica_valida.inscricaoEstadual == "5555"

def test_pessoa_cnpj_vazio():
    with pytest.raises(TypeError, match = "O CNPJ não pode ficar vazio!"):
        Juridica(222, "Rafael", "71988...", "Rafael@...", " ", "5555", Endereco("Rua A", 444, "Qd 10 Lt 7", "41.....", "Salvador", UnidadeFederativa.BAHIA))

def test_pessoa_cnpj_invalido():
    with pytest.raises(TypeError, match = "O CNPJ deve ser um texto!"):
        Juridica(222, "Rafael", "71988...", "Rafael@...", 45800, "5555", Endereco("Rua A", 444, "Qd 10 Lt 7", "41.....", "Salvador", UnidadeFederativa.BAHIA))

def test_pessoa_inscricao_estadual_vazio():
    with pytest.raises(TypeError, match = "A inscrição estadual não pode ficar vazio!"):
        Juridica(222, "Rafael", "71988...", "Rafael@...", "45800...", " ", Endereco("Rua A", 444, "Qd 10 Lt 7", "41.....", "Salvador", UnidadeFederativa.BAHIA))

def test_pessoa_inscricao_estadual_invalido():
    with pytest.raises(TypeError, match="A inscrição estadual deve ser um texto!"):
        Juridica(222, "Rafael", "71988...", "Rafael@...", "45800...", 5555, Endereco("Rua A", 444, "Qd 10 Lt 7", "41.....", "Salvador", UnidadeFederativa.BAHIA))