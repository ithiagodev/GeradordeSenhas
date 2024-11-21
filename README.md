## Gerenciador de Senhas
Aplicação em Python para gerar, armazenar, visualizar e remover senhas de forma segura. As senhas geradas são armazenadas em um arquivo de texto e podem ser acessadas facilmente. O sistema é ideal para quem precisa gerenciar diversas senhas de forma organizada e eficiente.

## Requisitos
Este projeto é desenvolvido inteiramente em Python. Certifique-se de que a versão do Python em sua máquina seja compatível com o código utilizado.

### Instalação de dependências (se necessário):
Instale as dependências executando:
```bash
pip install -r requirements.txt
```
**Obs:** Este projeto não utiliza bibliotecas externas, então, por padrão, não há dependências listadas.

## Estrutura dos Arquivos
1. **Main Script (ex.: `Painel.py`)**: Arquivo principal para executar a aplicação, contendo a função `menu` que exibe as opções interativas para o gerenciamento das senhas.
2. **Funções de Gerenciamento**:
   - **Gerar Senha**: Cria uma senha segura com letras maiúsculas, minúsculas, números e símbolos.
   - **Adicionar Senha**: Adiciona uma nova senha associada a um nome.
   - **Visualizar Senhas**: Exibe todas as senhas armazenadas no sistema.
   - **Remover Senha**: Remove uma senha com base no ID e reorganiza as IDs das senhas no arquivo `.txt`.

3. **Diretório `db/`**:
   - **senhas.txt**: Arquivo principal que armazena as senhas geradas, junto com seus IDs e nomes.

## Como Executar
Certifique-se de ter o Python instalado na sua máquina.

No terminal, execute:
```bash
python painel.py
```
O menu interativo será exibido, permitindo que você gere, visualize ou remova senhas.


## Funcionalidades
1. **Inicialização**: O programa cria automaticamente o diretório `db/` e o arquivo `senhas.txt` para armazenar as senhas.
2. **Menu de Controle**: Ao executar o programa, você terá um menu interativo com as opções
3. **Gerar Senha**: Cria uma senha segura e a associa a um nome.
4. **Mostrar Todas as Senhas**: Exibe todas as senhas armazenadas, junto com o nome associado e o ID.
5. **Remover Senha**: Permite remover uma senha baseada no seu ID.
6. **Armazenamento em Arquivo**: As senhas são armazenadas em `db/senhas.txt`, mantendo o histórico de todas as senhas geradas, com seus respectivos IDs.
7. **Sair**: Encerra o programa.

## Fluxo de Funcionamento
1. **Inicialização**: Verifica a existência do diretório `db/` e do arquivo `senhas.txt`. Caso não existam, o sistema os cria automaticamente.
2. **Menu Interativo**: Permite ao usuário gerar novas senhas, visualizar todas as senhas ou remover senhas de acordo com o ID.
3. **Armazenamento Persistente**: As senhas geradas são salvas em um arquivo `.txt`, permitindo fácil leitura e manipulação posterior.