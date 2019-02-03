import random
import pygame

ancho=650
alto=650
centro=[300,300]
NEGRO = [0, 0, 0]
VERDE = [0,255,0]
ROJO = [255, 0, 0]
map = pygame.image.load("terrenogen.png")

class Jugador (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([30,30])
        self.image.fill([0,250,0])
        self.rect=self.image.get_rect()
        self.rect.x=100
        self.rect.y=300
        self.vel_x=0
        self.vel_y=0

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

class Bloque (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image =pygame.Surface([50,50])
        self.image.fill(VERDE)
        self.rect = self.image.get_rect()
        self.click = False
    def update(self):
        if self.click:
            self.rect.center = pygame.mouse.get_pos()

class Generador (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20,20])
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()

class Enemigo (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([30,30])
        self.image.fill([0,250,250])
        self.rect=self.image.get_rect()
        self.rect.x=50
        self.rect.y=50
        self.vel_x=5
        self.vel_y=0

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y


class Bala (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20,10])
        self.image.fill([250,250,250])
        self.rect=self.image.get_rect()
        self.rect.x=0
        self.rect.y=0
        self.vel_x=10
        self.vel_y=0

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

class Muro(pygame.sprite.Sprite):
    def __init__(self, an, al):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([an,al])
        self.image.fill([250,250,0])
        self.rect=self.image.get_rect()

if __name__ == '__main__':
    #Definicion de variables
    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])

    jugadores = pygame.sprite.Group()
    enemigos = pygame.sprite.Group()
    todos = pygame.sprite.Group()
    muros = pygame.sprite.Group()
    flag = 0

    jugador = Jugador()
    m1 = Muro(20,600)
    m2 = Muro(20,600)
    m3 = Muro(600,20)
    m4 = Muro(600,20)
    m1.rect.x=0
    m1.rect.y=0
    m2.rect.x=580
    m2.rect.y=0
    m3.rect.x=0
    m3.rect.y=0
    m4.rect.x=0
    m4.rect.y=580
    todos.add(m1)
    muros.add(m1)
    todos.add(m2)
    muros.add(m2)
    todos.add(m3)
    muros.add(m3)
    todos.add(m4)
    muros.add(m4)

    m5 = Muro(100,50)
    m6 = Muro(60,100)
    m5.rect.x=300
    m5.rect.y=450
    m6.rect.x=120
    m6.rect.y=150
    todos.add(m5)
    muros.add(m5)
    todos.add(m6)
    muros.add(m6)

    m7 = Generador()
    m7.rect.x = 100
    m7.rect.y = 100
    todos.add(m7)

    m8 = Bloque()
    m8.rect.x = -500

    e = Enemigo()

    jugadores.add(jugador)
    todos.add(jugador)
    enemigos.add(e)
    todos.add(e)

    reloj=pygame.time.Clock()
    fin=False
    while not fin:
        #Gestion de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    jugador.vel_y=-5
                    jugador.vel_x=0
                if event.key == pygame.K_DOWN:
                    jugador.vel_y=5
                    jugador.vel_x=0
                if event.key == pygame.K_LEFT:
                    jugador.vel_y=0
                    jugador.vel_x=-5
                if event.key == pygame.K_RIGHT:
                    jugador.vel_y=0
                    jugador.vel_x=5
            if event.type == pygame.KEYUP:
                jugador.vel_y=0
                jugador.vel_x=0
            if event.type == pygame.MOUSEBUTTONDOWN:
                if m7.rect.collidepoint(event.pos):
                    m8 = Bloque()
                    todos.add(m8)
                    flag = 1
                if m8.rect.collidepoint(event.pos):
                    m8.click = True
            if event.type == pygame.MOUSEBUTTONUP and flag != 0:
                if m8.rect.collidepoint(event.pos):
                    m8.click = False

        #Logica del juego

        ls_col = pygame.sprite.spritecollide(jugador, muros, False)
        for m in ls_col:
            if (jugador.vel_x > 0) and (jugador.rect.right >= m.rect.left):
                jugador.vel_x = 0
                jugador.rect.right = m.rect.left
            if (jugador.vel_y > 0) and (jugador.rect.bottom >= m.rect.top):
                jugador.vel_y = 0
                jugador.rect.bottom = m.rect.top
            if (jugador.vel_x < 0) and (jugador.rect.left <= m.rect.right):
                jugador.vel_x = 0
                jugador.rect.left = m.rect.right
            if (jugador.vel_y < 0) and (jugador.rect.top <= m.rect.bottom):
                jugador.vel_y = 0
                jugador.rect.top = m.rect.bottom

        ls_coli = pygame.sprite.spritecollide(e, muros, False)
        for m in ls_coli:
            if (e.vel_x > 0) and (e.rect.right >= m.rect.left):
                e.vel_x = 0
                e.vel_y = 3
                e.rect.right = m.rect.left
            else:
                if (e.vel_y > 0) and (e.rect.bottom >= e.rect.top):
                    e.vel_y = 0
                    e.vel_x =-3
                    e.rect.bottom = m.rect.top
                else:
                    if (e.vel_x < 0) and (e.rect.left <= m.rect.right):
                        e.vel_x = 0
                        e.vel_y =-3
                        e.rect.left = m.rect.right
                    else:
                        if (e.vel_y < 0) and (e.rect.top <= m.rect.bottom):
                            e.vel_y = 0
                            e.vel_x = 3
                            e.rect.top = m.rect.bottom

        todos.update()
        pantalla.blit(map, [0,0])
        pantalla.fill(NEGRO)
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(50)
