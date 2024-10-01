import pytest
from models.cliente import Cliente
from models.enums.estado_civil import EstadoCivil
from models.enums.sexo import Sexo
from models.endereco import Endereco
from models.enums.unidade_federativa import UnidadeFederativa

@pytest.fixture
def cliente_valido():
    cliente1 = Cliente(222, "Rafael", "71988...", "Rafael@...", Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "02/08/2001", 8888, Endereco("Rua A", 444, "Qd 10 Lt 7", "41.....", "Salvador", UnidadeFederativa.BAHIA) )
    return cliente1

def test_protocolo_de_atendimento_valido(cliente_valido):
    assert cliente_valido.protocoloatendimento == 8888

def test_protocolo_de_atendimento_vazio():
    with pytest.raises(TypeError, match = "O protocolo de atendimento não pode ficar vazio!"):
        Cliente(222, "Rafael", "71988...", "Rafael@...", Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "02/08/2001", None, Endereco("Rua A", 444, "Qd 10 Lt 7", "41.....", "Salvador", UnidadeFederativa.BAHIA) )

def test_protocolo_de_atendimento_tipo_invalido():
    with pytest.raises(TypeError, match = "O protocolo de atendimento deve ser composto por números inteiros!"):
        Cliente(222, "Rafael", "71988...", "Rafael@...", Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "02/08/2001", "8888", Endereco("Rua A", 444, "Qd 10 Lt 7", "41.....", "Salvador", UnidadeFederativa.BAHIA) )

