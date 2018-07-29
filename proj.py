lista_professor = []
lista_disciplina = []
lista_aluno = []
lista_turma = []
#Criando funçôes auxiliares
def printa():
    for x in range(100):
        print()
def valida_cpf():
    while True:
        try:
            lista = list(input("CPF /EX:[abc.def.ghi-jk]/: "))
            soma1 = 0
            soma2 = 0
            contador1 = 1
            contador2 = 9
            confere1 = int(lista[12])
            confere2 = int(lista[13])
            for k in range(11):
                if lista[k].isalnum():
                    numero = int(lista[k])
                    soma1 += numero * contador1
                    soma2 += numero * contador2
                    contador1 += 1
                    contador2 -= 1
            resto2 = (soma2 % 11) % 10
            resto1 = (soma1 % 11) % 10
            if confere1 == resto1 and confere2 == resto2:
                print("CPF válido")
                break
            else:
                print("CPF inválido")
        except:
            print("CPF inválido")
def pede_nome():
    return(input("Nome: "))

def grava_existe_aluno():
    nome_arq = input("Digite o nome do arquivo[nome.txt]: ")
    arquivo = open(nome_arq, "a", encoding="utf-8")
    for e in lista_aluno:
        arquivo.write("%s-%s\n" % (e[0], e[1]))

def grava_aluno():
    global lista_aluno
    nome_arq = input("Digite o nome do arquivo [nome.txt]: ")
    arquivo = open(nome_arq, "w", encoding="utf-8")
    for e in lista_aluno:
        arquivo.write("%s-%s\n" % (e[0], e[1]))
    arquivo.close()

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
        conjunto_cpf.append(cpf)
    quantos_alunos = int(input("Digite o número de alunos: "))
    conjunto_cpf_aluno = []
    for e in range(quantos_alunos):
        cpf_alunos = valida_cpf()
        conjunto_cpf_aluno.append(cpf_alunos)
    lista_turma.append([codigo_da_turma,periodo,codigo_da_disciplina,conjunto_cpf,conjunto_cpf_aluno])
    pergunta = input("Se deseja gravar [sim],caso contrário [nao]:")
    if(pergunta == "sim"):
        pergunta2 = input("Se o arquivo existe [sim],caso contrário [nao]")
        if(pergunta2 == "sim"):
            grava_existe_turma()
        else:
            grava_turma()

def grava_existe_turma():
    global lista_turma
    nome_arq = input("Digite o nome do arquivo[nome.txt]: ")
    arquivo = open(nome_arq, "a", encoding="utf-8")
    for e in lista_professor:
        arquivo.write("%s-%s-%s-%s-%s\n" % (e[0], e[1], e[2],e[3],e[4]))
    arquivo.close()
def grava_turma():
    global lista_turma
    nome_arq = input("Digite o nome do arquivo [nome.txt]: ")
    arquivo = open(nome_arq, "w", encoding="utf-8")
    for e in lista_turma:
        arquivo.write("%s-%s-%s-%s-%s\n" % (e[0], e[1], e[2],e[3],e[4]))
    arquivo.close()
def cpf_professor():
    return(input("CPF do professor: "))

def cpf_aluno():
    return(input("CPF do aluno(s): "))

def pede_departamento():
    return(input("Departamento: "))

def codigo_turma():
    return(input("Código da turma: "))

def codigo_disciplina():
    return(input("Código da disciplina: "))

def pede_periodo():
    return(input("Período: "))

def grava_existe_prof():
    global lista_professor
    nome_arq = input("Digite o nome do arquivo[nome.txt]: ")
    arquivo = open(nome_arq, "a", encoding="utf-8")
    for e in lista_professor:
        arquivo.write("%s-%s-%s\n" % (e[0], e[1], e[2]))
    arquivo.close()

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

def grava_prof():
    global lista_professor
    nome_arq = input("Digite o nome do arquivo [nome.txt]: ")
    arquivo = open(nome_arq,"w",encoding="utf-8")
    for e in lista_professor:
        arquivo.write("%s-%s-%s\n"%(e[0],e[1],e[2]))
    arquivo.close()

def grava_disciplina():
    global lista_disciplina
    nome_arq = input("Digite o nome do arquivo [nome.txt]: ")
    arquivo = open(nome_arq, "w", encoding="utf-8")
    for e in lista_disciplina:
        arquivo.write("%s-%s\n" % (e[0], e[1]))
    arquivo.close()

def grava_existe_disciplina():
    global lista_disciplina
    nome_arq = input("Digite o nome do arquivo[nome.txt]: ")
    arquivo = open(nome_arq, "a", encoding="utf-8")
    for e in lista_disciplina:
        arquivo.write("%s-%s\n" % (e[0], e[1]))
    arquivo.close()

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

def ler_prof():
    global lista_professor
    lista_ou_arquivo = input("Deseja ver em lista[lista] ou arquivo[arquivo]: ")
    if(lista_ou_arquivo == "arquivo"):
        nome_arq = input("Digite o nome do arquivo[nome.txt]: ")
        arquivo = open(nome_arq, "r", encoding="utf-8")
        lista = []
        for dados in arquivo.readlines():
            nome,cpf,departamento = dados.strip("\n").split("-")
            lista.append([nome,cpf,departamento])
        pergunta = input("Se deseja ver todos os professores [sim],caso contrário [nao]: ")
        if(pergunta == "sim"):
            for x in range(len(lista)):
                print(" ".join(lista[x]))
        else:
            pergunta2 = input("Digite o nome do professor a procurar: ")
            flag = 0
            for i in range(len(lista)):
                if(pergunta2 in lista[i]):
                    flag = 1
                    break
                else:
                    flag = 0
            if(flag == 1):
                print("Encontrado:")
                for k in range(len(lista[i])):
                    print(lista[i][k])

            else:
                print("Não encontrado")
        arquivo.close()
    else:
        pergunta = input("Se deseja ver todos os professores [sim],caso contrário [nao]: ")
        if (pergunta == "sim"):
            for x in range(len(lista_professor)):
                print(" ".join(lista_professor[x]))
        else:
            pergunta2 = input("Digite o nome do professor a procurar: ")
            flag = 0
            for i in range(len(lista_professor)):
                if (pergunta2 in lista_professor[i]):
                    flag = 1
                    break
                else:
                    flag = 0
            if (flag == 1):
                print("Encontrado:")
                for k in range(len(lista_professor[i])):
                    print(lista_professor[i][k])

            else:
                print("Não encontrado")
def menu2():
    print("""
========MENU==========
1 - Professor
2 - Turma
3 - Aluno
4 - Disciplina
    
5 - Voltar
======================""")
    nova_escolha = int(input("""
Escolha:"""))
    return nova_escolha
def menu():
    print(""" 
========MENU==========
1 - Criação
2 - Consulta
3 - Atualização 
4 - Excluir
5 - Relatórios #quando fizer deve fazer outro menu p atas de exercicio e tal
    
0 - sair
======================""")
    escolha = int(input("""
Escolha:"""))
    return escolha

while True:
    escolha = menu()
    print(escolha)
    if(escolha == 0):
        print("O programa encerrou")
        break
    elif(escolha == 1):
        printa()
        nova_escolha = menu2()
        if(nova_escolha == 1):
            cria_prof()
        elif(nova_escolha == 2):
            cria_turma()
        elif(nova_escolha == 3):
            cria_aluno()
        elif(nova_escolha == 4):
            cria_disciplina()
    elif(escolha == 2):
        printa()
        nova_escolha = menu2()
        if(nova_escolha == 1):
            ler_prof()
    '''elif (opcao == 2):

    elif (opcao == 3):
    elif (opcao == 4):
    elif (opcao == 5):
    elif (opcao == 6):
    elif (opcao == 7):
    elif (opcao == 8):
    elif (opcao == 9):
    elif (opcao == 10):
    elif (opcao == 11):
    elif (opcao == 12):
    elif (opcao == 13):
    elif (opcao == 14):
    elif (opcao == 15):
    elif (opcao == 16):'''
https://drive.google.com/file/d/0B3ouk05r7UFPaWNna1NYMWlpZTQ/view
https://drive.google.com/file/d/0B3ouk05r7UFPT0hQVXZiQUM4VEU/view