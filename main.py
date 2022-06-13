import pygame

from DataAdapter import DataAdapter
from Bird import Bird

pygame.init()

#get game variables
dataAdapter = DataAdapter()
groundScroll = dataAdapter.groundScroll
scrollSpeed = dataAdapter.scrollSpeed
screenWidth = dataAdapter.screenWidth
screenHeight = dataAdapter.screenHeight
groundSize = dataAdapter.groundSize
groundHeight = dataAdapter.groundHeight
fps = dataAdapter.fps


#Define game variables
clock = pygame.time.Clock()
flying = False
gameOver = False

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

    if flappy.rect.bottom > groundHeight:
        gameOver = True
        flying = False

    if gameOver == False:
        groundScroll -= scrollSpeed
        if abs(groundScroll) > screenWidth:
            groundScroll = 0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and flying == False and gameOver == False:
            flying = True

    pygame.display.update()

pygame.quit()