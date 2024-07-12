from moviepy.editor import VideoFileClip
from tkinter import *
from tkinter import ttk
import pandas as pd
import numpy as np
import pygame
import random
import sys
import os


# Inicialização do Pygame
pygame.mixer.init()
pygame.init()

class Animal:
    def __init__(self, nome, imagem, audio, estado):
        self.nome = nome
        self.imagem = imagem
        self.audio = audio
        self.estado = estado

current_path = os.path.dirname(__file__)

aguia = Animal("ÁGUIA", pygame.image.load(os.path.join(current_path, "aguia_imagem.png")), "aguia_audio.mp3", False)
baleia = Animal("BALEIA", pygame.image.load(os.path.join(current_path, "baleia_imagem.png")), "baleia_audio.mp3", False)
cachorro = Animal("CACHORRO", pygame.image.load(os.path.join(current_path, "cachorro_imagem.png")), "cachorro_audio.mp3", False)
cavalo = Animal("CAVALO", pygame.image.load(os.path.join(current_path, "cavalo_imagem.png")), "cavalo_audio.mp3", False)
coruja = Animal("CORUJA", pygame.image.load(os.path.join(current_path, "coruja_imagem.png")), "coruja_audio.mp3", False)
corvo = Animal("CORVO", pygame.image.load(os.path.join(current_path, "corvo_imagem.png")), "corvo_audio.mp3", False)
elefante = Animal("ELEFANTE", pygame.image.load(os.path.join(current_path, "elefante_imagem.png")), "elefante_audio.mp3", False)
galinha = Animal("GALINHA", pygame.image.load(os.path.join(current_path, "galinha_imagem.png")), "galinha_audio.mp3", False)
gato = Animal("GATO", pygame.image.load(os.path.join(current_path, "gato_imagem.png")), "gato_audio.mp3", False)
grilo = Animal("GRILO", pygame.image.load(os.path.join(current_path, "grilo_imagem.png")), "grilo_audio.mp3", False)
lobo = Animal("LOBO", pygame.image.load(os.path.join(current_path, "lobo_imagem.png")), "lobo_audio.mp3", False)
macaco = Animal("MACACO", pygame.image.load(os.path.join(current_path, "macaco_imagem.png")), "macaco_audio.mp3", False)
mosquito = Animal("MOSQUITO", pygame.image.load(os.path.join(current_path, "mosquito_imagem.png")), "mosquito_audio.mp3", False)
ovelha = Animal("OVELHA", pygame.image.load(os.path.join(current_path, "ovelha_imagem.png")), "ovelha_audio.mp3", False)
pato = Animal("PATO", pygame.image.load(os.path.join(current_path, "pato_imagem.png")), "pato_audio.mp3", False)
peru = Animal("PERU", pygame.image.load(os.path.join(current_path, "peru_imagem.png")), "peru_audio.mp3", False)
porco = Animal("PORCO", pygame.image.load(os.path.join(current_path, "porco_imagem.png")), "porco_audio.mp3", False)
sapo = Animal("SAPO", pygame.image.load(os.path.join(current_path, "sapo_imagem.png")), "sapo_audio.mp3", False)
tigre = Animal("TIGRE", pygame.image.load(os.path.join(current_path, "tigre_imagem.png")), "tigre_audio.mp3", False)
urso = Animal("URSO", pygame.image.load(os.path.join(current_path, "urso_imagem.png")), "urso_audio.mp3", False)
vaca = Animal("VACA", pygame.image.load(os.path.join(current_path, "vaca_imagem.png")), "vaca_audio.mp3", False)

# Lista de animais ordenada alfabeticamente
vetor_animais = [aguia, baleia, cachorro, cavalo, coruja, corvo, elefante, galinha, gato, grilo, lobo, macaco, mosquito, ovelha, pato, peru, porco, sapo, tigre, urso, vaca]





# Dimensões das janelas dos menus
largura = 1280
altura = 720
janela = pygame.display.set_mode((largura, altura))

# Dimensões das janelas dos jogos
largura_janela_jogos = largura//3
altura_janela_jogos = altura//6

# Nome do jogo/janela
pygame.display.set_caption("Que Bicho e?")

# Fonte
fonte = pygame.font.SysFont("MV Boli", 20)
fonte_cronometro = pygame.font.SysFont("MV Boli", 40)

# Cores
PRETO = (0, 0, 0)
CINZA = (125, 125, 125)
BRANCO = (255, 255, 255)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

# Fundo // Background
imagem_fundo = pygame.image.load("background.jpeg").convert()
imagem_fundo = pygame.transform.smoothscale(imagem_fundo, (largura, altura))

# Fundo 2
imagem_fundo2 = pygame.image.load("fundo2.png").convert()
imagem_fundo2 = pygame.transform.smoothscale(imagem_fundo2, (largura, altura))

# Fundo 3
imagem_fundo3 = pygame.image.load("fundo3.png").convert()
imagem_fundo3 = pygame.transform.smoothscale(imagem_fundo3, (largura, altura))

# Pergaminho
pergaminho = pygame.image.load("pergaminho.png")
pergaminho = pygame.transform.smoothscale(pergaminho, (1200, 300))

# Tronco // Botão
botao_imagem = pygame.image.load("tronco.png")
botao_imagem = pygame.transform.smoothscale(botao_imagem, (250, 100))

# Controle
controle = pygame.image.load("controle.png")
controle = pygame.transform.smoothscale(controle, (50, 50))

# Play
play = pygame.image.load("play.png")
play = pygame.transform.smoothscale(play, (50, 50))

# Trofeu
trofeu = pygame.image.load("trofeu.png")
trofeu = pygame.transform.smoothscale(trofeu, (50, 50))

# Seta vermelha esquerda
setaesquerda = pygame.image.load("setaesquerda.png")
setaesquerda = pygame.transform.smoothscale(setaesquerda, (250, 100))

# Seta verde direita
setadireita = pygame.image.load("setadireita.png")
setadireita = pygame.transform.smoothscale(setadireita, (250, 100))

# Porta
porta = pygame.image.load("porta.png")
porta = pygame.transform.smoothscale(porta, (50, 50))

# Livro
livro = pygame.image.load("livro.png")
livro = pygame.transform.smoothscale(livro, (50, 50))

# Casa
casa = pygame.image.load("casa.png")
casa = pygame.transform.smoothscale(casa, (70, 70))

# Fase 2
tempo_fase1 = 240
tempo_fase2 = 180
Tamanho_carta = (100, 100)
FPS = 30

verso_carta = pygame.image.load("verso_carta.png")
verso_carta = pygame.transform.smoothscale(verso_carta, Tamanho_carta)

background_cartas = pygame.image.load("fundo_cartas.png")
background_cartas = pygame.transform.smoothscale(background_cartas, Tamanho_carta)


def carregar_arquivo(nome_arquivo):
    caminho_completo = os.path.join(os.path.dirname(__file__), nome_arquivo)
    if not os.path.isfile(caminho_completo):
        raise FileNotFoundError(f"Arquivo '{nome_arquivo}' não encontrado.")
    return caminho_completo


som_jogar = carregar_arquivo("jogar.mp3")
som_video_tutorial = carregar_arquivo("video_tutorial.mp3")
som_livro_de_animais = carregar_arquivo("livro_de_animais.mp3")
som_ranking = carregar_arquivo("ranking.mp3")
som_sair = carregar_arquivo("sair.mp3")
INTERVALO_REPETICAO = 2000

def desenhar_botao(x, y, largura, altura, texto, acao=None, som=None):
    janela.blit(botao_imagem, (x, y))
    texto_botao = fonte.render(texto, True, BRANCO)
    janela.blit(texto_botao, (x + 32 + largura // 2 - texto_botao.get_width() // 2, y + altura // 2 - texto_botao.get_height() // 2))
    return pygame.Rect(x, y, largura, altura), acao, som


def main():
    rodando = True
    musica_atual = None
    ultima_troca_tempo = 0

    while rodando:
        botoes = []
        var = 20

        janela.blit(imagem_fundo, (0, 0))

        botoes.append(desenhar_botao(50, 50 + var, 200, 100, "JOGAR", jogar, som_jogar))
        janela.blit(controle, (265, 95))

        botoes.append(desenhar_botao(50, 150 + var, 200, 100, "VIDEO TUTORIAL", video_tutorial, som_video_tutorial))
        janela.blit(play, (265, 195))

        botoes.append(desenhar_botao(50, 250 + var, 200, 100, "LIVRO DE ANIMAIS", livro_de_animais, som_livro_de_animais))
        janela.blit(livro, (290, 300))

        botoes.append(desenhar_botao(50, 350 + var, 200, 100, "RANKING", ranking, som_ranking))
        janela.blit(trofeu, (265, 400))

        botoes.append(desenhar_botao(50, 450 + var, 200, 100, "SAIR", sair, som_sair))
        janela.blit(porta, (265, 500))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for botao in botoes:
                    if botao[0].collidepoint(pos):
                        if botao[1]:  # Executar a ação associada ao botão
                            botao[1]()

        # Verificar se o mouse está sobre um botão
        pos = pygame.mouse.get_pos()
        musica_nova = None
        for botao in botoes:
            if botao[0].collidepoint(pos):
                musica_nova = botao[2]
                break

        # Se a música nova é diferente da atual ou o intervalo de repetição passou, trocar a música
        tempo_atual = pygame.time.get_ticks()
        if musica_nova != musica_atual or (musica_nova and tempo_atual - ultima_troca_tempo > INTERVALO_REPETICAO):
            if musica_nova:
                pygame.mixer.music.load(musica_nova)
                pygame.mixer.music.play()
                ultima_troca_tempo = tempo_atual
            else:
                pygame.mixer.music.stop()
            musica_atual = musica_nova

        pygame.display.flip()


def temporizador(texto, x):
    fonte_pausa = pygame.font.SysFont("MV Boli", 48)
    texto_temporizador = fonte_pausa.render(texto, True, (0, 0, 0))

    for i in range(5, 0, -1):
        segundos = fonte_pausa.render(f"{i}", True, (0, 0, 0))
        janela.blit(imagem_fundo, (0, 0))
        janela.blit(texto_temporizador, (x, 320))
        janela.blit(segundos, (620, 370))

        pygame.display.flip()
        pygame.time.wait(1000)

def jogar(): 
    jogador = inserir_nome()

    if jogador == -1:
        main()

    else:
        # Inicio da fase 1
        acertos_fase1 = []
        erros_fase1 = []

        texto1 = "ADVINHE O ANIMAL EM"
        temporizador(texto1, 350)
        
        for j in range(0, 5):
            status = fase_1(jogador, acertos_fase1, erros_fase1)
            if(status == -1):
                return

        texto2 = "O JOGO DA MEMÓRIA COMEÇA EM"
        temporizador(texto2, 200)
        

        # Inicio da fase 2
        retorno1 = fase_2(tempo_fase1)
        if(retorno1 == -5):
            return
        
        tempo_dificuldade_1 = tempo_fase1 - retorno1

        texto3 = "A PRÓXIMA RODADA COMEÇA EM"
        temporizador(texto3, 200)

        retorno2 = fase_2(tempo_fase2)
        if(retorno2 == -5):
            return

        tempo_dificuldade_2 = tempo_fase2 - retorno2


        # Janela de pontuação da rodada
        janela.blit(imagem_fundo, (0, 0))
        janela.blit(pergaminho, (40, 200))

        texto_nome = fonte.render(f"{jogador}", True, (0, 0, 0))
        retangulo_nome = texto_nome.get_rect()

        x_nome = (largura - retangulo_nome.width) // 2
        y_nome = ((altura - retangulo_nome.height) // 2) - 60

        janela.blit(texto_nome, (x_nome, y_nome))

        # Pontuação
        texto = fonte.render(f"PONTUAÇÃO: {len(acertos_fase1)}/5       1° TEMPO: {tempo_dificuldade_1}     2° TEMPO: {tempo_dificuldade_2}", True, (0, 0, 0))

        retangulo_texto = texto.get_rect()

        x_texto = (largura - retangulo_texto.width) // 2
        y_texto = (altura - retangulo_texto.height) // 2

        janela.blit(texto, (x_texto, y_texto))

        pygame.display.flip()
        pygame.time.wait(12000)
    
        arquivar_nomes(jogador, acertos_fase1, erros_fase1, len(acertos_fase1), tempo_dificuldade_1, tempo_dificuldade_2)


def arquivar_nomes(jogador, acertos_fase1, erros_fase1, pontuacao, tempo_dificuldade_1, tempo_dificuldade_2):
    try:
        df = pd.read_json('jogadores.json')

    except FileNotFoundError:
        df = pd.DataFrame(columns=['Nome', 'Acertos', 'Erros', 'Pontuação', '1° Tempo', '2° Tempo'])

    df = df._append({'Nome': jogador, 'Acertos': acertos_fase1, 'Erros': erros_fase1, 'Pontuação': pontuacao, '1° Tempo': tempo_dificuldade_1, '2° Tempo': tempo_dificuldade_2}, ignore_index=True)
    df = df.sort_values(by='Nome')
    df.to_json('jogadores.json', orient='records')

def inserir_nome():
    nome = ""
    inserindo = True

    fonte = pygame.font.SysFont("MV Boli", 48)
    
    while inserindo:
        janela.blit(imagem_fundo, (0, 0))

        # Renderiza o texto na tela
        texto = fonte.render("DIGITE SEU NOME", True, PRETO)
        janela.blit(texto, (largura//2 - texto.get_width()//2, altura//2 - texto.get_height()//2))

        # Renderiza o nome digitado
        texto_nome = fonte.render(nome.upper(), True, PRETO)
        janela.blit(texto_nome, (largura//2 - texto_nome.get_width()//2, altura//2 + 50))

        botao_menu = pygame.Rect(0, 0, 70, 70)
        janela.blit(casa, (0, 0))

        # Atualiza a tela
        pygame.display.flip()

        # Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if botao_menu.collidepoint(pos):
                    return -1

            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    inserindo = False

                elif evento.key == pygame.K_BACKSPACE:
                    nome = nome[:-1]

                else:
                    nome += evento.unicode

    return nome.upper().strip()


def fase_1(jogador, acertos_fase1, erros_fase1):
    janela.blit(imagem_fundo, (0, 0))
    pygame.display.flip()
    
    # Sortear 3 animais
    animais_sorteados = random.sample(vetor_animais, 3)
    animal_correto = random.choice(animais_sorteados)
    janela.blit(pygame.transform.smoothscale(animal_correto.imagem, (200, 200)), pygame.Rect(largura//2 - 100, altura//3 , 200, 200))
    
    botoes = []

    botoes_fase1 = pygame.image.load("tronco.png")
    botoes_fase1 = pygame.transform.smoothscale(botoes_fase1, (200, 100))

    for i, animal in enumerate(animais_sorteados):
        botao = pygame.Rect(i * (largura//3) + 150, altura - 150, 200, 100) 
        botoes.append(botao)
        # Desenha o tronco
        janela.blit(botoes_fase1, (i * (largura//3) + 150, altura - 150))
        
        # Escreve texto nos botões
        texto_botao = fonte.render(animal.nome, True, BRANCO)
        janela.blit(texto_botao, (i * (largura//3) + 200, altura - 110))

    botao_menu = pygame.Rect(0, 0, 70, 70)
    janela.blit(casa, (0, 0))
    
    pygame.display.flip()

    # Variável para controlar se o áudio está tocando
    audio_tocando = False
    audio_atual = None

    # Esperar clique do jogador
    while True:
        mouse_pos = pygame.mouse.get_pos()
        mouse_sobre_botao = False 

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if botao_menu.collidepoint(pos):
                    return -1

                for i, botao in enumerate(botoes):
                    if botao.collidepoint(pos):
                        if animais_sorteados[i] == animal_correto:
                            janela.blit(imagem_fundo, (0, 0))
                            fonte_fase_termino = pygame.font.SysFont("MV Boli", 30)
                            texto_acerto = fonte_fase_termino.render(random.choice(["PARABÉNS, VOCÊ CONSEGUIU", "MUITO BEM, VOCÊ ACERTOU", "MUITO BOM, ESTÁ CORRETO", "EXCELENTE, ESTÁ CERTO"]), True, PRETO)
                            retangulo_texto = texto_acerto.get_rect()
                            x_texto = (largura - retangulo_texto.width) // 2
                            y_texto = (altura - retangulo_texto.height) // 2
                            janela.blit(texto_acerto, (x_texto, y_texto))

                            pygame.display.flip()
                            acertos_fase1.append(animal_correto.nome)
                            pygame.mixer.music.stop()
                            pygame.time.wait(3000)

                        else:
                            janela.blit(imagem_fundo, (0, 0))
                            fonte_fase_termino = pygame.font.SysFont("MV Boli", 30)
                            texto_erro = fonte_fase_termino.render(random.choice(["VOCÊ ESTÁ QUASE LÁ, VAMOS TENTAR DE NOVO", "NÃO DESANIME, FOI MUITO PERTO", "NÃO FOI DESSA VEZ, MAS NA PRÓXIMA VAI", "NEM SEMPRE CONSEGUIMOS, MAS NÃO PODEMOS DESISTIR"]), True, PRETO)
                            retangulo_texto = texto_erro.get_rect()
                            x_texto = (largura - retangulo_texto.width) // 2
                            y_texto = (altura - retangulo_texto.height) // 2
                            janela.blit(texto_erro, (x_texto, y_texto))

                            pygame.display.flip()
                            pygame.mixer.music.stop()
                            pygame.time.wait(3000)
                            erros_fase1.append(animal_correto.nome)

                        pygame.mixer.music.stop()
                        return

        for i, botao in enumerate(botoes):
            if botao.collidepoint(mouse_pos):
                if not audio_tocando or audio_atual != animais_sorteados[i].audio:
                    pygame.mixer.music.load(animais_sorteados[i].audio)
                    pygame.mixer.music.play()
                    audio_tocando = True
                    audio_atual = animais_sorteados[i].audio
                mouse_sobre_botao = True
                break

        if not mouse_sobre_botao:
            if audio_tocando:
                pygame.mixer.music.stop()
                audio_tocando = False
                audio_atual = None


def fase_2(tempo_fase_atual):
    janela.blit(imagem_fundo3, (0, 0))
    pygame.display.flip()

    cartas_sorteadas1 = random.sample(vetor_animais, 8)
    cartas_sorteadas2 = cartas_sorteadas1

    vetor = []
    botoes = []

    vetor = cartas_sorteadas1 + cartas_sorteadas2
    random.shuffle(vetor)

    matriz = np.array(vetor).reshape(4, 4)
    matriz_aux = np.array(matriz).reshape(16)

    for i in range(0, 4):
        for j in range(0, 4):
            botao = pygame.Rect((i * (100 + 20) + largura_janela_jogos, j * (100 + 20) + altura_janela_jogos), Tamanho_carta) 
            pygame.draw.rect(janela, PRETO, botao, 2)
            botoes.append(botao)
            janela.blit(verso_carta, (i * (100 + 20) + largura_janela_jogos, j * (100 + 20) + altura_janela_jogos))
            
    pygame.display.flip()

    cartas_viradas = []
    cartas_acertadas = []

    clock = pygame.time.Clock()
    tempo_decorrido = tempo_fase_atual * FPS

    timer_running = True

    while len(cartas_acertadas) < 16 and tempo_decorrido > 0:
        janela.blit(botao_imagem, (largura-300,25))
        text = fonte_cronometro.render(str(tempo_decorrido//30), True, BRANCO)
        text_rect = text.get_rect(center=(largura-175,75))
        janela.blit(text, text_rect)

        botao_menu = pygame.Rect(0, 0, 70, 70)
        janela.blit(casa, (0, 0))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if(evento.type == pygame.MOUSEBUTTONDOWN):
                pygame.display.flip()
                pos = pygame.mouse.get_pos()
                if botao_menu.collidepoint(pos):
                    return -5
                
                for i, botao in enumerate(botoes):
                    if botao.collidepoint(pos) and i not in cartas_acertadas:
                        if i in cartas_viradas:
                            continue

                        cartas_viradas.append(i)
                        k = i // 4
                        j = i % 4
                        janela.blit(background_cartas, (k * (100 + 20) + largura_janela_jogos, j * (100 + 20) + altura_janela_jogos))
                        janela.blit(pygame.transform.smoothscale(matriz[k][j].imagem, Tamanho_carta), (k * (100 + 20) + largura_janela_jogos, j * (100 + 20) + altura_janela_jogos))             

                if(len(cartas_viradas) == 2):
                    pygame.display.flip()
                    # Cartas iguais
                    if(matriz_aux[cartas_viradas[0]].nome == matriz_aux[cartas_viradas[1]].nome) and cartas_viradas[0] != cartas_viradas[1]:
                        cartas_acertadas.append(cartas_viradas[0])
                        cartas_acertadas.append(cartas_viradas[1])

                    else:
                        # Cartas diferentes
                        pygame.time.wait(1000)
                        tempo_decorrido -= FPS
                        for i in cartas_viradas:
                            k = i // 4
                            j = i % 4
                            janela.blit(verso_carta, (k * (100 + 20) + largura_janela_jogos, j * (100 + 20) + altura_janela_jogos))

                    cartas_viradas = []
                
        pygame.display.flip()
        if timer_running:
            tempo_decorrido -= 1

        if tempo_decorrido <= 0:
            timer_running = False
            return 0
        
        clock.tick(FPS)  # Atualiza a cada 1 segundo
    
    return tempo_decorrido//FPS


def video_tutorial():
    janela = pygame.display.set_mode((largura, altura))
    caminho_video = "video.mp4"
    video = VideoFileClip(caminho_video)
    video.preview()
    return 


def botao_menu():
    return pygame.Rect(largura // 18, altura - 150, 200, 100)


def botao_proximo():
    return pygame.Rect(largura - 300, altura - 150, 200, 100)


def desenha_botao_esquerda(texto):
    janela.blit(setaesquerda, (largura // 18 - 60, altura - 130))
    botao_esquerda = botao_menu()
    texto_botao_esquerda = fonte.render(texto, True, BRANCO)
    janela.blit(texto_botao_esquerda, (botao_esquerda.x + 50, botao_esquerda.y + 50))
    return botao_esquerda


def desenha_botao_direita(texto):
    janela.blit(setadireita, (largura - 285, altura - 130))
    botao_direita = botao_proximo()
    texto_botao_direita = fonte.render(texto, True, BRANCO)
    janela.blit(texto_botao_direita, (botao_direita.x + 50, botao_direita.y + 50))
    return botao_direita


def desenha_estatico():
    janela.blit(imagem_fundo2, (0, 0))
    janela.blit(casa, (0, 0))


def desenha_animal(i):
    animal_atual = pygame.transform.smoothscale(vetor_animais[i].imagem, (200, 200))
    janela.blit(animal_atual, (largura // 2 - 100, altura // 2 - 200))
    janela.blit(botao_imagem, (largura // 2 - 125, altura // 2))
    nome_animal = fonte.render(vetor_animais[i].nome, True, BRANCO)
    janela.blit(nome_animal, (largura // 2 - 50, altura // 2 + 40))


som_menu = carregar_arquivo("menu.mp3")
som_proximo = carregar_arquivo("proximo.mp3")
som_anterior = carregar_arquivo("anterior.mp3")


def livro_de_animais():
    i = 0
    audio_tocando = {
        "menu": False,
        "proximo": False,
        "anterior": False,
        "animal": False
    }

    desenha_estatico()
    botao_casa = pygame.Rect(0, 0, 70, 70)

    while True:
        desenha_estatico()
        desenha_animal(i)

        botao_nome = pygame.Rect(largura // 2 - 100, altura // 2 + 10, 200, 100)

        if i == 0:
            botao_esquerda = desenha_botao_esquerda("MENU")
            botao_direita = desenha_botao_direita("PROXIMO")
            som_esquerda = som_menu
            som_direita = som_proximo

        elif 0 < i < len(vetor_animais) - 1:
            botao_esquerda = desenha_botao_esquerda("ANTERIOR")
            botao_direita = desenha_botao_direita("PROXIMO")
            som_esquerda = som_anterior
            som_direita = som_proximo

        else:
            botao_esquerda = desenha_botao_esquerda("ANTERIOR")
            botao_direita = None
            som_esquerda = som_anterior
            som_direita = None

        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if botao_casa.collidepoint(pos):
                    return

                if botao_esquerda.collidepoint(pos):
                    if i == 0:
                        return

                    elif i > 0:
                        i -= 1
                        desenha_estatico()
                        desenha_animal(i)
                        botao_esquerda = desenha_botao_esquerda("ANTERIOR" if i > 0 else "MENU")
                        botao_direita = desenha_botao_direita("PROXIMO" if i < len(vetor_animais) - 1 else None)
                        pygame.display.update()
                        for key in audio_tocando:
                            audio_tocando[key] = False

                if botao_direita and botao_direita.collidepoint(pos) and i < len(vetor_animais) - 1:
                    i += 1
                    desenha_estatico()
                    desenha_animal(i)
                    botao_esquerda = desenha_botao_esquerda("ANTERIOR")
                    botao_direita = desenha_botao_direita("PROXIMO" if i < len(vetor_animais) - 1 else None)
                    pygame.display.update()
                    for key in audio_tocando:
                        audio_tocando[key] = False

        pos = pygame.mouse.get_pos()

        # Audio animal
        if botao_nome.collidepoint(pos):
            if not audio_tocando["animal"]:
                pygame.mixer.music.load(vetor_animais[i].audio)
                pygame.mixer.music.play()
                audio_tocando["animal"] = True
        else:
            if audio_tocando["animal"]:
                pygame.mixer.music.stop()
                audio_tocando["animal"] = False

        # Audio anterior
        if botao_esquerda.collidepoint(pos):
            if not audio_tocando["anterior"]:
                pygame.mixer.music.load(som_esquerda)
                pygame.mixer.music.play()
                audio_tocando["anterior"] = True
        else:
            if audio_tocando["anterior"]:
                pygame.mixer.music.stop()
                audio_tocando["anterior"] = False

        # Audio menu
        if botao_casa.collidepoint(pos):
            if not audio_tocando["menu"]:
                pygame.mixer.music.load(som_menu)
                pygame.mixer.music.play()
                audio_tocando["menu"] = True
        else:
            if audio_tocando["menu"]:
                pygame.mixer.music.stop()
                audio_tocando["menu"] = False
        
        # Audio proximo
        if botao_direita and botao_direita.collidepoint(pos):
            if not audio_tocando["proximo"]:
                pygame.mixer.music.load(som_direita)
                pygame.mixer.music.play()
                audio_tocando["proximo"] = True
        else:
            if audio_tocando["proximo"]:
                pygame.mixer.music.stop()
                audio_tocando["proximo"] = False

        pygame.display.update()

def ranking():
    global canvas
    root = Tk()
    root.title("Ranking")
    root.geometry("1000x500")

    canvas = Canvas(root)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.bind_all("<MouseWheel>", on_mouse_wheel)  # Para Windows e macOS
    canvas.bind_all("<Button-4>", on_mouse_wheel)    # Para Linux
    canvas.bind_all("<Button-5>", on_mouse_wheel)    # Para Linux

    frame = Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    jogadores_adicionados = []  

    try:
        df = pd.read_json('jogadores.json')
        df['Média Tempo'] = (df['1° Tempo'] + df['2° Tempo']) / 2
        df_sorted = df.sort_values(by='Média Tempo', ascending=True)

        for _, row in df_sorted.iterrows():
            nome = row['Nome']
            if nome not in jogadores_adicionados:
                jogadores_adicionados.append(nome)  
                button = Button(frame, text=nome, command=lambda n=nome: mostra_info_jogador(n))
                button.pack(pady=10, padx=10)

        sair_button = Button(root, text="Sair", command=root.destroy, bg='red')
        sair_button.place(relx=1.0, rely=1.0, x=-20, y=-20, anchor='se')

    except FileNotFoundError:
        Label(frame, text="Não há jogadores registrados").pack()
        sair_button = Button(root, text="Sair", command=root.destroy, bg='red')
        sair_button.place(relx=1.0, rely=1.0, x=-20, y=-20, anchor='se')

    root.mainloop()

def mostra_info_jogador(nome):
    info_janela = Toplevel()
    info_janela.title(nome)
    info_janela.geometry("1200x600")

    try:
        df = pd.read_json('jogadores.json')
        jogador = df[df['Nome'] == nome]
        for index, row in jogador.iterrows():
            info_texto = f"NOME: {row['Nome']}      |       ACERTOS: {' - '.join(row['Acertos'])}       |       ERROS: {' - '.join(row['Erros'])}       |       PONTUAÇÃO: {row['Pontuação']} / 5       |    1° TEMPO: {row['1° Tempo']}/{tempo_fase1}    |       2° TEMPO: {row['2° Tempo']}/{tempo_fase2}"
            Label(info_janela, text=info_texto).pack()

    except FileNotFoundError:
        Label(info_janela, text="Não há jogadores registrados").pack()
        

def on_mouse_wheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")


def transicao():
    janela = pygame.display.set_mode((largura, altura))
    introducao = "introducao.mp4"
    video = VideoFileClip(introducao)
    video.preview()
    return 


def sair():
    pygame.quit()
    sys.exit()


transicao()
main()
