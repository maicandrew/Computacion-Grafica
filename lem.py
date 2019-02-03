import pygame,math,time
ancho = 640
alto = 480
centro = [320,240]
NEGRO = [0,0,0]
BLANCO = [255,255,255]
VERDE = [0, 255, 0]
pos = [0,0]
pos2 = [0,0]
flag = 0
pantalla = pygame.display.set_mode([ancho,alto])
reloj = pygame.time.Clock()

def ejes(s, p):
    pygame.draw.line(s, BLANCO, [0,p[1]], [ancho,p[1]], 1)
    pygame.draw.line(s, BLANCO, [p[0],0], [p[0],alto], 1)

def dot(s, p):
    pygame.draw.line(s, BLANCO, p, p, 1)

def cartesianas(p):
    x = p[0]*math.cos(math.radians(p[1]))
    y = p[0]*math.sin(math.radians(p[1]))
    return [x, y]

def cartesianas2(p):
    x = p[0]*math.cos(math.radians(p[1]))
    y = p[0]*math.sin(math.radians(p[1]))
    return [-x, y]

def polares(pos):
    r = int(math.sqrt(math.pow(pos[0],2)+math.pow(pos[1],2)))
    tetha = int(math.degrees(math.acos(pos[0]/r)))
    if pos[1] < 0:
        tetha = 360-tetha
    return [r,tetha]

def invplano(c, p):
    pos = [p[0] - c[0], c[1] - p[1]]
    return pos

def plano(c, p):
    return [c[0]+p[0],c[1]-p[1]]

fin = False
tetha = -45
while not fin:
    ejes(pantalla,centro)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag = 1
            pos = list(event.pos)
    if flag == 1:
        if tetha <= 45:
            r = math.sqrt(2*10000*math.cos(math.radians(2*tetha)))
            pos1 = plano(pos, cartesianas([r, tetha]))
            pos2 = plano(pos, cartesianas2([r, tetha]))
        tetha += 1
        pygame.draw.circle(pantalla, VERDE, [int(pos1[0]), int(pos1[1])], 5, 0)
        pygame.draw.circle(pantalla, VERDE, [int(pos2[0]), int(pos2[1])], 5, 0)
        pygame.display.flip()
    reloj.tick(100)
