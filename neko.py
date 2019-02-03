import pygame

ancho=600
alto=600
centro=[300,300]
NEGRO = [0, 0, 0]
VERDE = [0,255,0]
ROJO = [255, 0, 0]
sp = pygame.image.load("animals.png")
reloj = pygame.time.Clock()

class Jugador(pygame.sprite.Sprite):
    """docstring for Jugador."""
    def __init__(self):
        super(Jugador, self).__init__()
        self.accion = 0
        self.mov = False
        self.image = pygame.Surface.subsurface(sp, (96, 32, 32,32))
        self.con = 4
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
        self.vel_x = 0
        self.vel_y = 0
    def update(self):
        if self.mov:
            self.con = 3+((self.con+1)%3)
        else:
            self.con = 4
            self.accion = 0
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        self.image = pygame.Surface.subsurface(sp, (32*self.con, 32*(self.accion+4), 32,32))

jugador = Jugador()

if __name__ == '__main__':
    #DEfinicion de variables
    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])
    #for i in range(0,12):
        #for j in range(0,32):
        #    cuadro = pygame.Surface.subsurface(sp, (32*j, i*32, 32,32))
        #    pantalla.blit(cuadro, [32*j,32*i])
        #    pygame.display.flip()
    fin = False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    jugador.accion = 0
                    jugador.mov = True
                    jugador.con = 0
                    jugador.vel_y = 0
                    jugador.vel_x = 0
                    jugador.vel_y = 5
                elif event.key == pygame.K_UP:
                    jugador.accion = 3
                    jugador.mov = True
                    jugador.con = 0
                    jugador.vel_x = 0
                    jugador.vel_y = -5
                elif event.key == pygame.K_RIGHT:
                    jugador.accion = 2
                    jugador.mov = True
                    jugador.con = 0
                    jugador.vel_y = 0
                    jugador.vel_x = 5
                elif event.key == pygame.K_LEFT:
                    jugador.accion = 1
                    jugador.mov = True
                    jugador.con = 0
                    jugador.vel_y = 0
                    jugador.vel_x = -5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    jugador.vel_y = 0
                    jugador.mov = False
                elif event.key == pygame.K_UP:
                    jugador.vel_y = 0
                    jugador.mov = False
                elif event.key == pygame.K_RIGHT:
                    jugador.vel_x = 0
                    jugador.mov = False
                elif event.key == pygame.K_LEFT:
                    jugador.vel_x = 0
                    jugador.mov = False
        pantalla.fill(NEGRO)
        pantalla.blit(jugador.image, [jugador.rect.x,jugador.rect.y])
        jugador.update()
        pygame.display.flip()
        reloj.tick(10)
