import os

dicionario_de_restaurantes = {"Arvo": ["Moderna", "$$$$", 4.6, "Espinheiro"], "Parraxaxá": ["Regional", "$$", 4.3, "Boa Viagem"]}

os.system("clear") or None

print("Olá, bem vindo ao FRESERVO!\n\n")
restaurante_selecionado = ""

while restaurante_selecionado == "":
    print("Escolha como deseja pesquisar o restaurante.\n\n"\
      "Para pesquisar pelo:\n"\
      "-Nome do estabelecimento: Digite 1\n"\
      "-Filtro de Culinária: Digite 2\n"\
      "-Filtro de Faixa de Preço: Digite 3\n"\
      "-Filtro de Avaliação Média: Digite 4\n"\
      "-Filtro de Localização: Digite 5\n"
    )
    escolha = input("Qual a opção desejada. Digite de 1 a 5: ")

    lista_restaurantes_encontrados = []

    os.system("clear") or None

    try:
        escolha = int(escolha)
        if escolha in [1, 2, 3, 4, 5]:
            if escolha == 1:
                estabelecimento = input("Digite o nome do estabelecimento: ")
                for key in dicionario_de_restaurantes:
                    if estabelecimento.lower() in key.lower():
                        lista_restaurantes_encontrados.append(key)
            elif escolha == 2:
                culinaria = input("Escolha o tipo de culinária:\n"
                                  "1: Regional\n"\
                                  "2: Italiana\n"\
                                  "3: Japonesa\n"\
                                  "4: Portuguesa\n"\
                                  "5: Chinesa\n"\
                                  "6: Peruana\n"\
                                  "7: Tailandesa\n"\
                                  "8: Árabe\n"\
                                  "9: Hamburuger\n"\
                                  "10: Pizza\n"\
                                  "11: Moderna\n"\
                                  "12: Frutos do Mar\n"\
                                  "13: Bar\n"\
                                  "14: Café\n"\
                                  "Qual a opção desejada: ")
                if culinaria in ["Regional", "Italiana", "Japonesa", "Portuguesa", "Chinesa", "Peruana", "Tailandesa", "Árabe", "Hamburguer", "Pizza", "Moderna", "Frutos do Mar", "Bar", "Café"]:
                    for key in dicionario_de_restaurantes:
                        if culinaria.lower() in dicionario_de_restaurantes[key][0].lower():
                            lista_restaurantes_encontrados.append(key) 
            elif escolha == 3:
                faixa_preco = input("Qual a faixa de preço do estabelecimento que você deseja :\n"
                                    "1: $\n"\
                                    "2: $$\n"\
                                    "3: $$$\n"\
                                    "4: $$$$\n"\
                                    "5: $$$$$\n"\
                                    "Qual a opção desejada: ")
                if faixa_preco in ["$", "$$", "$$$", "$$$$", "$$$$$"]:
                    for key in dicionario_de_restaurantes:
                        if faixa_preco == dicionario_de_restaurantes[key][1]:
                            lista_restaurantes_encontrados.append(key)
                elif int(faixa_preco) in [1, 2, 3, 4, 5]:
                    for key in dicionario_de_restaurantes:
                        if (int(faixa_preco) * "$") == dicionario_de_restaurantes[key][1]:
                            lista_restaurantes_encontrados.append(key)
            elif escolha == 4:
                avaliacao = input("Digite a avaliação mínima (de 1 a 5): ")
                if avaliacao.replace(",", "", 1).isdigit():
                    for key in dicionario_de_restaurantes:
                        if float(avaliacao.replace(",", ".")) <= dicionario_de_restaurantes[key][2]:
                            lista_restaurantes_encontrados.append(key)
            elif escolha == 5:
                localizacao = input("Digite o bairro: ")
                for key in dicionario_de_restaurantes:
                    if localizacao.lower() in dicionario_de_restaurantes[key][3].lower():
                        lista_restaurantes_encontrados.append(key)

            os.system("clear") or None
            houve_selecao = False
            while not houve_selecao:
                if len(lista_restaurantes_encontrados) > 0 :
                    print("Foi/foram encontrado(s) o(s) seguinte(s) estabelecimentos:\n")
                    for i in range(len(lista_restaurantes_encontrados)):
                        print(f"{i+1}: {lista_restaurantes_encontrados[i]}")
                    restaurante_selecionado = input("\nInsira o número ou nome do estabelecimento que deseja selecionar.\nCaso deseje selecionar novamente o método de pesquisa do estabelecimento digite 0 ou nada: ")
                    if restaurante_selecionado.isdigit():
                        if int(restaurante_selecionado) == 0:
                            os.system("clear") or None
                            restaurante_selecionado = ""
                            houve_selecao = True
                        elif int(restaurante_selecionado) <= len(lista_restaurantes_encontrados):
                            restaurante_selecionado = lista_restaurantes_encontrados[int(restaurante_selecionado) - 1]
                            houve_selecao = True
                        else:
                            restaurante_selecionado = ""
                            os.system("clear") or None
                            print("------------------------------------------------------------")
                            print("\nA opção digitada não existe, por favor tente novamente.\n")
                            print("------------------------------------------------------------")
                    else:
                        if restaurante_selecionado == "" :
                            os.system("clear") or None
                            restaurante_selecionado = ""
                            houve_selecao = True
                        elif restaurante_selecionado.capitalize() in lista_restaurantes_encontrados:
                            restaurante_selecionado = restaurante_selecionado.capitalize()
                            houve_selecao = True
                        else:
                            restaurante_selecionado = ""
                            os.system("clear") or None
                            print("------------------------------------------------------------")
                            print("\nA opção digitada não existe, por favor tente novamente.\n")
                            print("------------------------------------------------------------")
                else:
                    houve_selecao = True
                    os.system("clear") or None
                    print("------------------------------------------------------------")
                    print("\nNão foram encontrados resultados.\n")
                    print("------------------------------------------------------------")
                    print("\nSelecione novamente o método de pesquisa do estabelecimento.\n")
        
        else:
            os.system("clear") or None
            print("------------------------------------------------------------")
            print("\nA opção digitada não existe, por favor tente novamente.\n")
            print("------------------------------------------------------------")
    except ValueError: 
        os.system("clear") or None
        print("------------------------------------------------------------")
        print("\nA opção digitada não existe, por favor tente novamente.\n")
        print("------------------------------------------------------------")

os.system("clear") or None
print(f"Você escolheu o estabelecimento: {restaurante_selecionado}")

