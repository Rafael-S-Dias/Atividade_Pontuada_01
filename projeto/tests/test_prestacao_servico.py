import pytest
from projeto.models.prestacao_servico import PrestacaoServico
from projeto.models.endereco import Endereco
from projeto.models.enums.unidade_federativa import UnidadeFederativa

@pytest.fixture
def prestacao_de_servico_valida():
    prestacao_servico1 = PrestacaoServico(222, "Rafael", "71988...", "Rafael@...", "45800...", "5555", "10/08/2019", "30/09/2024", Endereco("Rua A", 444, "Qd 10 Lt 7", "41.....", "Salvador", UnidadeFederativa.BAHIA))
    return prestacao_servico1

def test_contrato_inicio_valido(prestacao_de_servico_valida):
    assert prestacao_de_servico_valida.contratoInicio == "10/08/2019"

def test_contrato_fim_valido(prestacao_de_servico_valida):
    assert prestacao_de_servico_valida.contratoFim == "30/09/2024"

def test_pessoa_contrato_inicio_vazio():
    with pytest.raises(TypeError, match = "O inicio do contrato não pode ficar vazio!"):
        PrestacaoServico(222, "Rafael", "71988...", "Rafael@...", "45800...", "5555", " ", "30/09/2024", Endereco("Rua A", 444, "Qd 10 Lt 7", "41.....", "Salvador", UnidadeFederativa.BAHIA))

def test_pessoa_contrato_inicio_invalido():
    with pytest.raises(TypeError, match = "O inicio de contrato deve ser um texto!"):
        PrestacaoServico(222, "Rafael", "71988...", "Rafael@...", "45800...", "5555", 10082019, "30/09/2024", Endereco("Rua A", 444, "Qd 10 Lt 7", "41.....", "Salvador", UnidadeFederativa.BAHIA))

def test_pessoa_contrato_fim_vazio():
    with pytest.raises(TypeError, match = "O fim de contrato não pode ficar vazio!"):
        PrestacaoServico(222, "Rafael", "71988...", "Rafael@...", "45800...", "5555", "01/08/2019", " ", Endereco("Rua A", 444, "Qd 10 Lt 7", "41.....", "Salvador", UnidadeFederativa.BAHIA))

def test_pessoa_contrato_fim_invalido():
    with pytest.raises(TypeError, match = "O fim de contrato deve ser um texto!"):
        PrestacaoServico(222, "Rafael", "71988...", "Rafael@...", "45800...", "5555", "01/08/2019", 30092024, Endereco("Rua A", 444, "Qd 10 Lt 7", "41.....", "Salvador", UnidadeFederativa.BAHIA))