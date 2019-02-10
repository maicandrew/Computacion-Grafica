import pygame

def set_gatos(tam):
    gatos = dict()
    gato = pygame.image.load("Juego/Mapa y gatos/Gato1lv1.png")
    gato = pygame.transform.scale(gato,tam)
    gatos[1] = gato
    gato = pygame.image.load("Juego/Mapa y gatos/Gato2lv1.png")
    gato = pygame.transform.scale(gato,tam)
    gatos[2] = gato
    gato = pygame.image.load("Juego/Mapa y gatos/Gato3lv1.png")
    gato = pygame.transform.scale(gato,tam)
    gatos[3] = gato
    gato = pygame.image.load("Gato1.png")
    gato = pygame.transform.scale(gato,tam)
    gatos[4] = gato
    gato = pygame.image.load("Juego/Mapa y gatos/Gato1lv2.png")
    gato = pygame.transform.scale(gato,tam)
    gatos[5] = gato
    gato = pygame.image.load("Juego/Mapa y gatos/Gato2lv2.png")
    gato = pygame.transform.scale(gato,tam)
    gatos[6] = gato
    gato = pygame.image.load("Juego/Mapa y gatos/Gato3lv2.png")
    gato = pygame.transform.scale(gato,tam)
    gatos[7] = gato
    gato = pygame.image.load("Gato1.png")
    gato = pygame.transform.scale(gato,tam)
    gatos[8] = gato
    gato = pygame.image.load("Juego/Mapa y gatos/Gato1lv3.png")
    gato = pygame.transform.scale(gato,tam)
    gatos[9] = gato
    gato = pygame.image.load("Juego/Mapa y gatos/Gato2lv3.png")
    gato = pygame.transform.scale(gato,tam)
    gatos[10] = gato
    gato = pygame.image.load("Juego/Mapa y gatos/Gato3lv3.png")
    gato = pygame.transform.scale(gato,tam)
    gatos[11] = gato
    gato = pygame.image.load("Gato1.png")
    gato = pygame.transform.scale(gato,tam)
    gatos[12] = gato
    return gatos

def set_perros(tam):
    perros = dict()
    perro = pygame.image.load("Juego/enemigos/Enemigo2.png")
    perro = pygame.transform.scale(perro,[tam[0]*4, tam[1]*3])
    perros[1] = perro
    '''perro = pygame.image.load("Juego/Mapa y perros/perro2lv1.png")
    perro = pygame.transform.scale(perro,tam)
    perros[2] = perro
    perro = pygame.image.load("Juego/Mapa y perros/perro3lv1.png")
    perro = pygame.transform.scale(perro,tam)
    perros[3] = perro
    perro = pygame.image.load("perro1.png")
    perro = pygame.transform.scale(perro,tam)
    perros[4] = perro
    perro = pygame.image.load("Juego/Mapa y perros/perro1lv2.png")
    perro = pygame.transform.scale(perro,tam)
    perros[5] = perro
    perro = pygame.image.load("Juego/Mapa y perros/perro2lv2.png")
    perro = pygame.transform.scale(perro,tam)
    perros[6] = perro
    perro = pygame.image.load("Juego/Mapa y perros/perro3lv2.png")
    perro = pygame.transform.scale(perro,tam)
    perros[7] = perro
    perro = pygame.image.load("perro1.png")
    perro = pygame.transform.scale(perro,tam)
    perros[8] = perro
    perro = pygame.image.load("Juego/Mapa y perros/perro1lv3.png")
    perro = pygame.transform.scale(perro,tam)
    perros[9] = perro
    perro = pygame.image.load("Juego/Mapa y perros/perro2lv3.png")
    perro = pygame.transform.scale(perro,tam)
    perros[10] = perro
    perro = pygame.image.load("Juego/Mapa y perros/perro3lv3.png")
    perro = pygame.transform.scale(perro,tam)
    perros[11] = perro
    perro = pygame.image.load("perro1.png")
    perro = pygame.transform.scale(perro,tam)
    perros[12] = perro'''
    return perros

def set_balas(tam):
    balas = dict()
    bala = pygame.image.load("Juego/Mapa y gatos/disparos.png")
    bala = pygame.transform.scale(bala, [tam[0]*4, tam[1]*4])
    bala = pygame.Surface.subsurface(bala, (0, bala.get_height()*3/4, bala.get_width(), bala.get_height()*1/4))
    balas[1] = bala
    balas[2] = bala
    balas[3] = bala
    balas[4] = bala
    return balas
