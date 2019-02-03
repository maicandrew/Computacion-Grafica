import pygame,math,time
ancho = 640
alto = 480
angulo = 15
centro = [320,240]
NEGRO = [0,0,0]
BLANCO = [255,255,255]
pos1 = [100, 60]
pos2 = [250,210]
flag = 0
pantalla = pygame.display.set_mode([ancho,alto])
reloj = pygame.time.Clock()

def ejes(s, p):
    pygame.draw.line(s, BLANCO, [0,p[1]], [ancho,p[1]], 1)
    pygame.draw.line(s, BLANCO, [p[0],0], [p[0],alto], 1)

def dot(s, p):
    pygame.draw.line(s, BLANCO, p, p, 1)

def polares(p):
    return([p[0]*math.cos(math.radians(p[1])), p[0]*math.sin(math.radians(p[1]))])

def invpolares(pos):
    r = math.sqrt(math.pow(pos[0],2)+math.pow(pos[1],2))
    tetha = math.degrees(math.acos(pos[0]/r))
    if pos[1] < 0:
        tetha = 360-tetha
    return [r,tetha]

def invplano(c, p):
    pos = [p[0] - c[0], c[1] - p[1]]
    return pos

def plano(c, p):
    return [c[0]+p[0],c[1]-p[1]]

pygame.display.flip()
fin = False
while not fin:
    ejes(pantalla,centro)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin = True
        if event.type == pygame.KEYDOWN:
            dot(pantalla, plano(centro, polares(pos1)))
            dot(pantalla, plano(centro, polares(pos2)))
            pygame.display.flip()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = invplano(centro, event.pos)
            car = invpolares(pos)
            print(car)
    pygame.display.flip()
