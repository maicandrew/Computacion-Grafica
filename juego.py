import random
import pygame

ancho=600
alto=600
centro=[300,300]

def apantalla(c,p):
    x = c[0] + p[0]
    y = c[1] - p[1]
    return [x,y]

def acartesiana(c,p):
    x=p[0]-c[0]
    y=c[1]-p[1]
    return [x,y]

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
        self.salud=5

    def update(self):
        self.rect.x += self.vel_x
        if self.rect.y > 75:
            self.rect.y += self.vel_y
        elif self.vel_y > 0:
             self.rect.y+= self.vel_y
        else: self.rect.y = 75
        if self.rect.y>(alto-self.rect.height):
            self.rect.y= alto-self.rect.height


class Enemigo (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([30,30])
        self.image.fill([0,250,250])
        self.rect=self.image.get_rect()
        self.rect.x=0
        self.rect.y=0
        self.vel_x=0-random.randrange(3,5)
        self.vel_y=0
        self.espera=random.randrange(50)
        self.temp=random.randrange(100)
        self.disparo=False

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        if self.temp > 0:
            self.temp-=1
        else:
            self.disparo=True

        if self.espera > 0:
            self.espera-=1
        else:
            self.rect.x+=self.vel_x


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



if __name__ == '__main__':
    #DEfinicion de variables
    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])
    jugador = Jugador()

    jugadores = pygame.sprite.Group()
    enemigos = pygame.sprite.Group()
    todos = pygame.sprite.Group()
    balas = pygame.sprite.Group()
    balas_e = pygame.sprite.Group()

    jugadores.add(jugador)
    todos.add(jugador)

    num_enemigos=15
    for i in range(num_enemigos):
        e = Enemigo()
        e.rect.x=random.randrange(640,1000)
        e.rect.y=random.randrange(75,alto-e.rect.height)
        enemigos.add(e)
        todos.add(e)


    fuente=pygame.font.Font(None,32)
    reloj=pygame.time.Clock()
    ptos=0
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
                if event.key == pygame.K_SPACE:
                    b=Bala()
                    b.rect.x=jugador.rect.x
                    b.rect.y=jugador.rect.y
                    balas.add(b)
                    todos.add(b)


        #Logica del programa
        eliminados=0
        ls_col = pygame.sprite.spritecollide(jugador, enemigos, True)
        #ls_col = pygame.sprite.spritecollide(jugador, enemigos, False)
        for e in ls_col:
            ptos+=1
            print ('puntos; ', ptos)
            enemigos.remove(e)
            todos.remove(e)
            jugador.salud-=1
            eliminados+=1

        for b in balas_e:
            ls_colj=pygame.sprite.spritecollide(b,jugadores,False)
            if jugador in ls_colj:
                balas_e.remove(b)
                todos.remove(b)
                jugador.salud-=1
                print ('salud: ', jugador.salud)

            if b.rect.x < -20:
                balas_e.remove(b)
                todos.remove(b)

        for e in enemigos:
            if e.disparo:
                e.temp=random.randrange(100)
                e.disparo=False
                b=Bala()
                b.vel_x=-10
                b.rect.x=e.rect.x
                b.rect.y=e.rect.y
                b.image.fill([250,0,250])
                balas_e.add(b)
                todos.add(b)

            if e.rect.x < -30:
                enemigos.remove(e)
                todos.remove(e)
                eliminados+=1

        for e in balas:
            ls_coli = pygame.sprite.spritecollide(e, enemigos, True)
            for b in ls_coli:
                enemigos.remove(b)
                todos.remove(b)
                balas.remove(e)
                todos.remove(e)
                eliminados+=1
            if e.rect.x > ancho:
                balas.remove(e)
                todos.remove(e)

        for i in range(eliminados):
            e = Enemigo()
            e.rect.x=random.randrange(640,1200)
            e.rect.y=random.randrange(75,alto-e.rect.height)
            enemigos.add(e)
            todos.add(e)




        #REfresco de pantalla
        pantalla.fill([0,0,0])
        texto=fuente.render("Salud ", False,[250,250,250])
        txt_valor=fuente.render(str(jugador.salud), False, [250,250,250])
        pantalla.blit(texto,[50,10])
        pantalla.blit(txt_valor,[140,10])
        todos.update()
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(50)
