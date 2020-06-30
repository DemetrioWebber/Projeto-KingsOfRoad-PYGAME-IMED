import pygame
import time
import random
import assets
from savegame import funcaoArmazenamento

nome = input("Digite seu nome: ")
email = input("Digite seu E-mail: ")
funcaoArmazenamento(nome, email)

pygame.init()

#--------------Variaveis de definição----------------
tela_altura = 800
tela_largura = 800
gamedisplay = pygame.display.set_mode((tela_largura,tela_altura))
pygame.display.set_caption("Kings of Road")
icon = pygame.image.load("assets/icone.png.png")
pygame.display.set_icon(icon)
motormantendo = pygame.mixer.Sound("assets/mantendo.wav")
motoracelerando = pygame.mixer.Sound("assets/acelerando.wav")
freio = pygame.mixer.Sound("assets/freio.wav")
turbo = pygame.mixer.Sound("assets/turbo.wav")
estrelaimg = pygame.image.load("assets/estrela.png")
estrela = pygame.transform.scale(estrelaimg, (50,50))

clock = pygame.time.Clock()
#RGB
black = (0,0,0)
white = (255,255,255)
carronormal = pygame.image.load("assets/r33.png")
carro_largura = 180
carro_altura = 130
carro = pygame.transform.scale(carronormal, (carro_largura,carro_altura))

policianormal = pygame.image.load("assets/policia.png")
policia_largura = 180
policia_altura = 130
policia = pygame.transform.scale(policianormal, (policia_largura,policia_altura))

fundo = pygame.image.load("assets/fundo.png").convert()


#--------------funções globais--------------

def mostrarCarro(x,y):
    gamedisplay.blit(carro, (x,y))

def mostrapolicia(x,y):
    gamedisplay.blit(policia, (x,y))

def text_objects(text,font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def messageDisplay(text):
    largeText = pygame.font.Font("freesansbold.ttf", 100)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((tela_largura/2, tela_altura/2))
    gamedisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(3)
    gameloop()

def nivelprocurado(text):
    largeText = pygame.font.Font("freesansbold.ttf", 30)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((400, 50))
    gamedisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    

def escreveplacar(contador):
    font = pygame.font.SysFont("freesansbold.ttf", 50)
    text = font.render("Fugas: "+str(contador), True, white)
    gamedisplay.blit(text, (20,30))

def morreu():
    pygame.mixer.Sound.play(freio)
    pygame.mixer.music.stop()
    motormantendo.stop()
    motoracelerando.stop()
    turbo.stop()
    messageDisplay("Perdeu Playboy")
#----- loop do jogo ------

#-------------definição do game loop------------
def gameloop():
    pygame.mixer.music.load("assets/musica.wav")
    pygame.mixer.music.play(-1)
    desvios = 0
    fundo_posicaoY = 0
    policia_posicaoX = random.randrange(0, 700)
    policia_posicaoY = -100
    policia_velocidade = 0
    carro_posicaoX = 320
    carro_posicaoY = 670
    movimentoX = 0
    movimentoY = 0

    while True:
        #Vai fazer com que os elementos requisitados continuem sendo mostrados.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                funcaoArmazenamento(nome, email, desvios)
                quit()

    #-----------Mapeamento de teclas---------------
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                movimentoX = movimentoX - 1
            elif event.key == pygame.K_d:
                movimentoX = movimentoX + 1
            elif event.key == pygame.K_w:
                fundo_posicaoY = fundo_posicaoY + 5
                motoracelerando.play()
                motoracelerando.set_volume(0.4)
                motormantendo.stop()
                policia_velocidade = policia_velocidade + 4
            elif event.key == pygame.K_s:
                movimentoY = movimentoY + 1
                fundo_posicaoY = fundo_posicaoY - 1
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or pygame.K_d or pygame.K_w or pygame.K_s:
                movimentoX = 0
                movimentoY = 0
                motormantendo.play()
                motormantendo.set_volume(0.1)
                motoracelerando.stop()
                if event.key == pygame.K_w:
                    turbo.play()
                    turbo.set_volume(0.3)

        if carro_posicaoY > tela_altura - carro_altura:
            carro_posicaoY = tela_altura - carro_altura
        elif carro_posicaoY < 0:
            carro_posicaoY = 0
        

        if carro_posicaoX > tela_largura - carro_largura:
            carro_posicaoX = tela_largura - carro_largura
        elif carro_posicaoX < 0:
            carro_posicaoX = 0

        carro_posicaoX = carro_posicaoX + movimentoX
        carro_posicaoY = carro_posicaoY + movimentoY



    #------------------Fundo animado-------------------

        rel_fundoY = fundo_posicaoY % fundo.get_rect().width
        gamedisplay.blit(fundo, (0,rel_fundoY - fundo.get_rect().width))
        if rel_fundoY < tela_altura:
            gamedisplay.blit(fundo, (0, rel_fundoY + 10))
        fundo_posicaoY += 3

    #-----------------------Carros---------------------
        mostrarCarro(carro_posicaoX,carro_posicaoY)

    #----------------------Policia---------------------
        policia_posicaoY = policia_posicaoY + policia_velocidade
        if policia_posicaoY > 810:
            policia_posicaoY = -200
            policia_posicaoX = random.randrange(0, 700)
            desvios = desvios + 1
        if desvios < 10:
            policia_velocidade = 5
            gamedisplay.blit(estrela, (550, 20))
        elif desvios < 20:
            policia_velocidade = 10
            gamedisplay.blit(estrela, (550, 20)) and gamedisplay.blit(estrela, (600, 20))
        elif desvios < 30:
            policia_velocidade = 15
            gamedisplay.blit(estrela, (550, 20)) and gamedisplay.blit(estrela, (600, 20)) and gamedisplay.blit(estrela, (650, 20))
        elif desvios >= 30:
            policia_velocidade = 20
            gamedisplay.blit(estrela, (550, 20)) and gamedisplay.blit(estrela, (600, 20)) and gamedisplay.blit(estrela, (650, 20)) and gamedisplay.blit(estrela, (700, 20))
#------------------Contadores--------------------
        escreveplacar(desvios)

        mostrapolicia(policia_posicaoX,policia_posicaoY)
        nivelprocurado("Nivel de procurado: ")
#---------------------Colisao------------------------
        if carro_posicaoY + 10 < policia_posicaoY + policia_altura:
            if carro_posicaoX < policia_posicaoX and carro_posicaoX + carro_largura > policia_posicaoX or policia_posicaoX + policia_largura > carro_posicaoX and policia_posicaoX + policia_largura < carro_posicaoX + carro_largura:
                morreu()
                pygame.mixer.Sound.play(freio)

    #---------------------Update de tela----------------
        pygame.display.update()
        clock.tick(60)
gameloop()