from auxiliares import *


def grava_existe_aluno():
    arquivo = open("aluno.txt", "a", encoding="utf-8")
    for e in lista_aluno:
        arquivo.write("%s-%s\n" % (e[0], e[1]))

def grava_aluno():
    global lista_aluno
    arquivo = open("aluno.txt", "w", encoding="utf-8")
    for e in lista_aluno:
        arquivo.write("%s-%s\n" % (e[0], e[1]))
    arquivo.close()

def grava_existe_turma():
    global lista_turma
    arquivo = open("turma.txt", "a", encoding="utf-8")
    for e in lista_professor:
        arquivo.write("%s-%s-%s-%s-%s\n" % (e[0], e[1], e[2],e[3],e[4]))
    arquivo.close()

def grava_turma():
    global lista_turma
    arquivo = open("turma.txt", "w", encoding="utf-8")
    for e in lista_turma:
        arquivo.write("%s-%s-%s-%s-%s\n" % (e[0], e[1], e[2],e[3],e[4]))
    arquivo.close()

def grava_existe_prof():
    global lista_professor
    arquivo = open("professor.txt", "a", encoding="utf-8")
    for e in lista_professor:
        arquivo.write("%s-%s-%s\n" % (e[0], e[1], e[2]))
    arquivo.close()

def grava_prof():
    global lista_professor
    arquivo = open("professor.txt","w",encoding="utf-8")
    for e in lista_professor:
        arquivo.write("%s-%s-%s\n"%(e[0],e[1],e[2]))
    arquivo.close()

def grava_disciplina():
    global lista_disciplina
    arquivo = open("disciplina.txt", "w", encoding="utf-8")
    for e in lista_disciplina:
        arquivo.write("%s-%s\n" % (e[0], e[1]))
    arquivo.close()

def grava_existe_disciplina():
    global lista_disciplina
    arquivo = open("disciplina.txt", "a", encoding="utf-8")
    for e in lista_disciplina:
        arquivo.write("%s-%s\n" % (e[0], e[1]))
    arquivo.close()