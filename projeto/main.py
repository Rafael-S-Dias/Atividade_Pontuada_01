import os 
from models.medico import Medico
from models.endereco import Endereco
from models.enums.sexo import Sexo
from models.enums.estado_civil import EstadoCivil
from models.enums.setor import Setor
from models.enums.unidade_federativa import UnidadeFederativa

os.system("cls || clear")

endereco1 = Endereco("11", 12, "13", "14", "15", UnidadeFederativa.BAHIA)
medico1 = Medico(1, "2", "3", "4", Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "5", "6", "7", "8", Setor.JURIDICO, 9, "10", endereco1)

print(medico1)