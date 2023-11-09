import json


# Função para carregar o dicionário a partir do arquivo JSON
def carregar_espacos_verdes():
    try:
        with open('espacos_verdes.json', 'r', encoding='utf-8') as arquivo_json:
            return json.load(arquivo_json)
    except FileNotFoundError:
        return {}


def salvar_para_json(dicionario):
    try:
        with open('espacos_verdes.json', 'w', encoding='utf-8') as json_file:
            json.dump(dicionario, json_file, ensure_ascii=False, indent=4)
    except (IOError, PermissionError) as e:
        print(f"Erro ao salvar o arquivo JSON: {e}")


def verifica_resposta(resposta):
    while resposta != "s" and resposta != "n":
        resposta = input("Responda digitando 's' or 'n': ")

    return resposta


def obrigar_input(prompt):
    while True:
        entrada = input(prompt)
        if entrada.strip() != "":
            return entrada
        else:
            print("Por favor, digite algo.")


def obrigar_float(prompt, min_valor=0, max_valor=5):
    while True:
        entrada = input(prompt)
        try:
            valor_float = float(entrada)
            if min_valor <= valor_float <= max_valor:
                return valor_float
            else:
                print(f"Por favor, digite um número entre {min_valor} e {max_valor}.")
        except ValueError:
            print("Por favor, digite um número válido.")


def cadastrar_espaco_verde():
    nome_espaco = obrigar_input("Digite o espaço verde/evento que você quer cadastrar: ")

    if nome_espaco in espacos_verdes:
        alterar_informacoes(nome_espaco)
    else:
        adicionar_novo_espaco(nome_espaco)


def alterar_informacoes(nome_espaco):
    resposta = verifica_resposta(input(f"O espaço verde/evento '{nome_espaco}' já está cadastrado, você gostaria "
                                       f"de mudar as informações (s/n)? "))

    if resposta == "s":
        localizacao = obrigar_input("Digite a nova localização do espaço verde/evento: ")
        avaliacao = obrigar_float("Digite a avaliação do espaço verde/evento: ")
        descricao = obrigar_input("Digite a nova descrição do espaço verde/evento: ")

        espaco = espacos_verdes[nome_espaco]
        espaco["Localização"] = localizacao
        espaco["Avaliação"] = avaliacao
        espaco["Descrição"] = descricao

        print("Mudanças aplicadas!\n")
    else:
        print("Sem problemas!\n")


def adicionar_novo_espaco(nome_espaco):
    localizacao = obrigar_input("Digite a localização do espaço verde/evento: ")
    avaliacao = obrigar_float("Digite a avaliação do espaço verde/evento: ")
    descricao = obrigar_input("Digite a descrição do espaço verde/evento: ")

    espacos_verdes[nome_espaco] = {
        "Localização": localizacao,
        "Avaliação": avaliacao,
        "Descrição": descricao,
    }

    print(f"Espaço verde/evento '{nome_espaco}' cadastrado!\n")


def listar_espacos_verdes():
    print("Espaços Verdes Cadastrados:\n")
    for espaco in espacos_verdes:
        print(espaco)


def buscar_espaco_verde():
    nome_espaco = obrigar_input("Digite o nome do espaço/evento que deseja buscar: ")
    if nome_espaco in espacos_verdes:
        print(f"\nInformações sobre '{nome_espaco}':")
        print(f"Localização: {espacos_verdes[nome_espaco]['Localização']}")
        print(f"Avaliação: {espacos_verdes[nome_espaco]['Avaliação']}")
        print(f"Descrição: {espacos_verdes[nome_espaco]['Descrição']}\n")
    else:
        print(f"{nome_espaco} não encontrado. Talvez você queira cadastrar esse espaço/evento e seus espaços verdes.\n")


def comparar_espacos_verdes():
    nome_espaco1 = obrigar_input("Digite o nome do primeiro espaço verde/evento que deseja comparar: ")
    nome_espaco2 = obrigar_input("Digite o nome do segundo espaço verde/evento que deseja comparar: ")

    if nome_espaco1 in espacos_verdes and nome_espaco2 in espacos_verdes:
        avaliacao_espaco1 = espacos_verdes[nome_espaco1]["Avaliação"]
        avaliacao_espaco2 = espacos_verdes[nome_espaco2]["Avaliação"]

        if avaliacao_espaco1 > avaliacao_espaco2:
            print(f"{nome_espaco1} é melhor do que {nome_espaco2} com base na avaliação.")
        elif avaliacao_espaco1 < avaliacao_espaco2:
            print(f"{nome_espaco2} é melhor do que {nome_espaco1} com base na avaliação.")
        else:
            print(f"{nome_espaco1} e {nome_espaco2} têm a mesma avaliação.")
    else:
        print("Um dos espaços não foi encontrado. Certifique-se de que ambos os espaços estejam cadastrados.")


def ranquear_espacos_verdes():
    # Classifica os espaços verdes por avaliação em ordem decrescente e, em caso de empate, por nome
    espacos_classificados = sorted(espacos_verdes.items(), key=lambda x: (-x[1]["Avaliação"], x[0]))

    print("Espaços verdes/eventos ranqueados por avaliação:\n")

    for posicao, (nome_espaco, info_espaco) in enumerate(espacos_classificados, start=1):
        avaliacao = info_espaco["Avaliação"]
        print(f"{posicao}. {nome_espaco} - Avaliação: {avaliacao}")


def filtrar_por_avaliacao(avaliacao_minima):
    espacos_filtrados = []

    for nome_espaco, info_espaco in espacos_verdes.items():
        if info_espaco["Avaliação"] >= avaliacao_minima:
            espacos_filtrados.append((nome_espaco, info_espaco))

    return espacos_filtrados


def verifica_senha(senha):
    tem_letra = False
    tem_numero = False
    tem_especial = False

    for letra in senha:
        if letra.isalpha():
            tem_letra = True
        elif letra.isdigit():
            tem_numero = True
        elif letra in '!@#$%^&*()_+':
            tem_especial = True

    return tem_letra and tem_numero and tem_especial


def login():
    nome = obrigar_input("Digite seu nome: ")

    while True:
        senha = input("Digite sua senha (a senha deve conter número e caractere especial): ")
        if verifica_senha(senha):
            print("Acesso Concedido\n")
            break
        else:
            print("Acesso Negado\n")
            print("Digite a senha corretamente!")

    return nome


def main():
    resposta = verifica_resposta(input("Você gostaria de entrar no sistema (s/n)? "))
    if resposta == "s":
        nome = login()
        print(f"\nBem vindo {nome}. Essas são as opções disponíveis:")
        while True:
            print("\n1. Cadastrar um espaço verde/evento.")
            print("2. Listar todos os espaço verde/evento cadastrados.")
            print("3. Buscar informações sobre um espaço verde.")
            print("4. Comparar dois espaço verde/evento.")
            print("5. Ver o ranking dos mais bem avaliados.")
            print("6. Filtrar espaços verdes por avaliação mínima.")
            print("7. Sair e Salvar.")
            escolha = input(f"\nO que o/a senhor(a) {nome} gostaria de fazer (digite o número da operação): ")

            if escolha == "1":
                cadastrar_espaco_verde()
            elif escolha == "2":
                listar_espacos_verdes()
            elif escolha == "3":
                buscar_espaco_verde()
            elif escolha == "4":
                comparar_espacos_verdes()
            elif escolha == "5":
                ranquear_espacos_verdes()
            elif escolha == "6":
                avaliacao_minima = obrigar_float("Digite a avaliação mínima desejada: ")
                espacos_filtrados = filtrar_por_avaliacao(avaliacao_minima)
                if espacos_filtrados:
                    print("\nEspaços verdes/eventos com avaliação maior ou igual a", avaliacao_minima, ":\n")
                    for posicao, (nome_espaco, info_espaco) in enumerate(espacos_filtrados, start=1):
                        avaliacao = info_espaco["Avaliação"]
                        print(f"{posicao}. {nome_espaco} - Avaliação: {avaliacao}")
                else:
                    print("Nenhum espaço verde/evento atende ao critério de avaliação mínima.")
            elif escolha == "7":
                salvar_para_json(espacos_verdes)
                print("Muito obrigado por usar o nosso sistema. Volte sempre!")
                break
            else:
                print("\nOpção inválida. Por favor, escolha uma opção válida.")
    else:
        print("Sem problemas! Fique a vontade caso queria voltar.")


if __name__ == "__main__":
    espacos_verdes = carregar_espacos_verdes()
    main()
