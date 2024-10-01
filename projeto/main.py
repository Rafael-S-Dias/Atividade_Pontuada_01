import os 
from models.medico import Medico
from models.advogado import Advogado
from models.engenheiro import Engenheiro
from models.cliente import Cliente
from models.fornecedor import Fornecedor
from models.prestacao_servico import PrestacaoServico
from models.endereco import Endereco
from models.enums.sexo import Sexo
from models.enums.estado_civil import EstadoCivil
from models.enums.setor import Setor
from models.enums.unidade_federativa import UnidadeFederativa

os.system("cls || clear")

endereco1 = Endereco("Rua B", 202, "644", "41100...", "Salvador", UnidadeFederativa.BAHIA)
medico1 = Medico(1111, "Robert", "719999", "Bob_B@...", Sexo.MASCULINO, EstadoCivil.CASADO, "01/06/1988", "262", "298", "281", Setor.SAUDE, 10 ,"289", endereco1)
advogado1 = Advogado(2222, "Eddard", "719888", "NedStark@...", Sexo.MASCULINO, EstadoCivil.CASADO, "01/01/1989", "263", "298", "281", Setor.JURIDICO, 6 ,"289", endereco1)
engenheiro1 = Engenheiro(3333, "Stannis", "7198899", "Stannis_theMannis@...", Sexo.MASCULINO, EstadoCivil.CASADO, "01/01/1990", "264", "230", "281",Setor.ENGENHARIA, 1, "230", endereco1 )
cliente1 = Cliente(4444, "Jon", "7197777", "Bastard@...", Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "01/01/2009", 998, endereco1)
fornecedor1 = Fornecedor(5555, "Jaqen", "71989898", "ValarMorgulis@...", "?", "299", "Morte", endereco1 )
prestacao_servico1 = PrestacaoServico(6666, "Jon Con", "71987666", "O_Grifo_Renascido@...", "261", "231", "282", "232", endereco1)


print(medico1)
print(advogado1)
print(engenheiro1)
print(cliente1)
print(fornecedor1)
print(prestacao_servico1)


