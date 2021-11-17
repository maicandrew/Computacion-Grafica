import random
import time
import pygame
from set_images import *
from set_sounds import *
#Inicia setting de variables globales
pygame.init()
fact = 1300/1400
tics = 60
NEGRO = [0, 0, 0]
VERDE = [0,255,0]
ROJO = [255, 0, 0]
BLANCO = [255, 255, 255]
legal = [[240,80, 915,530], [180,65,925,513]]
reloj=pygame.time.Clock()
tam = dict()
#Diccionario de tamaños
tam = {
"bloque" : [75, 90],
"gato" : [150, 55],
"generador" : [75, 100],
"cartas" : [200, 270],
"balas" : [40, 36],
"enemigos" : [75, 75],
"moneda" : [25, 25],
"arco" : [50, 50],
"rayo" : [313, 56],
"espada" : [90, 75],
"boton" : [100, 20]
}
mapas = set_mapas(fact)
tam["mapa"] = [int(mapas[1][0].get_width()), int(mapas[1][0].get_height())]
healths = dict()
healths = {
1 : 3,
2 : 10,
3 : 4,
4 : 5,
5 : 3,
6 : 15,
7 : 4,
8 : 5,
9 : 3,
10 : 25,
11 : 6,
12 : 5,
}
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
damage_enemigos = dict()
damage_enemigos = {
1 : 1,
2 : 0.5,
3 : 1,
4 : 0.7,
5: 1,
6: 1.5
}
healths_enemigos = dict()
healths_enemigos = {
1 : 30,
2 : 45,
3 : 15,
4 : 9,
5: 27,
6: 18
}
frames_enemigos = dict()
frames_enemigos = {
1: [8,5,5,4],
2: [11,4,6,4],
3: [11,3,5,4],
4: [8,7,9,4],
5: [8,5,5,4],
6: [10,8,8,4]
}
cartas = set_cartas(tam["cartas"])
balas = set_balas(tam["balas"], tam["rayo"], tam["espada"])
gatos = set_gatos(tam["gato"])
perros = set_perros(tam["enemigos"])
bosses = set_boss(tam["enemigos"])
monedas = set_monedas(tam["moneda"])
botones = set_botones(0.5)
King = set_final(tam["gato"])
sounds_gatos = set_sounds_gatos()
explode = pygame.mixer.Sound("Juego/Sonidos/Explosion sonido efecto.wav")
#sounds_enemigos = set_sounds_enemigos()
arco = pygame.image.load("Juego/Cartas y mejoras/arco.png")
arco = pygame.transform.scale(arco, tam["arco"])
ancho = tam["mapa"][0]
alto = tam["mapa"][1]
tutos = set_tutorial([ancho, alto])
print(alto, ancho)

tam["linea"] = [ancho - legal[0][0], int((legal[0][3] - legal[0][1]) / 5)]
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
    def __init__(self, pos, value):
        pygame.sprite.Sprite.__init__(self)
        a = tam["moneda"]
        self.image = pygame.Surface.subsurface(monedas[value], (0,0,a[0], a[1]))
        self.rect = self.image.get_rect()
        self.con = 0
        self.dur = 15
        self.des = False
        self.value = value
        self.frames = 9
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        if self.value != 0:
            if self.con <= self.dur*tics:
                self.con += 1
            else:
                self.des = True
        a = tam["moneda"]
        self.image = pygame.Surface.subsurface(monedas[self.value], (0, 0, a[0], a[1]))

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

class DisparoEnemigo(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        a = tam["balas"]
        self.image = balas["jefe1"]
        self.rect = self.image.get_rect()
        self.type = type
        self.con = 0
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.vel = 120

    def update(self):
        self.rect.x -= self.vel/tics

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

class Espada(pygame.sprite.Sprite):
    def __init__(self, pos, type):
        pygame.sprite.Sprite.__init__(self)
        a = tam["espada"]
        self.image = pygame.Surface.subsurface(balas[type], (0, 0, a[0], a[1]))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.type = type
        self.lag = 0
        self.con = 0
        self.des = False

    def update(self):
        if self.lag <= 10:
            self.lag += 1
        elif self.con < 3:
            self.con += 1
            self.lag = 0
        else:
            self.des = True
        if self.type == 10:
            a= tam["espada"]
            self.image = pygame.Surface.subsurface(balas[self.type], (a[0]*self.con,0,a[0], a[1]))

class Torre (pygame.sprite.Sprite):
    def __init__(self, type, pos):
        pygame.sprite.Sprite.__init__(self)
        a = tam["gato"]
        self.image = pygame.Surface.subsurface(gatos[type], (0,0,a[0]/2,a[1]))
        self.type = type
        self.frame = 0
        self.con = 0
        self.rect = self.image.get_rect()
        if type in[1,5,9]:
            self.vel = 0.2
        else:
            self.vel = 0.5
        self.block = None
        self.lin = None
        self.range = None
        self.atk = 0
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.health = healths[type]
        self.perro = False
        self.click = True
        self.dead = False
        self.unlocked = True
        self.dis = None
        self.rayo = None
        self.sw = None
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
                    self.coin = Coin([self.rect.right,self.rect.y], int((self.type+1)/2))
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
                    if self.perro:
                        self.atk += 1
                    else:
                        self.atk = 0
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
                    if self.perro:
                        self.atk += 1
                    else:
                        self.atk = 0
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
                if self.atk < tics/self.vel:
                    if self.perro:
                        self.atk += 1
                    else:
                        self.atk = 0
                else:
                    self.sw = Espada([self.rect.right, self.rect.y], self.type)
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
        self.image = self.image = pygame.Surface.subsurface(perros[type], (0,0,a[0],a[1]))
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.type = type
        self.frames = 11
        self.action = 0
        self.health = healths_enemigos[type]
        self.frame = 2
        self.damage = damage_enemigos[type]
        self.atk_speed = 1
        if type == 6:
            self.mov_speed = 180
        else:
            self.mov_speed = 60
        self.dead = False
        self.lag = 0
        self.con = 0
        self.atk = 0
        self.punch = False

    def update(self):
        self.frames = frames_enemigos[self.type][self.action]
        #Caminar
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
            if self.lag <= 10:
                self.lag += 1
            else:
                self.lag = 0
                if self.con < self.frames-1:
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
                if self.con < self.frames-1:
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
                if self.con < self.frames-1:
                    self.con += 1
                else:
                    self.dead = True
        if self.health <= 0 and self.action != 3:
            self.frames = 0
            self.action = 3
            self.con = 0
        a = tam["enemigos"]
        self.image = pygame.Surface.subsurface(perros[self.type], (a[0]*self.con, self.action*a[1], a[0], a[1]))

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
        self.health = 50
        self.damage = 1000
        self.mov_speed = 30
        self.atk = 0
        self.atk_speed = 1
        self.lag = 0
        self.t = False
        self.punch = False
        self.dead = False

    def update(self):
        if self.type == 1:
            self.frames = 8
            en_x = self.frames - (self.con + 1)
            en_y = 0
            #Caminar y disparar
            if self.health > 0:
                if self.lag <= 10:
                    self.lag += 1
                else:
                    self.lag = 0
                    if self.con < self.frames-1:
                        self.con += 1
                    else:
                        self.con = 0
                if self.atk < tics/self.atk_speed:
                    self.atk += 1
                else:
                    self.atk = 0
                    self.punch = True
                if not self.t:
                    self.rect.x -= self.mov_speed/tics
            #Muriendo
            else:
                en_y = 1
                if self.lag <= 10:
                    self.lag += 1
                else:
                    self.lag = 0
                    if self.con < self.frames - 1:
                        self.con += 1
                    else:
                        self.con = 0
                        self.dead = True
        elif self.type == 2:
            en_y = 0
            #Caminar
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
                    if self.con < self.frames-1:
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
                    if self.con < self.frames-1:
                        self.con += 1
                    else:
                        self.dead = True
                en_y = 2
            if self.health <= 0 and self.action != 3:
                self.frames = 0
                self.action = 3
                self.con = 0
        #Saltando
        #if self.action == 4:
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

class KingSword(pygame.sprite.Sprite):
    def __init__(self, pos, type):
        pygame.sprite.Sprite.__init__(self)
        a = tam["cartas"]
        if type == 1:
            self.image = King["espada"]
        else:
            self.image = King["espada1"]
        self.rect = self.image.get_rect()
        self.type = type
        self.rect.x = pos[0]
        self.rect.y = pos[1]

def colocar(pos,lvl):
    if legal[lvl][0] <= pos[0] <= legal[lvl][2] and legal[lvl][1] <= pos[1] <= legal[lvl][3]:
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

class Linea(pygame.sprite.Sprite):
    def __init__(self, pos, tama):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(tama)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

class Texto(pygame.sprite.Sprite):
    def __init__(self, pos, texto):
        pygame.sprite.Sprite.__init__(self)
        fuente = pygame.font.Font(None, 40)
        text = fuente.render(texto, 0, NEGRO)
        self.image = text
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

class Pausa(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load("Juego/Menus/Cajon.png")
        self.image = pygame.transform.scale(image, [200, 140])
        self.rect = self.image.get_rect()
        self.rect.center = [int(ancho/2), int(alto/2)]

class Boton(pygame.sprite.Sprite):
    def __init__(self, pos, text = 0):
        pygame.sprite.Sprite.__init__(self)
        self.image = botones[text]
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
            self.cd = 0
            self.cant += 1
        else:
            self.gen = 1

def in_game(sc, lvl):
    #Definicion de variables
    pygame.mixer.init()
    pygame.mixer.set_num_channels(20)

    todos = pygame.sprite.Group()
    torres = pygame.sprite.Group()
    bloques = pygame.sprite.Group()
    enemigos = pygame.sprite.Group()
    hud = pygame.sprite.Group()
    disparo_enemigo = pygame.sprite.Group()
    disparos = pygame.sprite.Group()
    espadas = pygame.sprite.Group()
    rangos = pygame.sprite.Group()
    coins = pygame.sprite.Group()
    rayos = pygame.sprite.Group()
    lineas = pygame.sprite.Group()
    mapita = mapa(lvl)
    ge = GeneradorEnemigo()
    todos.add(mapita)
    todos.add(ge)

    botonpausa = Boton([0,0], "pausa")
    todos.add(botonpausa)

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

    espadita = None
    if lvl == 2:
        espadita = KingSword([110,432], 1)
        todos.add(espadita)

    gema = Coin([975,10], 0)
    todos.add(gema)

    x = legal[lvl-1][0]
    y = legal[lvl-1][1]
    for j in range(5):
        for i in range(9):
            bloque = Bloque([x + (i*tam["bloque"][0]), y + (j*tam["bloque"][1])])
            bloques.add(bloque)
        linea = Linea([x, y + (j*tam["linea"][1])], tam["linea"])
        lineas.add(linea)

    last = None
    mp = [0,0]
    fin=False
    lose = False
    win = False
    exit = False
    pause = False
    boss = None
    card = None
    bow = None
    nocard = False
    Total_score = 100500
    total_coins = 10000
    text = Texto([1000,10], str(total_coins))
    todos.add(text)
    pygame.mixer.music.load("Juego/Sonidos/Mapa1.mp3")
    pygame.mixer.music.play(-1)
    while not fin:
        #Gestion de eventos
        if not (lose or win or exit):
            if not(pause):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        fin=True
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if espadita != None:
                            if espadita.type > 1:
                                if espadita.rect.collidepoint(event.pos):
                                    for d in disparos:
                                        todos.remove(d)
                                    for r in rayos:
                                        todos.remove(r)
                                    for c in coins:
                                        todos.remove(coins)
                                    for g in hud:
                                        todos.remove(g)
                                    todos.draw(sc)
                                    Final_Scene(sc, todos)
                                    win = True
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
                        if botonpausa.rect.collidepoint(event.pos):
                            pause = True
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
                                    todos.add(m8)
                        for c in coins:
                            #verifica si la moneda lleva mucho tiempo y desaparece
                            if c.des:
                                coins.remove(c)
                                todos.remove(c)
                            #Verifica si se da click en la moneda para recolectarla
                            if c.rect.collidepoint(event.pos):
                                nocard = True
                                total_coins += c.value
                                Total_score -= c.value*5
                                print(total_coins)
                                coins.remove(c)
                                todos.remove(c)
                                break

                        for b in torres:
                            if b.rect.collidepoint(event.pos):
                                #Hace que la torre siga el mouse
                                if b.unlocked:
                                    b.click = True
                                    last = b
                                    break
                                elif not nocard:
                                    #Muestra la carta de stats
                                    card = Carta([b.rect.right, b.rect.y], b.type)
                                    bow = Arco([b.rect.right+tam["cartas"][0], b.rect.y], b)
                                    todos.add(bow)
                                    todos.add(card)

                        nocard = False
                    if event.type == pygame.MOUSEBUTTONUP:
                        if event.pos == mp or not colocar(event.pos, lvl-1):
                            #Si la torre está fuera de lugar, desaparece
                            todos.remove(last)
                            last = None
                        for t in torres:
                            #Suelta la torre
                            if t.rect.collidepoint(event.pos):
                                t.click = False

                        for b in bloques:
                            if b.rect.collidepoint(event.pos) and last != None:
                                if not b.oc:
                                    if last.type in [3, 7, 11]:
                                        lin_col = pygame.sprite.spritecollide(last, lineas, False)
                                        for l in lin_col:
                                            last.lin = l
                                            break
                                    elif last.type in [4, 8, 12]:
                                        last.range = Linea([last.rect.right, last.rect.y], tam["rayo"])
                                        rangos.add(last.range)
                                    #Si el bloque no está ocupado, pone la torre
                                    torres.add(last)
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
                                    last = None
                                break
                for t in torres:
                    if t.dead:
                        #Verifica si la torre está muerta y desocupa el bloque
                        t.block.oc = False
                        todos.remove(t)
                        torres.remove(t)
                    else:
                        d_col = pygame.sprite.spritecollide(t, disparo_enemigo, False)
                        for d in d_col:
                            t.health -= 2
                            todos.remove(d)
                            disparo_enemigo.remove(d)
                        if t.lin != None:
                            lin_ene = pygame.sprite.spritecollide(t.lin, enemigos, False)
                            if len(lin_ene) > 0:
                                t.perro = True
                            else: t.perro = False
                        elif t.type in [2, 6, 10]:
                            t_col = pygame.sprite.spritecollide(t, enemigos, False)
                            if len(t_col) > 0:
                                t.perro = True
                            else: t.perro = False
                        elif t.type in [4, 8, 12]:
                            r_col = pygame.sprite.spritecollide(t.range, enemigos, False)
                            if len(r_col):
                                t.perro = True
                            else:
                                t.perro = False
                        if t.dis != None:
                            #Genera el disparo
                            disparos.add(t.dis)
                            todos.add(t.dis)
                            sounds_gatos[t.type].play()
                            t.dis = None
                        if t.rayo != None:
                            rayos.add(t.rayo)
                            todos.add(t.rayo)
                            sounds_gatos[t.type].play()
                            t.rayo = None
                        if t.coin != None:
                            #Genera la moneda
                            coins.add(t.coin)
                            todos.add(t.coin)
                            sounds_gatos[t.type].play()
                            t.coin = None
                        if t.sw != None:
                            espadas.add(t.sw)
                            todos.add(t.sw)
                            sounds_gatos[t.type].play()
                            t.sw = None
                if ge.gen != 0:
                    if ge.cant <= ge.tope:
                        #Genera un e, nemigo en una línea al azar
                        en = Enemigo([ancho-tam["enemigos"][0],80+(random.randint(0,4)*tam["bloque"][1])], random.randint(1,6))
                        enemigos.add(en)
                        todos.add(en)
                        en = None
                        ge.gen = 0
                    else:
                        if len(enemigos.sprites()) == 0:
                            if not ge.boss:
                                pygame.mixer.music.stop()
                                pygame.mixer.music.load("Juego/Sonidos/WARNING!.mp3")
                                ge.cd = 11
                                ge.con = 0
                                ge.gen = 0
                                ge.boss = True
                                print("Boss is coming")
                                pygame.mixer.music.play()
                            elif boss == None:
                                boss = Boss([915,80], lvl)
                                enemigos.add(boss)
                                todos.add(boss)
                                pygame.mixer.music.stop()
                                pygame.mixer.music.load("Juego/Sonidos/Boss"+str(lvl)+".mp3")
                                pygame.mixer.music.play(-1)
                                print("Sale el boss")
                                if espadita != None:
                                    todos.remove(espadita)
                                    espadita = KingSword([110,432], lvl)
                                    todos.add(espadita)
                            else:
                                print("Gana")
                                win = True

                todos.remove(text)
                text = Texto([1000,10], str(total_coins))
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

                for e in espadas:
                    if e.des:
                        espadas.remove(e)
                        todos.remove(e)

                for enemigo in enemigos:
                    if enemigo.rect.x <= legal[lvl-1][0]:
                        #Pierde si un enemigo llega a la zona izquierda del jardín
                        lose = True
                        print("Pierde")
                    if enemigo.dead:
                        #Borra al enemigo si está muerto
                        c = Coin(enemigo.rect.center, 1)
                        coins.add(c)
                        todos.add(c)
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
                        for r in ls_col2:
                            enemigo.health -= damage[r.type]
                        ls_col3 = pygame.sprite.spritecollide(enemigo, espadas, False)
                        for es in ls_col3:
                            if es.con == 2:
                                enemigo.health -= damage[es.type]
                        #Verifica las colisiones con las torres
                        ls_coli = pygame.sprite.spritecollide(enemigo, torres, False)
                        #If para prevenir  que se queden parados si matan al gato que estaban atacando
                        if isinstance(enemigo, Boss) and enemigo.type == 1:
                            if enemigo.punch:
                                dis = DisparoEnemigo([enemigo.rect.left, enemigo.rect.y])
                                disparo_enemigo.add(dis)
                                todos.add(dis)
                                enemigo.punch = False
                            if len(ls_coli) > 0:
                                enemigo.t =  True
                            else:
                                enemigo.t = False
                        elif len(ls_coli) > 0:
                            for t in ls_coli:
                                if (not t.unlocked) and enemigo.action == 0:
                                    enemigo.action = 1
                                if enemigo.punch:
                                    if enemigo.type == 2 and isinstance(enemigo,Boss):
                                        explode.play()
                                    t.health -= enemigo.damage
                                    enemigo.punch = False
                                break
                        elif enemigo.action != 3:
                            enemigo.action = 0

                todos.update()
                todos.draw(sc)
                pygame.display.flip()
                reloj.tick(tics)
            else:
                pygame.mixer.music.pause()
                pausa = Pausa()
                continuar = Boton([int((ancho / 2) - 100), int((alto / 2) - 40)], "continuar")
                salir = Boton([continuar.rect.x + 55, continuar.rect.bottom + 20], "salir")
                sc.blit(pausa.image, [pausa.rect.x, pausa.rect.y])
                sc.blit(continuar.image, [continuar.rect.x, continuar.rect.y])
                sc.blit(salir.image, [salir.rect.x, salir.rect.y])
                pygame.display.flip()
                while not(exit or fin) and pause:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            fin=True
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if continuar.rect.collidepoint(event.pos):
                                pause = False
                                pygame.mixer.music.unpause()
                            elif salir.rect.collidepoint(event.pos):
                                exit = True
        else:
            fin = True
            pygame.mixer.music.stop()
    if win:
        Transition(sc, lvl, True)
    if lose:
        Transition(sc, lvl, False)
    if exit:
        Menu()

def Final_Scene(sc, todos):
    pygame.mixer.music.stop()
    GatoRey = King["gato"]
    sc.blit(GatoRey, [20,250])
    pygame.display.flip()
    omae = pygame.mixer.Sound("Juego/Escena final/Omae.wav")
    omae.play()
    time.sleep(omae.get_length())
    todos.draw(sc)
    pygame.display.flip()
    es = pygame.mixer.Sound("Juego/Escena final/Espada.wav")
    es.play()
    time.sleep(es.get_length())
    sc.blit(GatoRey, [950,240])
    pygame.display.flip()
    pygame.mixer.music.fadeout(2000)
    time.sleep(2)

def Transition(sc, lvl, v):
    if v:
        if lvl >= 2:
            pygame.mixer.music.load("Juego/Sonidos/Victoria.wav")
            pygame.mixer.music.play(-1)
            vic = pygame.image.load("Juego/Menus/Victoria.png")
            vic = pygame.transform.scale(vic, [ancho, alto])
            sc.blit(vic,[0,0])
            pygame.display.flip()
        else:
            if lvl == 0:
                his = pygame.image.load("Juego/Videos/Versiones T/IntroT.png")
                his = pygame.transform.scale(his, [ancho, alto])
                sc.blit(his,[0,0])
                pygame.display.flip()
            else:
                sc.fill(NEGRO)
                pygame.display.flip()
    else:
        pygame.mixer.music.load("Juego/Sonidos/Victoria.wav")
        pygame.mixer.music.play(-1)
        lose = pygame.image.load("Juego/Menus/Derrota.png")
        lose = pygame.transform.scale(lose, [ancho, alto])
        sc.blit(lose,[0,0])
        pygame.display.flip()
    next = False
    boton = Boton([1100, 520], "continuar")
    sc.blit(boton.image, [boton.rect.x, boton.rect.y])
    pygame.display.flip()
    while not next:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                next=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton.rect.collidepoint(event.pos):
                    next = True
    pygame.mixer.music.stop()
    if v and lvl <= 1:
            lvl += 1
            in_game(sc, lvl)
    else:
        Menu()


def Tutorial(sc):
    pygame.mixer.music.load("Juego/Tutorial/Tutorial.mp3")
    pygame.mixer.music.play(-1)
    i = 1
    while i <= 7:
        img = tutos[i]
        sc.blit(img, [0,0])
        next = False
        exit = False
        boton = Boton([1100, 520], "continuar")
        sc.blit(boton.image, [boton.rect.x, boton.rect.y])
        pygame.display.flip()
        while not (next or exit):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit=True
                    i = 9
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if boton.rect.collidepoint(event.pos):
                        next = True
        i += 1
    if not exit:
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
                in_game(pantalla, 2)
                #Transition(pantalla, 1, True)

if __name__ == '__main__':
    Menu()
