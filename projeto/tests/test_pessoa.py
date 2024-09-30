import pytest
from models.pessoa import Pessoa
from models.endereco import Endereco
from models.enums.unidade_federativa import UnidadeFederativa

@pytest.fixture
def pessoa_valida():
