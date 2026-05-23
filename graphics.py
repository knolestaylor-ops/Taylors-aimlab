import pygame
import random


class Target:
    def __init__(self, screen):
        self.radius = 20
        self.screen = pygame.display.set_mode((800, 600))
        self.color = pygame.Color(0, 255, 0)
        self.x = random.randrange(0 + self.radius, 800 - self.radius)
        self.y = random.randrange(0 + self.radius, 600 - self.radius)
        self.rect = pygame.Rect(self.x, self.y, self.radius, self.radius)

    def draw(self):
        pygame.draw.rect(self.screen, self.color,  self.rect)

    def move(self, x, y):
        pass





class Screen:
    def __init__(self, color):
        self.screen = pygame.display.set_mode((800, 600))
        self.color = color
        pygame.display.set_caption("Screen")

    def background(self):
        self.screen.fill(self.color)

    def blit(self, surface):
        self.screen.blit(surface, (0, 0))



class Counter:
    def __init__(self, screen, color):
        self.screen = screen
        self.color = color
        self.count = 0
        self.font = pygame.font.SysFont("Arial", 20)
        self.target_count = 0

    def get_count(self):
        return self.count

    def counting(self):
        self.count += 1
        return self.count

    def target_counting(self):
        self.target_count += 1
        return self.target_count

    def get_target_count(self):
        return self.target_count


    def draw(self):
        target_count = self.get_target_count()
        count = self.get_count()
        text_surface = self.font.render(f'{target_count}/{count}', True, self.color)
        return text_surface





