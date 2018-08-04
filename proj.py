from auxiliares import *
from cria import *
from ler import *
from atualiza import *
from apaga import *
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
        elif(nova_escolha == 2):
            ler_turma()
        elif(nova_escolha == 3):
            ler_aluno()
        elif(nova_escolha == 4):
            ler_disciplina()
    elif(escolha == 3):
        printa()
        nova_escolha = menu2()
        if(nova_escolha == 1):
            atualiza_prof()
    elif(escolha == 4):
        printa()
        nova_escolha = menu2()
        if(nova_escolha == 1):
            apaga_prof()
