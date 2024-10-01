import pytest
from models.pessoa import Pessoa
from models.endereco import Endereco
from models.enums.unidade_federativa import UnidadeFederativa

@pytest.fixture
def pessoa_valida():
    pessoa1 = Pessoa(222, "Rafael", "71988...", "Rafael@...", Endereco("Rua A", 444, "Qd 10 Lt 7", "41.....", "Salvador", UnidadeFederativa.BAHIA) )
    return pessoa1

def test_id_valido(pessoa_valida):
    assert pessoa_valida._id == 222

def test_nome_valido(pessoa_valida):
    assert pessoa_valida._nome == "Rafael"

def test_telefone_valido(pessoa_valida):
    assert pessoa_valida._telefone == "71988..." 

def test_email_valido(pessoa_valida):
    assert pessoa_valida._email == "Rafael@..."

def test_pessoa_id_tipo_invalido():
    with pytest.raises(TypeError, match = "O ID deve ser composto por números inteiros!"):
        Pessoa(333, "Rafael", "71988...", "Rafael@...", Endereco("Rua A", 444, "Qd 10 Lt 7", "41.....", "Salvador", UnidadeFederativa.BAHIA) )

def test_pessoa_id_vazio():
    with pytest.raises(TypeError, match = "O ID não pode ficar vazio!"):
        Pessoa(None, "Rafael", "71988...", "Rafael@...", Endereco("Rua A", 444, "Qd 10 Lt 7", "41.....", "Salvador", UnidadeFederativa.BAHIA) )

def test_pessoa_id_vazio():
    with pytest.raises(TypeError, match = "O ID não pode ficar vazio!"):
        Pessoa(-222, "Rafael", "71988...", "Rafael@...", Endereco("Rua A", 444, "Qd 10 Lt 7", "41.....", "Salvador", UnidadeFederativa.BAHIA) )

def test_nome_tipo_invalido():
    with pytest.raises(TypeError, match = "O nome deve ser um texto!"):
        Pessoa(222, 8888, "71988...", "Rafael@...", Endereco("Rua A", 444, "Qd 10 Lt 7", "41.....", "Salvador", UnidadeFederativa.BAHIA) )

def test_nome_vazio():
    with pytest.raises(TypeError, match="O nome não pode estar vazio!"):
        Pessoa(222, " ", "71988...", "Rafael@...", Endereco("Rua A", 444, "Qd 10 Lt 7", "41.....", "Salvador", UnidadeFederativa.BAHIA) )

def test_telefone_tipo_invalido():
    with pytest.raises(TypeError, match = "O telefone deve ser um texto!"):
        Pessoa(222, "Rafael", 71988, "Rafael@...", Endereco("Rua A", 444, "Qd 10 Lt 7", "41.....", "Salvador", UnidadeFederativa.BAHIA) )

def test_telefone_vazio():
    with pytest.raises(TypeError, match = "O telefone deve ser um texto!"):
        Pessoa(222, "Rafael", " ", "Rafael@...", Endereco("Rua A", 444, "Qd 10 Lt 7", "41.....", "Salvador", UnidadeFederativa.BAHIA) )

def test_email_tipo_invalido():
    with pytest.raises(TypeError, match="O email deve ser um texto!"):
        Pessoa(222, "Rafael", "71988...", 85595, Endereco("Rua A", 444, "Qd 10 Lt 7", "41.....", "Salvador", UnidadeFederativa.BAHIA) )

def test_email_vazio():
    with pytest.raises(TypeError, match = "O telefone deve ser um texto!"):
        Pessoa(222, "Rafael", 71988, " ", Endereco("Rua A", 444, "Qd 10 Lt 7", "41.....", "Salvador", UnidadeFederativa.BAHIA) )
