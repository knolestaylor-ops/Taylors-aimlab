import pygame
from pygame import event

class InputHandler:
    def __init__(self):
        self.left_click = False
        self.pos = [0,0]
        self.running = True
        self.event = event


    def handle_events(self, targets, counter):
        self.left_click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game(event)

            if self.mouse_click(event):
                self.update_count(event, counter)
                print(f"Clicked at: {self.pos}")

                for target in targets:
                    if self.clicked_target(target):
                        print(f"Clicked target: {target} at pos: {self.pos}")
                        targets.remove(target)
                        self.update_target_count(target, counter)


    def quit_game(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()


    def mouse_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.pos = event.pos
            self.left_click = True
        return self.left_click

    def clicked_target(self, target):
        return target.rect.collidepoint(self.pos)

    def update_target_count(self, target, counter):
        if self.clicked_target(target):
            counter.target_counting()
        return counter.get_count(), counter.get_target_count()

    def update_count(self, event, counter):
        if self.mouse_click(event):
            counter.counting()
        return counter.get_count(), counter.get_target_count()
