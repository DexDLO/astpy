from circleshape import CircleShape
import random
from constants import LINE_WIDTH
from constants import ASTEROID_MIN_RADIUS
import pygame
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        pygame.sprite.Sprite.__init__(self, self.containers)

    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH )
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")

        angle = random.uniform(20, 50)

        vel1 = self.velocity.rotate(angle)
        vel2 = self.velocity.rotate(-angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        rock1 = Asteroid(self.position.x, self.position.y, new_radius)
        rock2 = Asteroid(self.position.x, self.position.y, new_radius)

        rock1.velocity = vel1 * 1.2
        rock2.velocity = vel2 * 1.2

