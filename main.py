from constants import *
from player import *
import pygame

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    guy = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill('black')
        for thing in updateable:
            thing.update(dt)
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        dt = (clock.tick(60) / 1000)

if __name__ == "__main__":
    main()