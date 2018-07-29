from auxiliares import *
from cria import *
from ler import *

def menu2():
    print("""
========MENU==========
1 - Professor
2 - Turma
3 - Aluno
4 - Disciplinan
    
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
'''https://drive.google.com/file/d/0B3ouk05r7UFPaWNna1NYMWlpZTQ/view
https://drive.google.com/file/d/0B3ouk05r7UFPT0hQVXZiQUM4VEU/view'''