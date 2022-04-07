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
enemy_list = [] # lista que concentra todos os inimigos presentes no cenário
bg_margins = objects.Margin()

# 3 - Load images

background_fig = pygame.image.load("Images/background.png")

# 4 - keep looping through
while 1:
    # 5 - clear the screen before drawing it again
    screen.fill(0)
    # 6 - draw the screen elements
    screen.blit(background_fig, (0,0))
    bg_margins.draw(screen)
    p1.draw(screen)
    objects.draw_enemies(enemy_list,screen)
    for j in p1.bullet_list:
        j.update()  # update bullets
        if j.y_pos<0: # remove bullets that don't fit the screen anymore
            p1.bullet_list.remove(j)
        j.draw(screen) # display bullets
    # 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events
    keys[0] = False
    for event in pygame.event.get():
        # check if the event is the X button
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                keys[1] = False
            elif event.key == pygame.K_s:
                keys[2] = False
            elif event.key == pygame.K_d:
                keys[3] = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                keys[0] = True
            elif event.key == K_a:
                keys[1] = True
            elif event.key == K_s:
                keys[2] = True
            elif event.key == K_d:
                keys[3] = True


    # 9 - Move player
    if keys[0]:
        p1.shoot()
    if keys[1]:
        p1.move_left()
    elif keys[3]:
        p1.move_right()
    if keys[2]:
        pass

    # 10 - Move background
    bg_margins.move()

    # 11 - Move enemies
    objects.update_enemies(enemy_list)

    # 12 - Checks for collisions and deaths
    physics.check_bullet_kill(p1, enemy_list)
    if physics.check_enemy_collision(p1,enemy_list):
        exit(0)
    physics.check_scenario_collision(p1,bg_margins)




