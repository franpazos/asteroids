import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from bullet import Bullet

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable, )
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    Bullet.containers = (bullets, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0 # delta time

    # main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
            
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collision_check(player):
                print("GAME OVER")
                pygame.quit()
                return
            
        for asteroid in asteroids:
            for bullet in bullets:
                if asteroid.collision_check(bullet):
                    bullet.kill()
                    asteroid.split()

        screen.fill((0, 0, 0), rect=None, special_flags=0)

        for obj in drawable:
            obj.draw(screen)
            
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
