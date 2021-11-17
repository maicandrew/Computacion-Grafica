import random
import pygame
from set_images import *
#Inicia setting de variables globales
pygame.init()
fact = 1300/1400
tics = 60
NEGRO = [0, 0, 0]
VERDE = [0,255,0]
ROJO = [255, 0, 0]
BLANCO = [255, 255, 255]
nivel = 1
tam = dict()
#Diccionario de tamaños
tam = {
"bloque" : [75, 90],
"gato" : [150, 55],
"generador" : [75, 100],
"cartas" : [200, 270],
"balas" : [40, 36],
"enemigos" : [75, 55],
"moneda" : [25, 25],
"arco" : [50, 50],
"rayo" : [313, 56]
}
legal = [240,80, 915,530]
mapas = set_mapas(fact)
tam["mapa"] = [int(mapas[1][0].get_width()), int(mapas[1][0].get_height())]
moneda = pygame.image.load("Juego/Mapa y gatos/Moneda.png")
moneda = pygame.transform.scale(moneda, [tam["moneda"][0], tam["moneda"][1]])
costos = dict()
costos = {
1 : 5,
2 : 15,
3 : 10,
4 : 15,
5: 15,
6: 15,
7 : 15,
8 : 20,
9 : 30,
10 : 25,
11 : 20,
12 : 40
}
damage = dict()
damage = {
1 : 0,
2 : 1,
3 : 3,
4 : 2,
5 : 0,
6 : 2,
7 : 3,
8 : 3,
9 : 0,
10 : 3,
11 : 4,
12 : 6,
}
cartas = set_cartas(tam["cartas"])
balas = set_balas(tam["balas"], tam["rayo"])
gatos = set_gatos(tam["gato"])
perros = set_perros(tam["enemigos"])
bosses = set_boss(tam["enemigos"])
arco = pygame.image.load("Juego/Cartas y mejoras/arco.png")
arco = pygame.transform.scale(arco, tam["arco"])
ancho = tam["mapa"][0]
alto = tam["mapa"][1]
#Termina setting de variables globales

class mapa(pygame.sprite.Sprite):
    def __init__(self, lvl, bit = 29):
        pygame.sprite.Sprite.__init__(self)
        a = tam["mapa"]
        self.image = pygame.Surface.subsurface(mapas[lvl][0], (0,0,a[0], a[1]))
        self.con = 0
        self.frame = 0
        self.lvl = lvl
        self.bit = bit
        self.rect = self.image.get_rect()

    def update(self):
        if self.con < self.bit:
            self.con += 1
        else:
            self.frame = (self.frame + 1) % 2
            self.con = 0
        a = tam["mapa"]
        self.image = pygame.Surface.subsurface(mapas[self.lvl][self.frame], (0, 0, a[0], a[1]))

class Arco(pygame.sprite.Sprite):
    def __init__(self, pos, gato):
        pygame.sprite.Sprite.__init__(self)
        a = tam["arco"]
        self.image = pygame.Surface.subsurface(arco, (0, 0, a[0], a[1]))
        self.rect = self.image.get_rect()
        self.gato = gato
        self.rect.x=  pos[0]
        self.rect.y = pos[1]

class Coin(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        a = tam["moneda"]
        self.image = pygame.Surface.subsurface(moneda, (0,0,a[0], a[1]))
        self.rect = self.image.get_rect()
        self.con = 0
        self.dur = 15
        self.des = False
        self.frames = 9
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        if self.con <= self.dur*tics:
            self.con += 1
        else:
            self.des = True
        a = tam["moneda"]
        self.image = pygame.Surface.subsurface(moneda, (0, 0, a[0], a[1]))

class Disparo(pygame.sprite.Sprite):
    def __init__(self, pos, type):
        pygame.sprite.Sprite.__init__(self)
        a = tam["balas"]
        self.image = pygame.Surface.subsurface(balas[type], (0, 0, a[0], a[1]))
        self.rect = self.image.get_rect()
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

class Rayo(pygame.sprite.Sprite):
    def __init__(self, pos, type):
        pygame.sprite.Sprite.__init__(self)
        a = tam["rayo"]
        self.image = pygame.Surface.subsurface(balas[type], (0,0,a[0], a[1]))
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.type = type
        self.con = 0

    def update(self):
        if self.con < 9:
            self.con += 1
        else:
            self.con = 0
        a = tam["rayo"]
        self.image = pygame.Surface.subsurface(balas[self.type], (0, self.con*a[1], a[0], a[1]))

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
        self.rayo = None
        self.coin = None

    def upgrade(self):
        if self.type <= 8:
            self.type += 4
        else:
            print("Nivel máximo alcanzado")

    def update(self):
        if self.click and self.unlocked:
            self.rect.center = pygame.mouse.get_pos()
        else:
            if self.type == 1 or self.type == 5 or self.type == 9:
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
            elif self.type == 3 or self.type == 7 or self.type == 11:
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
            elif self.type == 4 or self.type == 8 or self.type == 12:
                if self.atk < tics/self.vel:
                    self.atk += 1
                else:
                    self.rayo = Rayo([self.rect.right,self.rect.y], self.type)
                    self.atk = 0
                if self.con < 10:
                    self.con += 1
                else:
                    self.frame = (self.frame + 1) % 2
                    self.con = 0
                if self.health <= 0:
                    self.dead = True
            elif self.type == 2 or self.type == 6 or self.type == 10:
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
        self.frames = 11
        self.action = 0
        self.health = 50
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
        en_y = 0
        if self.action == 0:
            if self.lag <= 10:
                self.lag += 1
            else:
                self.lag = 0
                if self.con < self.frames-1:
                    self.con += 1
                else:
                    self.con = 0
            self.rect.x -= self.mov_speed/tics
        #Parado
        elif self.action == 1:
            self.frames = 6
            if self.lag <= 10:
                self.lag += 1
            else:
                self.lag = 0
                if self.con < self.frames-1:
                    self.con += 1
                else:
                    self.con = 0
            en_y = 2
            if self.atk < tics/self.atk_speed:
                self.atk += 1
            else:
                self.action = 2
                self.frames = 1
                self.atk = 0
                self.con = 0
        #Atacando
        elif self.action == 2:
            self.frames = 6
            if self.lag <= 10:
                self.lag += 1
            else:
                self.lag = 0
                if self.con <= self.frames-1:
                    self.con += 1
                else:
                    self.action = 1
                    self.atk = 0
                    self.con = 0
                    self.punch = True
            en_y = 2
        #Muriendo
        elif self.action == 3:
            self.frames = 4
            if self.lag <= 10:
                self.lag += 1
            else:
                self.lag = 0
                if self.con <= self.frames-1:
                    self.con += 1
                else:
                    self.dead = True
            en_y = 5
        if self.health <= 0 and self.action != 3:
            self.frames = 0
            self.action = 3
            self.con = 0
        a = tam["enemigos"]
        self.image = pygame.Surface.subsurface(perros[self.type], (a[0]*self.con, en_y*a[1], a[0], a[1]))

class Boss(pygame.sprite.Sprite):
    def __init__(self, pos, type):
        pygame.sprite.Sprite.__init__(self)
        a = tam["enemigos"]
        self.image = pygame.Surface.subsurface(bosses[type], (0,0,a[0],a[1]))
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.frames = 4
        self.action = 0
        self.con = 0
        self.health = 500
        self.damage = 1000
        self.mov_speed = 480
        self.atk = 0
        self.atk_speed = 1
        self.lag = 0
        self.punch = False
        self.dead = False

    def update(self):
        #Caminar
        en_y = 0
        if self.action == 0:
            if self.lag <= 10:
                self.lag += 1
            else:
                self.lag = 0
                if self.con < self.frames-1:
                    self.con += 1
                else:
                    self.con = 0
            self.rect.x -= self.mov_speed/tics
        #Parado
        elif self.action == 1:
            self.frames = 4
            if self.lag <= 10:
                self.lag += 1
            else:
                self.lag = 0
                if self.con < self.frames-1:
                    self.con += 1
                else:
                    self.con = 0
            en_y = 0
            if self.atk < tics/self.atk_speed:
                self.atk += 1
            else:
                self.action = 2
                self.frames = 1
                self.atk = 0
                self.con = 0
        #Atacando
        elif self.action == 2:
            self.frames = 5
            if self.lag <= 10:
                self.lag += 1
            else:
                self.lag = 0
                if self.con <= self.frames-1:
                    self.con += 1
                else:
                    self.action = 1
                    self.atk = 0
                    self.con = 0
                    self.punch = True
            en_y = 1
        #Muriendo
        elif self.action == 3:
            self.frames = 3
            if self.lag <= 10:
                self.lag += 1
            else:
                self.lag = 0
                if self.con <= self.frames-1:
                    self.con += 1
                else:
                    self.dead = True
            en_y = 2
        if self.health <= 0 and self.action != 3:
            self.frames = 0
            self.action = 3
            self.con = 0
        a = tam["enemigos"]
        self.image = pygame.Surface.subsurface(bosses[self.type], (a[0]*self.con, en_y*a[1], a[0], a[1]))

class Carta(pygame.sprite.Sprite):
    def __init__(self, pos, type):
        pygame.sprite.Sprite.__init__(self)
        a = tam["cartas"]
        self.image = pygame.Surface.subsurface(cartas[type], (0, 0, a[0], a[1]))
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

def colocar(pos):
    if legal[0] <= pos[0] <= legal[2] and legal[1] <= pos[1] <= legal[3]:
        return True
    else: return False

class Bloque(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(tam["bloque"])
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.oc = False

class Texto(pygame.sprite.Sprite):
    def __init__(self, pos, texto):
        pygame.sprite.Sprite.__init__(self)
        fuente = pygame.font.Font(None, 40)
        text = fuente.render(texto, 0, BLANCO)
        self.image = text
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

class Generador (pygame.sprite.Sprite):
    def __init__(self, pos, type):
        pygame.sprite.Sprite.__init__(self)
        a = tam["generador"]
        self.image = pygame.Surface.subsurface(pygame.transform.scale(cartas[type], a), (0, 0,a[0], a[1]))
        self.rect=self.image.get_rect()
        self.type = type
        self.rect.x = pos[0]
        self.rect.y = pos[1]

class GeneradorEnemigo (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20,20])
        self.rect = self.image.get_rect()
        self.rect.x = ancho
        self.cd = 0
        self.con = 0
        self.cant = 0
        self.tope = 1
        self.gen = 0
        self.boss = False

    def update(self):
        if self.con <= self.cd*tics:
            self.con += 1
        elif self.cant <= self.tope:
            self.gen = 1
            self.con = 0
            self.cd = 10
            self.cant += 1

def in_game(sc, lvl):
    #Definicion de variables
    pygame.mixer.init()
    pygame.mixer.set_num_channels(20)

    todos = pygame.sprite.Group()
    torres = pygame.sprite.Group()
    bloques = pygame.sprite.Group()
    enemigos = pygame.sprite.Group()
    hud = pygame.sprite.Group()
    disparos = pygame.sprite.Group()
    coins = pygame.sprite.Group()
    rayos = pygame.sprite.Group()
    mapita = mapa(lvl)
    ge = GeneradorEnemigo()
    todos.add(mapita)
    todos.add(ge)

    g1 = Generador([20,30], 1)
    g2 = Generador([20,150], 2)
    g3 = Generador([20,270], 3)
    g4 = Generador([20,390], 4)
    hud.add(g1)
    todos.add(g1)
    hud.add(g2)
    todos.add(g2)
    hud.add(g3)
    todos.add(g3)
    hud.add(g4)
    todos.add(g4)

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
    card = None
    bow = None
    total_coins = 100
    text = Texto([0,0], str(total_coins))
    todos.add(text)
    pygame.mixer.music.load("Juego/Sonidos/Mapa1.mp3")
    pygame.mixer.music.play(-1)
    while not fin:
        #Gestion de eventos
        while not (lose or win or exit or fin):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fin=True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if bow != None:
                        if bow.rect.collidepoint(event.pos) and bow.gato.type <= 8:
                            if total_coins >= costos[bow.gato.type+4]:
                                bow.gato.upgrade()
                                total_coins -= costos[bow.gato.type]
                                print(total_coins)
                            else:
                                print("Monedas insuficientes")
                        todos.remove(bow)
                        bow = None
                    if card != None:
                        todos.remove(card)
                        card = None
                    for g in hud:
                        #Verifica qué generador quiere usar
                        if g.rect.collidepoint(event.pos):
                            if total_coins >= costos[g.type]:
                                mp = event.pos
                                m8 = Torre(g.type, event.pos)
                                last = m8
                                torres.add(m8)
                                todos.add(m8)
                    for b in torres:
                        if b.rect.collidepoint(event.pos):
                            #Hace que la torre siga el mouse
                            if b.unlocked:
                                b.click = True
                                last = b
                                break
                            else:
                                #Muestra la carta de stats
                                card = Carta([b.rect.right, b.rect.y], b.type)
                                bow = Arco([b.rect.right+tam["cartas"][0], b.rect.y], b)
                                todos.add(bow)
                                todos.add(card)
                    for c in coins:
                        #verifica si la moneda lleva mucho tiempo y desaparece
                        if c.des:
                            coins.remove(c)
                            todos.remove(c)
                        #Verifica si se da click en la moneda para recolectarla
                        if c.rect.collidepoint(event.pos):
                            total_coins += 5
                            print(total_coins)
                            coins.remove(c)
                            todos.remove(c)
                            break

                if event.type == pygame.MOUSEBUTTONUP:
                    if event.pos == mp or not colocar(event.pos):
                        #Si la torre está fuera de lugar, desaparece
                        todos.remove(last)
                        torres.remove(last)
                        last = None
                    for t in torres:
                        #Suelta la torre
                        if t.rect.collidepoint(event.pos):
                            t.click = False
                    for b in bloques:
                        if b.rect.collidepoint(event.pos) and last != None:
                            if not b.oc:
                                #Si el bloque no está ocupado, pone la torre
                                last.rect.center = b.rect.center
                                last.unlocked = False
                                last.block = b
                                b.oc = True
                                total_coins -= costos[last.type]
                                print(total_coins)
                                last = None
                            else:
                                #Si el bloque está ocupado, desaparece la torre que iba a poner
                                todos.remove(last)
                                torres.remove(last)
                                last = None
            for t in torres:
                if t.dis != None:
                    #Genera el disparo
                    disparos.add(t.dis)
                    todos.add(t.dis)
                    dis = pygame.mixer.Sound("C:/FFOutput/Gatolv1-2.wav")
                    dis.play()
                    t.dis = None
                if t.rayo != None:
                    rayos.add(t.rayo)
                    todos.add(t.rayo)
                    t.rayo = None
                if t.coin != None:
                    #Genera la moneda
                    coins.add(t.coin)
                    todos.add(t.coin)
                    t.coin = None
                if t.dead:
                    #Verifica si la torre está muerta y desocupa el bloque
                    t.block.oc = False
                    todos.remove(t)
                    torres.remove(t)
            if ge.gen != 0:
                if ge.cant <= ge.tope:
                    #Genera un enemigo en una línea al azar
                    en = Enemigo([915,80+(random.randint(0,4)*tam["bloque"][1])], 1)
                    enemigos.add(en)
                    todos.add(en)
                    en = None
                    ge.gen = 0
                else:
                    if len(enemigos.sprites()) == 0:
                        if not ge.boss:
                            boss = Boss([915,80], 1)
                            enemigos.add(boss)
                            todos.add(boss)
                            print("Sale el boss")
                            ge.boss = True
                        else:
                            print("Gana")
                            win = True

            todos.remove(text)
            text = Texto([0,0], str(total_coins))
            todos.add(text)

            for d in disparos:
                #elimina el disparo si pasó el limite de la pantalla
                if d.rect.x >= ancho:
                    disparos.remove(d)
                    todos.remove(d)

            for r in rayos:
                if r.con >= 9:
                    rayos.remove(r)
                    todos.remove(r)

            for enemigo in enemigos:
                if enemigo.rect.x <= legal[0]:
                    #Pierde si un enemigo llega a la zona izquierda del jardín
                    lose = True
                    print("Pierde")
                if enemigo.dead:
                    #Borra al enemigo si está muerto
                    todos.remove(enemigo)
                    enemigos.remove(enemigo)
                else:
                    #Verifica las colisiones con los disparos
                    ls_col = pygame.sprite.spritecollide(enemigo, disparos, False)
                    for d in ls_col:
                        enemigo.health -= damage[d.type]
                        todos.remove(d)
                        disparos.remove(d)
                    #Verifica las colisiones con los disparos
                    ls_col2 = pygame.sprite.spritecollide(enemigo, rayos, False)
                    for d in ls_col2:
                        enemigo.health -= damage[d.type]

                    #Verifica las colisiones con las torres
                    ls_coli = pygame.sprite.spritecollide(enemigo, torres, False)
                    #If para prevenir  que se queden parados si matan al gato que estaban atacando
                    if len(ls_coli) > 0:
                        for t in ls_coli:
                            if (not t.unlocked) and enemigo.action == 0:
                                enemigo.action = 1
                            if enemigo.punch:
                                t.health -= enemigo.damage
                                enemigo.punch = False
                            break
                    elif enemigo.action != 3:
                        enemigo.action = 0

            todos.update()
            todos.draw(sc)
            pygame.display.flip()
            reloj.tick(tics)
        fin = True
        pygame.mixer.music.stop()
    if win:
        in_game(sc, 2)
    if lose:
        Menu()

def Menu():
    menu = False
    pantalla=pygame.display.set_mode([ancho,alto])
    pantalla.fill(NEGRO)
    pygame.display.flip()
    while not menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                menu = True
                in_game(pantalla, 1)


if __name__ == '__main__':
    Menu()
