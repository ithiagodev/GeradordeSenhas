import sys,os
sys.path.insert(0,os.path.abspath(os.curdir))
from commands.index import *
from rich.progress import Progress
from time import sleep
from random import randint

def linha(tam=42):
    return "-" * tam

def cabeçalho(txt, cor="\033[34m"):
    print(linha())
    print(f'{cor}{txt.center(42)}\033[m')
    print(linha())

def barra():
    with Progress() as progress:
        task = progress.add_task('Gerando senha segura...', total = 100)
        while not progress.finished:
            numero = randint(1, 35)
            progress.update(task, advance=numero)
            sleep(1)
    print("Senha gerada com \033[32msucesso\033[m!")

# Menu para exibir o programa principal
def menu():
    inicializar_arquivo()

    while True:
        cabeçalho("GERENCIADOR DE SENHAS")
        print("Digite 1 para \033[32mGERAR SENHA\033[m")
        print("Digite 2 para \033[33mMOSTRAR TODAS AS SENHAS\033[m")
        print("Digite 3 para \033[31mREMOVER SENHA\033[m")
        print("Digite 4 para \033[31mSAIR DO GERENCIADOR DE SENHAS\033[m")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cabeçalho("GERAR SENHA")
            nome = input("Digite o nome para a senha: ")
            tamanho = input("Digite o tamanho da senha (\033[33mmínimo 8\033[m, Deixe em branco para usar o padrão 8): ")
            
            tamanho = int(tamanho) if tamanho.isdigit() else 8

            if tamanho < 8:
                tamanho = 8
            barra()
            senha = gerar_senha(tamanho)
            adicionar_senha(nome, senha)
        elif opcao == "2":
            cabeçalho("MOSTRANDO TODAS AS SENHAS")
            mostrar_senhas()
        elif opcao == "3":
            cabeçalho("REMOVER SENHA")
            id_remover = input("Digite o ID da senha a ser removida: ")
            remover_senha_por_id(id_remover)
        elif opcao == "4":
            cabeçalho("FINALIZANDO...", cor="\033[31m")
            sleep(2)
            print("Fim do programa. \033[32mvolte sempre\033[m!")
            break
        else:
            print("\033[31mOpção inválida!\033[m Escolha entre 1 e 4.")

menu()
