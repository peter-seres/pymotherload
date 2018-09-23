import pygame

class DynamicGameObject:
    def __init__(self, m, x=0, y=0, w=64, h=64):
        self.gravity = 200.
        self.damping = 450.
        self.e = 0.2

        self.m = m

        self.w = w
        self.h = h
        self.x = x
        self.y = y

        self.vx = 0
        self.vy = 0

        self.vmax = 300

        self.forces_x = [self.damping * (-self.vx)]
        self.forces_y = [self.gravity*self.m]

        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

    def _updatePosition(self, dt):
        ax = sum(self.forces_x)/self.m
        ay = sum(self.forces_y)/self.m

        self.vx += ax * dt
        self.vy += ay * dt

        # Limit max speed:
        if abs(self.vx) >= self.vmax and self.vx < 0:
            self.vx = -self.vmax
        elif abs(self.vx) >= self.vmax and self.vx >= 0:
            self.vx = self.vmax
        if abs(self.vy) >= self.vmax and self.vy < 0:
            self.vy = -self.vmax
        elif abs(self.vy) >= self.vmax and self.vy >= 0:
            self.vy = self.vmax

        self.x += self.vx * dt
        self.y += self.vy * dt

        self.reset_forces()

    def update_after_collision(self, dt):
        #self.x += -self.vx * dt
        self.y += -self.vy * dt

        self.vy = - self.vy * self.e

    def reset_forces(self):
        self.forces_x = [self.damping * (-self.vx)]
        self.forces_y = [self.gravity*self.m]

    def reset_y(self):
        self.forces_y = [self.gravity*self.m]

    def reset_x(self):
        self.forces_x = [0]

