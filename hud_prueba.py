import random
import pygame

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
"gato" : [120,44],
"generador" : [20,20],
"balas" : [20,20],
"enemigos" : [120, 44]
}
gatos = dict()
mapas = dict()
BLANCO = [255, 255, 255]
legal = [240,80, 915,530]
map = pygame.image.load("Mapa1.1.png")
tam["mapa"] = [int(map.get_width()*fact), int(map.get_height()*fact)]
map = pygame.transform.scale(map,tam["mapa"])
mapas[nivel] = map
gato = pygame.image.load("Gato1.png")
gato = pygame.transform.scale(gato,tam["gato"])
gatos[nivel] = gato
ancho = int(map.get_width()/2)
alto = int(map.get_height())

class mapa(pygame.sprite.Sprite):
    def __init__(self,image, lim = 29):
        pygame.sprite.Sprite.__init__(self)
        a = tam["mapa"]
        self.image = pygame.Surface.subsurface(image, (0,0,a[0]/2, a[1]))
        self.con = 0
        self.frame = 0
        self.lim = lim
        self.rect = self.image.get_rect()

    def update(self):
        if self.con < self.lim:
            self.con += 1
        else:
            self.frame = (self.frame + 1) % 2
            self.con = 0
        self.image = pygame.Surface.subsurface(mapas[nivel], (ancho*self.frame, 0, ancho, alto))

class Torre (pygame.sprite.Sprite):
    def __init__(self, type, pos):
        pygame.sprite.Sprite.__init__(self)
        a = tam["gato"]
        self.image = pygame.Surface.subsurface(gatos[type], (0,0,a[0]/2,a[1]))
        self.rect = self.image.get_rect()
        self.type = type
        self.frame = 0
        self.con = 0
        self.vel = 0.5
        self.lvl = 1
        self.atk = 0
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.health = 200
        self.click = True
        self.dead = False
        self.unlocked = True
        self.dis = None

    def update(self):
        if self.click and self.unlocked:
            self.rect.center = pygame.mouse.get_pos()
        else:
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

        a =tam["gato"]
        self.image = pygame.Surface.subsurface(gatos[self.type], (a[0]/2*self.frame, 0, a[0]/2, a[1]))

class Enemigo(pygame.sprite.Sprite):
    def __init__(self, pos, type):
        pygame.sprite.Sprite.__init__(self)
        a = tam["enemigos"]
        self.image = pygame.Surface([a[0]/2, a[1]])
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.type = type
        self.frames = 3
        self.action = 0
        self.health = 200
        self.atk_speed = 1
        self.mov_speed = 60
        self.dead = False
        self.con = 0
        self.atk = 0
        self.punch = False

    def update(self):
        #Caminar
        if self.action == 0:
            if self.con < self.frames:
                self.con += 1
            else:
                self.rect.x -= self.mov_speed/60
                self.con = 0
        #Parado
        elif self.action == 1:
            if self.con < self.frames:
                self.con += 1
            else:
                self.con = 0
            if e.atk < tics/e.atk_speed:
                    e.atk += 1
            else:
                e.action = 2
                e.atk = 0
                e.con = 0
        #Atacando
        elif self.action == 2:
            if self.con <= self.frames:
                self.con += 1
                self.image.fill(BLANCO)
            else:
                self.image.fill(NEGRO)
                self.action = 1
                self.atk = 0
                self.con = 0
                self.punch = True
        #Muriendo
        elif self.action == 3:
            if self.con <= self.frames:
                self.con += 1
            else:
                self.dead = True
        if self.health <= 0 and self.action != 3:
            self.action = 3
            self.con = 0
        #self.image = pygame.Surface.subsurface(gatos[self.type], (a[0]/2*self.frame, 0, a[0]/2, a[1]))

class Disparo(pygame.sprite.Sprite):
    def __init__(self, pos, type):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(tam["balas"])
        self.image.fill(NEGRO)
        self.rect = self.image.get_rect()
        self.damage = 25*type
        self.type = type
        #self.lvl = type
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.vel = 120+((type-1)*40)

    def update(self):
        self.rect.x += self.vel/tics

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
    def __init__(self, color, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(tam["generador"])
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

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
    mapita = mapa(map)
    todos.add(mapita)
    ene = Enemigo([915,80], 1)
    todos.add(ene)
    enemigos.add(ene)

    g1 = Generador(ROJO, [20,50])
    hud.add(g1)
    todos.add(g1)
    g2 = Generador(VERDE, [20,100])
    hud.add(g2)
    todos.add(g2)
    g3 = Generador(BLANCO, [20,150])
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
    while not fin:
        #Gestion de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if g1.rect.collidepoint(event.pos):
                    mp = event.pos
                    m8 = Torre(1, event.pos)
                    last = m8
                    torres.add(m8)
                    todos.add(m8)
                if g2.rect.collidepoint(event.pos):
                    mp = event.pos
                    m8 = Torre(1, event.pos)
                    last = m8
                    torres.add(m8)
                    todos.add(m8)
                if g3.rect.collidepoint(event.pos):
                    mp = event.pos
                    m8 = Torre(1, event.pos)
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

            if event.type == pygame.MOUSEBUTTONUP:
                if event.pos == mp or not colocar(event.pos):
                    todos.remove(last)
                    torres.remove(last)
                    last = None
                for t in torres:
                    if t.rect.collidepoint(event.pos):
                        t.click = False
                for b in  bloques:
                    if b.rect.collidepoint(event.pos) and last != None:
                        if not b.oc:
                            last.rect.center = b.rect.center
                            last.unlocked = False
                            b.oc = True
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
            if t.dead:
                todos.remove(t)
                torres.remove(t)

        for d in disparos:
            if d.rect.x >= ancho:
                disparos.remove(d)
                todos.remove(d)
        for e in enemigos:
            if e.dead:
                todos.remove(e)
                enemigos.remove(e)
            else:
                ls_col = pygame.sprite.spritecollide(e, disparos, False)
                for d in ls_col:
                    if d.type == 1:
                        e.health -= 25
                    todos.remove(d)
                    disparos.remove(d)
                ls_coli = pygame.sprite.spritecollide(e, torres, False)
                if len(ls_coli) > 0:
                    for t in ls_coli:
                        if not t.unlocked and e.action == 0:
                            e.action = 1
                        if e.punch:
                            t.health -= 25
                            e.punch = False
                elif not e.dead and not e.action == 3:
                    e.action = 0

        todos.update()
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(tics)
