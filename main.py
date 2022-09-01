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
ALIEN_RESIZE = pygame.transform.scale(ALIEN, (55, 40))

HERO = pygame.image.load(
        os.path.join('ASSETS', 'HERO.jpg'))
HERO_RESIZE = pygame.transform.scale(HERO, (55, 40))

def draw_window():
    WIN.fill(HOT_PINK)
    WIN.blit(ALIEN_RESIZE, (30, 10))
    WIN.blit(HERO_RESIZE, (300, 100))
    pygame.display.update()

def main():
    clock = pygame.time.Clock() # Clock object
    run = True
    while run:
        clock.tick(FPS) # Ensure we never go over this capped frame rate for performance
        draw_window() # Fill window color
        # Gets a list of all different events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    quit()

if __name__ == '__main__':
    main()

