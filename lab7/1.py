import pygame
from datetime import datetime

pygame.init()

screen = pygame.display.set_mode((1000,900))
pygame.display.set_caption('Mikki Maus Clock')
clock = pygame.time.Clock()

mainclock = pygame.image.load(r"C:\Users\erbol\Downloads\clock.png")
arrow_second = pygame.image.load(r"C:\Users\erbol\Downloads\leftarm.png")
arrow_minute =  pygame.image.load(r"C:\Users\erbol\Downloads\rightarm.png")

center = (500,450)

def rotate_image(image,angle,pos):
    
    rotated_image = pygame.transform.rotate(image,angle)
    new_rec = rotated_image.get_rect(center = pos)
    return rotated_image,new_rec

running = True
while running:
    
    screen.fill('White')

    time = datetime.now()
    minutes = time.minute
    seconds = time.second

    minute_angle = -minutes * 6-60
    second_angle = -seconds*6

    second_rotated, second_rect = rotate_image(arrow_second, second_angle, center)
    minute_rotated, minute_rect = rotate_image(arrow_minute, minute_angle, center)

    screen.blit(mainclock,(-200,-75))
    screen.blit(second_rotated,second_rect)
    screen.blit(minute_rotated,minute_rect)



    pygame.display.flip()
    clock.tick(120)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()




