import os
import random
import string

# Diretório e caminho do arquivo
diretorio = "db"
caminho_arquivo = os.path.join(diretorio, "senhas.txt")

# Cabeçalho para o arquivo .txt
GERENCIADOR_DE_SENHAS = "ID | NOME       | SENHA\n"

# Inicializar/Criar o arquivo e diretório
def inicializar_arquivo():
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)
        print(f"Pasta '{diretorio}' criada.")
    if not os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, "w") as arquivo:
            arquivo.write(GERENCIADOR_DE_SENHAS)
        print(f"Arquivo '{caminho_arquivo}' foi criado.")

# Gerar uma senha segura
def gerar_senha(tamanho=8):
    letras_maiusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    numeros = "1234567890"
    simbolos = "?%$!@&#"
    todos_caracteres = letras_maiusculas + letras_minusculas + numeros + simbolos
    senha = [
        random.choice(letras_maiusculas),
        random.choice(letras_minusculas),
        random.choice(numeros),
        random.choice(simbolos),
    ]
    senha += random.choices(todos_caracteres, k=tamanho - len(senha))
    random.shuffle(senha)
    return ''.join(senha)

# Adicionar uma nova senha ao arquivo .txt
def adicionar_senha(nome, senha):
    if not nome.strip():
        nome = "INDEFINIDO"
    with open(caminho_arquivo, "r") as arquivo:
        linhas = arquivo.readlines()
        ultimo_id = int(linhas[-1].split(" | ")[0]) if len(linhas) > 1 else 0
    novo_id = ultimo_id + 1
    with open(caminho_arquivo, "a") as arquivo:
        arquivo.write(f"{str(novo_id).ljust(2)} | {nome.upper().ljust(10)} | {senha}\n")
    print(f"Senha para '\033[32m{nome}\033[m' adicionada com sucesso!")

# Remover senha com base no ID e reorganizar IDs
def remover_senha_por_id(id_remover):
    with open(caminho_arquivo, "r") as arquivo:
        linhas = arquivo.readlines()

    if not any(linha.startswith(f"{id_remover} ") for linha in linhas[1:]):
        print(f"ID {id_remover} não encontrado.")
        return

    novas_linhas = [linhas[0]]
    nova_id = 1
    for linha in linhas[1:]:
        if not linha.startswith(f"{id_remover} "):
            partes = linha.split(" | ")
            novas_linhas.append(f"{str(nova_id).ljust(2)} | {partes[1].strip().ljust(10)} | {partes[2]}")
            nova_id += 1

    with open(caminho_arquivo, "w") as arquivo:
        arquivo.writelines(novas_linhas)
    print(f"Senha com ID {id_remover} removida e IDs reorganizados.")

# Mostrar todas as senhas salvas
def mostrar_senhas():
    with open(caminho_arquivo, "r") as arquivo:
        linhas = arquivo.readlines()

    if len(linhas) <= 1:
        print("\033[31mVocê ainda não cadastrou nenhuma senha.\033[m")
    else:
        print("".join(linhas))
