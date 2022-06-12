import pygame
from Bird import Bird

pygame.init()

#define game variables
groundScroll = 0
scrollSpeed = 4
screenWidth = 864
screenHeight = 936
clock = pygame.time.Clock()
fps = 60

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Flappy Bird')




#load images and scale images

#background
background = pygame.image.load('images/background-day.png')
background = pygame.transform.scale(background, (864, 936))

#ground
ground = pygame.image.load('images/base.png')
ground = pygame.transform.scale(ground, (864 , ground.get_height()))

birdGroup = pygame.sprite.Group()

flappy = Bird(100, int(screen_height / 2))

birdGroup.add(flappy)


run = True
while run:

    clock.tick(fps)

    #draw background
    screen.blit(background, (0,0))

    birdGroup.draw(screen)
    birdGroup.update()

    #draw and scroll the ground
    screen.blit(ground, (groundScroll, 768))
    groundScroll -= scrollSpeed
    if abs(groundScroll) > 35:
        groundScroll = 0


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()