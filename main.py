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


class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range(1, 4):
            img = pygame.image.load('images/redbird-midflap.png')
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.velocity = 0
        self.clicked = False

    def update(self):
        self.velocity += 0.5

        if(self.velocity>8):
            self.velocity=8

        if self.rect.bottom < dataAdapter.groundHeight:
            self.rect.y += int(self.velocity)

        if(pygame.mouse.get_pressed()[0] == 1 and self.clicked == False) :
            self.clicked = True
            self.vel -= 10

        if(pygame.mouse.get_pressed()[0] == 0) :
            self.clicked = False


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