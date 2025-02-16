import pygame 
pygame.init()
width = 1200
height = 700
sc = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
while True:
     for e in pygame.event.get():
          if e.type==pygame.QUIT:
               exit()
     pygame.display.flip()
     clock.tick(60)
