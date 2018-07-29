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
            lista = input("CPF /EX:[abc.def.ghi-jk]/: ")
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
                return lista.replace('-','').replace('.','')
            else:
                print("CPF inválido")
        except:
            print("CPF inválido")

def pede_nome():
    nome = (input("Nome: "))
    return nome

def cpf_professor():
    cpf = (input("CPF do professor: "))
    return cpf

def cpf_aluno():
    cpf = (input("CPF do aluno(s): "))
    return cpf

def pede_departamento():
    dpto = (input("Departamento: "))
    return dpto

def codigo_turma():
    turma = (input("Código da turma: "))
    return turma

def codigo_disciplina():
    disc = (input("Código da disciplina: "))
    return disc

def pede_periodo():
    per = (input("Período: "))
    return per