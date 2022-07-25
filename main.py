import pygame
import random
from pygame.locals import *
from Bird import Bird 
from Pipe import Pipe
from Button import Button

pygame.init()

clock = pygame.time.Clock()
fps = 60
screenWidth = 864
screenHeight = 936

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Flappy Bird')

font = pygame.font.SysFont('Bauhaus 93', 60)
color = (255, 255, 255) #white

groundScroll = 0
scrollSpeed = 4
flying = False
gameOver = False
pipeGap = 150
pipeFrequency = 1500
lastPipe = pygame.time.get_ticks() - pipeFrequency
score = 0
passPipe = False

bg = pygame.image.load('img/bg.png')
groundImg = pygame.image.load('img/ground.png')
buttonImg = pygame.image.load('img/restart.png')

birdGroup = pygame.sprite.Group()
pipeGroup = pygame.sprite.Group()
flappy = Bird(100, int(screenHeight / 2))
birdGroup.add(flappy)

def draw_text(text, font, textCol, x, y):
    img = font.render(text, True, textCol)
    screen.blit(img, (x, y))

def reset_game():
    pipeGroup.empty()
    flappy.rect.x = 100
    flappy.rect.y = int(screenHeight / 2)
    score = 0
    return score

button = Button(screenWidth // 2 - 50, screenHeight // 2 - 100, buttonImg)
run = True
while run:

    clock.tick(fps)
    screen.blit(bg, (0,0))

    birdGroup.draw(screen)
    birdGroup.update(flying, gameOver)
    pipeGroup.draw(screen)

    screen.blit(groundImg, (groundScroll, 768))

    if len(pipeGroup) > 0:
        if birdGroup.sprites()[0].rect.left > pipeGroup.sprites()[0].rect.left\
            and birdGroup.sprites()[0].rect.right < pipeGroup.sprites()[0].rect.right\
            and passPipe == False:
            passPipe = True
        if passPipe == True:
            if birdGroup.sprites()[0].rect.left > pipeGroup.sprites()[0].rect.right:
                score += 1
                passPipe = False

    draw_text(str(score), font, color, int(screenWidth / 2), 20)

    if pygame.sprite.groupcollide(birdGroup, pipeGroup, False, False) or flappy.rect.top < 0:
        gameOver = True

    if flappy.rect.bottom >= 768:
        gameOver = True
        flying = False


    if gameOver == False and flying == True:

        timeNow = pygame.time.get_ticks()
        if timeNow - lastPipe > pipeFrequency:
            pipeHeight = random.randint(-100, 100)
            bottomPipe = Pipe(screenWidth, int(screenHeight / 2) + pipeHeight, -1, pipeGap)
            topPipe = Pipe(screenWidth, int(screenHeight / 2) + pipeHeight, 1, pipeGap)
            pipeGroup.add(bottomPipe)
            pipeGroup.add(topPipe)
            lastPipe = timeNow

        groundScroll -= scrollSpeed
        if abs(groundScroll) > 35:
            groundScroll = 0
        pipeGroup.update(scrollSpeed)

        print("X and Y of a bird: " + str(birdGroup.sprites()[0].getRect()))
        if(len(pipeGroup.sprites()) != 0):
            print("top pipe: " + str(pipeGroup.sprites()[0].getRect()))
            print("bottom pipe: " + str(pipeGroup.sprites()[1].getRect()))

    if gameOver == True:
        if button.draw(screen) == True:
            gameOver = False
            score = reset_game()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and flying == False and gameOver == False:
            flying = True

    pygame.display.update()

pygame.quit()