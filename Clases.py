import pygame
ancho 640
alto 480
a = 20
NEGRO = [0, 0, 0]
BLANCO = [255, 255, 255]
VERDE = [0, 255, 0]
vel = 2
pantalla = pygame.display.set_mode([ancho,alto])
reloj = pygame.time.Clock()
pos = [320,240]

class cuadros(pygame.sprite.Sprite):
    def __init__(self, pos, color, len, vel):
        super().__init__(self)
        self.image = pygame.surface([len,len])
        self.image.fill(color)
        self.pos = pos
        self.vel = vel
        self.rect  =self.image.get_rect()
    def update(self):
        self.pos += self.vel
        
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
