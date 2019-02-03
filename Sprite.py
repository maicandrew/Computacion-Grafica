import pygame
ancho = 640
alto = 480
NEGRO = [0,0,0]
vel = 5
pantalla = pygame.display.set_mode([ancho,alto])
reloj = pygame.time.Clock()
pos = [320,240]
posfondo = [0, 0]
fondo = pygame.image.load('fondo.jpg')
sprite = pygame.image.load('sprite.png')
def dibfondo(pos, image, s):
    s.blit(image, pos)
def sprite1 (pos,image, s):
    s.blit(image,pos)
a = sprite.get_rect()
b = fondo.get_rect()
dibfondo(posfondo, fondo, pantalla)
sprite1(pos, sprite, pantalla)
pygame.display.flip()
fin = False
while not fin:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin = True
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
            if (pos[1] + a[3] < alto):
                pos[1] += vel
            elif (pos[1] + a[3] < b[3]+posfondo[1]):
                    posfondo[1] -= vel
        if event.key == pygame.K_UP:
            if (pos[1] > 0):
                pos[1] -= vel
            elif(pos[1] > posfondo[1]):
                    posfondo[1] += vel
        if event.key == pygame.K_LEFT:
            if (pos[0] > 0):
              pos[0] -= vel
            elif(pos[0] > posfondo[0]):
                  posfondo[0] += vel
        if event.key == pygame.K_RIGHT:
            if (pos[0] + a[2] < ancho):
                pos[0] += vel
            elif(pos[0] + a[2] < b[2]+posfondo[0]):
                    posfondo[0] -= vel
    pantalla.fill(NEGRO)
    dibfondo(posfondo, fondo, pantalla)
    sprite1(pos,sprite, pantalla)
    pygame.display.flip()
    reloj.tick(50)
