import os
from datetime import date, timedelta, datetime

dicionario_de_restaurantes = {
    "Cais Rooftop Lounge Bar": [
        "Brasileira",
        "$$$$",
        4.0,
        "Recife Antigo",
        ["Tarde", "Noite"],
    ],
    "Lupi Pizzeria": ["Italiana", "$$$", 5.0, "Boa Viagem", ["Tarde", "Noite"]],
    "Entre amigos o Bode": ["Brasileira", "$$", 4.5, "Boa Viagem", ["Tarde", "Noite"]],
    "Olinda Art&Grill": ["Frutos Do Mar", "$$$", 4.5, "Olinda", ["Tarde", "Noite"]],
    "Coco Bambu Recife": [
        "Brasileira",
        "$$$",
        5.0,
        "Boa Viagem",
        ["Manhã", "Tarde", "Noite"],
    ],
    "Granpasta": ["Italiana", "$$", 5.0, "Boa Viagem", ["Tarde", "Noite"]],
    "Adega do Futuro": ["Contemporânea", "$$$", 5.0, "Graças", ["Tarde", "Noite"]],
    "Tasca Ibérica": ["Portuguesa", "$$$", 5.0, "Olinda", ["Tarde", "Noite"]],
    "Restaurante Leite": [
        "Brasileira",
        "$$$$",
        4.5,
        "Santo Antônio",
        ["Tarde", "Noite"],
    ],
    "Chiwake": ["Peruana", "$$$$", 4.5, "Graças", ["Tarde", "Noite"]],
    "Taberna Japonesa Quina do Futuro": [
        "Japonesa",
        "$$$$",
        4.5,
        "Aflitos",
        ["Tarde", "Noite"],
    ],
    "Mingus Zé Maria": ["Francesa", "$$$$", 4.5, "Pina", ["Tarde", "Noite"]],
    "Ça Va": ["Francesa", "$$$$", 4.5, "Boa Viagem", ["Tarde", "Noite"]],
    "My Burguer": ["Americana", "$$", 4.5, "Poço da Panela", ["Tarde", "Noite"]],
    "Vasto Recife": ["Americana", "$$$$", 5.0, "Boa Viagem", ["Tarde", "Noite"]],
}
lista_culinaria = [
    "Brasileira",
    "Italiana",
    "Japonesa",
    "Portuguesa",
    "Chinesa",
    "Francesa",
    "Peruana",
    "Tailandesa",
    "Árabe",
    "Americana",
    "Peruana",
    "Portuguesa",
    "Pizza",
    "Contemporânea",
    "Frutos Do Mar",
    "Bar",
    "Café",
]
lista_faixa_preco = ["$", "$$", "$$$", "$$$$", "$$$$$"]


def printItemsLista(lista: []):
    for i in range(len(lista)):
        print(f"{i+1}: {lista[i]}")


def criarListaNumeros(lista: []):
    nova_lista = []
    for i in range(len(lista)):
        nova_lista.append(i + 1)
    return nova_lista


def realizarReservaRestaurante(restaurante):
    infos_reserva = {}
    lista_turnos_disponiveis = dicionario_de_restaurantes[restaurante][4]
    lista_campos_reserva = ["Quantidade de Pessoas", "Nome", "Telefone", "Email"]
    data_atual = date.today()
    data_selecionada = ""
    lista_datas = []
    turno_selecionado = ""

    for i in range(5):
        dias_soma = timedelta(days=i)
        lista_datas.append((data_atual + dias_soma).strftime("%d/%m/%Y"))

    os.system("clear") or None
    while data_selecionada == "":
        print("Qual a data que deseja realizar a reserva:\n")

        for i in range(len(lista_datas)):
            print(f"{i+1}: {str(lista_datas[i])}")
        data_selecionada = input(
            "\nInsira o número ou data que deseja selecionar."
            "\nCaso deseje voltar a selecionar novamente o método de pesquisa do estabelecimento digite 0 ou nada: "
        )
        if data_selecionada.isdigit():
            if int(data_selecionada) == 0:
                os.system("clear") or None
                return ""
            elif int(data_selecionada) <= len(lista_datas):
                data_selecionada = str(lista_datas[int(data_selecionada) - 1])
            else:
                data_selecionada = ""
                os.system("clear") or None
                print("===================================================")
                print("\nA opção digitada não existe, por favor tente novamente.\n")
                print("===================================================")
        else:
            if data_selecionada == "":
                os.system("clear") or None
                return ""
            elif (
                datetime.strptime(data_selecionada, "%d/%m/%Y").strftime("%d/%m/%Y")
                in lista_datas
            ):
                data_selecionada = data_selecionada
            else:
                data_selecionada = ""
                os.system("clear") or None
                print("===================================================")
                print("\nA opção digitada não existe, por favor tente novamente.\n")
                print("===================================================")

    os.system("clear") or None

    while turno_selecionado == "":
        print(
            f"Foi/foram encontrado(s) o(s) seguinte(s) turnos disponíveis para reserva na data {data_selecionada}:\n"
        )
        for i in range(len(lista_turnos_disponiveis)):
            print(f"{i+1}: {lista_turnos_disponiveis[i]}")
        turno_selecionado = input(
            "\nInsira o número ou nome do turno que deseja selecionar."
            "\nCaso deseje voltar a selecionar novamente o método de pesquisa do estabelecimento digite 0 ou nada: "
        )
        if turno_selecionado.isdigit():
            if int(turno_selecionado) == 0:
                os.system("clear") or None
                return ""
            elif int(turno_selecionado) <= len(lista_turnos_disponiveis):
                turno_selecionado = lista_turnos_disponiveis[int(turno_selecionado) - 1]
            else:
                turno_selecionado = ""
                os.system("clear") or None
                print("===================================================")
                print("\nA opção digitada não existe, por favor tente novamente.\n")
                print("===================================================")
        else:
            if turno_selecionado == "":
                os.system("clear") or None
                return ""
            elif turno_selecionado in lista_turnos_disponiveis:
                turno_selecionado = turno_selecionado
            else:
                turno_selecionado = ""
                os.system("clear") or None
                print("===================================================")
                print("\nA opção digitada não existe, por favor tente novamente.\n")
                print("===================================================")

    os.system("clear") or None

    infos_reserva["Restaurante"] = restaurante
    infos_reserva["Data"] = data_selecionada
    infos_reserva["Turno"] = turno_selecionado

    os.system("clear") or None

    print(
        "Para finalizar a reserva por favor insira as informações solicitadas abaixo:"
    )
    for campo in lista_campos_reserva:
        info_usuario = input(f"{campo}: ")
        infos_reserva[campo] = info_usuario

    os.system("clear") or None
    print(
        "===================================================\n"
        "RESERVA FINALIZADA!\n"
        "===================================================\n"
        "\nAbaixo segue resumo da reserva:\n"
    )
    for key in infos_reserva:
        print(f"{key}: {infos_reserva[key]}")

    with open("reservas.txt", "a") as arquivo:
        arquivo.write(f"\n{infos_reserva['Nome']} = {infos_reserva}")

    return restaurante


os.system("clear") or None

print("Olá, bem vindo ao FRESERVO!\n\n")
restaurante_selecionado = ""

while restaurante_selecionado == "":
    print(
        "Escolha como deseja pesquisar o restaurante.\n\n"
        "Para pesquisar pelo:\n"
        "Digite 1: Nome do estabelecimento\n"
        "Digite 2: Filtro de Culinária\n"
        "Digite 3: Filtro de Faixa de Preço\n"
        "Digite 4: Filtro de Avaliação Média\n"
        "Digite 5: Filtro de Localização\n"
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
                print("Escolha o tipo de culinária:")
                printItemsLista(lista_culinaria)
                culinaria = input("Qual a opção desejada: ")
                if culinaria in lista_culinaria:
                    for key in dicionario_de_restaurantes:
                        if (
                            culinaria.lower()
                            in dicionario_de_restaurantes[key][0].lower()
                        ):
                            lista_restaurantes_encontrados.append(key)
                elif int(culinaria) in criarListaNumeros(lista_culinaria):
                    for key in dicionario_de_restaurantes:
                        if (
                            lista_culinaria[int(culinaria) - 1]
                            == dicionario_de_restaurantes[key][0]
                        ):
                            lista_restaurantes_encontrados.append(key)
            elif escolha == 3:
                print("Qual a faixa de preço do estabelecimento que você deseja :")
                printItemsLista(lista_faixa_preco)
                faixa_preco = input("Qual a opção desejada: ")
                if faixa_preco in lista_faixa_preco:
                    for key in dicionario_de_restaurantes:
                        if faixa_preco == dicionario_de_restaurantes[key][1]:
                            lista_restaurantes_encontrados.append(key)
                elif int(faixa_preco) in criarListaNumeros(lista_faixa_preco):
                    for key in dicionario_de_restaurantes:
                        if (int(faixa_preco) * "$") == dicionario_de_restaurantes[key][
                            1
                        ]:
                            lista_restaurantes_encontrados.append(key)
            elif escolha == 4:
                avaliacao = input("Digite a avaliação mínima (de 1 a 5): ")
                if avaliacao.replace(",", "", 1).isdigit():
                    for key in dicionario_de_restaurantes:
                        if (
                            float(avaliacao.replace(",", "."))
                            <= dicionario_de_restaurantes[key][2]
                        ):
                            lista_restaurantes_encontrados.append(key)
            elif escolha == 5:
                localizacao = input("Digite o bairro: ")
                for key in dicionario_de_restaurantes:
                    if (
                        localizacao.lower()
                        in dicionario_de_restaurantes[key][3].lower()
                    ):
                        lista_restaurantes_encontrados.append(key)

            os.system("clear") or None
            houve_selecao = False
            while not houve_selecao:
                if len(lista_restaurantes_encontrados) > 0:
                    print(
                        "Foi/foram encontrado(s) o(s) seguinte(s) estabelecimentos:\n"
                    )
                    for i in range(len(lista_restaurantes_encontrados)):
                        print(f"{i+1}: {lista_restaurantes_encontrados[i]}")
                    restaurante_selecionado = input(
                        "\nInsira o número ou nome do estabelecimento que deseja selecionar."
                        "\nCaso deseje selecionar novamente o método de pesquisa do estabelecimento digite 0 ou nada: "
                    )
                    if restaurante_selecionado.isdigit():
                        if int(restaurante_selecionado) == 0:
                            os.system("clear") or None
                            restaurante_selecionado = ""
                            houve_selecao = True
                        elif int(restaurante_selecionado) <= len(
                            lista_restaurantes_encontrados
                        ):
                            restaurante_selecionado = lista_restaurantes_encontrados[
                                int(restaurante_selecionado) - 1
                            ]
                            restaurante_selecionado = realizarReservaRestaurante(
                                restaurante_selecionado
                            )
                            houve_selecao = True
                        else:
                            restaurante_selecionado = ""
                            os.system("clear") or None
                            print("===================================================")
                            print(
                                "\nA opção digitada não existe, por favor tente novamente.\n"
                            )
                            print("===================================================")
                    else:
                        if restaurante_selecionado == "":
                            os.system("clear") or None
                            restaurante_selecionado = ""
                            houve_selecao = True
                        elif (
                            restaurante_selecionado.capitalize()
                            in lista_restaurantes_encontrados
                        ):
                            restaurante_selecionado = (
                                restaurante_selecionado.capitalize()
                            )
                            restaurante_selecionado = realizarReservaRestaurante(
                                restaurante_selecionado
                            )
                            houve_selecao = True
                        else:
                            restaurante_selecionado = ""
                            os.system("clear") or None
                            print("===================================================")
                            print(
                                "\nA opção digitada não existe, por favor tente novamente.\n"
                            )
                            print("===================================================")
                else:
                    houve_selecao = True
                    os.system("clear") or None
                    print("===================================================")
                    print("\nNão foram encontrados resultados.\n")
                    print("===================================================")
                    print(
                        "\nSelecione novamente o método de pesquisa do estabelecimento.\n"
                    )

        else:
            os.system("clear") or None
            print("===================================================")
            print("\nA opção digitada não existe, por favor tente novamente.\n")
            print("===================================================")
    except ValueError:
        os.system("clear") or None
        print("===================================================")
        print("\nA opção digitada não existe, por favor tente novamente.\n")
        print("===================================================")
