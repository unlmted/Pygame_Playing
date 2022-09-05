from re import A
import pygame
import os
from sys import platform
pygame.font.init()
pygame.mixer.init() # Starts the sound aspect of pygame

# CONSTANTS
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # Display
pygame.display.set_caption("Brendon's Game")
WHITE = (255, 255, 255)
HOT_PINK = (227, 28, 121)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
FPS = 60 # how many frames per second game updates at
ALIEN = pygame.image.load(
        os.path.join('ASSETS', 'ALIEN.png'))
ALIEN_RESIZE = pygame.transform.rotate(pygame.transform.scale(ALIEN, (55, 55)), 270)
HERO = pygame.image.load(
        os.path.join('ASSETS', 'HERO.png'))
HERO_RESIZE = pygame.transform.rotate(pygame.transform.scale(HERO, (55, 55)), 90)
VEL = 5 # Velocity (how much characters move)
BORDER = pygame.Rect((WIDTH//2)-5, 0, 10, HEIGHT)
BULLETS_VELOCITY = 7 # projectile speed
MAX_BULLETS = 30
HERO_HIT = pygame.USEREVENT + 1 # User event 1
ALIEN_HIT = pygame.USEREVENT + 2 # User event 2
SPACE = pygame.transform.scale(pygame.image.load(
    os.path.join('ASSETS', 'space.png')), (WIDTH, HEIGHT))
BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('ASSETS', 'HIT.mp3'))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('ASSETS', 'GUN_SHOT.mp3'))
WINNER_SOUND = pygame.mixer.Sound(os.path.join('ASSETS', 'WINNER.mp3'))
AMBIENT_SOUND = pygame.mixer.Sound(os.path.join('ASSETS', 'AMBIENT.mp3'))
HEALTH_FONT = pygame.font.SysFont('comicssans', 40) # defining font we want to use
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

#determine OS for key mapping
if platform == "darwin":
    fire_button_right = pygame.K_m
else:
    fire_button_right = pygame.K_RCTRL

def hero_movement(keys_pressed, hero):
    if keys_pressed[pygame.K_a] and (hero.x - VEL) > 0:  # left
        hero.x -= VEL
    if keys_pressed[pygame.K_d] and (hero.x + VEL + hero.width) < (BORDER.x):  # right
        hero.x += VEL
    if keys_pressed[pygame.K_w] and (hero.y - VEL) > 0:
        hero.y -= VEL
    if keys_pressed[pygame.K_s] and (hero.y + VEL + hero.width) < HEIGHT :
        hero.y += VEL

def alien_movement(keys_pressed, alien):
    if keys_pressed[pygame.K_UP] and (alien.y - VEL) > 0 :
        alien.y -= VEL
    if keys_pressed[pygame.K_DOWN] and (alien.y + VEL + alien.width) < HEIGHT:
        alien.y += VEL
    if keys_pressed[pygame.K_LEFT] and (alien.x - VEL) > (BORDER.x):
        alien.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and (alien.x + VEL + alien.width) < WIDTH:
        alien.x += VEL

def draw_window(hero, alien, hero_bullets, alien_bullets, hero_alive, alien_alive, hero_health, alien_health):
    WIN.blit(SPACE, (0,0))
    pygame.draw.rect(WIN, WHITE, BORDER)
    hero_health_text = HEALTH_FONT.render("Health: " + str(hero_health), 1, WHITE) # Use this font to render some text
    alien_health_text = HEALTH_FONT.render("Health: " + str(alien_health), 1, WHITE)
    WIN.blit(alien_health_text, (WIDTH - alien_health_text.get_width() - 20, 10))
    WIN.blit(hero_health_text, (10, 10))
    if hero_alive:
        WIN.blit(HERO_RESIZE, (hero.x, hero.y))
    if alien_alive:
        WIN.blit(ALIEN_RESIZE, (alien.x, alien.y)) 
    for bullet in hero_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in alien_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

    pygame.display.update()

def handle_bullets(hero_bullets, alien_bullets, hero, alien, hero_alive, alien_alive):
    if hero_alive:
        for bullet in hero_bullets:
            bullet.x += BULLETS_VELOCITY
            if alien.colliderect(bullet):
                pygame.event.post(pygame.event.Event(ALIEN_HIT))
                hero_bullets.remove(bullet)
            elif bullet.x > WIDTH:
                hero_bullets.remove(bullet)
    if alien_alive:
        for bullet in alien_bullets:
            bullet.x -= BULLETS_VELOCITY
            if hero.colliderect(bullet):
                pygame.event.post(pygame.event.Event(HERO_HIT))
                alien_bullets.remove(bullet)
            elif bullet.x < 0:
                alien_bullets.remove(bullet)

def draw_winner(winner_text):
    winner = WINNER_FONT.render(winner_text, 1, WHITE)
    WIN.blit(winner,(WIDTH//2 - winner.get_width()//2, HEIGHT//2 - winner.get_height()//2))
    pygame.display.update()
    WINNER_SOUND.play()
    pygame.time.delay(5000) # delay by 5 seconds

def main():
    hero = pygame.Rect(10, 30, 55, 55)
    alien = pygame.Rect(500, 300, 55, 55)
    alien_bullets = [] # empty list for the bullets
    hero_bullets = [] 
    hero_health = 3
    alien_health = 3
    clock = pygame.time.Clock() # Clock object
    alien_alive = True
    hero_alive = True
    run = True
    AMBIENT_SOUND.play()
    while run:
        clock.tick(FPS) # Ensure we never go over this capped frame rate for performance
        # Gets a list of all different events
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == fire_button_right and len(alien_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect((alien.x + alien.width), (alien.y + alien.height//2 - 2), 10, 5)
                    alien_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
                if event.key == pygame.K_LCTRL and len(hero_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(hero.x, (hero.y + hero.height//2 - 2), 10, 5)
                    hero_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
            if event.type == pygame.QUIT:
                run = False
            if event.type == HERO_HIT:
                if hero_health > 0:
                    hero_health -= 1
                    print("Hero hit")
                    BULLET_HIT_SOUND.play()
            if event.type == ALIEN_HIT:
                if alien_health > 0:
                    alien_health -= 1
                    print("Alien hit")
                    BULLET_HIT_SOUND.play()

        winner_text = ""
        if hero_health == 0:
            hero_alive = False
            winner_text = "Alien Wins!"
        if alien_health == 0:
            alien_alive = False
            winner_text = "Hero Wins!"
        if winner_text != "":
            draw_winner(winner_text)
            main()

        keys_pressed = pygame.key.get_pressed() # tells which keys are being pressed down
        hero_movement(keys_pressed, hero)
        alien_movement(keys_pressed, alien)
        handle_bullets(hero_bullets, alien_bullets, hero, alien, hero_alive, alien_alive)
        draw_window(hero, alien, alien_bullets, hero_bullets, hero_alive, alien_alive, hero_health, alien_health) # Fill window color
        
    quit()

if __name__ == '__main__':
    main()

