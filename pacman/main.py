import pygame

from pacman import Pacman
from colors import BLACK, RED, GREEN
from ghost import Ghost
from scenario import Scenario

pygame.init()

screen_boundaries = (800, 600)

screen = pygame.display.set_mode(screen_boundaries, 0)

if __name__ == "__main__":
    size = 600 // 30

    pacman = Pacman(size)
    blink = Ghost(RED, size)
    ghost = Ghost(GREEN, size)
    scenario = Scenario(size)

    while True:
        # Calculate rules
        pacman.calculate_rules(scenario)

        # Draw screen
        screen.fill(BLACK)

        scenario.draw(screen)
        blink.draw(screen)
        ghost.draw(screen)
        pacman.draw(screen)

        blink.calculate_rules(scenario)
        ghost.calculate_rules(scenario)

        pygame.display.update()
        pygame.time.delay(50)

        events = pygame.event.get()

        pacman.process_events(events)
        scenario.process_events(events)

