import pygame
from DataAdapter import DataAdapter

dataAdapter = DataAdapter()


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
            self.velocity -= 10

        if(pygame.mouse.get_pressed()[0] == 0) :
            self.clicked = False

             
