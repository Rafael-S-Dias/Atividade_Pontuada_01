import pytest
from projeto.models.endereco import Endereco
from projeto.models.enums.unidade_federativa import UnidadeFederativa

@pytest.fixture
def endereco_valido():
    endereco1 = Endereco("Rua A", 444, "Qd 10 Lt 7", "41.....", "Salvador", UnidadeFederativa.BAHIA)
    return endereco1

def test_logradouro_valido(endereco_valido):
    assert endereco_valido.logradouro == "Rua A"

def test_numero_valido(endereco_valido):
    assert endereco_valido.numero == 444

def test_complemento_valido(endereco_valido):
    assert endereco_valido.complemento == "Qd 10 Lt 7"

def test_cep_valido(endereco_valido):
    assert endereco_valido.cep == "41....."

def test_cidade_valida(endereco_valido):
    assert endereco_valido.cidade == "Salvador"

def test_uf_valida(endereco_valido):
    assert endereco_valido.uf == UnidadeFederativa.BAHIA

def test_logradouro_vazio():
    with pytest.raises(TypeError, match = "O logradouro não pode ficar vazio!"):
       Endereco(" ", 444, "Qd 10 Lt 7", "41.....", "Salvador", UnidadeFederativa.BAHIA) 

def test_logradouro_tipo_invalido():
    with pytest.raises(TypeError, match = "O logradouro deve ser um texto!"):
       Endereco(111, 444, "Qd 10 Lt 7", "41.....", "Salvador", UnidadeFederativa.BAHIA) 

def test_numero_vazio():
    with pytest.raises(TypeError, match = "O número não pode ficar vazio!"):
        Endereco("Rua A", None, "Qd 10 Lt 7", "41.....", "Salvador", UnidadeFederativa.BAHIA)

def test_numero_negativo():
    with pytest.raises(TypeError, match = "O número não pode ser composto por números negativos!"):
        Endereco("Rua A", -444, "Qd 10 Lt 7", "41.....", "Salvador", UnidadeFederativa.BAHIA)

def test_numero_tipo_invalido():
    with pytest.raises(TypeError, match = "O número deve ser um texto!"):
        Endereco("Rua A", "444", "Qd 10 Lt 7", "41.....", "Salvador", UnidadeFederativa.BAHIA)

def test_complemento_vazio():
    with pytest.raises(TypeError, match = "O complemento não pode ficar vazio!"):
        Endereco("Rua A", 444, " ", "41.....", "Salvador", UnidadeFederativa.BAHIA)

def test_complemento_tipo_invalido():
    with pytest.raises(TypeError, match = "O complemento deve ser um texto!"):
        Endereco("Rua A", 444, 1, "41.....", "Salvador", UnidadeFederativa.BAHIA)

def test_cep_vazio():
    with pytest.raises(TypeError, match = "O CEP não pode ficar vazio!"):
        Endereco("Rua A", 444, "Qd 10 Lt 7", " ", "Salvador", UnidadeFederativa.BAHIA)

def test_cep_tipo_invalido():
    with pytest.raises(TypeError, match = "O CEP deve ser um texto!"):
        Endereco("Rua A", 444, "Qd 10 Lt 7", 10, "Salvador", UnidadeFederativa.BAHIA)

def test_cidade_vazio():
    with pytest.raises(TypeError, match = "A cidade não pode ficar vazio!"):
        Endereco("Rua A", 444, "Qd 10 Lt 7", "41.....", " ", UnidadeFederativa.BAHIA)

def test_cidade_tipo_invalido():
    with pytest.raises(TypeError, match = "A cidade deve ser um texto!"):
        Endereco("Rua A", 444, "Qd 10 Lt 7", "41.....", 10, UnidadeFederativa.BAHIA)
