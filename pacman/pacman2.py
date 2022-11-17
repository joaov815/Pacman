import pygame

from pacman import Pacman
from colors import BLACK
from scenario import Scenario

pygame.init()

screen_boundaries = (800, 600)
screen_cells_boundaries = (30, 0)

screen = pygame.display.set_mode(screen_boundaries, 0)

if __name__ == "__main__":
    size = 600 // 30

    pacman = Pacman(size)
    scenario = Scenario(size)

    while True:
        # Calculate rules
        pacman.calculate_rules(scenario)

        # Draw screen
        screen.fill(BLACK)

        scenario.draw(screen)
        pacman.draw(screen)
        pygame.display.update()

        pygame.time.delay(50)

        events = pygame.event.get()

        pacman.process_events(events)

        # Capture events
        for event in events:
            if event.type == pygame.QUIT:
                exit()
