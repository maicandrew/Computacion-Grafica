import pygame

def set_sounds_gatos():
    gatos = dict()
    gato = pygame.mixer.Sound("Juego/Sonidos/Gatolv1-2.wav")
    gatos[1] = gato
    gatos[5] = gato
    gato = pygame.mixer.Sound("Juego/Sonidos/Gato1lv3.wav")
    gatos[9] = gato
    gato = pygame.mixer.Sound("Juego/Sonidos/Tankelv1.wav")
    gatos[2] = gato
    gato = pygame.mixer.Sound("Juego/Sonidos/Tankelv2.wav")
    gatos[6] = gato
    gato = pygame.mixer.Sound("Juego/Sonidos/Tankelv3.wav")
    gatos[10] = gato
    gato = pygame.mixer.Sound("Juego/Sonidos/Gatolv1-2.wav")
    gatos[3] = gato
    gato = pygame.mixer.Sound("Juego/Sonidos/Gatolv1-2.wav")
    gatos[7] = gato
    gato = pygame.mixer.Sound("Juego/Sonidos/Gatolv1-2.wav")
    gatos[11] = gato
    gato = pygame.mixer.Sound("Juego/Sonidos/Magolv1.wav")
    gatos[4] = gato
    gato = pygame.mixer.Sound("Juego/Sonidos/Magolv2.wav")
    gatos[8] = gato
    gato = pygame.mixer.Sound("Juego/Sonidos/Magolv3.wav")
    gatos[12] = gato
    return gatos
