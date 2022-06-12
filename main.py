import pygame
from Bird import Bird

pygame.init()

#define game variables
groundScroll = 0
scrollSpeed = 5
screenWidth = 864
screenHeight = 936

groundSize = (screenWidth, 150)
groundHeight = screenHeight- groundSize[1]

clock = pygame.time.Clock()
fps = 60

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Flappy Bird')

#load images and scale images

#background
background = pygame.image.load('images/background-day.png')
background = pygame.transform.scale(background, (screenWidth, screenHeight))

#ground
ground = pygame.image.load('images/base.png')
ground = pygame.transform.scale(ground, groundSize)

birdGroup = pygame.sprite.Group()

flappy = Bird(100, int(screenHeight / 2))

birdGroup.add(flappy)


run = True
while run:

    clock.tick(fps)

    #draw background
    screen.blit(background, (0,0))

    birdGroup.draw(screen)
    birdGroup.update()

    #draw and scroll the ground
    screen.blit(ground, (groundScroll, groundHeight))
    screen.blit(ground, (groundScroll + screenWidth, groundHeight))
    groundScroll -= scrollSpeed
    if abs(groundScroll) > screenWidth:
        groundScroll = 0


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()