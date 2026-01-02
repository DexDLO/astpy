import pygame
from constants import *
from logger import log_state
from player import Player
from circleshape import CircleShape


def main():
    # 1. Initialize Pygame (Always do this first)
    pygame.init()
    
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    # 2. Setup the screen INSIDE main
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Optional: Setup a clock to control framerate (makes the game smooth)
    clock = pygame.time.Clock()
    ship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)



    forever = True
    dt = 0
    

    # 3. The Game Loop
    while forever:
        # --- Handle Input ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                forever = False

        # --- Game Logic ---
        log_state() # Keeping your custom logger
        

        dt = clock.tick(60) / 1000

        # update game state
        ship.update(dt)

        # draw
        screen.fill((0, 0, 0))
        ship.draw(screen)
        pygame.display.flip()

    # Quit pygame when the loop finishes
    pygame.quit()

if __name__ == "__main__":
    main()
        