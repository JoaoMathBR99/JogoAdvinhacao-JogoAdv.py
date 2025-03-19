import random  # Importa o módulo random para gerar números aleatórios, essencial para definir o número secreto
import tkinter as tk  # Importa o módulo tkinter para criar a interface gráfica
from tkinter import messagebox  # Importa messagebox para exibir caixas de diálogo informativas
import time  # Importa o módulo time para animações baseadas em tempo
import threading  # Importa o módulo threading para rodar animações sem travar a interface

# Configuração da janela principal
root = tk.Tk()  # Cria a janela principal da aplicação
title("Jogo de Adivinhação")  # Define o título da janela
root.geometry("400x400")  # Define o tamanho da janela (400 pixels de largura e altura)
root.configure(bg="#282c34")  # Define a cor de fundo da janela para um tom escuro, agradável para leitura

# Variáveis globais
numero_secreto = random.randint(1, 100)  # Gera um número aleatório entre 1 e 100 que o usuário deve adivinhar
tentativas = 0  # Inicializa o contador de tentativas, importante para o feedback ao usuário

# Função para processar o palpite do usuário
def verificar_palpite():
    global tentativas, numero_secreto
    try:
        palpite = int(entry.get())  # Obtém o valor digitado no campo de entrada e converte para inteiro
        tentativas += 1  # Incrementa o número de tentativas a cada entrada válida
        if palpite < 1 or palpite > 100:
            mensagem_label.config(text="Digite um número entre 1 e 100", fg="red")  # Mensagem de erro para entrada fora do intervalo
        elif palpite < numero_secreto:
            mensagem_label.config(text="Muito baixo! Tente novamente.", fg="cyan")  # Mensagem quando o palpite for menor que o número secreto
        elif palpite > numero_secreto:
            mensagem_label.config(text="Muito alto! Tente novamente.", fg="cyan")  # Mensagem quando o palpite for maior que o número secreto
        else:
            mensagem_label.config(text=f"Parabéns! Você acertou em {tentativas} tentativas.", fg="green")  # Mensagem de acerto
            animacao_vitoria()  # Chama a função de animação de vitória
            reiniciar_jogo()  # Reinicia o jogo para permitir nova jogada
    except ValueError:  # Captura erro caso o usuário insira um valor inválido
        mensagem_label.config(text="Entrada inválida! Digite um número inteiro.", fg="red")  # Mensagem de erro para entrada inválida

# Função para reiniciar o jogo
def reiniciar_jogo():
    global numero_secreto, tentativas
    numero_secreto = random.randint(1, 100)  # Gera um novo número aleatório
    tentativas = 0  # Reseta o contador de tentativas para começar um novo jogo
    entry.delete(0, tk.END)  # Limpa o campo de entrada para nova jogada

# Função de animação ao ganhar
def animacao_vitoria():
    def efeito():
        for _ in range(5):  # Alterna as cores de fundo 5 vezes para criar um efeito visual comemorativo
            root.configure(bg="#00ff00")  # Muda a cor de fundo para verde (efeito de vitória)
            time.sleep(0.2)  # Aguarda 0.2 segundos
            root.configure(bg="#282c34")  # Retorna à cor original da interface
            time.sleep(0.2)  # Aguarda mais 0.2 segundos
    threading.Thread(target=efeito).start()  # Executa a animação em uma thread separada para não travar a interface

# Interface gráfica
# Rótulo do título do jogo
titulo_label = tk.Label(
    root, text="Jogo de Adivinhação", font=("Arial", 16, "bold"), bg="#282c34", fg="white"
)  # Exibe o título do jogo com fonte Arial, negrito e cor branca sobre fundo escuro
titulo_label.pack(pady=20)  # Posiciona o título com espaçamento de 20 pixels

# Campo de entrada para o palpite do usuário
entry = tk.Entry(root, font=("Arial", 14), width=10)  # Criação do campo de entrada para digitação do número
tentry.pack(pady=10)  # Posiciona o campo de entrada com espaçamento de 10 pixels

# Botão para verificar o palpite
botao = tk.Button(
    root, text="Verificar", font=("Arial", 12), command=verificar_palpite, bg="#61afef", fg="white"
)  # Criação do botão que chama a função verificar_palpite quando clicado
botao.pack(pady=10)  # Posiciona o botão com espaçamento de 10 pixels

# Rótulo para exibir mensagens ao usuário
mensagem_label = tk.Label(
    root, text="", font=("Arial", 12), bg="#282c34", fg="white"
)  # Rótulo usado para exibir mensagens ao usuário durante o jogo
mensagem_label.pack(pady=10)  # Posiciona o rótulo com espaçamento de 10 pixels

root.mainloop()  # Inicia o loop principal da interface gráfica para manter a janela aberta e interativa
