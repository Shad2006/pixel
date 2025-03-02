import pygame 
from random import randrange

pygame.init()
width = 1200
height = 700
fps = 60
paddle_w = 300
paddle_h = 30
ball_r = 20
ball_speed = 6
ball_d = ball_r * 2
ball = pygame.Rect(randrange(ball_d, width - ball_d), height / 2, ball_d, ball_d)
dx = 1
dy = -1
paddle = pygame.Rect(width/2 - paddle_w/2, height - paddle_h - 10, paddle_w, paddle_h)
p_speed = 15
sc = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
blocks = [
    pygame.Rect(10+120*i, 10+70*j, 100, 50)
    for i in range(10)
    for j in range(5)
]
colors = [
    (randrange(0, 256), randrange(0, 256), randrange(0, 256))
    for i in range(10)
    for j in range(5)
]
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()

    sc.fill((0, 0, 0))
    

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= p_speed
    elif key[pygame.K_RIGHT] and paddle.right < width:
        paddle.x += p_speed
    

    ball.x += ball_speed * dx
    ball.y += ball_speed * dy
    if ball.centerx<ball_r or ball.centerx>width-ball_r:
        dx=-dx
        #при else мяч движется только влево-вправо
    elif ball.centery < ball_r or ball.centery > height - ball_r:
        dy = -dy
    elif ball.colliderect(paddle) and dy > 0:
        dy = -dy

    pygame.draw.rect(sc, pygame.Color("Orange"), paddle)
    pygame.draw.circle(sc, pygame.Color("white"), ball.center, ball_r)
    [
        pygame.draw.rect(sc, colors[color], block)
        for color, block in enumerate(blocks)
    ]

    pygame.display.flip()
    clock.tick(fps)
