import random
import pygame
from set_images import *

fact = 1300/1400
tics = 60
NEGRO = [0, 0, 0]
VERDE = [0,255,0]
ROJO = [255, 0, 0]
BLANCO = [255, 255, 255]
nivel = 1
tam = dict()
tam = {
"bloque" : [75,90],
"gato" : [150,55],
"generador" : [20,20],
"balas" : [40,36],
"enemigos" : [75, 55],
"moneda" : [25, 25]
}
legal = [240,80, 915,530]
mapas = set_mapas(fact)
tam["mapa"] = [int(mapas[1][0].get_width()), int(mapas[1][0].get_height())]
moneda = pygame.image.load("Juego/Mapa y gatos/Moneda.png")
moneda = pygame.transform.scale(moneda, [tam["moneda"][0], tam["moneda"][1]])
costos = dict()
costos = {
1 : 5,
2 : 10,
3 : 20,
4 : 30,
}
balas = set_balas(tam["balas"])
gatos = set_gatos(tam["gato"])
perros = set_perros(tam["enemigos"])
ancho = tam["mapa"][0]
alto = tam["mapa"][1]

class mapa(pygame.sprite.Sprite):
    def __init__(self, lvl, bit = 29):
        pygame.sprite.Sprite.__init__(self)
        a = tam["mapa"]
        self.image = pygame.Surface.subsurface(mapas[lvl][0], (0,0,a[0], a[1]))
        self.con = 0
        self.frame = 0
        self.bit = bit
        self.rect = self.image.get_rect()

    def update(self):
        if self.con < self.bit:
            self.con += 1
        else:
            self.frame = (self.frame + 1) % 2
            self.con = 0
        a = tam["mapa"]
        self.image = pygame.Surface.subsurface(mapas[nivel][self.frame], (0, 0, a[0], a[1]))

class Coin(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        a = tam["moneda"]
        self.image = pygame.Surface.subsurface(moneda, (0,0,a[0], a[1]))
        self.rect = self.image.get_rect()
        self.con = 0
        self.dur = 15
        self.frames = 9
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        if self.con <= self.dur*tics:
            self.con += 1
        a = tam["moneda"]
        self.image = pygame.Surface.subsurface(moneda, (0, 0, a[0], a[1]))

class Disparo(pygame.sprite.Sprite):
    def __init__(self, pos, type):
        pygame.sprite.Sprite.__init__(self)
        a = tam["balas"]
        self.image = pygame.Surface.subsurface(balas[type], (0, 0, a[0], a[1]))
        self.rect = self.image.get_rect()
        self.damage = 25
        self.type = type
        self.con = 0
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.vel = 120+((type-1)*40)

    def update(self):
        self.rect.x += self.vel/tics
        if self.con <= 2:
            self.con += 1
        else:
            self.con = 0
        a = tam["balas"]
        self.image = pygame.Surface.subsurface(balas[self.type], (a[0]*self.con, 0, a[0], a[1]))

class Torre (pygame.sprite.Sprite):
    def __init__(self, type, pos):
        pygame.sprite.Sprite.__init__(self)
        a = tam["gato"]
        self.image = pygame.Surface.subsurface(gatos[type], (0,0,a[0]/2,a[1]))
        self.type = type
        self.frame = 0
        self.con = 0
        self.rect = self.image.get_rect()
        self.vel = 0.5
        self.block = None
        self.atk = 0
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.health = 200
        self.click = True
        self.dead = False
        self.unlocked = True
        self.dis = None
        self.coin = None

    def update(self):
        if self.click and self.unlocked:
            self.rect.center = pygame.mouse.get_pos()
        else:
            if self.type == 1:
                if self.atk < tics/self.vel:
                    self.atk += 1
                else:
                    self.coin = Coin([self.rect.right,self.rect.y])
                    self.atk = 0
                if self.con < 10:
                    self.con += 1
                else:
                    self.frame = (self.frame + 1) % 2
                    self.con = 0
                if self.health <= 0:
                    self.dead = True
            elif self.type == 4 or self.type == 3:
                if self.atk < tics/self.vel:
                    self.atk += 1
                else:
                    self.dis = Disparo([self.rect.right,self.rect.y], self.type)
                    self.atk = 0
                if self.con < 10:
                    self.con += 1
                else:
                    self.frame = (self.frame + 1) % 2
                    self.con = 0
                if self.health <= 0:
                    self.dead = True
            elif self.type == 2:
                if self.con < 10:
                    self.con += 1
                else:
                    self.frame = (self.frame + 1) % 2
                    self.con = 0
                if self.health <= 0:
                    self.dead = True
        a =tam["gato"]
        self.image = pygame.Surface.subsurface(gatos[self.type], (a[0]/2*self.frame, 0, a[0]/2, a[1]))

class Enemigo(pygame.sprite.Sprite):
    def __init__(self, pos, type):
        pygame.sprite.Sprite.__init__(self)
        a = tam["enemigos"]
        self.image = self.image = pygame.Surface.subsurface(perros[type], (0,0,a[0],a[1]))
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.type = type
        self.frames = 3
        self.action = 0
        self.health = 200
        self.frame = 2
        self.damage = 25
        self.atk_speed = 1
        self.mov_speed = 120
        self.dead = False
        self.lag = 0
        self.con = 0
        self.atk = 0
        self.punch = False

    def update(self):
        #Caminar
        if self.action == 0:
            if self.lag <= 10:
                self.lag += 1
            else:
                self.lag = 0
                if self.con < self.frames:
                    self.con += 1
                else:
                    self.con = 0
            self.rect.x -= self.mov_speed/tics
        #Parado
        elif self.action == 1:
            if self.lag <= 10:
                self.lag += 1
            else:
                self.lag = 0
                if self.con < self.frames:
                    self.con += 1
                else:
                    self.con = 0
            if self.atk < tics/self.atk_speed:
                self.atk += 1
            else:
                self.action = 2
                self.frames = 1
                self.atk = 0
                self.con = 0
        #Atacando
        elif self.action == 2:
            if self.lag <= 10:
                self.lag += 1
            else:
                self.lag = 0
                if self.con <= self.frames:
                    self.con += 1
                else:
                    self.action = 1
                    self.atk = 0
                    self.con = 0
                    self.punch = True
        #Muriendo
        elif self.action == 3:
            if self.lag <= 10:
                self.lag += 1
            else:
                self.lag = 0
                if self.con <= self.frames:
                    self.con += 1
                else:
                    self.dead = True
        if self.health <= 0 and self.action != 3:
            self.frames = 0
            self.action = 3
            self.con = 0
        a = tam["enemigos"]
        en_y = 0
        if self.action < 2:
            en_y = self.action
        else: en_y = self.action - 1
        self.image = pygame.Surface.subsurface(perros[self.type], (a[0]*self.con, en_y*a[1], a[0], a[1]))

def colocar(pos):
    if legal[0] <= pos[0] <= legal[2] and legal[1] <= pos[1] <= legal[3]:
        return True
    else: return False

'''class stats(pygame.sprote.Sprite):
    def __init__(self, b, pos):
        pygame.sprite.Sprite.__init__(self)'''

class Bloque(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(tam["bloque"])
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.oc = False

class Generador (pygame.sprite.Sprite):
    def __init__(self, pos, type):
        pygame.sprite.Sprite.__init__(self)
        a = tam["gato"]
        self.image = pygame.Surface.subsurface(gatos[type], (0, 0,a[0]/2, a[1]))
        self.rect=self.image.get_rect()
        self.type = type
        self.rect.x = pos[0]
        self.rect.y = pos[1]

class GeneradorEnemigo (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20,20])
        self.rect = self.image.get_rect()
        self.cd = 0
        self.con = 0
        self.cant = 0
        self.tope = 3
        self.gen = 0

    def update(self):
        if self.con <= self.cd*tics:
            self.con += 1
        elif self.cant <= self.tope:
            self.gen = 1
            self.con = 0
            self.cd = 10
            self.cant += 1

if __name__ == '__main__':
    #Definicion de variables
    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])

    todos = pygame.sprite.Group()
    torres = pygame.sprite.Group()
    bloques = pygame.sprite.Group()
    enemigos = pygame.sprite.Group()
    hud = pygame.sprite.Group()
    disparos = pygame.sprite.Group()
    coins = pygame.sprite.Group()
    mapita = mapa(1)
    ge = GeneradorEnemigo()
    todos.add(mapita)
    todos.add(ge)

    g1 = Generador([20,50], 1)
    g2 = Generador([20,200], 2)
    g3 = Generador([20,350], 3)
    hud.add(g1)
    todos.add(g1)
    hud.add(g2)
    todos.add(g2)
    hud.add(g3)
    todos.add(g3)

    x = legal[0]
    y = legal[1]
    for i in range(9):
        for j in range(5):
            bloque = Bloque([x + (i*tam["bloque"][0]), y + (j*tam["bloque"][1])])
            bloques.add(bloque)

    last = None
    mp = [0,0]
    reloj=pygame.time.Clock()
    fin=False
    lose = False
    win = False
    exit = False
    total_coins = 100
    while not fin:
        #Gestion de eventos
        while not (lose or win or exit or fin):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fin=True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for g in hud:
                        if g.rect.collidepoint(event.pos):
                            if total_coins >= costos[g.type]:
                                mp = event.pos
                                m8 = Torre(g.type, event.pos)
                                last = m8
                                torres.add(m8)
                                todos.add(m8)
                    for b in torres:
                        if b.rect.collidepoint(event.pos):
                            if b.unlocked:
                                b.click = True
                                last = b
                                break
                            '''else:
                                stats(b, event.pos)'''
                    for c in coins:
                        if c.rect.collidepoint(event.pos):
                            total_coins += 5
                            print(total_coins)
                            coins.remove(c)
                            todos.remove(c)
                            break

                if event.type == pygame.MOUSEBUTTONUP:
                    if event.pos == mp or not colocar(event.pos):
                        todos.remove(last)
                        torres.remove(last)
                        last = None
                    for t in torres:
                        if t.rect.collidepoint(event.pos):
                            t.click = False
                    for b in bloques:
                        if b.rect.collidepoint(event.pos) and last != None:
                            if not b.oc:
                                last.rect.center = b.rect.center
                                last.unlocked = False
                                last.block = b
                                b.oc = True
                                total_coins -= costos[last.type]
                                print(total_coins)
                                last = None
                            else:
                                todos.remove(last)
                                torres.remove(last)
                                last = None
            for t in torres:
                if t.dis != None:
                    disparos.add(t.dis)
                    todos.add(t.dis)
                    t.dis = None
                if t.coin != None:
                    coins.add(t.coin)
                    todos.add(t.coin)
                    t.coin = None
                if t.dead:
                    t.block.oc = False
                    todos.remove(t)
                    torres.remove(t)
            if ge.gen != 0:
                en = Enemigo([915,80+(random.randint(0,4)*tam["bloque"][1])], 1)
                enemigos.add(en)
                todos.add(en)
                en = None
                ge.gen = 0

            for d in disparos:
                if d.rect.x >= ancho:
                    disparos.remove(d)
                    todos.remove(d)

            for enemigo in enemigos:
                if enemigo.rect.x <= legal[0]:
                    lose = True
                    print("Pierde")
                if enemigo.dead or enemigo.rect.x <= 0:
                    todos.remove(enemigo)
                    enemigos.remove(enemigo)
                else:
                    ls_col = pygame.sprite.spritecollide(enemigo, disparos, False)
                    for d in ls_col:
                        enemigo.health -= d.damage
                        todos.remove(d)
                        disparos.remove(d)
                    ls_coli = pygame.sprite.spritecollide(enemigo, torres, False)
                    if len(ls_coli) > 0:
                        for t in ls_coli:
                            if (not t.unlocked) and enemigo.action == 0:
                                enemigo.action = 1
                            if enemigo.punch:
                                t.health -= enemigo.damage
                                enemigo.punch = False
                    elif enemigo.action != 3:
                        enemigo.action = 0
            if ge.cant > ge.tope:
                if len(enemigos.sprites()) == 0:
                    win = True
                    print("Gana")

            todos.update()
            todos.draw(pantalla)
            pygame.display.flip()
            reloj.tick(tics)
        fin = True
