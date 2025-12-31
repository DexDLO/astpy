import pygame
from constants import *
from logger import log_state

def main():
    # 1. Initialize Pygame (Always do this first)
    pygame.init()
    
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    # 2. Setup the screen INSIDE main
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Optional: Setup a clock to control framerate (makes the game smooth)
    clock = pygame.time.Clock()

    forever = True

    # 3. The Game Loop
    while forever:
        # --- Handle Input ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                forever = False

        # --- Game Logic ---
        log_state() # Keeping your custom logger
        
        # --- Draw ---
        # FIX: Use 'screen', and put color in double brackets ((r, g, b))
        screen.fill((0, 0, 0)) # Usually Asteroids is black (0,0,0), but use (255,255,255) for white
        
        # FIX: This must be INSIDE the loop to update the screen every frame
        pygame.display.flip()

        # Limit the game to 60 frames per second (prevents CPU overheating)
        #clock.tick(60)

    # Quit pygame when the loop finishes
    pygame.quit()

if __name__ == "__main__":
    main()
        