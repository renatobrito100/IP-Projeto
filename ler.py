from auxiliares import *
def ler_prof():
    global lista_professor
    lista_ou_arquivo = input("Deseja ver em lista[lista] ou arquivo[arquivo]: ")
    if(lista_ou_arquivo == "arquivo"):
        arquivo = open("professor.txt", "r", encoding="utf-8")
        lista = []
        for dados in arquivo.readlines():
            nome,cpf,departamento = dados.strip("\n").split("-")
            lista.append([nome,cpf,departamento])
        for x in range(len(lista)):
            print(" ".join(lista[x]))
        arquivo.close()
    else:
        for x in range(len(lista_professor)):
            print(" ".join(lista_professor[x]))

def ler_turma():
    global lista_turma
    lista_ou_arquivo = input("Deseja ver em lista[lista] ou arquivo[arquivo]: ")
    if(lista_ou_arquivo == "arquivo"):
        arquivo = open("turma.txt", "r", encoding="utf-8")
        lista = []
        for dados in arquivo.readlines():
            codigo_da_turma,periodo,codido_disciplina,cpf_professor,cpf_aluno = dados.strip("\n").split("-")
            lista = [codigo_da_turma,periodo,codido_disciplina,cpf_professor,cpf_aluno]
            p = ''            
            for x in range(len(lista)):
                p += lista[x] + '\n'
            print(p)
        arquivo.close()
    else:
        p = ''
        for x in range(len(lista_turma)):
            p += str(lista_turma[x]) + '\n'
        print(p)

def ler_aluno():
    global lista_aluno
    lista_ou_arquivo = input("Deseja ver em lista[lista] ou arquivo[arquivo]: ")
    if (lista_ou_arquivo == "arquivo"):
        arquivo = open("aluno.txt" "r", encoding="utf-8")
        lista = []
        for dados in arquivo.readlines():
            nome, cpf = dados.strip("\n").split("-")
            lista.append([nome, cpf])
        for x in range(len(lista)):
            print(" ".join(lista[x]))
        arquivo.close()
    else:
        for x in range(len(lista_aluno)):
            print(" ".join(lista_aluno[x]))

def ler_disciplina():
    global lista_disciplina
    lista_ou_arquivo = input("Deseja ver em lista[lista] ou arquivo[arquivo]: ")
    if (lista_ou_arquivo == "arquivo"):
        arquivo = open("disciplina.txt", "r", encoding="utf-8")
        lista = []
        for dados in arquivo.readlines():
            codigo, nome = dados.strip("\n").split("-")
            lista.append([codigo,nome])
        for x in range(len(lista)):
            print(" ".join(lista[x]))
        arquivo.close()
    else:
        for x in range(len(lista_disciplina)):
            print(" ".join(lista_disciplina[x]))
