import pygame
GLOBAL_OFFSET = [0, 0]

class StaticGameObject(pygame.sprite.Sprite):
    def __init__(self, imgPath, x=0, y=0, w=64, h=64):
        pygame.sprite.Sprite.__init__(self)
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        self.renderable = pygame.image.load(imgPath)
        self.renderable = pygame.transform.scale(self.renderable, (w, h))

        self.rect = self.renderable.get_rect()
        self.rect.center = (self.x, self.y)

    def render(self, screen):
        # render_x = int(self.x)
        # render_y = int(self.y)
        screen.blit(self.renderable, (self.x-GLOBAL_OFFSET[0], self.y-GLOBAL_OFFSET[1]))


    def update_sprite(self, newPath):
        self.renderable = pygame.image.load(newPath)
        self.renderable = pygame.transform.scale(self.renderable, (self.w, self.h))