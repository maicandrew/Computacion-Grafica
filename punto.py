import pygame,math,time
ancho = 640
alto = 480
angulo = 10
centro = [320,240]
centro1 = [50,50]
NEGRO = [0,0,0]
BLANCO = [255,255,255]
flag = 0
pos = [0, 0]
pos2 = [0, 0]
pantalla = pygame.display.set_mode([ancho,alto])
def rotar(punto,angulo = 1):
    x = punto[0]*math.cos(math.radians(angulo)) - punto[1]*math.sin(math.radians(angulo))
    y = punto[0]*math.sin(math.radians(angulo)) + punto[1]*math.cos(math.radians(angulo))
    return [x,y]

def ejes(s, p):
    pygame.draw.line(s, BLANCO, [0,p[1]], [ancho,p[1]], 1)
    pygame.draw.line(s, BLANCO, [p[0],0], [p[0],alto], 1)

def dot(s, p):
    pygame.draw.line(s, BLANCO, p, p, 1)

def plano(c, p):
    return [c[0]+p[0],c[1]-p[1]]
def invplano(c, p):
    pos = [p[0] - c[0], c[1] - p[1]]
    return pos
fin = False
while not fin:
    ejes(pantalla,centro)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if flag == 0:
                pos1 = list(event.pos)
                if pos1[0] < centro[0] and pos1[1] > centro[1]:
                    flag = 1
                else: flag = 0
            elif flag == 1:
                pos2 = list(event.pos)
                if pos2[0] < centro[0] and pos2[1] > centro[1]:
                    flag = 2
                    pantalla.fill(NEGRO)
                    pygame.draw.line(pantalla,BLANCO, pos1, pos2, 3)
                else: flag = 0
        if event.type == pygame.KEYDOWN:
            if flag == 2:
                pos2 = invplano(pos1, pos2)
                pos2 = rotar(pos2, angulo)
                pos2 = plano(pos1, pos2)
                pygame.draw.line(pantalla, BLANCO, pos1, pos2, 3)
                pygame.display.flip()
        pygame.display.flip()
