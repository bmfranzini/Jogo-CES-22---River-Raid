import pygame
import random

width = 750
height = 750

speed = 3

bullet_fig = pygame.image.load("Images/bullet.png")
player_fig = pygame.image.load("Images/player.png")
img_helicopter = pygame.image.load("Images/helicopter_enemy.png")
img_zeppelin = pygame.image.load("Images/zeppelin_enemy.png")
img_type1 = pygame.image.load("Images/Margin_type1.png")
img_type2l = pygame.image.load("Images/Margin_type2l.png")
img_type2r = pygame.image.load("Images/Margin_type2r.png")

class Player:
    def __init__(self, x_pos, fuel, level, score):
        self.x_pos = x_pos
        self.y_pos = 600
        self.fuel = fuel
        self.level = level
        self.score = score
        self.bullet_list = []
        self.img = player_fig
        self.width = self.img.get_width()
        self.height = self.img.get_height()
    def shoot(self):
        new_bullet = Bullet(self.x_pos + 45, self.y_pos)
        self.bullet_list.append(new_bullet)
    def move_right(self):
        self.x_pos += 5
    def move_left(self):
        self.x_pos -= 5
    def die(self): # possivelmente mudar para check_for_death
        pass
    def draw(self, screen):
        #self.img.get_rect(topleft=(self.x_pos, self.y_pos))
        screen.blit(self.img,(self.x_pos, self.y_pos))
    def get_mask(self):
        return pygame.mask.from_surface(self.img)

class Bullet:
    def __init__(self, x_pos, y_pos): #possivelmente adicionar velocidade
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = bullet_fig.get_width()
        self.height = bullet_fig.get_height()
    def update(self):
        self.y_pos -= 5
    def draw(self, screen):
        screen.blit(bullet_fig, (self.x_pos, self.y_pos))


class Enemy: # Classe pai
    def __init__(self, x_pos, y_pos,dir, x_speed):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.dir = dir
        self.x_speed = x_speed #precisa ser tal que inimigos sempre colidam com player
    def flip(self):
        if self.dir == 'right':
            self.dir = 'left'
        elif self.dir == 'left':
            self.dir = 'right'


class Helicopter(Enemy):
    global speed
    def __init__(self, x_pos, y_pos,dir, x_speed):
        super().__init__(x_pos,y_pos,dir, x_speed)
        self.width = img_helicopter.get_width()
        self.height = img_helicopter.get_height()
        self.img = img_helicopter
    def update(self):
        if self.dir == 'right':
            self.x_pos += self.x_speed
        else:
            self.x_pos -= self.x_speed
        self.y_pos += speed
        #self.img.get_rect(topleft=(self.x_pos, self.y_pos))
    def draw(self,screen):
        if self.dir == 'left':
            flipped_img = pygame.transform.flip(self.img, True, False)
            screen.blit(flipped_img, (self.x_pos, self.y_pos))
        else:
            screen.blit(self.img, (self.x_pos, self.y_pos))
    def get_mask(self):
        return pygame.mask.from_surface(self.img)


class Zeppelin(Enemy):
    global speed
    def __init__(self, x_pos, y_pos,dir, x_speed):
        super().__init__(x_pos,y_pos,dir, x_speed)
        self.width = img_zeppelin.get_width()
        self.height = img_zeppelin.get_height()
        self.img = img_zeppelin
    def update(self):
        if self.dir == 'right':
            self.x_pos += self.x_speed
        else:
            self.x_pos -= self.x_speed
        self.y_pos += speed
        #self.img.get_rect(topleft=(self.x_pos, self.y_pos))
    def draw(self,screen):
        if self.dir == 'left':
            screen.blit(self.img, (self.x_pos, self.y_pos))
        else:
            flipped_img = pygame.transform.flip(self.img, True, False)
            screen.blit(flipped_img, (self.x_pos, self.y_pos))
    def get_mask(self):
        return pygame.mask.from_surface(self.img)


class Bird:
    def __init__(self, x_pos, y_pos):
        pass
    def update(self):
        pass

def update_enemies(enemy_list):
    if enemy_list == []:
        temp1 = random.choice([1, 2])
        temp2 = random.choice([1, 2])
        x0 = random.randrange(0, width)
        if temp1 ==1:
            enemy = Helicopter(x0,0,'right', 10) if temp2 == 1 else Helicopter(width,0,'left', 10)
        else:
            enemy = Zeppelin(x0, 0, 'right', 3) if temp2 == 1 else Zeppelin(width, 0, 'left', 3)
        enemy_list.append(enemy)
    for enemy in enemy_list:
        enemy.update()
        if(enemy.y_pos > height):
            enemy_list.remove(enemy)
        elif enemy.x_pos > width or enemy.x_pos<0:
            enemy.flip()
def draw_enemies(enemy_list, screen):
    for enemy in enemy_list:
        enemy.draw(screen)


class Margin:
    global speed
    block1_width = img_type1.get_width()
    block2_width = img_type2r.get_width()
    num_of_blocks = 4

    def __init__(self, x1=0, x2 = width - block1_width):
        self.left_margin = [img_type1,img_type1, img_type2l, img_type1, img_type1,img_type1, img_type2l, img_type1,img_type2l, img_type1, img_type1,img_type1] #lista com 3*num_of_blocks objetos
        self.right_margin = [img_type1,img_type1, img_type2r, img_type1, img_type1,img_type1, img_type2r, img_type1, img_type2r, img_type1, img_type1,img_type1]
        self.x1 = x1
        self.x2 = x2
        self.y = 0
    def move(self):
        self.y += speed # updates reference position
        if self.y%(3*height) == 2*height: # updates first set of blocks when it is not visible

            for j in range(self.num_of_blocks):
                temp = random.choice([1,2])
                if temp == 1:
                    self.left_margin[j] = img_type1
                    self.right_margin[j] = img_type1
                elif temp == 2:
                    self.left_margin[j] = img_type2l
                    self.right_margin[j] = img_type2r
        elif self.y%(3*height) == 0: # updates second set of blocks when it is not visible
            for j in range(self.num_of_blocks, 2 * self.num_of_blocks):
                temp = random.choice([1,2])
                if temp == 1:
                    self.left_margin[j] = img_type1
                    self.right_margin[j] = img_type1
                elif temp == 2:
                    self.left_margin[j] = img_type2l
                    self.right_margin[j] = img_type2r
        elif self.y%(3*height) == height: # updates third set of blocks when it is not visible
            for j in range(2*self.num_of_blocks, 3 * self.num_of_blocks):
                temp = random.choice([1,2])
                if temp == 1:
                    self.left_margin[j] = img_type1
                    self.right_margin[j] = img_type1
                elif temp == 2:
                    self.left_margin[j] = img_type2l
                    self.right_margin[j] = img_type2r


    def draw(self, screen):
        for i in range(3*self.num_of_blocks):
            screen.blit(self.left_margin[i], (self.x1 % width, (self.y + height * (self.num_of_blocks - 1 - i) / self.num_of_blocks) % (3 * height) - height / self.num_of_blocks))
            if self.right_margin[i] == img_type2r:
                screen.blit(self.right_margin[i], (self.x2 % width + self.block1_width - self.block2_width, (self.y + height * (self.num_of_blocks - 1 - i) / self.num_of_blocks) % (3 * height) - height / self.num_of_blocks))
            else:
                screen.blit(self.right_margin[i], (self.x2 % width, (self.y + height * (self.num_of_blocks - 1 - i) / self.num_of_blocks) % (3 * height) - height / self.num_of_blocks))
    def get_mask(self):
        pass
