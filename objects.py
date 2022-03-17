class Player:
    def __init__(self, x_pos, fuel, level, score):
        self.x_pos = x_pos
        self.y_pos = 600
        self.fuel = fuel
        self.level = level
        self.score = score
        self.bullet_list = []
    def shoot(self):
        new_bullet = Bullet(self.x_pos + 45, self.y_pos)
        self.bullet_list.append(new_bullet)
    def move_right(self):
        self.x_pos += 5
    def move_left(self):
        self.x_pos -= 5
    def die(self): # possivelmente mudar para check_for_death
        pass

class Bullet:
    def __init__(self, x_pos, y_pos): #possivelmente adicionar velocidade
        self.x_pos = x_pos
        self.y_pos = y_pos
    def update(self):
        self.y_pos -=5

class Helicopter:
    def __init__(self, x_pos, y_pos):
        pass
    def update(self):
        pass


class Ship:
    def __init__(self, x_pos, y_pos):
        pass
    def update(self):
        pass


class Bird:
    def __init__(self, x_pos, y_pos):
        pass
    def update(self):
        pass

'''import pygame
import os
import random

TELA_LARGURA = 500
TELA_ALTURA = 800

IMAGEM_BACKGROUND = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')))'''

#um lado da margem....colocar outra flipada
class Margem:
    VELOCIDADE = 5
    ALTURA = IMAGEM_MARGEM.get_width()
    IMAGEM = IMAGEM_MARGEM

    #passa a coordenada x e y1 e y1 vem na sequencia 
    def __init__(x, self):
        self.x = x
        self.y1 = 0
        self.y2 = self.ALTURA
    # y1 1 imagem descendo e na sequencia desce a 2
    def mover(self):
        self.y1 -= self.VELOCIDADE
        self.y2 -= self.VELOCIDADE

        if self.y1 + self.ALTURA > 0:
            self.y1 = self.y2 + self.ALTURA
        if self.y2 + self.ALTURA > 0:
            self.y2 = self.y1 + self.ALTURA

    def desenhar(self, tela):
        tela.blit(self.IMAGEM, (self.x, self.y1))
        tela.blit(self.IMAGEM, (self.x, self.y2))