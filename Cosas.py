import pygame,math,time
ancho = 640
alto = 480
angulo = 15
centro = [320,240]
centro1 = [50,50]
NEGRO = [0,0,0]
BLANCO = [255,255,255]
pos = [0, 0]
flag = 0
pantalla = pygame.display.set_mode([ancho,alto])
reloj = pygame.time.Clock()

def ejes(s, p):
    pygame.draw.line(s, BLANCO, [0,p[1]], [ancho,p[1]], 1)
    pygame.draw.line(s, BLANCO, [p[0],0], [p[0],alto], 1)

def dot(s, p):
    pygame.draw.line(s, BLANCO, p, p, 1)

def plano(c, p):
    return [c[0]+p[0],c[1]-p[1]]

fin = False
while not fin:
    ejes(pantalla,centro)
    pygame.display.flip()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
            fin = True
      if event.type == pygame.MOUSEBUTTONDOWN:
          pos[0] = event.pos[0]
          pos[1] = event.pos[1]
          pygame.draw.circle(pantalla,BLANCO, [pos[0], centro[1]], int(math.fabs(centro[1]-pos[1])), 0)
          flag = 1
    if (flag == 1):
        ejes(pantalla,centro)
        if (pos[0] < centro[0]):
            for i in range(0,2*(centro[0]-pos[0])):
                pos[0] += 1
                pantalla.fill(NEGRO)
                ejes(pantalla,centro)
                pygame.draw.circle(pantalla,BLANCO, [pos[0], centro[1]], int(math.fabs(centro[1]-pos[1])), 0)
                pygame.display.flip()
        if (pos[0] >= centro[0]):
            for i in range(0,2*(pos[0]-centro[0])):
                pos[0] -= 1
                pantalla.fill(NEGRO)
                ejes(pantalla,centro)
                pygame.draw.circle(pantalla,BLANCO, [pos[0], centro[1]], int(math.fabs(centro[1]-pos[1])), 0)
                pygame.display.flip()
        reloj.tick(50)
