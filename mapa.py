import pygame, math

ancho=600
alto=600
centro=[300,300]
NEGRO = [0, 0, 0]
VERDE = [0,255,0]
ROJO = [255, 0, 0]
sp = pygame.image.load("ken.png")
reloj = pygame.time.Clock()

def pasos(pos1, pos2):
    dx = pos2[0]-pos1[0]
    dy = pos2[1]-pos1[1]
    steps = 0
    if math.fabs(abs(dx)) >= math.fabs(abs(dy)):
        steps = int(math.fabs(dx))
    else: steps = int(math.fabs(dy))
    dx /= steps
    dy /= steps
    return [steps, dx, dy]

class Jugador(pygame.sprite.Sprite):
    """docstring for Jugador."""
    def __init__(self):
        super(Jugador, self).__init__()
        self.accion = 1
        self.frames = 4
        self.image = pygame.Surface.subsurface(sp, (0, 80, 70,80))
        self.con = 0
        self.busy = False
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
        self.vel_x = 0
        self.vel_y = 0
    def update(self):
        if self.con < self.frames-1:
            self.con += 1
        else:
            self.con = 0
            self.accion = 1
            self.frames = 4
            self.busy = False
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        self.image = pygame.Surface.subsurface(sp, (70*self.con, 80*self.accion, 70, 80))

class Bola(pygame.sprite.Sprite):
    def __init__ (self, pos, dir):
        super(Bola, self).__init__()
        self.f = 4
        self.image = pygame.Surface.subsurface(sp, (0, 320, 70, 80))
        self.con = 0
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.dir = dir
        algo = pasos(pos, dir)
        self.steps = algo[0]
        self.dx = algo[1]
        self.dy = algo[2]

    def update(self):
        if self.f == 4:
            self.con = (self.con + 1) % 2
            if self.steps >= 0:
                x = int(self.rect.center[0]+self.dx*10)
                y = int(self.rect.center[1]+self.dy*10)
                self.steps = self.steps-10
                self.rect.center = [x,y]
            else:
                self.f = 5
                self.con = 0
        else:
            self.con += self.con+1
        self.image = pygame.Surface.subsurface(sp, (70*self.con, 80*self.f, 70, 80))

jugador = Jugador()
todos = pygame.sprite.Group()
bolas = pygame.sprite.Group()
todos.add(jugador)

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
            if event.type == pygame.MOUSEBUTTONDOWN and not(jugador.busy):
                jugador.accion = 0
                jugador.frames = 4
                jugador.busy = True
                jugador.con = 0
                jugador.vel_y = 0
                jugador.vel_x = 0
                bola = Bola([jugador.rect.x+60,jugador.rect.y], event.pos)
                bolas.add(bola)
                todos.add(bola)
            if event.type == pygame.KEYDOWN and not(jugador.busy):
                if event.key == pygame.K_a:
                    jugador.accion = 6
                    jugador.frames = 5
                    jugador.busy = True
                    jugador.con = 0
                    jugador.vel_y = 0
                    jugador.vel_x = 0
                elif event.key == pygame.K_s:
                    jugador.accion = 8
                    jugador.frames = 7
                    jugador.busy = True
                    jugador.con = 0
                    jugador.vel_y = 0
                    jugador.vel_x = 0
                elif event.key == pygame.K_d:
                    jugador.accion = 7
                    jugador.frames = 5
                    jugador.busy = True
                    jugador.con = 0
                    jugador.vel_y = 0
                    jugador.vel_x = 0
                elif event.key == pygame.K_w:
                    jugador.accion = 2
                    jugador.frames = 3
                    jugador.busy = True
                    jugador.con = 0
                    jugador.vel_y = 0
                    jugador.vel_x = 0
                elif event.key == pygame.K_DOWN:
                    jugador.vel_y = 5
                elif event.key == pygame.K_UP:
                    jugador.vel_y = -5
                elif event.key == pygame.K_RIGHT:
                    jugador.vel_x = 5
                elif event.key == pygame.K_LEFT:
                    jugador.vel_x = -5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    jugador.vel_y = 0
                elif event.key == pygame.K_UP:
                    jugador.vel_y = 0
                elif event.key == pygame.K_RIGHT:
                    jugador.vel_x = 0
                elif event.key == pygame.K_LEFT:
                    jugador.vel_x = 0

        for b in bolas:
            if b.steps <= 0 and b.con > 2:
                bolas.remove(b)
                todos.remove(b)
        pantalla.fill(NEGRO)
        todos.update()
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(10)
