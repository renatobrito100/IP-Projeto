from auxiliares import *
from grava import *

def cria_aluno():
    global lista_aluno
    nome = pede_nome()
    cpf = valida_cpf()
    lista_aluno.append([nome,cpf])
    pergunta = input("Se deseja gravar [sim],caso contrário [nao]:")
    if (pergunta == "sim"):
        pergunta2 = input("Se o arquivo existe [sim],caso contrário [nao]")
        if (pergunta2 == "sim"):
            grava_existe_aluno()
        else:
            grava_aluno()

def cria_turma():
    global lista_turma
    codigo_da_turma = codigo_turma()
    periodo = pede_periodo()
    codigo_da_disciplina = codigo_disciplina()
    quantos_professores = int(input("Digite o número de profesores que ministram a turma: "))
    conjunto_cpf = []
    for i in range(quantos_professores):
        cpf = valida_cpf()
        conjunto_cpf.append(int(cpf))
    quantos_alunos = int(input("Digite o número de alunos: "))
    conjunto_cpf_aluno = []
    for e in range(quantos_alunos):
        cpf_alunos = valida_cpf()
        conjunto_cpf_aluno.append(int(cpf_alunos))
    lista_turma.append([codigo_da_turma,periodo,codigo_da_disciplina,conjunto_cpf,conjunto_cpf_aluno])
    pergunta = input("Se deseja gravar [sim],caso contrário [nao]:")
    if(pergunta == "sim"):
        pergunta2 = input("Se o arquivo existe [sim],caso contrário [nao]")
        if(pergunta2 == "sim"):
            grava_existe_turma()
        else:
            grava_turma()


def cria_prof():
    global lista_professor
    nome = pede_nome()
    cpf = valida_cpf()
    departamento = pede_departamento()
    lista_professor.append([nome,cpf,departamento])
    pergunta = input("Se deseja gravar [sim],caso contrário [nao]:")
    if(pergunta == "sim"):
        pergunta2 = input("Se o arquivo existe [sim],caso contrário [nao]")
        if(pergunta2 == "sim"):
            grava_existe_prof()
        else:
            grava_prof()


def cria_disciplina():
    global lista_disciplina
    codigo = codigo_disciplina()
    nome = pede_nome()
    lista_disciplina.append([codigo,nome])
    pergunta = input("Se deseja gravar [sim],caso contrário [nao]:")
    if(pergunta == "sim"):
        pergunta2 = input("Se o arquivo existe [sim],caso contrário [nao]")
        if(pergunta2 == "sim"):
            grava_existe_disciplina()
        else:
            grava_disciplina()
