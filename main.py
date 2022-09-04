import pygame
import os

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
ALIEN_RESIZE = pygame.transform.scale(ALIEN, (55, 55))
HERO = pygame.image.load(
        os.path.join('ASSETS', 'HERO.png'))
HERO_RESIZE = pygame.transform.rotate(pygame.transform.scale(HERO, (55, 55)), 115)
VEL = 5 # Velocity (how much characters move)
BORDER = pygame.Rect((WIDTH//2)-5, 0, 10, HEIGHT)
BULLETS_VELOCITY = 7 # projectile speed
MAX_BULLETS = 3
HERO_HIT = pygame.USEREVENT + 1 # User event 1
ALIEN_HIT = pygame.USEREVENT + 2 # User event 2

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

def draw_window(hero, alien, hero_bullets, alien_bullets):
    WIN.fill(HOT_PINK)
    pygame.draw.rect(WIN, WHITE, BORDER)
    WIN.blit(ALIEN_RESIZE, (alien.x, alien.y))
    WIN.blit(HERO_RESIZE, (hero.x, hero.y))

    for bullet in hero_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in alien_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

    pygame.display.update()

def handle_bullets(hero_bullets, alien_bullets, hero, alien):
    for bullet in hero_bullets:
        bullet.x += BULLETS_VELOCITY
            pygame.event.post(pygame.event.Event(ALIEN_HIT))
            hero_bullets.remove(bullet)
    for bullet in alien_bullets:
        bullet.x -= BULLETS_VELOCITY
        if hero.colliderect(bullet):
            pygame.event.post(pygame.event.Event(HERO_HIT))
            alien_bullets.remove(bullet)

def main():
    hero = pygame.Rect(10, 30, 55, 55)
    alien = pygame.Rect(500, 300, 55, 55)

    alien_bullets = [] # empty list for the bullets
    hero_bullets = [] 
    clock = pygame.time.Clock() # Clock object
    run = True

    while run:
        clock.tick(FPS) # Ensure we never go over this capped frame rate for performance
        # Gets a list of all different events
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(alien_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect((alien.x + alien.width), (alien.y + alien.height//2 - 2), 10, 5)
                    alien_bullets.append(bullet)
                if event.key == pygame.K_RCTRL and len(hero_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(hero.x, (hero.y + hero.height//2 - 2), 10, 5)
                    hero_bullets.append(bullet)
            if event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed() # tells which keys are being pressed down
        hero_movement(keys_pressed, hero)
        
        alien_movement(keys_pressed, alien)

        handle_bullets(hero_bullets, alien_bullets, hero, alien)

        draw_window(hero, alien, alien_bullets, hero_bullets) # Fill window color
        print(alien_bullets, hero_bullets)
    quit()

if __name__ == '__main__':
    main()

