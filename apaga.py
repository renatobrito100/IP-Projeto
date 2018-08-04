from auxiliares import *
def apaga_prof():
    perg =input("Se deseja apagar em lista digite [lista],caso contrário, [arquivo]: ")
    if(perg == "lista"):
        name = pede_nome()
        contador = 0
        for dados in range(len(lista_professor)):
            if(name in lista_professor[dados]):
                print("Encontrado")
                print(lista_professor)
                break
            else:
                contador += 1
        if(contador == len(lista_professor)):
            print("Não encontrado")
        else:
            lista_professor.remove(lista_professor[dados])
            print(lista_professor)
    elif(perg == "arquivo"):
       volta_lista_prof()
       name = pede_nome()
       contador = 0
       for dados in range(len(lista_professor)):
           if (name in lista_professor[dados]):
               print("Encontrado")
               print(lista_professor)
               break
           else:
               contador += 1
       if (contador == len(lista_professor)):
           print("Não encontrado")
       else:
            lista_professor.remove(lista_professor[dados])
            print(lista_professor)
            arquivo = open("professor.txt", "w", encoding="utf-8")
            for j in range(len(lista_professor)):
                arquivo.write("%s-%s-%s\n"%(j[0],str(j[1]),j[2]))
            arquivo.close()
    #elif(perg == "aquivo"):
     #   volta_lista_prof()