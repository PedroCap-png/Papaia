onibus = []


def cadastrar():
    linha = int(input("Numero da linha: "))
    rota = input("Nome da rota: ")
    onibus.append([linha, rota])
    print("Onibus cadastrado com sucesso!")


def listar():
    print("\nLISTA DE ONIBUS")
    if len(onibus) == 0:
        print("Nenhum onibus cadastrado!")
        return
    for o in onibus:
        print("Linha:", o[0], "- Rota:", o[1])


def ordenar():
    if len(onibus) == 0:
        print("Nenhum onibus cadastrado!")
        return
    print("1 - Ordenar por linha")
    print("2 - Ordenar por rota")
    opcao = input("Escolha: ")
    if opcao == "1":
        criterio = 0
    elif opcao == "2":
        criterio = 1
    else:
        print("Opcao invalida!")
        return
    n = len(onibus)
    for i in range(n):
        for j in range(n - i - 1):
            if onibus[j][criterio] > onibus[j + 1][criterio]:
                onibus[j], onibus[j + 1] = onibus[j + 1], onibus[j]
    print("Lista ordenada!")
    listar()


def buscar():
    if len(onibus) == 0:
        print("Nenhum onibus cadastrado!")
        return
    linha = int(input("Digite a linha que deseja buscar: "))
    for o in onibus:
        if o[0] == linha:
            print("Linha:", o[0], "- Rota:", o[1])
            return
    print("Linha nao encontrada!")


def menu():
    while True:
        print("\n===== SISTEMA DE ONIBUS =====")
        print("1 - Cadastrar onibus")
        print("2 - Listar onibus")
        print("3 - Ordenar onibus")
        print("4 - Buscar onibus")
        print("0 - Sair")
        opcao = input("Escolha uma opcao: ")
        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            ordenar()
        elif opcao == "4":
            buscar()
        elif opcao == "0":
            print("Encerrando sistema...")
            break
        else:
            print("Opcao invalida!")


menu()
