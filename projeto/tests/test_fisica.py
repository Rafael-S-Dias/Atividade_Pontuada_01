import pytest
from projeto.models.fisica import Fisica
from projeto.models.endereco import Endereco
from projeto.models.enums.unidade_federativa import UnidadeFederativa
from projeto.models.enums.sexo import Sexo
from projeto.models.enums.estado_civil import EstadoCivil

@pytest.fixture
def fisica_valida():
    pessoa_fisica1 = Fisica(222, "Rafael", "71988...", "Rafael@...", Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "10/08/2001", Endereco("Rua A", 444, "Qd 10 Lt 7", "41.....", "Salvador", UnidadeFederativa.BAHIA) )
    return pessoa_fisica1

def test_sexo_valido(fisica_valida):
    assert fisica_valida.sexo == Sexo.MASCULINO

def test_estado_civil_valido(fisica_valida):
    assert fisica_valida.estadoCivil == EstadoCivil.SOLTEIRO

def test_data_de_nascimento_valido(fisica_valida):
    assert fisica_valida.dataNascimento == "10/08/2001"

def test_data_de_nascimento_vazio():
    with pytest.raises(TypeError, match = "A data de nascimento não pode ficar vazio!"):
        Fisica(222, "Rafael", "71988...", "Rafael@...", Sexo.MASCULINO, EstadoCivil.SOLTEIRO, " ", Endereco("Rua A", 444, "Qd 10 Lt 7", "41.....", "Salvador", UnidadeFederativa.BAHIA) )

def test_data_de_nascimento_tipo_invalido():
    with pytest.raises(TypeError, match = "A data de nascimento deve ser um texto!"):
        Fisica(222, "Rafael", "71988...", "Rafael@...", Sexo.MASCULINO, EstadoCivil.SOLTEIRO, 10082001, Endereco("Rua A", 444, "Qd 10 Lt 7", "41.....", "Salvador", UnidadeFederativa.BAHIA) )