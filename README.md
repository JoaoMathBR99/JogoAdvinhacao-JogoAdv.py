# JogoAdvinhacao-JogoAdv.py
Jogo de Advinhação

Aqui você verá um jogo de advinhação criado com python, usando alguns modulos como random, para gerar o numero aleatorio, tkinter para criar a interface grafica.

Inicialize o repositório Git no seu computador
Abra o terminal (Prompt de Comando no Windows ou Terminal no macOS/Linux).

Navegue até a pasta do seu projeto:

Use o comando cd para ir até o diretório onde você salvou o arquivo do jogo (por exemplo, cd caminho/para/o/seu/projeto).
Inicialize o repositório Git: Execute o seguinte comando no terminal:

bash
Copiar
Editar
git init
Isso cria um repositório Git na pasta do seu projeto.

Passo 4: Adicione os arquivos ao repositório
Adicione o arquivo Python ao repositório: Caso ainda não tenha, salve o código do jogo em um arquivo com a extensão .py (por exemplo, jogo_adivinhacao.py).

Adicione o arquivo ao Git:

bash
Copiar
Editar
git add jogo_adivinhacao.py
Esse comando adiciona o arquivo ao repositório Git local.

Passo 5: Faça o commit dos arquivos
O próximo passo é salvar as alterações com o Git. Execute o seguinte comando para fazer o commit:

bash
Copiar
Editar
git commit -m "Adiciona código do Jogo de Adivinhação"
Isso salva o estado atual dos arquivos no repositório com a mensagem de commit fornecida.

Passo 6: Conecte o repositório local ao repositório remoto no GitHub
Copie a URL do repositório no GitHub:

Vá para a página do seu repositório recém-criado no GitHub.
Clique no botão "Code" e copie a URL que aparece (usualmente no formato https://github.com/usuario/nome-repositorio.git).
Conecte seu repositório local ao GitHub:

No terminal, execute o seguinte comando (substitua pela URL copiada):

bash
Copiar
Editar
git remote add origin https://github.com/usuario/nome-repositorio.git
Passo 7: Envie o código para o GitHub
Agora que você tem o repositório local e o remoto conectados, envie os arquivos para o GitHub com o comando:

bash
Copiar
Editar
git push -u origin master
Isso envia o código do seu jogo para o GitHub.

Passo 8: Adicionar um arquivo README (opcional, mas recomendado)
Crie um arquivo README.md: Esse arquivo serve para descrever o que é o seu projeto e como usá-lo. No terminal, crie um novo arquivo com o comando:

bash
Copiar
Editar
touch README.md
Edite o arquivo README.md:

Abra o arquivo README.md com seu editor de texto favorito e adicione informações sobre o projeto. Por exemplo:

markdown
Copiar
Editar
# Jogo de Adivinhação

Este é um jogo de adivinhação simples em Python, onde o objetivo é adivinhar um número entre 1 e 100 gerado aleatoriamente.

## Como Executar

1. Certifique-se de ter o Python instalado na sua máquina.
2. Clone este repositório:
   ```bash
   git clone https://github.com/usuario/nome-repositorio.git
Navegue até a pasta do projeto:
bash
Copiar
Editar
cd nome-repositorio
Execute o código:
bash
Copiar
Editar
python jogo_adivinhacao.py
Tecnologias
Python
Tkinter (para interface gráfica)
sql
Copiar
Editar

Salve o arquivo e adicione ao Git com os seguintes comandos:

```bash
git add README.md
git commit -m "Adiciona README com instruções"
git push origin master
Passo 9: Executar o Jogo
Agora que o código está no GitHub, para executá-lo:

Clone o repositório (caso você não tenha o projeto na sua máquina):

bash
Copiar
Editar
git clone https://github.com/usuario/nome-repositorio.git
Instale o Python (se ainda não o fez) a partir de https://www.python.org/.

Navegue até a pasta do projeto:

bash
Copiar
Editar
cd nome-repositorio
Execute o jogo com o seguinte comando:

bash
Copiar
Editar
python jogo_adivinhacao.py
