import pytest
from models.engenheiro import Engenheiro
from models.enums.estado_civil import EstadoCivil
from models.enums.sexo import Sexo
from models.endereco import Endereco
from models.enums.unidade_federativa import UnidadeFederativa
from models.enums.setor import Setor

def advogado_valido():
    advogado1 = Engenheiro(222, "Rafael", "71988...", "Rafael@...", Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "02/08/2001", "88888", "5555", "4444", Setor.JURIDICO, 2500, "777", Endereco("Rua A", 444, "Qd 10 Lt 7", "41.....", "Salvador", UnidadeFederativa.BAHIA) )
    return advogado1

def test_oab_valido(advogado_valido):
    assert advogado_valido.crea == "888"

def test_oab_vazio():
    with pytest.raises(TypeError, match = "O OAB não pode ficar vazio!"):
        Engenheiro(222, "Rafael", "71988...", "Rafael@...", Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "02/08/2001", "88888", "5555", "4444", Setor.JURIDICO, 2500, " ", Endereco("Rua A", 444, "Qd 10 Lt 7", "41.....", "Salvador", UnidadeFederativa.BAHIA) )

def test_oab_tipo_invalido():
    with pytest.raises(TypeError, match = "O OAB deve se manter como texto!"):
        Engenheiro(222, "Rafael", "71988...", "Rafael@...", Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "02/08/2001", "88888", "5555", "4444", Setor.JURIDICO, 2500, 777, Endereco("Rua A", 444, "Qd 10 Lt 7", "41.....", "Salvador", UnidadeFederativa.BAHIA) )

