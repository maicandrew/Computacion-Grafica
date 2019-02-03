import pygame
ancho = 640
alto = 480
NEGRO = [0,0,0]
vel = 5
pantalla = pygame.display.set_mode([ancho,alto])
reloj = pygame.time.Clock()
pos = [320,240]
def cruz (pos,surface):
    pygame.draw.line(surface,[255,0,0], [pos[0]-5, pos[1]], [pos[0]+5, pos[1]],1)
    pygame.draw.line(surface,[255,0,0], [pos[0], pos[1]-5], [pos[0], pos[1]+5],1)
cruz(pos,pantalla)
pygame.display.flip()
fin = False
while not fin:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin = True
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
            if (pos[1] + 5 >= alto):
                pos[1] = 0
            else: pos[1] += vel
        if event.key == pygame.K_UP:
            if (pos[1] - 5 <= 0):
                pos[1] = alto
            else: pos[1] -= vel
        if event.key == pygame.K_LEFT:
            if (pos[0] - 5 <= 0):
                pos[0] = ancho
            else: pos[0] -= vel
        if event.key == pygame.K_RIGHT:
            if (pos[0] + 5 >= ancho):
                pos[0] = 0
            else: pos[0] += vel
    pantalla.fill(NEGRO)
    cruz(pos,pantalla)
    pygame.display.flip()
    reloj.tick(50)
