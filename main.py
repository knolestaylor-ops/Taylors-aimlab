import pygame
from input_handler import InputHandler
from graphics import Target, Screen, Counter
from menu import Menu
BLACK = (0,0,0)
WHITE = (255,255,255)

def spawn_new_target(screen):
    return Target(screen)

def main():
    pygame.init()


    # initializes screen from screen class
    screen = Screen(BLACK)

    # creates a list of targets from target class
    NUM_TARGETS = 3
    targets = [Target(screen) for i in range (0, NUM_TARGETS)]
    # initializes the input handler from the inputhandler class
    input_handler = InputHandler()

    counter = Counter(screen, WHITE)

    clock = pygame.time.Clock()

    running = True
    start_time = pygame.time.get_ticks()
    total_time = 30

# Main game loop
    while running:
        # Main menu logic
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        # Gameplay logic
        screen.background()
        for target in targets:
            # Target method, draws rectangle with hitbox
            target.draw()
            input_handler.handle_events(targets, counter)

            if not targets:
                end_time = pygame.time.get_ticks()
                elapsed_time = (end_time - start_time) / 1000
                print(f"Time to complete: {elapsed_time}")
                time_left = total_time - (pygame.time.get_ticks() - elapsed_time) / 1000
                print(f"Time left: {time_left}")
                targets = [Target(screen) for i in range(0, NUM_TARGETS)]

                start_time = pygame.time.get_ticks()

        screen.blit(counter.draw())
        pygame.display.flip()

        clock.tick(60)
    pygame.quit()

if __name__ == '__main__':
    main()
