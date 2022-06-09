import pygame

pygame.init()
screen = pygame.display.set_mode((500,1000))

clock = pygame.time.Clock()
fps = 60

background_size = (500, 1000)

base_size = (background_size[0]+background_size[0]/10, 200)
base_position = (0, background_size[1]- 200)
base_x = 0
base_x_speed = 3

pipe_size = (background_size[0]/10, background_size[1]/5)
pipe_position = (base_position[0] + pipe_size[0], base_position[1] - pipe_size[1])

background = pygame.image.load("images/background-day.png").convert()
background = pygame.transform.scale(background, background_size)

base = pygame.image.load("images/base.png").convert()
base = pygame.transform.scale(base, base_size)

bird = pygame.image.load("images/bluebird-midflap.png").convert()
bird_movement = 0

pipe = pygame.image.load("images/pipe-green.png").convert()
pipe = pygame.transform.scale(pipe, pipe_size)


#simulacija
while True:
    
    clock.tick(fps)

    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            pygame.quit()
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_SPACE):
                bird_movement -= 50

    bird_movement += 3
    screen.blit(background, (0,0))
    screen.blit(bird, (50, int(background_size[1] / 2)+bird_movement))
    
    #adding base, and moving it 
    screen.blit(base, (base_x, base_position[1]))
    base_x -= base_x_speed
    if abs(base_x) > background_size[0]/10 - 15:
        base_x = 0

    screen.blit(pipe, pipe_position)

    pygame.display.update()
