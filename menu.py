import pygame



class Menu:
    def __init__(self, screen, color):
        self.screen = screen
        self.color = color
        self.START = True
        self.font = pygame.font.SysFont('Arial', 20)

    def fill(self):
        self.screen.background()

    def draw_START(self):
        self.screen.background()
        text_surf = self.font.render("Taylor's Aimlab", True, self.color)
        return text_surf

