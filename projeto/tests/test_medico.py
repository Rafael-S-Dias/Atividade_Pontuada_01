import pytest
from models.medico import Medico
from models.enums.estado_civil import EstadoCivil
from models.enums.sexo import Sexo
from models.endereco import Endereco
from models.enums.unidade_federativa import UnidadeFederativa
from models.enums.setor import Setor

@pytest.fixture
def medico_valido():
    medico1 = Medico(222, "Rafael", "71988...", "Rafael@...", Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "02/08/2001", "88888", "5555", "4444", Setor.JURIDICO, 2500, "999", Endereco("Rua A", 444, "Qd 10 Lt 7", "41.....", "Salvador", UnidadeFederativa.BAHIA) )
    return medico1

def test_crm_valido(medico_valido):
    assert medico_valido.crm == "999"

def test_crm_vazio():
    with pytest.raises(TypeError, match = "O CRM não pode ficar vazio!"):
        Medico(222, "Rafael", "71988...", "Rafael@...", Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "02/08/2001", "88888", "5555", "4444", Setor.JURIDICO, 2500, " ", Endereco("Rua A", 444, "Qd 10 Lt 7", "41.....", "Salvador", UnidadeFederativa.BAHIA) )

def test_crm_tipo_invalido():
    with pytest.raises(TypeError, match = "O CRM deve se manter como texto!"):
        Medico(222, "Rafael", "71988...", "Rafael@...", Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "02/08/2001", "88888", "5555", "4444", Setor.JURIDICO, 2500, 999, Endereco("Rua A", 444, "Qd 10 Lt 7", "41.....", "Salvador", UnidadeFederativa.BAHIA) )