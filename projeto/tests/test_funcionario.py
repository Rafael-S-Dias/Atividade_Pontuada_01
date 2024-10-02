import pytest
from projeto.models.funcionario import Funcionario
from projeto.models.enums.estado_civil import EstadoCivil
from projeto.models.enums.sexo import Sexo
from projeto.models.endereco import Endereco
from projeto.models.enums.unidade_federativa import UnidadeFederativa
from projeto.models.enums.setor import Setor

@pytest.fixture
def funcionario_valido():
    funcionario1 = Funcionario(222, "Rafael", "71988...", "Rafael@...", Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "02/08/2001", "88888", "5555", "4444", Setor.JURIDICO, 2500, Endereco("Rua A", 444, "Qd 10 Lt 7", "41.....", "Salvador", UnidadeFederativa.BAHIA) )
    return funcionario1

def test_cpf_valido(funcionario_valido):
    assert funcionario_valido.cpf == "88888"

def test_rg_valido(funcionario_valido):
    assert funcionario_valido.rg == "5555"

def test_matricula_valido(funcionario_valido):
    assert funcionario_valido.matricula == "4444"

def test_setor_valido(funcionario_valido):
    assert funcionario_valido.setor == Setor.JURIDICO

def test_salario_valido(funcionario_valido):
    assert funcionario_valido.salario == 2500


def test_cpf_vazio():
    with pytest.raises(TypeError, match = "O CPF não pode ficar vazio!"):
        Funcionario(222, "Rafael", "71988...", "Rafael@...", Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "02/08/2001", " ", "5555", "4444", Setor.JURIDICO, 2500, Endereco("Rua A", 444, "Qd 10 Lt 7", "41.....", "Salvador", UnidadeFederativa.BAHIA) )

def test_cpf_tipo_invalido():
    with pytest.raises(TypeError, match = "O CPF deve ser um texto!"):
        Funcionario(222, "Rafael", "71988...", "Rafael@...", Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "02/08/2001", 88888, "5555", "4444", Setor.JURIDICO, 2500, Endereco("Rua A", 444, "Qd 10 Lt 7", "41.....", "Salvador", UnidadeFederativa.BAHIA) )

def test_rg_vazio():
    with pytest.raises(TypeError, match = "O RG não pode ficar vazio!"):
        Funcionario(222, "Rafael", "71988...", "Rafael@...", Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "02/08/2001", "88888", " ", "4444", Setor.JURIDICO, 2500, Endereco("Rua A", 444, "Qd 10 Lt 7", "41.....", "Salvador", UnidadeFederativa.BAHIA) )

def test_rg_tipo_invalido():
    with pytest.raises(TypeError, match = "O RG deve se manter como texto!"):
        Funcionario(222, "Rafael", "71988...", "Rafael@...", Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "02/08/2001", "88888", 5555, "4444", Setor.JURIDICO, 2500, Endereco("Rua A", 444, "Qd 10 Lt 7", "41.....", "Salvador", UnidadeFederativa.BAHIA) )
    
def test_matricula_vazio():  
    with pytest.raises(TypeError, match = "A matricula não pode ficar vazio!"):
        Funcionario(222, "Rafael", "71988...", "Rafael@...", Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "02/08/2001", "88888", "5555", " ", Setor.JURIDICO, 2500, Endereco("Rua A", 444, "Qd 10 Lt 7", "41.....", "Salvador", UnidadeFederativa.BAHIA) )

def test_matricula_tipo_invalido():  
    with pytest.raises(TypeError, match = "A matricula deve ser um texto!"):
        Funcionario(222, "Rafael", "71988...", "Rafael@...", Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "02/08/2001", "88888", "5555", 4444, Setor.JURIDICO, 2500, Endereco("Rua A", 444, "Qd 10 Lt 7", "41.....", "Salvador", UnidadeFederativa.BAHIA) )

def test_salario_vazio():
    with pytest.raises(TypeError, match = "O salário não pode ficar vazio!"):
        Funcionario(222, "Rafael", "71988...", "Rafael@...", Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "02/08/2001", "88888", "5555", "4444", Setor.JURIDICO, None, Endereco("Rua A", 444, "Qd 10 Lt 7", "41.....", "Salvador", UnidadeFederativa.BAHIA) )

def test_salario_tipo_invalido():
    with pytest.raises(TypeError, match = "O salário deve ser composto por números!"):
        Funcionario(222, "Rafael", "71988...", "Rafael@...", Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "02/08/2001", "88888", "5555", "4444", Setor.JURIDICO, "2500", Endereco("Rua A", 444, "Qd 10 Lt 7", "41.....", "Salvador", UnidadeFederativa.BAHIA) )

def test_salario_negativo():
    with pytest.raises(ValueError, match = "O salário não pode ser negativo!"):
        Funcionario(222, "Rafael", "71988...", "Rafael@...", Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "02/08/2001", "88888", "5555", "4444", Setor.JURIDICO, -2500, Endereco("Rua A", 444, "Qd 10 Lt 7", "41.....", "Salvador", UnidadeFederativa.BAHIA) )