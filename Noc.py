import pygame,math,time
ancho = 640
alto = 480
angulo = 15
centro = [320,240]
centro1 = [50,50]
NEGRO = [0,0,0]
BLANCO = [255,255,255]
pos1 = [0, 0]
pos2 = [0, 0]
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
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
            fin = True
      if event.type == pygame.MOUSEBUTTONDOWN:
          pygame.draw.circle(pantalla,BLANCO, event.pos, 5, 0)
          pygame.display.flip()
          if flag == 0:
              pos1[0] = event.pos[0]
              pos1[1] = event.pos[1]
              flag = 1
          elif flag == 1:
                  pos2[0] = event.pos[0]
                  pos2[1] = event.pos[1]
                  flag = 2
          elif flag == 2:
                      pos1[0] = event.pos[0]
                      pos1[1] = event.pos[1]
                      flag = 1
    if (flag == 2):
        dx = pos2[0]-pos1[0]
        dy = pos2[1]-pos1[1]
        steps = 0
        if math.fabs(abs(dx)) >= math.fabs(abs(dy)):
            steps = int(math.fabs(dx))
        else: steps = int(math.fabs(dy))
        dx /= steps
        dy /= steps
        x = pos1[0]
        y = pos1[1]
        for i in range(0,steps):
            pantalla.fill(NEGRO)
            pygame.draw.circle(pantalla,BLANCO, [int(x),int(y)], 5, 1)
            pygame.display.flip()
            x += dx
            y += dy
        flag = 0
    reloj.tick(50)
