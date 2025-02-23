import pygame 
from random import randrange
pygame.init()
width = 1200
height = 700
paddle_w =300 # размер длина платформы
paddle_h =30 #размер ширина платформы
ball_r = 20 #радиус окружности
ball_speed =6 #скорость движения мяча
ball_d =ball_r*2 #диаметр окружности
paddle = pygame.Rect(width/2-paddle_w/2, height - paddle_h-10, paddle_w,paddle_h)
p_speed = 15
sc = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
while True:
     for e in pygame.event.get():
          if e.type==pygame.QUIT:
               exit()
     pygame.draw.rect(sc, pygame.Color("Orange"), paddle) #вид платформы
     key = pygame.key.get_pressed() #распознание нажатой клавиши
     if key[pygame.K_LEFT] and paddle.left>0:
          new_x = paddle.left - p_speed
          paddle.x = new_x
     if key[pygame.K_RIGHT] and paddle.right<width:
          paddle.right += p_speed #новые координаты платформы, кстати, почему здесь двое переменных, а не три
     pygame.display.flip()
     clock.tick(60)
