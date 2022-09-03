import pygame
import os

# CONSTANTS
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # Display
pygame.display.set_caption("Brendon's Game")
WHITE = (255, 255, 255)
HOT_PINK = (227, 28, 121)
FPS = 60 # how many frames per second game updates at
ALIEN = pygame.image.load(
        os.path.join('ASSETS', 'ALIEN.jpg'))
ALIEN_RESIZE = pygame.transform.scale(ALIEN, (55, 55))
HERO = pygame.image.load(
        os.path.join('ASSETS', 'HERO.jpg'))
HERO_RESIZE = pygame.transform.rotate(pygame.transform.scale(HERO, (55, 55)), 115)
VEL = 5 # Velocity (how much characters move)
BORDER = pygame.Rect((WIDTH/2)-5, 0, 10, HEIGHT)

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

def draw_window(hero, alien):
    WIN.fill(HOT_PINK)
    pygame.draw.rect(WIN, WHITE, BORDER)
    WIN.blit(ALIEN_RESIZE, (alien.x, alien.y))
    WIN.blit(HERO_RESIZE, (hero.x, hero.y))
    pygame.display.update()
def main():
    hero = pygame.Rect(10, 30, 55, 55)
    alien = pygame.Rect(500, 300, 55, 55)
    clock = pygame.time.Clock() # Clock object
    run = True
    while run:
        clock.tick(FPS) # Ensure we never go over this capped frame rate for performance
        draw_window(hero, alien) # Fill window color
        keys_pressed = pygame.key.get_pressed() # tells which keys are being pressed down
        hero_movement(keys_pressed, hero)
        alien_movement(keys_pressed, alien)
        # Gets a list of all different events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    quit()

if __name__ == '__main__':
    main()

