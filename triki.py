import pygame,math,time
ancho = 600
NEGRO = [0,0,0]
BLANCO = [255,255,255]
VERDE = [0,255,0]
ROJO = [255,0,0]
mat = [[0,0,0],[0,0,0],[0,0,0]]
flag = 0
pantalla = pygame.display.set_mode([ancho,ancho])
botones = pygame.sprite.Group()

class Ret (pygame.sprite.Sprite):
    def __init__(self, col):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([100,50])
        self.image.fill(col)
        self.rect = self.image.get_rect()

def lineas(s):
    pygame.draw.line(s, BLANCO, [0,ancho/3], [ancho,ancho/3], 5)
    pygame.draw.line(s, BLANCO, [0,2*ancho/3], [ancho,2*ancho/3], 5)
    pygame.draw.line(s, BLANCO, [ancho/3,0], [ancho/3,ancho], 5)
    pygame.draw.line(s, BLANCO, [2*ancho/3,0], [2*ancho/3,ancho], 5)

def cruz(s, p):
    pygame.draw.line(s, BLANCO, [int(p[0]-(ancho/12)), int(p[1]-(ancho/12))], [int(p[0]+(ancho/12)),int(p[1]+(ancho/12))], 5)
    pygame.draw.line(s, BLANCO, [int(p[0]-(ancho/12)), int(p[1]+(ancho/12))], [int(p[0]+(ancho/12)),int(p[1]-(ancho/12))], 5)

def isWinner(bo, t):
    if t:
        le = 1
    else: le = 2
    # Given a board and a player’s letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don’t have to type as much.
    return ((bo[0][0] == le and bo[0][1] == le and bo[0][2] == le) or # across the top
    (bo[1][0] == le and bo[1][1] == le and bo[1][2] == le) or # across the middle
    (bo[2][0] == le and bo[2][1] == le and bo[2][2] == le) or # across the bottom
    (bo[0][0] == le and bo[1][1] == le and bo[2][2] == le) or # down the left side
    (bo[0][2] == le and bo[1][1] == le and bo[2][0] == le) or # down the middle
    (bo[0][0] == le and bo[1][0] == le and bo[2][0] == le) or # down the right side
    (bo[0][1] == le and bo[1][1] == le and bo[2][1] == le) or # diagonal
    (bo[0][2] == le and bo[1][2] == le and bo[2][2] == le)) # diagonal

def algo(s, p, t):
    x = int(((6*p[0]/ancho)-1)/2)
    y = int(((6*p[1]/ancho)-1)/2)
    if turno == True:
        if mat[x][y] == 0:
            mat[x][y] = 1
            cruz(s, p)
            return True
    else:
        if mat[x][y] == 0:
            pygame.draw.circle(s,BLANCO, [int(p[0]),int(p[1])], int(ancho/12), 5)
            mat[x][y] = 2
            return True
    return False

turno = True
fin = False
while not fin:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin = True
        if flag == 0:
            lineas(pantalla)
            if event.type == pygame.MOUSEBUTTONDOWN:
                s = True
                pos = [event.pos[0],event.pos[1]]
                if pos[0] <= ancho/3 and pos[1] <= ancho/3:
                    s = algo(pantalla, [ancho/6, ancho/6], turno)
                elif pos[0] <= ancho/3 and pos[1] <= 2*ancho/3:
                    s = algo(pantalla, [ancho/6, ancho/2], turno)
                elif pos[0] <= ancho/3 and pos[1] <= ancho:
                    s = algo(pantalla, [ancho/6, 5*ancho/6], turno)
                elif pos[0] <= 2*ancho/3 and pos[1] <= ancho/3:
                    s = algo(pantalla, [ancho/2, ancho/6], turno)
                elif pos[0] <= 2*ancho/3 and pos[1] <= 2*ancho/3:
                    s = algo(pantalla, [ancho/2, ancho/2], turno)
                elif pos[0] <= 2*ancho/3 and pos[1] <= ancho:
                    s = algo(pantalla, [ancho/2, 5*ancho/6], turno)
                elif pos[0] <= ancho and pos[1] <= ancho/3:
                    s = algo(pantalla, [5*ancho/6, ancho/6], turno)
                elif pos[0] <= ancho and pos[1] <= 2*ancho/3:
                    s = algo(pantalla, [5*ancho/6, ancho/2], turno)
                elif pos[0] <= ancho and pos[1] <= ancho:
                    s = algo(pantalla, [5*ancho/6, 5*ancho/6], turno)
                pygame.display.flip()
                if isWinner(mat, turno):
                    flag = 1
                elif s:
                    turno = not(turno)
        else:
            ganador = pygame.image.load("gana1.png")
            pantalla.fill(NEGRO)
            if not turno:
                ganador = pygame.image.load("gana2.png")
            pantalla.blit(ganador, [150,50])
            volver = Ret(VERDE)
            volver.rect.x = 250
            volver.rect.y = 300
            botones.add(volver)
            salir = Ret(ROJO)
            salir.rect.x = 250
            salir.rect.y = 500
            botones.add(salir)
            botones.draw(pantalla)
            pygame.display.flip()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if volver.rect.collidepoint(event.pos):
                    mat = [[0,0,0],[0,0,0],[0,0,0]]
                    pantalla.fill(NEGRO)
                    turno = True
                    flag = 0
                elif salir.rect.collidepoint(event.pos):
                    fin = True
