import pytest
from models.engenheiro import Engenheiro
from models.enums.estado_civil import EstadoCivil
from models.enums.sexo import Sexo
from models.endereco import Endereco
from models.enums.unidade_federativa import UnidadeFederativa
from models.enums.setor import Setor

def engenheiro_valido():
    engenheiro1 = Engenheiro(222, "Rafael", "71988...", "Rafael@...", Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "02/08/2001", "88888", "5555", "4444", Setor.JURIDICO, 2500, "888", Endereco("Rua A", 444, "Qd 10 Lt 7", "41.....", "Salvador", UnidadeFederativa.BAHIA) )
    return engenheiro1

def test_crea_valido(engenheiro_valido):
    assert engenheiro_valido.crea == "888"

def test_crea_vazio():
    with pytest.raises(TypeError, match = "O CREA não pode ficar vazio!"):
        Engenheiro(222, "Rafael", "71988...", "Rafael@...", Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "02/08/2001", "88888", "5555", "4444", Setor.JURIDICO, 2500, " ", Endereco("Rua A", 444, "Qd 10 Lt 7", "41.....", "Salvador", UnidadeFederativa.BAHIA) )

def test_crea_tipo_invalido():
    with pytest.raises(TypeError, match = "O CREA deve se manter como texto!"):
        Engenheiro(222, "Rafael", "71988...", "Rafael@...", Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "02/08/2001", "88888", "5555", "4444", Setor.JURIDICO, 2500, 888, Endereco("Rua A", 444, "Qd 10 Lt 7", "41.....", "Salvador", UnidadeFederativa.BAHIA) )