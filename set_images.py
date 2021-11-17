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
    gato = pygame.image.load("Juego/Mapa y gatos/Gato4lv1.png")
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
    gato = pygame.image.load("Juego/Mapa y gatos/Gato4lv2.png")
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
    gato = pygame.image.load("Juego/Mapa y gatos/Gato4lv3.png")
    gato = pygame.transform.scale(gato,tam)
    gatos[12] = gato
    return gatos

def set_perros(tam):
    perros = dict()
    perro = pygame.image.load("Juego/enemigos/Enemigo2.1.png")
    perro = pygame.transform.scale(perro,[tam[0]*11, tam[1]*4])
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

def set_balas(tam, tam2, tam3):
    balas = dict()
    bala = pygame.image.load("Juego/Mapa y gatos/disparos.png")
    bala = pygame.transform.scale(bala, [tam[0]*4, tam[1]*4])
    bala = pygame.Surface.subsurface(bala, (0, bala.get_height()*3/4, bala.get_width(), bala.get_height()*1/4))
    espada = pygame.image.load("Juego/Mapa y gatos/EfectoEspadaLv1.png")
    espada = pygame.transform.scale(espada, [tam3[0], tam3[1]])
    espada = pygame.Surface.subsurface(espada, (0, 0, espada.get_width(), espada.get_height()))
    balas[1] = bala
    balas[2] = espada
    balas[3] = bala
    bala1 = pygame.image.load("Juego/Mapa y gatos/Hechisolv2-3.png")
    bala1 = pygame.transform.scale(bala1, [tam2[0]*2, tam2[1]*10])
    bala1 = pygame.Surface.subsurface(bala1, (0, 0, bala1.get_width(), bala1.get_height()))
    balas[4] = bala1
    espada = pygame.image.load("Juego/Mapa y gatos/EfectoEspadaLv2.png")
    espada = pygame.transform.scale(espada, [tam3[0], tam3[1]])
    espada = pygame.Surface.subsurface(espada, (0, 0, espada.get_width(), espada.get_height()))
    balas[5] = bala
    balas[6] = espada
    balas[7] = bala
    balas[8] = bala1
    balas[9] = bala
    espada = pygame.image.load("Juego/Mapa y gatos/EfectoEspadaLv3.png")
    espada = pygame.transform.scale(espada, [tam3[0]*4, tam3[1]])
    espada = pygame.Surface.subsurface(espada, (0, 0, espada.get_width(), espada.get_height()))
    balas[10] = espada
    balas[11] = bala
    balas[12] = bala1
    bala = pygame.image.load("Juego/enemigos/DisparoMegaP.png")
    bala = pygame.Surface.subsurface(bala, (41, 0, 84, bala.get_height()))
    bala = pygame.transform.scale(bala, tam)
    balas["jefe1"] = bala
    return balas

def set_cartas(tam):
    cartas = dict()
    carta = pygame.image.load("Juego/Cartas y mejoras/Carta 1.png")
    carta = pygame.transform.scale(carta, tam)
    cartas[1] = carta
    carta = pygame.image.load("Juego/Cartas y mejoras/Carta 7.png")
    carta = pygame.transform.scale(carta, tam)
    cartas[2] = carta
    carta = pygame.image.load("Juego/Cartas y mejoras/Carta 4.png")
    carta = pygame.transform.scale(carta, tam)
    cartas[3] = carta
    carta = pygame.image.load("Juego/Cartas y mejoras/Carta 10.png")
    carta = pygame.transform.scale(carta, tam)
    cartas[4] = carta
    carta = pygame.image.load("Juego/Cartas y mejoras/Carta 2.png")
    carta = pygame.transform.scale(carta, tam)
    cartas[5] = carta
    carta = pygame.image.load("Juego/Cartas y mejoras/Carta 8.png")
    carta = pygame.transform.scale(carta, tam)
    cartas[6] = carta
    carta = pygame.image.load("Juego/Cartas y mejoras/Carta 5.png")
    carta = pygame.transform.scale(carta, tam)
    cartas[7] = carta
    carta = pygame.image.load("Juego/Cartas y mejoras/Carta 11.png")
    carta = pygame.transform.scale(carta, tam)
    cartas[8] = carta
    carta = pygame.image.load("Juego/Cartas y mejoras/Carta 3.png")
    carta = pygame.transform.scale(carta, tam)
    cartas[9] = carta
    carta = pygame.image.load("Juego/Cartas y mejoras/Carta 9.png")
    carta = pygame.transform.scale(carta, tam)
    cartas[10] = carta
    carta = pygame.image.load("Juego/Cartas y mejoras/Carta 6.png")
    carta = pygame.transform.scale(carta, tam)
    cartas[11] = carta
    carta = pygame.image.load("Juego/Cartas y mejoras/Carta 12.png")
    carta = pygame.transform.scale(carta, tam)
    cartas[12] = carta
    return cartas

def set_mapas(factor):
    mapas = dict()
    mapa = []
    mapita = pygame.image.load("Juego/Mapa y gatos/Mapa1.1.jpg")
    mapita = pygame.transform.scale(mapita, [int(mapita.get_width()*factor), int(mapita.get_height()*factor)])
    mapa.append(mapita)
    mapita = pygame.image.load("Juego/Mapa y gatos/Mapa1.2.jpg")
    mapita = pygame.transform.scale(mapita, [int(mapita.get_width()*factor), int(mapita.get_height()*factor)])
    mapa.append(mapita)
    mapas[1] = mapa
    return mapas

def set_boss(tam):
    jefes = dict()
    jefe = pygame.image.load("Juego/enemigos/Boss1.png")
    jefe = pygame.transform.scale(jefe, [tam[0]*8, tam[1]*2])
    jefes[1] = jefe
    jefe = pygame.image.load("Juego/enemigos/Boss2.png")
    jefe = pygame.transform.scale(jefe, [tam[0]*6, tam[1]*3])
    jefes[2] = jefe
    return jefes

def set_botones(fact):
    botones = dict()
    boton = pygame.image.load("Juego/Menus/Continuar.png")
    boton = pygame.transform.scale(boton, [int(boton.get_width()*fact), int(boton.get_height()*fact)])
    botones["continuar"] = boton
    boton = pygame.image.load("Juego/Menus/Play.png")
    boton = pygame.transform.scale(boton, [int(boton.get_width()*fact), int(boton.get_height()*fact)])
    botones["jugar"] = boton
    boton = pygame.image.load("Juego/Menus/Salir.png")
    boton = pygame.transform.scale(boton, [int(boton.get_width()*fact), int(boton.get_height()*fact)])
    botones["salir"] = boton
    boton = pygame.image.load("Juego/Menus/Historia.png")
    boton = pygame.transform.scale(boton, [int(boton.get_width()*fact), int(boton.get_height()*fact)])
    botones["historia"] = boton
    botones[0] = pygame.Surface([20,20])
    return botones

def set_monedas(tam):
    monedas = dict()
    moneda = pygame.image.load("Juego/Sistema de economia/Moneda1.png")
    moneda = pygame.transform.scale(moneda, tam)
    monedas[1] = moneda
    moneda = pygame.image.load("Juego/Sistema de economia/Moneda3.png")
    moneda = pygame.transform.scale(moneda, tam)
    monedas[3] = moneda
    moneda = pygame.image.load("Juego/Sistema de economia/Moneda5.png")
    moneda = pygame.transform.scale(moneda, tam)
    monedas[5] = moneda
    moneda = pygame.image.load("Juego/Sistema de economia/Moneda.png")
    moneda = pygame.transform.scale(moneda, tam)
    monedas[0] = moneda
    return monedas
