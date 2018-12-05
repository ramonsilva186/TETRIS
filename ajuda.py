import pygame
from pygame.locals import *
import ferramentas_menu as ferramentas
import menu

pygame.init() #inicia o pygame

#cores
vermelho = [255,0,0]
preto = [0, 0, 0]
branco = [255, 255, 255]

tamanho = largura, altura = (700, 460) #tamanho da tela
pygame.display.set_caption('TETRIS') # mensagem no topo da tela
tela = pygame.display.set_mode(tamanho)

imagem_fundo = 'ajudaimg.jpg' #imagem de fundo
imagem = pygame.image.load(imagem_fundo).convert()
clock = pygame.time.Clock()

def ajuda(): #função de ajuda do jogo

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        tela.blit(imagem, (0, 0))
        pygame.display.update()

        #opçõe de volta ao menu principal
        cursor3 = ferramentas.fer_menu(tela, ['Voltar'], 50, 400, None, 35, 1.4, preto, preto)

        if cursor3 == 0: #se a opção escolhida for 0, volta ao menu principal
            menu.menu_principal()

        exit()


