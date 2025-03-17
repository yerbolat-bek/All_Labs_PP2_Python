import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Red Ball')

x,y = 400, 300

speed = 20
R = 25


t = True
while t:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            t = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and y - R - speed >= 0:
        y -= speed
    if keys[pygame.K_DOWN] and y + R + speed <= 600:
        y += speed
    if keys[pygame.K_LEFT] and x - R - speed >= 0:
        x -= speed
    if keys[pygame.K_RIGHT] and x + R + speed <= 800:
        x += speed


    screen.fill('White')
    pygame.draw.circle(screen,'Red',(x,y),R)
    pygame.display.update()
    
pygame.quit()    


