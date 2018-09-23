import pygame


class TextObject:
    def __init__(self, x, y, text="Add text!", font_size=15, color=(0, 0, 0), warningcolor=(255, 0, 0)):
        pygame.font.init()
        self.x = x
        self.y = y
        self.font_size = font_size
        self.font = pygame.font.SysFont("monospace", self.font_size)

        self.text = text
        self.idlecolor = color
        self.warningcolor = warningcolor

        self.color = color

    def render(self, screen):
        label = self.font.render(self.text, 1, self.color)
        screen.blit(label, (self.x, self.y))

    def update_text(self, new_text, warning=False):
        if warning:
            self.color = self.warningcolor
        else:
            self.color = self.idlecolor

        self.text = new_text