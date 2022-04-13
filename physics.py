from objects import max_fuel
def check_scenario_collision(p1, bg_margins):  # checks if player has collided with background elements
    player_mask = p1.get_mask()
    y_margin = []
    masks = []
    x_margin = []
    for i in bg_margins.get_mask():
        x_margin.append(i[0])
        y_margin.append(i[1])
        masks.append(i[2])
    distance1 = (x_margin[0] - p1.x_pos, int(y_margin[0]-p1.y_pos))
    distance2 = (x_margin[1] - p1.x_pos, int(y_margin[0]-p1.y_pos))
    collision1 = player_mask.overlap(masks[0], distance1)
    collision2 = player_mask.overlap(masks[1], distance2)
    return (collision1 or collision2)


def check_enemy_collision(p1, enemy_list):  # checks if player has collides with an enemy
    player_mask = p1.get_mask()
    for enemy in enemy_list:
        enemy_mask = enemy.get_mask()
        distance = (enemy.x_pos - p1.x_pos, enemy.y_pos-p1.y_pos)
        collision = player_mask.overlap(enemy_mask, distance)
        if collision:
            return True
    return False


def check_bullet_kill(p1, enemy_list):  # checks if any bullet has reached an enemy
    for enemy in enemy_list:
        for bullet in p1.bullet_list:
            if (bullet.y_pos - enemy.y_pos < enemy.height and enemy.y_pos - bullet.y_pos < bullet.height) and (bullet.x_pos - enemy.x_pos < enemy.width and enemy.x_pos - bullet.x_pos < bullet.width):
                enemy_list.remove(enemy)
                p1.bullet_list.remove(bullet)
                p1.score += max_fuel
                break

def check_fuel_collision(p1, fuel_list):
    player_mask = p1.get_mask()
    for fuel in fuel_list:
        fuel_mask = fuel.get_mask()
        distance = (fuel.x_pos - p1.x_pos, fuel.y_pos - p1.y_pos)
        collision = player_mask.overlap(fuel_mask, distance)
        if collision:
            p1.fuel = 1000
            fuel_list.remove(fuel)
            break