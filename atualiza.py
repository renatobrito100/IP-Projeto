from auxiliares import *
from grava import *
def atualiza_prof():
    global lista_professor
    perg = input("Se deseja atualizar em lista digite [lista], caso contrário, [arquivo]: ")
    if(perg == "lista"):
        name = pede_nome()
        for x in range(len(lista_professor)):
            if(lista_professor[x][0]) == name:
                new = ''
                for e in range(len(lista_professor[x])):
                    new += lista_professor[x][e] + " "
                print(new)
                nome = pede_nome()
                cpf = valida_cpf()
                departamento = pede_departamento()
                lista_professor[x] = [nome,cpf,departamento]
    elif(perg == 'arquivo'):
        name = pede_nome()
        arq = open('professor.txt', 'r')
        lista_momento = []
        for line in arq:
            tira = line.split('-')
            tira[2] = tira[2].split('\n')
            tira[2] = tira[2][0]
            lista_momento.append(tira)
        for i in range(len(lista_momento)):
            if(lista_momento[i][0] == name):
                new = ''
                for e in range(len(lista_momento[i])):
                    new += lista_momento[i][e] + " "
                print(new)
                nome = pede_nome()
                cpf = valida_cpf()
                departamento = pede_departamento()
                lista_momento[i] = [nome,cpf,departamento]
        grava_prof(lista_momento)
     # else:
        #    print("Não encontrado")
    #elif(perg == "arquivo"):
     #   nome_arq = input("Digite o nome do arquivo[nome.txt]: ")
      #  name = pede_nome()
       # read = nome_arq.redlines()
        #for x in range(len(read)):
         #   if (read[x][0]) == name:
          #      new = ''
           #     for e in range(len(read[x])):
            #        new += read[x][e] + " "
             #   print(new)
              #  nome = pede_nome()
               # cpf = valida_cpf()
                #departamento = pede_departamento()
                #lista_professor[x] = [nome, cpf, departamento]
                #arquivo.close()
        #else:
         #   print("Não encontrado")
          #      for info2 in range(len(lista_professor)):
           #         if(lista_professor[info2][0] == name):
            #            nome_arq = input("Digite o nome do arquivo[nome.txt]: ")
             #           arquivo2 = open(nome_arq,"w",enconding = "utf-8")
              #          nome = pede_nome()
               #         cpf = valida_cpf()
                #        departamento = pede_departamento()
                 #       lista_professor[info2] = ([nome,cpf,departamento])
                  #      print(lista_professor)
                   #     for e in lista_professor:
                    #        arquivo.write("%s-%s-%s\n" % (e[0], e[1], e[2]))
                #arquivo.close()"""
