class Player:
    def __init__(self, x_pos, fuel, level, score):
        self.x_pos = x_pos
        self.y_pos = 600
        self.fuel = fuel
        self.level = level
        self.score = score
        self.bullet_list = []
    def shoot(self):
        new_bullet = Bullet(self.x_pos, self.y_pos)
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