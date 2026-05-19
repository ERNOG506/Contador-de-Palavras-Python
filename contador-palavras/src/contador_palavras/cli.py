from contador_palavras.counter import contar_palavras, contar_palavras_em_arquivo


def main() -> None:
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            contar_frase_digitada()
        elif opcao == "2":
            contar_arquivo_texto()
        elif opcao == "0":
            print("Programa encerrado. Ate logo!")
            break
        else:
            print("Opcao invalida. Tente novamente.")


def mostrar_menu() -> None:
    print("\n===== Contador de Palavras =====")
    print("1. Contar palavras de uma frase")
    print("2. Contar palavras de um arquivo de texto")
    print("0. Sair")


def contar_frase_digitada() -> None:
    frase = input("Informe em uma frase algo em que voce pensou hoje: ").strip()

    if not frase:
        print("Voce nao digitou nenhuma frase.")
        return

    quantidade = contar_palavras(frase)
    print(
        "Legal! Voce acabou de me dizer no que pensou "
        f"usando {quantidade} palavras!"
    )


def contar_arquivo_texto() -> None:
    caminho = input("Informe o caminho do arquivo de texto: ").strip()

    if not caminho:
        print("Voce nao informou o caminho do arquivo.")
        return

    try:
        quantidade = contar_palavras_em_arquivo(caminho)
    except FileNotFoundError:
        print("Arquivo nao encontrado. Confira o caminho e tente novamente.")
    except UnicodeDecodeError:
        print("Nao foi possivel ler o arquivo. Use um arquivo de texto em UTF-8.")
    except ValueError as erro:
        print(f"Erro: {erro}")
    else:
        print(f"O arquivo informado possui {quantidade} palavras.")
