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

def draw_window(hero, alien):
    WIN.fill(HOT_PINK)
    WIN.blit(ALIEN_RESIZE, (alien.x, alien.y))
    WIN.blit(HERO_RESIZE, (hero.x, hero.y))
    pygame.display.update()

def main():
    hero = pygame.Rect(100, 300, 55, 55)
    alien = pygame.Rect(500, 300, 55, 55)
    clock = pygame.time.Clock() # Clock object
    run = True
    while run:
        clock.tick(FPS) # Ensure we never go over this capped frame rate for performance
        draw_window(hero, alien) # Fill window color
        keys_pressed = pygame.key.get_pressed() # tells which keys are being pressed down

        if keys_pressed[pygame.K_a]: # left
            hero.x -= 1
        elif keys_pressed[pygame.K_d]: # right
            hero.x += 1
        elif keys_pressed[pygame.K_w]:
            hero.y -= 1
        elif keys_pressed[pygame.K_s]:
            hero.y += 1

        if keys_pressed[pygame.K_u]:
            alien.y -= 1
        elif keys_pressed[pygame.K_j]:
            alien.y += 1
        elif keys_pressed[pygame.K_h]:
            alien.x -= 1
        elif keys_pressed[pygame.K_k]:
            alien.x += 1


        # Gets a list of all different events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    quit()

if __name__ == '__main__':
    main()

