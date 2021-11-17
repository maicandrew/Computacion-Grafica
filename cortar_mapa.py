import pygame

ancho=1200
alto=400
centro=[300,300]
NEGRO = [0, 0, 0]
VERDE = [0,255,0]
ROJO = [255, 0, 0]
map = pygame.image.load("terrenogen.png")
fin = False
pygame.init()
pantalla=pygame.display.set_mode([ancho,alto])

while not fin:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin=True
    for i in range(32):
        for j in range(12):
            im = pygame.Surface.subsurface(map, (i*32, j*32, 32, 32))
            pantalla.blit(im, [32*i, 32*j])
            pygame.display.flip()
