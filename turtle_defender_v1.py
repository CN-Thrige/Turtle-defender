

#importer pygame fra biblotektet (library)
import pygame
import sys
import random

pygame.init()

#opsætnign af skærm
screen_width = 640
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#tilføje et billede!
turtle_img = pygame.image.load("p_turtle.png")
turtle_speed = 5
turtle_width = turtle_img.get_width()
turtle_height = turtle_img.get_height()
turtle_x = screen_width // 10 - turtle_width // 10
turtle_y = screen_height - turtle_height - 10
turtle_img= pygame.transform.scale(turtle_img,(turtle_img.get_width()/10,turtle_img.get_height()/10))

#opsætning af kugler
bullet_width = 5
bullet_height = 10
bullet_speed = 7
bullets = []
bullety = []

# opsætning af fjenderne
enemy_width = 50
enemy_height = 60
enemy_speed = 2
enemies = []
# hvornår fjenderne skal dukke op, heraf fremgå det at det er hver 2 sekund
enemy_timer = 0
enemy_spawn_time = 2000

#opsætning:
clock = pygame.time.Clock()
running = True
x=0
delta_time = 0.1

def check_collision(rect1, rect2):
    return pygame.Rect(rect1).colliderect(pygame.Rect(rect2))

#main loop for computerspillet, kapitel 4 i starting out with python
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                #skaber en kugle på spillerens nuværende postion
                bullet_x = turtle_x + turtle_width // 2 - bullet_width // 2
                bullet_y = turtle_y
                bullets.append([bullet_x, bullet_y])

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and turtle_x > 0:
        turtle_x -= turtle_speed

    if keys[pygame.K_RIGHT] and turtle_x < screen_width- turtle_width:
        turtle_x += turtle_speed

# opsætning af kuglens postions!
    for bullet in bullets:
        bullet[1] -= bullet_speed

    bullets = [bullet for bullet in bullets if bullet[1] > 0]

# opsætning af fjerner og føder ny

    current_time = pygame.time.get_ticks()
    if current_time - enemy_timer > enemy_spawn_time:
        enemy_x = random.randint(0, screen_width - enemy_width)
        enemy_y = -enemy_height
        enemies.append([enemy_x, enemy_y])
        enemy_timer = current_time

    for enemy in enemies:
        enemy[1] += enemy_speed

 # tjekker om kuglen har ramt
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if check_collision((bullet[0], bullet[1], bullet_width, bullet_height),
                                   (enemy[0], enemy[1], enemy_width, enemy_height)):
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    break

# fjerner fjenden fra skærmen!
    enemies = [enemy for enemy in enemies if enemy[1] < screen_height]

# udfylder skærmen i farve!
    screen.fill("light blue")

#tegner spilleren
    screen.blit(turtle_img, (x, 550))
    x += 50 * delta_time

 # tegner kuglen
    for bullet in bullets:
        pygame.draw.rect(screen, (255, 255, 255), (bullet[0], bullet[1], bullet_width, bullet_height))

# tegner fjernen
    for enemy in enemies:
        pygame.draw.rect(screen, (255, 0, 0), (enemy[0], enemy[1], enemy_width, enemy_height))

    pygame.display.flip()
    delta_time = clock.tick(60)
    delta_time = max(0.001,min(0.1,delta_time))

    clock.tick(60)
