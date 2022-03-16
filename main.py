# 1 - Import library
import pygame
from pygame.locals import *
import objects
import physics

# 2 - Initialize the game
pygame.init()
width, height = 750, 750
screen = pygame.display.set_mode((width, height))
keys = [False, False, False, False] #keyboard keys being pressed -> W (atirar),A (esquerda),S,D (direita)
p1 = objects.Player(300,100,1,0)
enemy_list = [] # lista que concentra todos os inimigos presentes no cenário -> a implementar

# 3 - Load images
player_fig = pygame.image.load("Images/player.png")
background_fig = pygame.image.load("Images/background.png")
bullet_fig = pygame.image.load("Images/bullet.png")

# 4 - keep looping through
while 1:
    # 5 - clear the screen before drawing it again
    screen.fill(0)
    # 6 - draw the screen elements
    screen.blit(background_fig, (0,0))
    screen.blit(player_fig,(p1.x_pos, p1.y_pos))
    for j in p1.bullet_list:
        j.update()  # update bullets
        if j.y_pos<0: # remove bullets that don't fit the screen anymore
            p1.bullet_list.remove(j)
        screen.blit(bullet_fig, (j.x_pos, j.y_pos)) # display bullets
    # 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                keys[0] = True
            elif event.key == K_a:
                keys[1] = True
            elif event.key == K_s:
                keys[2] = True
            elif event.key == K_d:
                keys[3] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                keys[0] = False
            elif event.key == pygame.K_a:
                keys[1] = False
            elif event.key == pygame.K_s:
                keys[2] = False
            elif event.key == pygame.K_d:
                keys[3] = False

        # 9 - Move player
        if keys[0]:
            p1.shoot()
        if keys[1]:
            p1.move_left()
        elif keys[3]:
            p1.move_right()
        if keys[2]:
            pass

