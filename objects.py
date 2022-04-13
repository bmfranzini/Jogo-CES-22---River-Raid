import pygame
import random

width = 750
height = 750
player_y = 600
max_fuel = 1000

speed = 3

bullet_fig = pygame.image.load("Images/bullet.png")
player_fig = pygame.image.load("Images/player.png")
fuel_fig = pygame.image.load("Images/fuel.png")
fuel_fig = pygame.transform.scale(fuel_fig,(50,50))
img_helicopter = pygame.image.load("Images/helicopter_enemy.png")
img_zeppelin = pygame.image.load("Images/zeppelin_enemy.png")
img_type1 = pygame.image.load("Images/margin_1_.png")
img_type1 = pygame.transform.scale(img_type1, (60, 750))
img_type2l = pygame.image.load("Images/margin_2l.png")
img_type2l = pygame.transform.scale(img_type2l, (250, 750))
img_type2r = pygame.image.load("Images/margin_2r.png")
img_type2r = pygame.transform.scale(img_type2r, (250, 750))
game_over = pygame.image.load("Images/Game_Over.png")
margin_left = [(0,img_type1), (0,img_type2l)]
margin_right = [(width - img_type1.get_width(),img_type1), (width-img_type2r.get_width(),img_type2r)]
max_width =  max(img_type1.get_width(), img_type2r.get_width())

class Player:

    def __init__(self, x_pos, fuel, level, score):
        self.x_pos = x_pos
        self.y_pos = player_y
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
        screen.blit(self.img,(self.x_pos, self.y_pos))

    def get_mask(self):
        return pygame.mask.from_surface(self.img)

    def draw_score(self, screen):
        font = pygame.font.Font(None, 36)
        text = font.render(f'Score: {self.score}', 1, (0, 0, 0))
        textpos = text.get_rect(centerx = width / 2 - 100)
        screen.blit(text, textpos)

    def draw_fuel(self, screen):
        font = pygame.font.Font(None, 36)
        text = font.render(f'Fuel: {self.fuel}', 1, (0, 0, 0))
        textpos = text.get_rect(centerx = width / 2 + 100)
        screen.blit(text, textpos)


class Bullet:

    def __init__(self, x_pos, y_pos): # possivelmente adicionar velocidade
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = bullet_fig.get_width()
        self.height = bullet_fig.get_height()
        self.img = bullet_fig

    def update(self):
        self.y_pos -= 5

    def draw(self, screen):
        screen.blit(self.img, (self.x_pos, self.y_pos))


class Enemy: # Classe pai
    def __init__(self, x_pos, y_pos, dir, x_speed):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.dir = dir
        self.x_speed = x_speed # precisa ser tal que inimigos sempre colidam com player

    def flip(self):
        if self.dir == 'right':
            self.dir = 'left'
        elif self.dir == 'left':
            self.dir = 'right'


class Helicopter(Enemy):
    global speed

    def __init__(self, x_pos, y_pos, dir, x_speed):
        super().__init__(x_pos, y_pos, dir, x_speed)
        self.width = img_helicopter.get_width()
        self.height = img_helicopter.get_height()
        self.img = img_helicopter

    def update(self):
        if self.dir == 'right':
            self.x_pos += self.x_speed
        elif self.dir == 'left':
            self.x_pos -= self.x_speed
        self.y_pos += speed

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

    def __init__(self, x_pos, y_pos, dir, x_speed):
        super().__init__(x_pos, y_pos, dir, x_speed)
        self.width = img_zeppelin.get_width()
        self.height = img_zeppelin.get_height()
        self.img = img_zeppelin

    def update(self):
        if self.dir == 'right':
            self.x_pos += self.x_speed
        elif self.dir == 'left':
            self.x_pos -= self.x_speed
        self.y_pos += speed

    def draw(self, screen):
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
        new_enemy = True
    else:
        new_enemy = random.random() < 0.01/(len(enemy_list))**2
    if new_enemy:
        temp1 = random.choice([1, 2])
        temp2 = random.choice([1, 2])
        x0 = random.randrange(0, width)
        if temp1 == 1:
            enemy = Helicopter(x0, 0, 'right', 4) if temp2 == 1 else Helicopter(width, 0, 'left', 4)
        else:
            enemy = Zeppelin(x0, 0, 'right', 3) if temp2 == 1 else Zeppelin(width, 0, 'left', 3)
        enemy_list.append(enemy)
    for enemy in enemy_list:
        enemy.update()
        if enemy.y_pos > height:
            enemy_list.remove(enemy)
        elif enemy.x_pos > width or enemy.x_pos<0:
            enemy.flip()


def draw_enemies(enemy_list, screen):
    for enemy in enemy_list:
        enemy.draw(screen)

class Fuel:
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.img = fuel_fig

    def update(self):
        self.y_pos += speed
    def draw(self, screen):
        screen.blit(self.img, (self.x_pos, self.y_pos))
    def get_mask(self):
        return pygame.mask.from_surface(self.img)

def update_fuel(fuel_list, p1):
    p1.fuel -= 1
    if fuel_list == [] and (random.random() < 0.001 or p1.fuel< 100):
        x0 = random.randrange(max_width, width-max_width) 
        fuel_list.append(Fuel(x0,0))
    for fuel in fuel_list:
        fuel.update()
        if fuel.y_pos > height:
            fuel_list.remove(fuel)
        elif fuel.x_pos > width or fuel.x_pos<0:
            fuel.flip()

def draw_fuel(fuel_list, screen):
    for fuel in fuel_list:
        fuel.draw(screen)

class Margin:
    global speed
    num_of_blocks = 1

    def __init__(self):
        self.left_margin = [margin_left[0],margin_left[0], margin_left[1]] #lista com 3*num_of_blocks objetos
        self.right_margin = [margin_right[0],margin_right[0], margin_right[1]]
        self.y = 0
        self.y_plot = [0,0,0]#lista com 3*num_of_blocks que armazena o y de plot de cada um dos blocos

    def move(self):
        self.y += speed # updates reference position
        for i in range(3):
            self.y_plot[i] = (self.y + height * (self.num_of_blocks - 1 - i) / self.num_of_blocks) % (3 * height) - height / self.num_of_blocks
        if self.y%(3*height) == 2*height: # updates first set of blocks when it is not visible

            for j in range(self.num_of_blocks):
                temp = random.choice(range(len(margin_right)))
                self.left_margin[j] = margin_left[temp]
                self.right_margin[j] = margin_right[temp]
        elif self.y%(3*height) == 0: # updates second set of blocks when it is not visible
            for j in range(self.num_of_blocks, 2 * self.num_of_blocks):
                temp = random.choice(range(len(margin_right)))
                self.left_margin[j] = margin_left[temp]
                self.right_margin[j] = margin_right[temp]
        elif self.y%(3*height) == height: # updates third set of blocks when it is not visible
            for j in range(2*self.num_of_blocks, 3 * self.num_of_blocks):
                temp = random.choice(range(len(margin_right)))
                self.left_margin[j] = margin_left[temp]
                self.right_margin[j] = margin_right[temp]

    def draw(self, screen):
        for i in range(3*self.num_of_blocks):
            screen.blit(self.left_margin[i][1], (self.left_margin[i][0], self.y_plot[i]))
            screen.blit(self.right_margin[i][1], (self.right_margin[i][0], self.y_plot[i]))
    def get_mask(self):
        list = []
        for i in range(len(self.y_plot)):
            if self.y_plot[i] >= player_y - height and self.y_plot[i] <= player_y:
                list = [(self.left_margin[i][0], self.y_plot[i], pygame.mask.from_surface(self.left_margin[i][1])),
                        (self.right_margin[i][0], self.y_plot[i], pygame.mask.from_surface(self.right_margin[i][1]))]
        return list

